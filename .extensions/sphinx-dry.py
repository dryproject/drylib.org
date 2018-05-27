# -*- coding: utf-8 -*-
#
# Sphinx extension for generating the DRYlib documentation.
#
# Written by Arto Bendiken <http://ar.to/>.
#
# This is free and unencumbered software released into the public domain.

import re

from docutils import nodes
from sphinx import addnodes
from sphinx.directives import ObjectDescription
from sphinx.domains import Domain, ObjType
from sphinx.locale import l_, _

class DRYObject(ObjectDescription):
    def handle_signature(self, sig, sig_node):
        result = self.describe_signature(sig, sig_node) # TODO
        if result is None:
            return sig
        return result

    def describe_signature(self, _sig, _sig_node):
        # type: (unicode, addnodes.desc_signature) -> None
        raise NotImplementedError()

    def add_target_and_index(self, name, sig, sig_node):
        target_name = '%s-%s' % (self.objtype, name) # for <a href="..."
        if target_name not in self.state.document.ids:
            sig_node['names'].append(target_name)
            sig_node['ids'].append(target_name)
            sig_node['first'] = (not self.names)
            self.state.document.note_explicit_target(sig_node)

            objects = self.env.domaindata[self.domain]['objects']
            key = (self.objtype, name)
            if key in objects:
                self.state_machine.reporter.warning(
                    'duplicate definition of %s %s, ' % (self.objtype, name) +
                    'other instance in ' + self.env.doc2path(objects[key]),
                    line=self.lineno)
            objects[key] = self.env.docname
        index_text = self.get_index_text(self.objtype, name)
        if index_text:
            self.indexnode['entries'].append(('single', index_text, target_name, '', None))

    def make_namespace_prefix(self, name):
        return addnodes.desc_addname(name, name)

    def make_parameter_list(self, *params):
      result = addnodes.desc_parameterlist()
      for param in params:
          result += addnodes.desc_parameter(param, param, noemph=True)
      return result

def make_directive(directive_name, namespace_separator=None):
    class DRYDirective(DRYObject):
        def get_index_text(self, _objtype, name):
            domain_label = self.env.domains[self.domain].label
            return _('%s (%s %s)') % (name, domain_label, directive_name)

        def describe_signature(self, sig, sig_node):
            directive_annot = directive_name + ' '
            sig_node += addnodes.desc_annotation(directive_annot, directive_annot)

            if namespace_separator is not None:
                namespace_prefix = self.env.ref_context.get('dry:namespace')
                if namespace_prefix is not None:
                    sig_node += self.make_namespace_prefix(namespace_prefix + namespace_separator)

            sig_node += addnodes.desc_name(sig, sig)

    return DRYDirective

def make_namespace_directive(directive_name):
    class DRYNamespaceDirective(make_directive(directive_name, None)):
        def run(self):
            env = self.state.document.settings.env
            env.ref_context['dry:namespace'] = self.arguments[0].strip()
            return super().run()

    return DRYNamespaceDirective

class DRYModuleObject(make_namespace_directive('module')):
    pass

class DRYFunctionObject(make_directive('function')):
    pass

class DRYTypeObject(make_directive('type')):
    pass

class DRYDomain(Domain):
    """DRY domain."""

    name, label = 'dry', l_('DRY')
    object_types = {
      'module':   ObjType(l_('module'),   'module'),
      'function': ObjType(l_('function'), 'function'),
      'type':     ObjType(l_('type'),     'type'),
    }
    directives = {
      'module':   DRYModuleObject,
      'function': DRYFunctionObject,
      'type':     DRYTypeObject,
    }
    roles = {}
    initial_data = {
      'objects': {},  # (objtype, name) -> docname
    }
    data_version = 0 # bump this when the format of self.data changes

def setup(app):
    # See: http://www.sphinx-doc.org/en/stable/extdev/appapi.html
    app.require_sphinx('1.7')
    app.add_domain(DRYDomain)
    return {'version': '0.0.0', 'parallel_read_safe': True}
