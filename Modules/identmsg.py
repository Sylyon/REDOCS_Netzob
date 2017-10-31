from netzob.all import *

"""# we extract from the pcap every message which is going to 8000, i.e. the client messages 
msgs=PCAPImporter.readFile('../Exemples/test.pcap', bpfFilter='dst port 8000').values()

print("All messages:")
for i in range(0,len(msgs)-1):
    print(msgs[i])
sym=Symbol(messages=msgs)"""


def staticmessage(msgs):
	result= True
	m=len(msgs[0].data)
	for i in range(1,len(msgs)):
		if (m!=len(msgs[i].data)):
			result= False
	return result
"print(staticmessage(msgs))"
def staticfield(sym):
	result=True
	"print(len(sym.fields[0]))"
	"""print(sym.fields[0].getValues())
	
	for s in sym.fields:
		print(s)"""
	L=[]
	for i in range(0,len(sym.fields)):
		a=len(sym.fields[i].getValues()[0])
		"""print("etalon=")
		print(a)"""
		for j in range(1,len(sym.fields[i].getValues())):
			if(len(sym.fields[i].getValues()[j])!=a):
				"""print("taille champ")
				print(len(sym.fields[i].getValues()[j]))"""
				result=False
		L.append(Result)
	return L

def Binfield(sym):
	"print(len(sym.fields[0]))"
	"""print(sym.fields[0].getValues())
	
	for s in sym.fields:
		print(s)"""
	L=[]
	for i in range(0,len(sym.fields)):
		result=False
		for j in range(1,len(sym.fields[i].getValues())):
			for k in range(0,len(sym.fields[i].getValues()[j])):
				"print(sym.fields[i].getValues()[j][k])"
				if (not result):	
					if(sym.fields[i].getValues()[j][k]>128):
						result=True
				"""print("taille champ")
				print(len(sym.fields[i].getValues()[j]))
				result=False"""
		L.append(result)
	return L

def Binmessage(msgs):
	result= False
	for j in range(0, len(msgs)):
		for i in range(0,len(msgs[j].data)):
			if (msgs[j].data[i]>128):
				result= True
	return result
"print(Binmessage(msgs))"
	
