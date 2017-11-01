#!/usr/bin/env python3

from netzob.all import *

def modifyMessageByte(m, index, newByte):
    assert isinstance(index,int), "Index is not an integer"
    assert isinstance(newByte,int), "newByte is not an integer"
    if (index +1) > len(m):
        raise ValueError('Index is bigger than byte array length!!')
        return -1
    tmp_data = bytearray(m.data())
    tmp_data[index] = newByte
    return bytes(tmp_data)
    
