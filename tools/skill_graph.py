"""Skill Graph for hawk-community-skills.

This module provides graph-based skill dependency analysis and
recommendation, inspired by LangGraph and knowledge graph patterns.
"""

from typing import List, Dict, Any, Optional, Set
from dataclasses import dataclass, field
from collections import deque
import json


@dataclass
class SkillNode:
    """Represents a skill in the skill graph."""
    id: str
    name: str
    description: str = ""
    tags: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    properties: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "tags": self.tags,
            "dependencies": self.dependencies,
            "properties": self.properties
        }


@dataclass
class SkillEdge:
    """Represents a dependency between skills."""
    source: str
    target: str
    kind: str = "depends_on"
    weight: float = 1.0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source": self.source,
            "target": self.target,
            "kind": self.kind,
            "weight": self.weight
        }


class SkillGraph:
    """Graph-based skill dependency analysis and recommendation.

    This class provides a fluent API for building skill graphs and
    querying them for dependencies, recommendations, and analysis.

    Example:
        graph = SkillGraph()
        graph.skill("coding", "Code Generation")
        graph.skill("testing", "Test Generation")
        graph.depends_on("testing", "coding")

        # Find dependencies
        deps = graph.get_dependencies("testing")
    """

    def __init__(self):
        self._nodes: Dict[str, SkillNode] = {}
        self._edges: List[SkillEdge] = []
        self._adj: Dict[str, List[str]] = {}

    def skill(self, id: str, name: str = "", description: str = "",
              tags: List[str] = None, **properties) -> "SkillGraph":
        """Add a skill to the graph."""
        if id in self._nodes:
            return self
        node = SkillNode(
            id=id,
            name=name or id,
            description=description,
            tags=tags or [],
            properties=properties
        )
        self._nodes[id] = node
        self._adj[id] = []
        return self

    def depends_on(self, source: str, target: str, weight: float = 1.0) -> "SkillGraph":
        """Add a dependency edge from source to target."""
        if source not in self._nodes or target not in self._nodes:
            raise ValueError(f"Skill not found: {source if source not in self._nodes else target}")
        edge = SkillEdge(source=source, target=target, kind="depends_on", weight=weight)
        self._edges.append(edge)
        self._adj[source].append(target)
        # Update dependency list
        self._nodes[source].dependencies.append(target)
        return self

    def get_skill(self, id: str) -> Optional[SkillNode]:
        """Get a skill by ID."""
        return self._nodes.get(id)

    def get_skills(self) -> List[SkillNode]:
        """Get all skills."""
        return list(self._nodes.values())

    def get_edges(self) -> List[SkillEdge]:
        """Get all edges."""
        return self._edges

    def find_by_tag(self, tag: str) -> List[SkillNode]:
        """Find all skills with a specific tag."""
        return [s for s in self._nodes.values() if tag in s.tags]

    def get_dependencies(self, skill_id: str) -> List[str]:
        """Get all dependencies of a skill."""
        if skill_id not in self._nodes:
            return []
        return self._nodes[skill_id].dependencies

    def get_dependents(self, skill_id: str) -> List[str]:
        """Get all skills that depend on this skill."""
        dependents = []
        for edge in self._edges:
            if edge.target == skill_id:
                dependents.append(edge.source)
        return dependents

    def topological_sort(self) -> List[str]:
        """Return skills in topological order (dependencies first)."""
        in_degree = {node_id: 0 for node_id in self._nodes}
        for edge in self._edges:
            in_degree[edge.source] = in_degree.get(edge.source, 0) + 1

        queue = deque([node_id for node_id, degree in in_degree.items() if degree == 0])
        result = []

        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor in self._adj.get(current, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result

    def recommend_skills(self, known_skills: List[str], max_recommendations: int = 5) -> List[str]:
        """Recommend skills based on known skills.

        Uses a simple collaborative filtering approach: find skills
        that are commonly depended on by the known skills.
        """
        recommendations = {}

        for skill_id in known_skills:
            if skill_id not in self._nodes:
                continue
            for dep in self._nodes[skill_id].dependencies:
                recommendations[dep] = recommendations.get(dep, 0) + 1

        # Sort by recommendation count
        sorted_recs = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
        return [skill for skill, count in sorted_recs[:max_recommendations]]

    def to_dict(self) -> Dict[str, Any]:
        """Export graph as a dictionary."""
        return {
            "nodes": [n.to_dict() for n in self._nodes.values()],
            "edges": [e.to_dict() for e in self._edges]
        }

    def to_json(self) -> str:
        """Export graph as JSON."""
        return json.dumps(self.to_dict(), indent=2)

    def __len__(self) -> int:
        return len(self._nodes)

    def __contains__(self, skill_id: str) -> bool:
        return skill_id in self._nodes
