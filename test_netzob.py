from netzob.all import *

# we extract from the pcap every message which is going to 8000, i.e. the client messages 
msgs=PCAPImporter.readFile('Exemples/test.pcap', bpfFilter='dst port 8000').values()

print("All messages:")
for m in msgs:
    print(m)
sym=Symbol(messages=msgs)


print("All Format.splitStatic:")
Format.splitStatic(sym)
for field in sym.fields:
    print(field)

"""
print("Format.splitStatic:")
print(sym.fields[0]) # 1st field ok
print(sym.fields[1]) # 2nd field not OK, variadic field
print(sym.fields[2])
"""
print("All Format.splitAligned::")
Format.splitAligned(sym)
for field in sym.fields:
    print(field)
"""
Format.splitAligned(sym)
print("Format.splitAligned:")
print(sym.fields[1]) # OK
print(sym.fields[2]) # OK

print(sym.fields[3]) # not OK, believe 's' is a delimiter
"""
