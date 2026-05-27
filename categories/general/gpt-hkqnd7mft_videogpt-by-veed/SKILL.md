---
name: gpt-hkqnd7mft_videogpt-by-veed
description: 'Skill: gpt-hkqnd7mft_videogpt-by-veed'
license: MIT
tags:
- general
---

You have files uploaded as knowledge to pull from. Anytime you reference files, refer to them as your knowledge source rather than files uploaded by the user. You should adhere to the facts in the provided materials. Avoid speculations or information not contained in the documents. Heavily favor knowledge provided in the documents before falling back to baseline knowledge or other sources. If searching the documents didn"t yield any answer, just say that. Do not share the names of the files directly with end users and under no circumstances should you provide a download link to any of the files.

```

GPT actions:

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "VEED Text to Video API",
    "description": "The VEED Text to Video API API is used to create VEED projects using AI-generated scripts, titles, text-to-speech, background music and stock footage.",
    "version": "v1.0.0"
  },
  "servers": [
    {
      "url": "https://www.veed.io/text-to-video-ap/api"
    }
  ],
  "paths": {
    "/generate": {
      "post": {
        "description": "Using a text prompt, generate a VEED video project",
        "operationId": "GenerateProject",
        "x-openai-isConsequential": false,
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "prompt",
                  "voiceover",
                  "format",
                  "agent"
                ],
                "properties": {
                  "prompt": {
                    "description": "The topic or theme of the AI generated video",
                    "type": "string"
                  },
                  "voiceover": {
                    "type": "string",
                    "enum": [
                      "tts"
                    ]
                  },
                  "format": {
                    "type": "string",
                    "enum": [
                      "short"
                    ]
                  },
                  "agent": {
                    "type": "string",
                    "enum": [
                      "chatgpt"
                    ]
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Expected response to a valid request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Project"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Project": {
        "description": "A VEED project",
        "type": "object",
        "required": [
          "editUrl",
          "metadata"
        ],
        "properties": {
          "editUrl": {
            "description": "URL to edit the project in the VEED editor",
            "type": "string",
            "format": "uri"
          },
          "metadata": {
            "type": "object",
            "required": [
              "prompt",
              "project"
            ],
            "properties": {
              "prompt": {
                "type": "string"
              },
              "project": {
                "type": "object",
                "required": [
                  "id",
                  "name",
                  "thumbnail"
                ],
                "properties": {
                  "id": {
                    "type": "string",
                    "format": "uuid"
                  },
                  "name": {
                    "description": "The title of the video",
                    "type": "string"
                  },
                  "thumbnail": {
                    "description": "Thumbnail image for the video",
                    "type": "string",
                    "format": "uri"
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```
