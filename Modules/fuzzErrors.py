#!/usr/bin/env python3

from netzob.all import *
from Levenshtein import distance as Ldist
import socket
import copy
import random

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

if __name__ == '__main__':
    print('Resemblance C1')
    messages = PCAPImporter.readFile("../S7-Pcap/C1.pcap")
    print(createErrorMsgs(messages,'157.136.198.69', 102))
