#!/usr/bin/env python3

from netzob.all import *

def sendHTTP(aMessage,ip,port):
	""" Send a message to a HTTP server
	
	Open a chanel, send the message wait the answer, close the chanel and return the answer from the server

    Args: 
    	aMessage (string)      : A message.
    	ip (string)            : The ip adress of the serveur
    	port (int)             : The port of the server

    Returns:
    	received_data (list)   : A list of the answers of the server

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
	#Le port du serveur HTTP
	port = 8000
	#Adresse Ip du serveur HTTP (ici localhost)
	ip = "127.0.0.1"

	#On crée un message HTTP
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
