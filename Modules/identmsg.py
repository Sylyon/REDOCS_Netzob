from netzob.all import *

# we extract from the pcap every message which is going to 8000, i.e. the client messages 
msgs=PCAPImporter.readFile('../Exemples/test.pcap', bpfFilter='dst port 8000').values()

"""print("All messages:")
for i in range(0,len(msgs)-1):
    print(msgs[i])
sym=Symbol(messages=msgs)"""

def staticmessage(msgs):
	result= True
	m=len(msgs[0].data)
	for i in range(1,len(msgs)-1):
		if (m!=len(msgs[i].data)):
			result= False
	return result
"print(staticmessage(msgs))"
def Binmessage(msgs):
	result= False
	for j in range(0, len(msgs)-1):
		for i in range(0,len(msgs[j].data)-1):
			if (msgs[j].data[i]>128):
				result= True
	return result
print(Binmessage(msgs))
	
