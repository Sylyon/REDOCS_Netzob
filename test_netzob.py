from netzob.all import *

# we extract from the pcap every message which is going to 8000, i.e. the client messages 
msgs=PCAPImporter.readFile('Exemples/test.pcap', bpfFilter='dst port 8000').values()

for m in msgs:
    print(m)

sym=Symbol(messages=msgs)

Format.splitStatic(sym)
print("Format.splitStatic:")
print(sym.fields[0]) # 1st field ok
print(sym.fields[1]) # 2nd field not OK, variadic field

Format.splitAligned(sym)
print("Format.splitAligned:")
print(sym.fields[1]) # OK
print(sym.fields[2]) # OK

print(sym.fields[3]) # not OK, believe 's' is a delimiter

