"""
cryptography.py
Author: Nils Kingston   
Credit: Roger

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
from operator import add
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
a = ""
while a != "q":
    a = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if a == "e":
        encripting = input("What do you want to encript? ")
        jumbler = input("What should the key be? ")
        list(encripting)
        for x in encripting:
            associations.find(x)
        list(jumbler)
        for x in jumbler:
            associations.find(x)
        jumbled = map(add, encripting, jumbler)
        
        
      
    elif a == "d":
        jumbled_code = input("Message?")
        key = input("Key?")
        list(jumbled_code)
        list(key)
        message = [x1 - x2 for (x1, x2) in zip(jumbled_code, key)]
        
    elif a == "q":
        print("Goodbye!")
    else: 
        print("Did not understand try again")

