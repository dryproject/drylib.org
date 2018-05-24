# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_bootstrap_theme

# -- Project information -----------------------------------------------------

project = 'DRYlib'
#copyright = None
author = 'Arto Bendiken'

version = '2018-05-24'
release = '2018-05-24'

# -- General configuration ---------------------------------------------------

needs_sphinx = '1.7'
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
]
templates_path = ['.templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = ['.build', '.themes', 'CHANGES.rst', 'CREDITS.rst', 'README.rst', 'TODO.rst']
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
#html_theme_options = {}
html_static_path = []
html_extra_path = ['.static']
#html_sidebars = {}

# -- Options for HTMLHelp output ---------------------------------------------

htmlhelp_basename = 'drylib'

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    #'pointsize': '10pt', # ('10pt', '11pt' or '12pt').
    #'preamble': '',
    #'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'drylib.tex', project, author, 'manual'),
]

# -- Options for manual page output ------------------------------------------

man_pages = [
    (master_doc, 'drylib', project, [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

texinfo_documents = [
    (master_doc, 'drylib', project,
     author, 'DRYlib', 'One line description of project.',
     'Miscellaneous'),
]

# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

todo_include_todos = True
