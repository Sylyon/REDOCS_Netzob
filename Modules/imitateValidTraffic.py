#!/usr/bin/env python3

from netzob.all import *
from Levenshtein import distance as Ldist
import socket

def sendTCP(msgs,ip,port):
	""" Send a message to a server
	
	Open a chanel, send the message, close the chanel and return the answer from the server

	Args: 
		msgs (string)     : The messages capture in the pcap.
		ip (string)       : The ip adress of the serveur
		port (int)        : The port of the server

	Returns:

	Authors: Bastien DROUOT

	Date: 01/11/2017 : 11h45
	"""
	sym=Symbol(messages=msgs)
	received_datas=list()
	channel = TCPClient(remoteIP=str(ip), remotePort=port)
	channel.open()
	for field in sym.fields:
		for b in field.getValues():
			channel.write(b)
			received_datas.append(channel.read())
	channel.close()
	return received_datas

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

def ressemblance(fileRoute):
	""" Ressemblance
	
	Donne la resemblance le rejeu et la réponce 
	Args:
		fileRoute (string)   : Le chemin du fichier pcapc

	Returns:
		rep 2 (List)         : La resemblance du message recut et du message attendu ( chaque element de la list représent la distance Levenshtein entre les messages)

	Authors: Bastien DROUOT

	Date: 01/11/2017 : 15h00
	"""
	port = 102
	ip = "157.136.198.69"
	msgs=PCAPImporter.readFile(fileRoute, bpfFilter='dst port 102').values()
	rep1=sendTCP_raw(msgs,ip,port)
	msgs=PCAPImporter.readFile(fileRoute, bpfFilter='src port 102').values()
	sym=Symbol(messages=msgs)
	rep2=list()
	i=0
	for field in sym.fields:
		for b in field.getValues():
			rep2.append(Ldist(rep1[i],b)*100/len(b))
			i=i+1
	return rep2

if __name__ == '__main__':
	print('Resemblance C1')
	print(ressemblance('../S7-Pcaps/C1.pcap'))
	print('Resemblance R1')
	print(ressemblance('../S7-Pcaps/R1.pcap'))
	print('Resemblance W1')
	print(ressemblance('../S7-Pcaps/W1.pcap'))
	print('Resemblance Rs')
	print(ressemblance('../S7-Pcaps/Rs.pcap'))
	print('Resemblance Ws')
	print(ressemblance('../S7-Pcaps/Ws.pcap'))
