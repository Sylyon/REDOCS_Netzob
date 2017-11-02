from netzob.all import *

# we extract from the pcap every message which is going to 8000, i.e. the client messages 
msgs=PCAPImporter.readFile('../../S7-Pcaps/10[C1D1].pcap', bpfFilter='dst port 102').values()

print("10[C1D1].pcap = 10  (connection, deconnection):")
for m in msgs:
    print(m)
sym=Symbol(messages=msgs)

print("############################################################")

print("10[C1D1].pcap splitStatic :")
Format.splitStatic(sym)
for field in sym.fields:
    print(field)

print("############################################################")

print("10[C1D1].pcap splitAligned:")
Format.splitAligned(sym)
for field in sym.fields:
    print(field)