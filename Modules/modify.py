#!/usr/bin/env python3

from netzob.all import *
import copy

def modifyMessageByte(m, index, newByte):
    assert isinstance(index,int), "Index is not an integer"
    assert isinstance(newByte,int), "newByte is not an integer"
    if (index +1) > len(m.data):
        raise ValueError('Index is bigger than byte array length!!')
        return -1
    tmp_data = bytearray(m.data)
    tmp_data[index] = newByte
    retM = copy.copy(m)
    retM.data = tmp_data
    return retM

