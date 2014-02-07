from importlib import import_module

from satest.model import meta
from satest.util import to_underscore_style, AttrDict

__all__ = ['init_model', 'import_models']


def init_model(engine):
    meta.Session.configure(bind=engine)


def import_models(*models):
    imports = AttrDict()
    for model in models:
        module_name = to_underscore_style(model)
        module = import_module('.' + module_name, __package__)
        imports[model] = getattr(module, model)
    return imports
