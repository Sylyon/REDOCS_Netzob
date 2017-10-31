# -*- coding: utf-8 -*-
import logging
import sys
logging.basicConfig(level=logging.INFO)
sys.path.insert(0, "../../../netzob/src/")

from netzob.all import *
#---------------------------
def sendHTTP(aMessage,ip,port):
	""" Send a message to a HTTP server
	
	Open a chanel, send the message, close the chanel and return the answer from the server

    Args: 
    	aMessage (string) : A message.
    	ip (string)       : The ip adress of the serveur
    	port (int)        : The port of the server

    Returns:

    Authors: Bastien DROUOT

    Date: 31/10/2017 : 9h45
	"""
	channel = TCPClient(remoteIP=str(ip), remotePort=port)
	channel.open()
	channel.write(str.encode(message))
	received_data = channel.read()
	channel.close()
	return received_data

 
if __name__ == '__main__':
	port = 8000
	ip = "127.0.0.1"
	messages = PCAPImporter.readFile("../Exemples/test.pcap").values()
	message = "GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n"
	#Start HTTP server berfor
	#Send message
	print("Message : ")
	print(message)
	print("Answer : ")
	print(sendHTTP(message,ip,port))
	print("Message : ")
	print(messages[0])
	print("Answer : ")
	print(sendHTTP(messages[0],ip,port))