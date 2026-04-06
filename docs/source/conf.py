# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Exoplanets_Phase_Curves'
copyright = '2026, Louis-Julien Cartigny'
author = 'Louis-Julien Cartigny'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # Google / NumPy docstrings
]

import os
import sys
sys.path.insert(0, os.path.abspath(".."))


html_theme = "sphinx_rtd_theme"