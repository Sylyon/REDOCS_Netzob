# -*- coding: utf-8 -*-
import logging
import sys
logging.basicConfig(level=logging.INFO)
sys.path.insert(0, "../../../netzob/src/")

from netzob.all import *
#---------------------------
messages = PCAPImporter.readFile("test.pcap").values()
#for m in messages:
#	print(m)
print(messages[0].source)
print(messages[0].destination)
print(message[0].data)