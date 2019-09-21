# -*- coding: utf-8 -*-
import datetime as dt
import sys
from pathlib import Path

import pytz

sys.path.insert(0, str(Path.cwd().parent))
from cenv_tool import __version__


NOW = dt.datetime.utcnow()
PROJECT_NAME = 'cenv'
HOMEPAGE = 'https://www.ouroboros.info'


project = PROJECT_NAME
copyright = f'{NOW.year}, Simon Kallfass'
author = 'Simon Kallfass'
version = __version__
release = str(NOW.year)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_autodoc_typehints',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None


html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = f'{PROJECT_NAME}doc'
html_logo = '_static/logo.png'
html_title = PROJECT_NAME
html_short_title = PROJECT_NAME
html_last_updated_fmt = NOW.replace(tzinfo=pytz.utc).isoformat()
html_show_sourcelink = False


html_theme_options = {
    'canonical_url': HOMEPAGE,
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'display_version': True,
}


napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_include_init_with_doc = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_examples = True
napoleon_use_param = True
napoleon_use_keyword = True
napoleon_use_rtype = False
napoleon_use_ivar = True
