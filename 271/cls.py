import inspect


def get_classes(mod):
    """Return a list of all classes in module 'mod'"""
    return [name for name, obj in inspect.getmembers(mod) if inspect.isclass(obj) and name[0].isupper()]
