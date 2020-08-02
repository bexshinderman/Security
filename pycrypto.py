# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 01:24:01 2020

@author: Bex.0
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto import Random

#key represents 26 uppercase letters - substitution cipher - 
key = open('sub_key.txt', 'r').read()
data = open('sub_ciphertext.txt', 'r').read()
print(key)
print(type(key))
print(data)
print(type(data))
import os
def decryption(data):

    key = open('sub_key.txt', 'r').read()
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip('{')
	#Key is FROM the printout of 'secret' in encryption
	#below is the encryption.
	encryption = open('sub_ciphertext.txt', 'r').read()
	cipher = AES.new(key)
	decoded = DecodeAES(cipher, encryption)
	print(decoded)
decryption(data)