from netzob.all import *

# we extract from the pcap every message which is going to 8000, i.e. the client messages 
msgs=PCAPImporter.readFile('C5_U5.pcap', bpfFilter='dst port 102').values()


sym=Symbol(messages=msgs)


print("C5_U5 splitAligned:")
Format.splitAligned(sym)
for field in sym.fields:
    print(field)