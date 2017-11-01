from netzob.all import *


def staticmessage(msgs):
	result= True
	m=len(msgs[0].data)
	for i in range(1,len(msgs)):
		if (m!=len(msgs[i].data)):
			result= False
	return result
def staticfield(sym):
	

	L=[]
	for i in range(0,len(sym.fields)):
		result=True
		a=len(sym.fields[i].getValues()[0])
		for j in range(1,len(sym.fields[i].getValues())):
			if(len(sym.fields[i].getValues()[j])!=a):
				result=False
		L.append(result)
	return L

def Binfield(sym):
	L=[]
	for i in range(0,len(sym.fields)):
		result=False
		for j in range(1,len(sym.fields[i].getValues())):
			for k in range(0,len(sym.fields[i].getValues()[j])):
				if (not result):	
					if(sym.fields[i].getValues()[j][k]>128):
						result=True
		L.append(result)
	return L

def Binmessage(msgs):
	result= False
	for j in range(0, len(msgs)):
		for i in range(0,len(msgs[j].data)):
			if (msgs[j].data[i]>128):
				result= True
	return result

"""def nbfield(sym):
	D=finddelimiters(sym)
	SplitDelimiter(sym,RAW('D'))
	return len(sym.fields)"""
def form(sym):
	L2=["Stat"]
	L1=["Bin"]
	"""L3=["nbfields"]"""
	L1.extend(Binfield(sym))
	L2.extend(staticfield(sym))
	"L3=.extend(nbfield(sym))"
	L1.extend(L2)
	return L1	

def Checkform(msgdata,msgcheck):
	newmsg=msgdata
	symdata=Symbol(messages=msgdata)
	Format.splitAligned(symdata) "trouver mieux"
	newmsg.extend(msgcheck)
	symcheck=Symbol(messages=newmsg)
	Format.splitAligned(symcheck) "trouver mieux"
	Ldata=form(symdata)
	print(Ldata)
	Lcheck=form(symcheck)
	print(Lcheck)
	return (Lcheck==Ldata)

	
