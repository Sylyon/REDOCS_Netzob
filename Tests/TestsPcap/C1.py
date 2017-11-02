from netzob.all import *

# we extract from the pcap every message which is going to 8000, i.e. the client messages 
msgs=PCAPImporter.readFile('../../S7-Pcaps/C1.pcap', bpfFilter='dst port 102').values()

sym=Symbol(messages=msgs)

print("C1 splitAligned:")
Format.splitAligned(sym)
for field in sym.fields:
    print(field)