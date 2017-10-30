# -*- coding: utf-8 -*-
import logging
import sys
logging.basicConfig(level=logging.INFO)
sys.path.insert(0, "../../../netzob/src/")

from netzob.all import *
#---------------------------
#On crée un ASCII de valeur "hello"
f= Field(domain=ASCII("hello"), name="field1")
#On génére de Field créer 
print(f.specialize())

#On crée bitArray de taille 16 généré aléatoirement
print(Field(BitArray(nbBits=16)).specialize())