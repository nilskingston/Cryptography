"""
cryptography.py
Author: Nils Kingston   
Credit: Roger

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
from itertools import cycle
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
a = ""
while a != "q":
    a = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if a == "e":
        encripting = input("What do you want to encript? ")
        jumbler = input("What should the key be? ")
        e_list = []
        for x in encripting:
            e_list.append(associations.find(x))
        j_list = []
        for x in jumbler:
            j_list.append(associations.find(x))
        newlist = []
        length = len(e_list)
        for x in range(length):
            newlist.append(e_list[x] + j_list[x])
        print(newlist)
      
    elif a == "d":
        jumbled_code = input("Message?")
        key = input("Key?")
        jum_list = []
        for x in jumbled_code:
            jum_list.append(associations.find(x))
        k_list = []
        for x in key:
            k_list.append(associations.find(x))
        list = []
        length = len(jum_list)
        for x in range(length):
            list.append(jum_list[x] - k_list[x])
        print(list)
        
    elif a == "q":
        print("Goodbye!")
    else: 
        print("Did not understand try again")

