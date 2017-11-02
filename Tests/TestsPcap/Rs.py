from netzob.all import *

# we extract from the pcap every message which is going to 8000, i.e. the client messages 
msgs=PCAPImporter.readFile('../../S7-Pcaps/Rs.pcap', bpfFilter='dst port 102').values()

print("Rs.pcap = Many Read:")
for m in msgs:
    print(m)
sym=Symbol(messages=msgs)

print("############################################################")

print("Rs.pcap splitStatic :")
Format.splitStatic(sym)
for field in sym.fields:
    print(field)

print("############################################################")

print("Rs.pcap splitAligned:")
Format.splitAligned(sym)
for field in sym.fields:
    print(field)