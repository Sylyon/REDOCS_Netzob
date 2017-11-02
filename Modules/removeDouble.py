#!/usr/bin/env python3

from netzob.all import *

def removeDouble(aList):
	""" removeDouble
	
	Remove double elment in a list of list
	Args:
		aList (List)         : a list of list
	
	Returns:
		rep 2 (List)         : a list of list

	Authors: Bastien DROUOT

	Date: 02/11/2017 : 14h00
	"""
	rep=list()
	tmp=list()
	for i in aList:
		tmp2=str(i)
		tmp2=tmp2.replace("[","")
		tmp2=tmp2.replace("]","")
		tmp.append(tmp2)
	iComp=0
	for i in tmp:
		aBool=True
		jComp=0
		for j in tmp:
			if iComp != jComp:
				if i in j:
					aBool=False
			jComp=jComp+1
		if aBool:
			rep.append(aList[iComp])
		iComp=iComp+1
	return rep

if __name__ == '__main__':
	L=[[1,2,3],[1,2],[1,1],[4,1,5,1,3,1,4,1,2,1,1,4,5]]
	print(removeDouble(L))