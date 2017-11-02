#!/usr/bin/env python3

from netzob.all import *
from Levenshtein import distance as Ldist
import socket
import copy
import random
import identmsg
from clustering import hamming_byte
import difflib
import binascii
from termcolor import colored
import time
import os

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
        original = str(orig).partition("'")[-1].rpartition("'")[0] 
        modified = str(msg).partition("'")[-1].rpartition("'")[0]
        print("The difference between original & \"modified\" REQUESTs:")
        print(original)
        print(show_diff(original, modified))
        print()
        resp=sendTCP_raw_bytes(msg,ip,port)
        #print ("Original response:")
        #print (orig)
        #print ("Fuzzed response:")
        #print (resp)
        return (hamming_byte(resp,orig)/len(orig), orig, resp)
    except socket.timeout:
        return False

def show_diff(text, n_text):
    """
    Unify operations between two compared strings seqm is a difflib.
    SequenceMatcher instance whose a & b are strings
    """
    seqm = difflib.SequenceMatcher(None, text, n_text)
    output= []
    for opcode, a0, a1, b0, b1 in seqm.get_opcodes():
        if opcode == 'equal':
            output.append(seqm.a[a0:a1])
        elif opcode == 'insert':
            output.append(colored(seqm.b[b0:b1],'red'))
        elif opcode == 'delete':
            output.append(colored(seqm.a[a0:a1],'blue'))
        elif opcode == 'replace':
            output.append(colored(seqm.b[b0:b1],'green'))
    return ''.join(output)

if __name__ == '__main__':
    os.system('clear')
    whatIsthis = """
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,@@@,@@@@@,@@#,@@@@@@@,@@@@@@@,,@@@@@@,@@@@,,,,,,,,(@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,@@,,@@@@@,,@#,,@@@@@,,,@@@@@,,,,@@@@@,,,(@,,,,,,,,@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,@*,,@@@@@,,@/,,@@@@@,,,@@@@@,,,,@@@@@,,@,,,,,,,,,,@@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,@@@@@,,,,,,@@@@@,@@@@@@@,,,,@@@@@,@@,,,,,,,,,,*@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,@@@@@,,,,,,@@@@@,,,@@@@@,,,,@@@@@,,@,,,,,,,,,,,@@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,@@@@@,,,,,,@@@@@,,,@@@@@,,,,@@@@@,,,,@,,,,,,@,,#@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,@@@@@,,,,,,@@@@@,,,@@@@@,,,,@@@@@,,,@@,,,,,@@,,,@@@@@@@@@@@@@@@@/,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,%%%%%%#,,,,(%%%%%%,%%%%%%/,,%%%%%%,%%%%,,,,*@@&,,&@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@,,,@@@@@@@@@@@@@@@@/,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*@@@&,,,@@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@,,,,,@@@@@@@@@@@@@@@@*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,(@@@%,,,,,@@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@,,,,,,,@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@*,,,,,,,@@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@,,,,,,,,/@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@,,,,,,,,,,@@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@,,,,,,,,,,%@@@@@@@@@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@,,,@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,,,,@@@*@@@@%&@@,,@@@@@&*@@@@,,,,,,@@@@@,,,,*@@@@@@,,,&@@@@@,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@,,*@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,,,,@&,*@@@@%,/@,,,@@@@@,,,@@,,,,,*@@@@@,,,,,,@@@@@(,*&@@@@,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@,,,,,,,,,,,,,,@@@@@@@@@@@@@@@@@,,,,,,,,,@,,*@@@@%,,@,,,@@@@@,,@,,,,,,,@,@@@@@,,,,,,@@@@@,(&@@@@,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,/@@@%,,,,,,,,,,,,,,@@@@@@@@@@@@@@@@@,,,@@@@@*,,,*@@@@%,,,,,,@@@@&/@@,,,,,,@*,@@@@@,,,,,@,@@@@@*&@@@@,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*@@@@*,,,,,,,,,,,,,,,@@@@@@@@@@@@@@@@&,,,,,,,,,,,*@@@@%,,,,,,@@@@@,,@,,,,,,@,,,@@@@@,,,,@,@@@@@,&@@@@,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@@@@*,,,,,,,,,,,,,,@@@@@@@@@@@@@@@@@,,,,,,,,,,,*@@@@%,,,,,,@@@@@,,,,@,,,@,@@@@@@@@,,,,@,,@@@,,&@@@@,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,#@@@@@@@@@@@@@@,,,,,,,,@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,,*@@@@%,,,,,,@@@@&,,(@@,,&@,,,,*@@@@@,,,@&,,@&,,@@@@@,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,(@@@@@@@@@@@@@@,,,,,,,,@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,,//////*,,,,//////*////,////,,,//////*,///*,/,,*//////,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,Onur,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,Bastien,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,Paul,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,Florent,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    """
    print(whatIsthis)
    time.sleep(1)
    print('# DEMO: Impact of the Fields')
    time.sleep(1)
    print()
    print('-- Importing sample network traffic for S7... ',end='')
    messages = PCAPImporter.readFile("../S7-Pcaps/C1.pcap")
    time.sleep(3)
    print('done!')
    #print(createErrorMsgs(messages,'157.136.198.69', 102))
    print('-- Splitting into fields w/ %s method... ' % colored('Netzob','cyan'),end='')
    sym=Symbol(messages=messages.values())
    Format.splitAligned(sym)
    time.sleep(3) 
    print('done!')
    print('-- Determining static and dynamic fields: ')
    time.sleep(2)
    for idx,field in enumerate(sym.fields[:-1]):
        print()
        typField = identmsg.detect_encoding(field)
        if typField is None:
            typField = "BINARY"
        if not identmsg.is_static(field):
           print ("DYNAMIC       Type: %s" % typField)
        else:
            print ("STATIC        Type: %s" % typField)
            #print ("Length is %d" % len(field.getValues()[0]))
        print ("%d. " % idx,end='')
        print(field)
        time.sleep(1)
        #else:
        #    print ("Index %d is dynamic!" % idx)
    #print (myTup)
            #print (field)
    print()
    print("### Chosing the %s!" % colored("Field 11", attrs = ['bold']))
    print("-- Preparing and sending the requests...")
    time.sleep(3)
    diff_perc, orig, resp = diff_msg(sym,11,b'\x03\x00\xff', "157.136.198.69", 102)
    original = str(orig).partition("'")[-1].rpartition("'")[0]
    modified = str(resp).partition("'")[-1].rpartition("'")[0]
    time.sleep(3)
    print("# The difference between original & \"modified\" RESPONSEs:")
    print(original)
    print(show_diff(original, modified))
    print()
    time.sleep(3)
    print("# The difference in bytes is:", diff_perc)
    time.sleep(2)
    print()
    print ("- Au revoir!")
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
