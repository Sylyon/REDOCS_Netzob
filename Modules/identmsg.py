from netzob.all import *
import string
import struct

def is_static(field):
    """
    is_static - tell whether the field is static, i.e every value are identical
    return a boolean
    param: field as obtained with symbol.fields[i]
    """
    l=field.getValues()
    for v in l:
        if v!=l[0]:
            return False
    return True

def detect_encoding(field):
    """
    detect_encoding - give possible type
    return type
    param: field as obtained with symbol.fields[i]
    """
    v=field.getValues()
    data=b''.join([m for m in v])
    if len([c for c in data if chr(c) in string.printable])==len(data):
        return "TEXT"
    if is_static(field):
        st={2:"H",4:"I",8:"L"}
        lv=len(v[0])
        if lv in [2,4,8]:
            N=[struct.unpack(">"+st(lv),x)[0] for x in v]
            return ("%dbits INTEGER[%d,%d] or BINARY" % (len(lv)*8, min(N), max(N)))
    else:
        return "BINARY"

def get_shape(sym):
    """
    get_shape - shape of a symbol in the form
                ((STATIC, BINARY), (DYNAMIC, TEXT), ...)
    param: symbol to analyse
    return shape tuple
    """
    return tuple([("STATIC" if is_static(f) else "DYNAMIC", detect_encoding(f)) for f in sym.fields])

def is_shape(sym,shape):
    """
    is_shape - tell whether the symbol is of the shape shape
    return boolean
    param: symbol and shape obtain by get_shape
    """
    return get_shape(sym)==shape
