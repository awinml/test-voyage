"""Sphinx configuration."""

project = "Test Voyage"
author = "Ashwin Mathur"
copyright = "2024, Ashwin Mathur"  # noqa: A001
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
