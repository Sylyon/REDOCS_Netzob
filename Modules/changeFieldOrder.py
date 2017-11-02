#!/usr/bin/env python3

from netzob.all import *


def changeFielddOrder(symbol,fieldNum1,fieldNum2):
	""" changeFielddOrder
	
	Change l'ordre de 2 field dans un symbole, retourne un symbol

	Args:
		symbol     ()   : Le symbol du quel on veut modifier l'ordre des Fields
		fieldNum1  ()   : Le numéro du 1er Field a inverser 
		fieldNum2  ()   : Le numéro du 2nd Field a inverser 

	Returns:
		rep        ()   : Un symbol avec les Fields inverser

	Authors: Bastien DROUOT

	Date: 01/11/2017
	"""
	rep=list()
	i=0
	for field in symbol.fields:
		if i==fieldNum1:
			rep.append(symbol.fields[fieldNum2])
		elif i==fieldNum2:
			rep.append(symbol.fields[fieldNum1])
		else:
			rep.append(field)
		i=i+1
	return rep


if __name__ == '__main__':
	# On construit un message et des field a la main pour facilement tester la fonction changeFielddOrder
	messages = [RawMessage("{0}, what's up in {1} ?".format(pseudo, city)) for pseudo in ['netzob', 'zoby'] for city in ['Paris', 'Berlin']]
	f1 = Field(["netzob", "zoby", "lapy", "sygus"], name="pseudo")
	f2 = Field(", what's up in ", name="whatsup")
	f3 = Field(["Paris", "Berlin", "New-York"], name="city")
	f4 = Field(" ?", name="end")
	symbol = Symbol([f1, f2, f3, f4], messages=messages)

	#On print le symbol avant et après l'inversion des Fields
	for field in symbol.fields:
		print(field)
	for field in changeFielddOrder(symbol,1,3):
		print(field)