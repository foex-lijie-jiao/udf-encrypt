#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyaes
import base64

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

class AESCipher:
    def __init__(self):
        self.key = 'strengthandhonor'
        self.cipher = pyaes.new(self.key)
 
    def encrypt(self, text):
        enc = self.cipher.encrypt(pad(text))
        return base64.b64encode(enc)
 
    def decrypt(self, text):
        enc = base64.b64decode(text)
        return unpad(self.cipher.decrypt(enc))
