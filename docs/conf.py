# Configuration file for the Sphinx documentation builder.
import os
import sys
import django
# Add the project directory to the sys.path
sys.path.insert(0, os.path.abspath('..'))
# Set the Django settings module environment variable
<<<<<<< HEAD

=======
>>>>>>> container
os.environ['DJANGO_SETTINGS_MODULE'] = 'hyperion.settings'
# Setup Django
django.setup()

#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# Name of the project
<<<<<<< HEAD
project = 'mandy consolidation'
=======
project = 'hyperion'
>>>>>>> container
# The copyright information
copyright = '2024, mandy'
# The author of the project
author = 'mandy'
# The release version of the project
release = '01/09/2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# List of Sphinx extensions to use
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon"
]

# Paths that contain templates
templates_path = ['_templates']
# Patterns to exclude when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
