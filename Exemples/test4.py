# -*- coding: utf-8 -*-
import logging
import sys
logging.basicConfig(level=logging.INFO)
sys.path.insert(0, "../../../netzob/src/")

from netzob.all import *
#---------------------------
"""This request roughlylooks like:
4 bytes initialy blank
the "getL" string
4 bytes value that can either be 1 or 0
a random botID on 4 bytes
"""
getL = Symbol(name="GETL", fields=[
	   Field(name="CRC", domain=Raw(b'\x00\x00\x00\x00')),
	   Field(name="Command", domain=ASCII("getL")),
	   Field(name="Flag", domain=Alt([Raw('\x00\x00\x00\x00'),Raw('\x00\x00\x00\x01')])),
	   Field(name="BID", domain=Raw(nbBytes=4))])
print(getL.specialize())