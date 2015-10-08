"""
cryptography.py
Author: Nils Kingston   
Credit: Roger

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""

associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
a = ""
while a != "q":
    a = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if a == "e":
        encripting = input("What do you want to encript?")
        jumbler = input("What should the key be?")
        list(encripting)
        list(jumbler)
        jumbled = [sum(x) for x in zip(encripting, key)]
        print(jumbled)
      
    elif a == "d":
        jumbled_code = input("Message?")
        key = input("Key?")
        list(jumbled_code)
        
    elif a == "q":
        print("Goodbye!")
    else: 
        print("Did not understand try again")

