#!/usr/bin/env python3

from netzob.all import *
from collections import Counter
import copy

def frequent_partial_msg(L):
	"""
	frequent_partial_msg - get the frequency of beginning of the messages
	return a dictionnary with the histograms for each lenth
	param: list of raw messages
	"""
	d,r={},{} # two dict to avoid 'RuntimeError: dictionary changed size during iteration'
	for l in range(2,max([len(x) for x in L])):
		d[l]=dict(Counter([x[:l] for x in L if len(x)>=l]))
		# get rid of unique items
		r[l]=copy.copy(d[l]) 
		for k in d[l]:
			if d[l][k]<2: r[l].pop(k)
		if r[l]=={}: r.pop(l)
	return r

def shappingToSplitAligned(msgs):
	""" shappingToSplitAligned
	Perform a splitAligneds and remove eatch time the "strange" messages
	Take messages and return messages 
	Args: 
		msg (string)                     : List of messages.

	Returns:
		(rep2,rep3) (string,string)      : 2 List of message sort to be splitAligned more effeciently.

	Authors: Bastien DROUOT

	Date: 02/11/2017 : 10h20
	"""
	sym=Symbol(messages=msgs)
	Format.splitAligned(sym)
	i=0
	for field in sym.fields:
		if i%2:
			#Si i est impaire = si field est non static
			rep=list() # Liste de ligne
			for line in field.getValues():
				rep.append(line)
			D=frequent_partial_msg(rep)
			keys=list(D.keys())
			keys.reverse()
			for aKey in keys:
				for aKey2 in D[aKey].keys():
					if D[aKey][aKey2] > (len(rep)/2):
						repIndex=[j for j in range(len(field.getValues())) if field.getValues()[j][:len(aKey2)] == aKey2]
						rep2=list()
						rep3=list()
						k=0
						print(repIndex)
						for line2 in Symbol(messages=msgs).fields[0].getValues():
							if k in repIndex:
								rep2.append(RawMessage(line2))
							else:
								rep3.append(RawMessage(line2))
							k=k+1
						return (rep2,rep3)
		i=i+1
	return (msgs, msgs)

if __name__ == '__main__':
	msgs=PCAPImporter.readFile('../S7-Pcaps/Ws_U3.pcap', bpfFilter='dst port 102').values()

	(shap,other)=shappingToSplitAligned(msgs)
	
	sym=Symbol(messages=msgs)
	Format.splitAligned(sym)
	sym2=Symbol(messages=shap)
	Format.splitAligned(sym2)
	sym3=Symbol(messages=other)
	Format.splitAligned(sym3)
	i=0
	for field in sym.fields:
		print(field)
		if i<len(sym2.fields):
			print(sym2.fields[i])
		if i<len(sym3.fields):
			print(sym3.fields[i])
		print('##########################')
		i=i+1
