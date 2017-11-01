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

def multiSplitAligned(msgs):
	""" multiSplitAligned
	Perform many splitAligneds and remove eatch time the "strange" messages 
	Args: 
		msg (string)      : List of messages.

	Returns:

	Authors: Bastien DROUOT

	Date: 31/10/2017 : 9h45
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
					if D[aKey][aKey2] > (len(D)/2):
						repIndex=[j for j in range(len(field.getValues())) if field.getValues()[j][:len(aKey2)] == aKey2]
						rep2=list()
						k=0
						for line2 in Symbol(messages=msgs).fields[0].getValues():
							print(k)
							print(repIndex)
							if k in repIndex:
								rep2.append(line2)
							k=k+1
						return rep2
		i=i+1
	return False

if __name__ == '__main__':
	msgs=PCAPImporter.readFile('../S7-Pcap/C1.pcap', bpfFilter='dst port 102').values()
	rep=multiSplitAligned(msgs)
	print(rep)
	"""D=frequent_partial_msg(L)
	print (D)
	for length in D: # we browse for every length found
		print(D[length])
		# get most frequent
		mf=max(D[length],key=lambda x:D[length][x])
		print("most frequent:", mf)"""
