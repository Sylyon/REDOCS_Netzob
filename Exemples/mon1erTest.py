# -*- coding: utf-8 -*-
import logging
import sys
logging.basicConfig(level=logging.INFO)
sys.path.insert(0, "../../../netzob/src/")

from netzob.all import *
msg1 = RawMessage("hello world")
msg2 = RawMessage("hello brucon")
s = Symbol(name="Helloworld", messages=[msg1, msg2])
print(s)