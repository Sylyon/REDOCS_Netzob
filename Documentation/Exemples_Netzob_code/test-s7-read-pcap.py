from netzob.all import *
from identmsg.py import *
# we extract from the pcap every message which is going to 8000, i.e. the client messages 
msgs1=PCAPImporter.readFile('s7-write.pcap', bpfFilter='dst port 102').values()
msgs2=PCAPImporter.readFile('s7-read.pcap', bpfFilter='dst port 102').values()
msgs3=PCAPImporter.readFile('s7-writemanyvalue.pcap', bpfFilter='dst port 102').values()
msgs4=PCAPImporter.readFile('s7-readmanyvalue.pcap', bpfFilter='dst port 102').values()
print("write:")
for m in msgs1:
    print(m)
sym1=Symbol(messages=msgs1)

print("####################")

print("read:")
for m in msgs2:
    print(m)
sym2=Symbol(messages=msgs2)

print("####################")

print("write many value:")
for m in msgs3:
    print(m)
sym3=Symbol(messages=msgs3)

print("####################")

print("read many value:")
for m in msgs4:
    print(m)
sym4=Symbol(messages=msgs4)

print("####################")
print("####################")

print("write.splitStatic:")
Format.splitStatic(sym1)
for field in sym1.fields:
    print(field)

print("####################")

print("read.splitStatic:")
Format.splitStatic(sym2)
for field in sym2.fields:
    print(field)

print("####################")

print("write many value.splitStatic:")
Format.splitStatic(sym3)
for field in sym3.fields:
    print(field)

print("####################")

print("read many value.splitStatic:")
Format.splitStatic(sym4)
for field in sym4.fields:
    print(field)

print("####################")
print("####################")

print("write.splitAligned::")
Format.splitAligned(sym1)
for field in sym1.fields:
    print(field)

print("####################")

print("read.splitAligned::")
Format.splitAligned(sym2)
for field in sym2.fields:
    print(field)

print("####################")

print("write many value.splitAligned::")
Format.splitAligned(sym3)
for field in sym3.fields:
    print(field)

print("####################")

print("read many value.splitAligned::")
Format.splitAligned(sym4)
for field in sym4.fields:
    print(field)