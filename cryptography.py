"""
cryptography.py
Author: Nils Kingston   
Credit: Roger

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
#from itertools import cycle
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
        if len(e_list) > len(j_list):
            combined_list = list(zip(e_list, cycle(j_list)))
        else:
            combined_list = list(zip(cycle(e_list), j_list))
        print(combined_list)
    elif a == "d":
        jumbled_code = input("Message? ")
        key = input("Key? ")
        jum_list = []
        for x in jumbled_code:
            jum_list.append(associations.find(x))
        k_list = []
        for x in key:
            k_list.append(associations.find(x))
        if len(jum_list) > len(k_list):
            unscrambled = list(zip(jum_list, cycle(k_list)))
        else:
            unsrcambled = list(zip(cycle(jum_list), k_list))
        print(unscrambled)
        
        
    elif a == "q":
        print("Goodbye!")
    else: 
        print("Did not understand try again")

