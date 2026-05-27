---
name: bpl-txt-functions
description: "System prompt - functions"
license: MIT
tags: [system-prompt]
domain: general
version: 1.0
author: TheBigPromptLibrary
---

.. _nn_functions:

.. currentmodule:: mlx.nn

Functions
---------

Layers without parameters (e.g. activation functions) are also provided as
simple functions.

.. autosummary::
   :toctree: _autosummary_functions
   :template: nn-module-template.rst

   gelu
   gelu_approx
   gelu_fast_approx
   mish
   prelu
   relu
   selu
   silu
   step