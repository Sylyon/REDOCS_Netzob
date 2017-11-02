from netzob.all import *

def is_static(field):
    """
    is_static - tell whether the field is static, i.e every value are identical
    return a boolean
    param: field as obtained with symbol.fields[i]
    """
    l=field.getValues():
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
    data=b''.join([m.data for m in v])
    if len([c in string.printable for c in data])==len(data):
        return "TEXT"
    if is_static(field):
        st={2:"H",4:"I",8:"L"}
        if len(v[0]) in [2,4,8]:
            N=[struct.unpack(">"+,x)[0] for x in v]
            print("%dbits INTEGER : min=%d, max=%d, mean=%f" % (len(v[0])*8, min(N), max(N), sum(N)/len(N)))
            return "INTEGER OR BINARY"
    else:
        return "BINARY"

