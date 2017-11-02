#!/usr/bin/env python3

from netzob.all import *
from Levenshtein import distance as Ldist
import socket

def sendTCP_raw(msgs,ip,port):
    """
    sendTCP_raw - same as sendTCP but without Symbol processing 
                  or channel initialization (thus _much_ faster)
    """
    s=socket.socket()
    s.connect((ip,port))
    r=[]
    for m in msgs:
        s.send(m.data)
        r.append(s.recv(1000))
    return r

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
#    try:
#    retVal = s.recv(1000))

def statelessMsgs(messages, repeatCount, ip, port):
    msgList = list()
    for m in messages.values():
        rspList = list()
        for i in range(repeatCount):
            try:
                response = sendTCP_raw_single(m, ip, port)
                rspList.append(response)
            except socket.timeout:
                #print("Socket timeout reached.")
                pass
        if len(rspList) == len(set(rspList)):
            msgList.append(m)
    return msgList

if __name__ == '__main__':
    print('Resemblance C1')
    messages = PCAPImporter.readFile("../S7-Pcaps/C1.pcap")
    print(statelessMsgs(messages,10,'157.136.198.69', 102))
