from netzob.all import *

def detectIncrement(msgs):
	""" detectIncrement
	
	Detecte if a field incremented

	Args:
		msg                  : A message
	
	Returns:

	Authors: Bastien DROUOT

	Date: 02/11/2017 : 15h10
	"""
	rep=list()
	sym=Symbol(messages=msgs)
	Format.splitAligned(sym)
	for i,field in enumerate(sym.fields): # i = field number
		if i%2: #Si on a un field impaire = non static
			for j,line in enumerate(field.getValues()):#j = line number
				if j<(len(field.getValues())-1): #On ne prend pas la dernier ligne
					for k,elem in enumerate(line): # k = byte number
						if len(field.getValues()[j+1])>k:
							if (elem+1)==(field.getValues()[j+1][k]):
								rep.append((i,j,k))

	return rep


if __name__ == '__main__':
	msgs=PCAPImporter.readFile('../S7-Pcaps/Ws.pcap', bpfFilter='dst port 102').values()
	rep=detectIncrement(msgs)
	for i in rep:
		print("Increment detecter pour la Field n°{0}, de la ligne n°{1} à {2} pour le bit n°{3}".format(i[0],i[1],i[1]+1,i[2]))