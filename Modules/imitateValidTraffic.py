#!/usr/bin/env python3

from netzob.all import *

msgs=PCAPImporter.readFile('10[C1D1].pcap', bpfFilter='dst port 102').values()
def connection():
	""" Connection
	
	Replay a connection message

    Args:

    Returns:

    Authors: Bastien DROUOT

    Date: 01/11/2017 : 11h15
	"""
	msgs=PCAPImporter.readFile('10[C1D1].pcap', bpfFilter='dst port 102').values()