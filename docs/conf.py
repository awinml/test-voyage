"""Sphinx configuration."""
project = "Test Voyage"
author = "Ashwin Mathur"
copyright = "2024, Ashwin Mathur"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
