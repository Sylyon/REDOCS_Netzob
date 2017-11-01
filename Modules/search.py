#!/usr/bin/env python3

from netzob.all import *
import binascii
import codecs


def searchMessageByte(m, searchQuery):
    searchByte = None
    if isinstance(searchQuery,int):
        searchByte = bytes([searchQuery])
    elif isinstance(searchQuery,str):
        searchByte = searchQuery.encode()
    else:
        searchByte = codecs.encode(searchQuery)
    if len(m.data) < len(searchQuery):
        raise ValueError('Length of search exceeds package')
        return -1
    messageHexStr =binascii.hexlify(m.data).decode("utf-8")
    searchHexStr = binascii.hexlify(searchByte).decode("utf-8")
    
    if searchHexStr in messageHexStr:
        return True
    else:
        return False
