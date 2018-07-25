#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import getpass
#import sys
import base64
from Crypto.Cipher import AES
from Crypto.Random import random


def make_16_long(string_):
    return string_ + (16-(len(string_)%16))*"\x00"

def decorate(message):
    print "━" * len(message)
    print message
    print "━" * len(message)
    
def encrypt_file(file_path):
    opened_file = open(file_path, "r")
    file_content = opened_file.read()
    

def encrypt():
    string_ = raw_input("Encrypt dis: ")
    key1 = getpass.getpass("Da key: ")
    key2 = getpass.getpass("Da key again: ")
    if key1 == key2:
        key = make_16_long(key1)
    else:
	print "keys don't match, try again"
	return
    iv = ""
    string_edited = make_16_long(string_)
    for i in range(16):
        iv += random.choice(string.ascii_letters+string.digits+string.punctuation)
    obj = AES.new(key, AES.MODE_CBC, iv)
    text = iv + obj.encrypt(string_edited)
    message = base64.b64encode(text)
    decorate(message)

def decrypt():
    user = "secrets"
    token_file_path = user
    try:
        token_file = open(token_file_path, "r")
        token_b64 = token_file.read()
    except:
        print "Error loading secrets file"
    key = ""
    key = getpass.getpass("Do u no da key?: ")
    key = make_16_long(key)
    text = base64.b64decode(token_b64)
    iv = ""
    thing = ""
    for i in range(len(text)):
        if i <= 15:
            iv += text[i]
        else:
            thing += text[i]
    obj = AES.new(key, AES.MODE_CBC, iv)
    string_ = obj.decrypt(thing)
    string_ = string_.replace("\x00", "")
    decorate(string_)

def run():
    mode = raw_input("Do you want to load or store secrets? [L/s]: ")
    mode = mode.lower()
    if mode == "s":
        encrypt()
    elif mode == "l":
        decrypt()
    else:
        decrypt()

def main():
    loop_ask = raw_input("Run in loop?(Y/N): ").lower()
    if loop_ask == "y":
        loop = True
    elif loop_ask == "n":
        loop = False
    else:
        print "Since you can't type I'll go without loop."
	loop = False
    if loop:
        while loop:
            run()
    elif not loop:
	    run()

if __name__ == "__main__":
    run()
