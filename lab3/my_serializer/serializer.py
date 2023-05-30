import inspect
import re
import types

from my_serializer.constants import BASE_TYPES, SIMILAR_COLLECTIONS, CODE_ATTRIBUTES

def serialize(obj):

    if isinstance(obj, tuple(BASE_TYPES.values())):
        return serialize_base_types(obj)

    elif isinstance(obj, types.NoneType):
        return serialize_none_type()

    elif isinstance(obj, tuple(SIMILAR_COLLECTIONS.values())):
        return serialize_similar_collections(obj)

    elif isinstance(obj, dict):
        return serialize_dict(obj)

    elif inspect.isfunction(obj):
        return serialize_function(obj)

    elif inspect.iscode(obj):
        return serialize_code(obj)

    elif isinstance(obj, types.CellType):
        return serialize_cell(obj)

def get_obj_type(obj):
    return re.search(r"\'(\w+)\'", str(type(obj)))[1]

def serialize_base_types(obj):
    srz = dict()

    srz["type"] = get_obj_type(obj)
    srz["value"] = obj
    return srz

def serialize_none_type():
    srz = dict()

    srz["type"] = "NoneType"
    srz["value"] = "definitely none"
    return srz

def serialize_similar_collections(obj):
    srz = dict()

    srz["type"] = get_obj_type(obj)
    srz["value"] = [serialize(item) for item in obj]
    return srz

def serialize_dict(obj):
    srz = dict()

    srz["type"] = get_obj_type(obj)
    srz["value"] = [[serialize(key), serialize(value)] for (key, value) in obj.items()]
    return srz

def serialize_function(obj):
    srz = dict()
    srz["type"] = "function"
    srz["value"] = full_function_serialize(obj)

    return srz

def full_function_serialize(obj, cls=None):
    value = dict()

    value["__name__"] = obj.__name__
    value["__globals__"] = get_globals(obj, cls)
    value["__closure__"] = serialize(obj.__closure__)

    arguments = {key: serialize(value) for key, value in inspect.getmembers(obj.__code__)
                 if key in CODE_ATTRIBUTES}

    value["__code__"] = arguments

    return value


def get_globals(func, cls=None):
    glob = dict()

    for glob_var in func.__code__.co_names:
        if (glob_var in func.__globals__):
            if (isinstance(func.__globals__[glob_var], types.ModuleType)):
                glob["module " + glob_var] = serialize(func.__globals__[glob_var].__name__)

            elif (inspect.isclass(func.__globals__[glob_var])):
                if (cls and func.__globals__[glob_var] != cls) or (not cls):
                    glob[glob_var] = serialize(func.__globals__[glob_var])


            elif (glob_var != func.__code__.co_name):
                glob[glob_var] = serialize(func.__globals__[glob_var])

            # на случай рекурсии
            else:
                glob[glob_var] = serialize(func.__name__)

    return glob

def serialize_code(obj):
    srz = dict()

    srz["type"] = "code"
    srz["value"] = {key: serialize(value) for key, value in inspect.getmembers(obj)
                    if key in CODE_ATTRIBUTES}
    return srz


def serialize_cell(obj):
    srz = dict()

    srz["type"] = "cell"
    srz["value"] = serialize(obj.cell_contents)

    return srz