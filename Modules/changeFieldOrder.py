#!/usr/bin/env python3

from netzob.all import *

"""
	On par du symbole déja trié en chant bien défini !!!
"""
def changeFielddOrder(symbol,fieldNum1,fieldNum2):
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
	messages = [RawMessage("{0}, what's up in {1} ?".format(pseudo, city)) for pseudo in ['netzob', 'zoby'] for city in ['Paris', 'Berlin']]
	f1 = Field(["netzob", "zoby", "lapy", "sygus"], name="pseudo")
	f2 = Field(", what's up in ", name="whatsup")
	f3 = Field(["Paris", "Berlin", "New-York"], name="city")
	f4 = Field(" ?", name="end")
	symbol = Symbol([f1, f2, f3, f4], messages=messages)

	for field in symbol.fields:
		print(field)
	for field in changeFielddOrder(symbol,1,3):
		print(field)