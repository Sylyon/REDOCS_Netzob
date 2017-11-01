#!/usr/bin/env python3

from netzob.all import *

def multiSplitAligned(msgs):
	""" multiSplitAligned
	Perform many splitAligneds and remove eatch time the "strange" messages 
	Args: 
		msg (string)      : List of messages.

	Returns:

	Authors: Bastien DROUOT

	Date: 01/11/2017 : 11h00
	"""
	sym=Symbol(messages=msgs)
	Format.splitAligned(sym)
	i=0
	for field in sym.fields:
		if i%2:
			#Si i est impaire = si field est non static
			if i>4:
				rep=list() # Liste de ligne
				for line in field.getValues():
					tmp=list() # Liste de chaque octé d'une ligne
					for elem in line:
						tmp.append(elem)
					rep.append(tmp)
				#TODO
				break
		i=i+1
	return True

if __name__ == '__main__':
	msgs=PCAPImporter.readFile('../S7-Pcap/C1.pcap', bpfFilter='dst port 102').values()
	multiSplitAligned(msgs)