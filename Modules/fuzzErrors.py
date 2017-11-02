#!/usr/bin/env python3

from netzob.all import *
from Levenshtein import distance as Ldist
import socket
import copy
import random
import identmsg
from clustering import hamming_byte

def sendTCP_raw_single(m,ip,port):
    """
    sendTCP_raw_singe - same as sendTCP_raw but for single message
    """
    s=socket.socket()
    s.settimeout(1)
    s.connect((ip,port))
    s.send(m.data)
    #print ("RetVal: %s" % s.recv(1000))
    return s.recv(1000)


def sendTCP_raw_bytes(data,ip,port):
    """
    sendTCP_raw_bytes - same as sendTCP_raw_singe but for raw bytes
    """
    s=socket.socket()
    s.settimeout(3)
    s.connect((ip,port))
    s.send(data)
    #print ("RetVal: %s" % s.recv(1000))
    return s.recv(1000)

def createErrorMsgs(messages, ip, port):
    """
    This function gets a sample pcap file and puts random
    bytes inside the all fields. Then sends it to the server.
    It returns all possible error messages in list.
    """
    rspList = list()
    for m in messages.values():
        randomBS = copy.copy(m)
        randomBS_arr = bytearray(randomBS.data)
        for idx,bytInt in enumerate(randomBS_arr):
            randomBS_arr[idx] = random.randint(0,255)
        randomBS = bytes(randomBS_arr)
        try:
            response = sendTCP_raw_bytes(randomBS, ip, port)
            print (response)
            if response not in rspList:
                rspList.append(response)
        except socket.timeout:
            #print("Socket timeout reached.")
            continue
    return rspList

def diff_msg(sym,fi,val,ip,port):
    """
    diff_msg - modify one field to value and get the difference with the original
    return False if timeout or the ratio of change
    param: sym, symbol containing a message with
    param: fi, field index of the field to alter
    param: val, value to replace the field with
    param: ip, port to connect to
    """
    orig=sym.getValues()[0]
    try:
        respOrig=sendTCP_raw_bytes(orig,ip,port)
    except socket.timeout:
        return False

    msg=b''
    for i in range(len(sym.fields)):
        msg+=sym.fields[i].getValues()[0] if fi!=i else val
    try:
        resp=sendTCP_raw_bytes(msg,ip,port)
        print ("Original response:")
        print (orig)
        print ("Fuzzed response:")
        print (resp)
        return hamming_byte(resp,orig)/len(orig)
    except socket.timeout:
        return False

if __name__ == '__main__':
    print('Resemblance C1')
    messages = PCAPImporter.readFile("../S7-Pcap/C1.pcap")
    #print(createErrorMsgs(messages,'157.136.198.69', 102))
    sym=Symbol(messages=messages.values())
    Format.splitAligned(sym)
#    for idx,field in enumerate(sym.fields):
#        if not identmsg.is_static(field):
#            print ("Index %d is dynamic!" % idx)
#            print ("Type is %s" % identmsg.detect_encoding(field))
#            print ("Length is %d" % len(field.getValues()[0]))
        
        #else:
        #    print ("Index %d is dynamic!" % idx)
            #print (field)
    #print (myTup)
    print("The difference is:", diff_msg(sym,11,b'\x03\x00\xff', "157.136.198.69", 102))
"""
Index 1 is dynamic!
Type is BINARY
Length is 4
Index 3 is dynamic!
Type is BINARY
Length is 0
Index 5 is dynamic!
Type is BINARY
Length is 0
Index 7 is dynamic!
Type is BINARY
Length is 1
Index 9 is dynamic!
Type is BINARY
Length is 5
Index 11 is dynamic!
Type is BINARY
Length is 3
Index 13 is dynamic!
Type is BINARY
Length is 1
"""
