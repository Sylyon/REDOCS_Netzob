from netzob.all import *

# we extract from the pcap every message which is going to 8000, i.e. the client messages 
msgs=PCAPImporter.readFile('C1.pcap', bpfFilter='dst port 102').values()

print("C1 = 1 connection:")
for m in msgs:
    print(m)
sym=Symbol(messages=msgs)

print("############################################################")

print("C1 splitStatic :")
Format.splitStatic(sym)
for field in sym.fields:
    print(field)

print("############################################################")

print("C1 splitAligned:")
Format.splitAligned(sym)
for field in sym.fields:
    print(field)