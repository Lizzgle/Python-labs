
BASE_TYPES = {"str": str, "int": int, "bool": bool, "float": float, "complex": complex}

BASE_COLLECTIONS = {"list": list, "tuple": tuple, "frozenset": frozenset, "set": set, "bytes": bytes,
                    "bytearray": bytearray, "dict": dict}

SIMILAR_COLLECTIONS = {"list": list, "tuple": tuple, "frozenset": frozenset, "set": set, "bytes": bytes,
                       "bytearray": bytearray}

CODE_ATTRIBUTES = ("co_argcount",
                    "co_posonlyargcount",
                    "co_kwonlyargcount",
                    "co_nlocals",
                    "co_stacksize",
                    "co_flags",
                    "co_code",
                    "co_consts",
                    "co_names",
                    "co_varnames",
                    "co_filename",
                    "co_name",
                    #"co_qualname",
                    "co_firstlineno",
                    "co_lnotab",
                    #"co_exceptiontable",
                    "co_freevars",
                    "co_cellvars")