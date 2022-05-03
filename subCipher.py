# subCipher.py
 
from microbit import *
import random
 
# Cipher functiopn
def scramble(text,dex):
    alpha  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789:,{}'"
    crypta = "abcdefghijklmnopqrstuvwxyz 123456789:,{}'abcdefghijklmnopqrstuvwxyz 123456789:,{}'abcdefghijklmnopqrstuvwxyz 123456789:,{}'"
    result = ""
 
    for letter in text:
        letter = letter.upper()
        index = alpha.find(letter)+dex
        result = result + crypta[index]
 
    return result
 
# The script generates a random shift and takes user input a string to encrypt.
 
sleep(1000)
 
dex=random.randint(5,20)

while True:
    result = scramble(input("Enter a string: ").upper(),dex)
 
    print("result =", result)
