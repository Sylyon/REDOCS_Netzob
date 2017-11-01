from netzob.all import *
from identmsg import *
# we extract from the pcap every message which is going to 8000, i.e. the client messages 
msgs1=PCAPImporter.readFile('../Exemples/s7-example-connection-readmessages.pcap', bpfFilter='dst port 102').values()
msgs2=PCAPImporter.readFile('../Exemples/s7-example-connection-writemessages.pcap', bpfFilter='dst port 102').values()

print("readmessages:")
for m in msgs1:
    print(m)
sym1=Symbol(messages=msgs1)

print("readmessages:")
for m in msgs2:
    print(m)
sym2=Symbol(messages=msgs2)

print("-----------------------------------------------------------------------")

"""print("writemessages:")
for m in msgs2:
    print(m)
sym2=Symbol(messages=msgs2)"""
"""print("message 1 est binaire?")
print(Binmessage(msgs1))

print("message 2 est binaire?")
print(Binmessage(msgs2))

print("message 1 est static?")
print(staticmessage(msgs1))

print("message 2 est static?")
print(staticmessage(msgs2))"""





print("All Format.splitAligned:")
sym=Symbol(messages=msgs1)
Format.splitAligned(sym)
for field in sym.fields:
    print(field)

"""print("message 1 static field?")
L=staticfield(sym)
print(L)"""

"""print("message 1 form?")
L=form(sym)
print(L)"""

print("checkform msgs1 msgs2")
B=Checkform(msgs1,msgs2)
print(B)

"""
print("message 1 Bin field?")
L=Binfield(sym)
print(L)"""

"print(len(sym.fields[0].getValues()[0]))"



"""
print("Format.splitStatic:")
print(sym.fields[0]) # 1st field ok
print(sym.fields[1]) # 2nd field not OK, variadic field
print(sym.fields[2])

print("All Format.splitAligned::")
Format.splitAligned(sym)
for field in sym.fields:
    print(field)

Format.splitAligned(sym)
print("Format.splitAligned:")
print(sym.fields[1]) # OK
print(sym.fields[2]) # OK

print(sym.fields[3]) # not OK, believe 's' is a delimiter
"""
