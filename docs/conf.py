# -*- coding: utf-8 -*-
#
# Read the Docs Template documentation build configuration file, created by
# sphinx-quickstart on Tue Aug 26 14:19:49 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
from sphinx.ext.autosummary import Autosummary
from sphinx.ext.autosummary import get_documenter
from docutils.parsers.rst import directives
from sphinx.util.inspect import safe_getattr
import re

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

xobjects_branch = 'main'
xfields_branch = 'main'
xtrack_branch = 'main'
xpart_branch = 'main'
xdeps_branch = 'main'
xmask_branch = 'main'

os.system(
    f'git clone --single-branch --branch {xobjects_branch} '
    'https://github.com/xsuite/xobjects')
os.system(
    f'git clone --single-branch --branch {xfields_branch} '
    'https://github.com/xsuite/xfields')
os.system(
    f'git clone --single-branch --branch {xtrack_branch} '
    'https://github.com/xsuite/xtrack')
os.system(
    f'git clone --single-branch --branch {xpart_branch} '
    'https://github.com/xsuite/xpart')
os.system(
    f'git clone --single-branch --branch {xdeps_branch} '
    'https://github.com/xsuite/xdeps')
os.system(
    f'git clone --single-branch --branch {xmask_branch} '
    'https://github.com/xsuite/xmask')

sys.path.insert(0, os.path.abspath('./xobjects'))
sys.path.insert(0, os.path.abspath('./xtrack'))
sys.path.insert(0, os.path.abspath('./xfields'))
sys.path.insert(0, os.path.abspath('./xpart'))
sys.path.insert(0, os.path.abspath('./xdeps'))
import xobjects
import xfields
import xtrack
import xpart
import xdeps

### GENERATE code snippets
snippet_files = {
    'xpart/examples/particles_generation/000_basics.py':
        'generated_code_snippets/basics_part.py',
    'xpart/examples/particles_generation/001a_build_particles_set.py':
        'generated_code_snippets/build_particles_set.py',
    'xpart/examples/particles_generation/001at_build_particles_set_with_tracker.py':
        'generated_code_snippets/build_particles_set_with_tracker.py',
    'xpart/examples/particles_generation/001b_build_particles_shift.py':
        'generated_code_snippets/build_particles_shift.py',
    'xpart/examples/particles_generation/001bt_build_particles_shift_with_tracker.py':
        'generated_code_snippets/build_particles_shift_with_tracker.py',
    'xpart/examples/particles_generation/001c_build_particles_normalized.py':
        'generated_code_snippets/build_particles_normalized.py',
    'xpart/examples/particles_generation/006_match_at_element.py':
        'generated_code_snippets/match_at_element.py',
    'xpart/examples/particles_generation/003_pencil.py':
        'generated_code_snippets/pencil.py',
    'xpart/examples/particles_generation/004_generate_gaussian.py':
        'generated_code_snippets/gaussian.py',
    'xpart/examples/particles_generation/002_halo.py':
        'generated_code_snippets/halo.py',
    'xpart/examples/save_and_load/000_to_from_dict.py':
        'generated_code_snippets/to_from_dict.py',
    'xpart/examples/save_and_load/001_save_load_json.py':
        'generated_code_snippets/save_load_json.py',
    'xpart/examples/save_and_load/002_save_load_pickle.py':
        'generated_code_snippets/save_load_pickle.py',
    'xpart/examples/save_and_load/003_save_load_with_pandas.py':
        'generated_code_snippets/save_load_with_pandas.py',
    'xpart/examples/merge_copy_filter/000_merge.py':
        'generated_code_snippets/merge.py',
    'xpart/examples/merge_copy_filter/001_copy.py':
        'generated_code_snippets/copy.py',
    'xpart/examples/merge_copy_filter/002_filter.py':
        'generated_code_snippets/filter.py',
    'xtrack/examples/spacecharge/000_spacecharge_example.py':
        'generated_code_snippets/spacecharge.py',
    'xtrack/examples/acceleration/000_acceleration.py':
        'generated_code_snippets/acceleration.py',
    'xtrack/examples/collimation/001_loss_location_refinement.py':
        'generated_code_snippets/loss_location_refinement.py',
    'xtrack/examples/collimation/003_all_together.py':
        'generated_code_snippets/beam_interaction.py',
    'xtrack/examples/twiss/000_twiss.py':
        'generated_code_snippets/twiss.py',
    'xtrack/examples/twiss/003_match_tune_chroma.py':
        'generated_code_snippets/match_tune_chroma.py',
    'xtrack/examples/twiss/003b_match_4c_bump.py':
        'generated_code_snippets/match_4c_bump.py',
    'xtrack/examples/twiss/008_4d_twiss_and_particle_match.py':
        'generated_code_snippets/method_4d.py',
    'xtrack/examples/twiss/011_tune_vs_delta.py':
        'generated_code_snippets/tune_vs_delta.py',
    'xtrack/examples/twiss/017_table_slicing.py':
        'generated_code_snippets/table_slicing.py',
    'xtrack/examples/footprint/000_footprint.py':
        'generated_code_snippets/footprint.py',
    'xtrack/examples/to_json/000_lattice_to_json.py':
        'generated_code_snippets/tojson.py',
    'xtrack/examples/knobs/001_lhc.py':
        'generated_code_snippets/expressions.py',
    'xtrack/examples/pyheadtail_interface/004_imped_spacech_cpu_gpu.py':
        'generated_code_snippets/combined_cpu_gpu.py',
    'xtrack/examples/monitor/000_example_quick_monitor.py':
        'generated_code_snippets/quick_monitor.py',
    'xtrack/examples/monitor/001_example_custom_monitor.py':
        'generated_code_snippets/custom_monitor.py',
    'xtrack/examples/monitor/002_example_custom_monitor_multiframe.py':
        'generated_code_snippets/multiframe_monitor.py',
    'xtrack/examples/monitor/003_monitors_as_beam_elements.py':
        'generated_code_snippets/monitors_as_beam_elements.py',
    'xtrack/examples/monitor/004_monitor_standalone.py':
        'generated_code_snippets/monitor_standalone.py',
    'xtrack/examples/radiation/005_radiation_example.py':
        'generated_code_snippets/radiation.py',
    'xtrack/examples/element_internal_record/000_internal_record.py':
        'generated_code_snippets/internal_record.py',
    'xtrack/examples/element_internal_record/001_multirecord.py':
        'generated_code_snippets/internal_multirecord.py',
    'xtrack/examples/element_internal_record/002_record_in_individual_element.py':
        'generated_code_snippets/internal_record_standalone.py',
    'xtrack/examples/multisetter/000_sps_50hz_ripple.py':
        'generated_code_snippets/ripple.py',
    'xtrack/examples/tapering/000_taper.py':
        'generated_code_snippets/taper.py',
    'xtrack/examples/freeze_longitudinal/000_freeze_unfreeze_explicit.py':
        'generated_code_snippets/freeze_unfreeze_explicit.py',
    'xtrack/examples/freeze_longitudinal/001_freeze_context_manager.py':
        'generated_code_snippets/freeze_freeze_context_manager.py',
    'xtrack/examples/freeze_longitudinal/002_freeze_individual_methods.py':
        'generated_code_snippets/freeze_individual_methods.py',
    'xtrack/examples/optimized_tracker/000_optimized_tracker.py':
        'generated_code_snippets/optimized_tracker.py',
    'xmask/examples/hllhc14_collision/000_build_collider_from_mad_model.py':
        'generated_code_snippets/build_collider_from_mad_model.py',
    'xmask/examples/hllhc14_collision/001_install_beambeam.py':
        'generated_code_snippets/install_beambeam.py',
    'xmask/examples/hllhc14_collision/002_knobs_and_tuning.py':
        'generated_code_snippets/knobs_and_tuning.py',
    'xmask/examples/hllhc14_collision/003_configure_beambeam.py':
        'generated_code_snippets/configure_beambeam.py',
    'xmask/examples/hllhc15_collision/004_footprint.py':
        'generated_code_snippets/footprint_with_bb.py',
}

for ss, tt in snippet_files.items():
    with open(ss, 'r') as fid:
        cc = fid.read()

    cc = cc.split('#!end-doc-part')[0]
    cc = cc.strip()

    lines = cc.split('\n')
    lines = [ll for ll in lines if '#!skip-doc' not in ll]

    # Remove copyright statement if present
    comment_char = '#'
    if (len(lines) > 0 and
        lines[0].startswith(comment_char + ' ' + 'copyright ##')):
        for ill, ll in enumerate(lines):
            assert ll.startswith(comment_char)
            if ll.startswith(comment_char + ' ' + '########'):
                end_cpright = ill
                break
        lines = lines[end_cpright+1:]

    # Remove empty lines at the beginning
    while len(lines) > 0 and lines[0].strip() == '':
        lines = lines[1:]

    cc = '\n'.join(lines)

    with open(tt, 'w') as fid:
        fid.write(cc)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.doctest',
              'sphinx.ext.extlinks',
              'sphinx.ext.intersphinx',
              'sphinx.ext.mathjax',
              'sphinx.ext.napoleon',
              #'sphinx.ext.linkcode'
              ]

# Add any paths that contain templates here, relative to this directory.ls 
templates_path = ['_templates']

autosummary_generate = True
autosummary_generate_overwrite = True

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Xsuite'
copyright = u'2021, CERN'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.2.1'
# The full version, including alpha/beta/rc tags.
release = '0.2.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_logo = "figures/xsuite-alpha-long.png"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'ReadtheDocsTemplatedoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'ReadtheDocsTemplate.tex', u'Read the Docs Template Documentation',
   u'Read the Docs', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'readthedocstemplate', u'Read the Docs Template Documentation',
     [u'Read the Docs'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'ReadtheDocsTemplate', u'Read the Docs Template Documentation',
   u'Read the Docs', 'ReadtheDocsTemplate', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

autoclass_content = 'both'

# The below class allows us to display an automatically generated table of
# methods and attributes for a class.
# Adapted from https://stackoverflow.com/a/30783465
class AutoAutoSummary(Autosummary):

    option_spec = {
        'methods': directives.unchanged,
        'attributes': directives.unchanged
    }

    required_arguments = 1

    def get_members(self, obj, typ, include_public=None):
        if not include_public:
            include_public = []
        items = []
        for name in obj.__dict__.keys():
            try:
                documenter = get_documenter(self.env.app, safe_getattr(obj, name), obj)
            except AttributeError:
                continue
            if documenter.objtype == typ:
                items.append(name)
        public = [x for x in items if x in include_public or not x.startswith('_')]
        return public, items

    def run(self):
        clazz = str(self.arguments[0])
        try:
            (module_name, class_name) = clazz.rsplit('.', 1)
            m = __import__(module_name, globals(), locals(), [class_name])
            c = getattr(m, class_name)
            if 'methods' in self.options:
                _, methods = self.get_members(c, 'method', ['__init__'])

                self.content = ["~%s.%s" % (clazz, method) for method in methods if not method.startswith('_')]
            if 'attributes' in self.options:
                _, attribs = self.get_members(c, 'attribute')
                self.content = ["~%s.%s" % (clazz, attrib) for attrib in attribs if not attrib.startswith('_')]
        finally:
            return super(AutoAutoSummary, self).run()

def setup(app):
    app.add_directive('autoautosummary', AutoAutoSummary)
