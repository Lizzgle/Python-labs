import re
import types

from my_serializer.constants import BASE_TYPES

def serialize(obj):

    if isinstance(obj, tuple(BASE_TYPES.values())):
        return serialize_base_types(obj)

    elif isinstance(obj, types.NoneType):
        return serialize_none_type()

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
