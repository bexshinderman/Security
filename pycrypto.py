# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 01:24:01 2020

@author: Bex.0
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto import Random
import base64
#key represents 26 uppercase letters - substitution cipher - 
key = open('sub_key.txt', 'r').read()
data = open('sub_ciphertext.txt', 'r').read()
print(key)
print(type(key))
print(data)
print(type(data))
import os
def decryption(encryptedString):
	PADDING = '{'
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
	#Key is FROM the printout of 'secret' in encryption
	#below is the encryption.
	encryption = encryptedString
	key = open('sub_key.txt', 'r').read()
	cipher = AES.new(key)
	decoded = DecodeAES(cipher, encryption)
	print(decoded)
decryption(data)