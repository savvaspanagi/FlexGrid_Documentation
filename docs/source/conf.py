# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup: import flexgridpy from sibling FlexGridPy repo (local builds)
_flexgridpy_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..', 'FlexGridPy')
)
if os.path.isdir(_flexgridpy_root):
    sys.path.insert(0, _flexgridpy_root)

# -- Project information

project = 'FlexGridPy'
copyright = '2025, EAC / SPS-LAB'
author = 'Savvas Panagi'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
]

autosummary_generate = True

autodoc_default_options = {
    'members': True,
    'undoc-members': False,
    'show-inheritance': True,
    'member-order': 'bysource',
}

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pandapower': ('https://pandapower.readthedocs.io/en/latest/', None),
    'pyomo': ('https://pyomo.readthedocs.io/en/stable/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'
