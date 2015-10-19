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
assoc = 100*associations
a = ""
while a != "q":
    a = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if a == "e":
        encripting = input("Message: ")
        jumbler = input("Key: ")
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
        list1, list2 = zip(*combined_list)
        final = [x + y for x, y in zip(list1, list2)]
        for x in final:
            print(assoc[x], end='')
        print("")
        print("")
    elif a == "d":
        jumbled_code = input("Message: ")
        key = input("Key: ")
        jum_list = []
        for x in jumbled_code:
            jum_list.append(associations.find(x))
        k_list = []
        for x in key:
            k_list.append(associations.find(x))
        if len(jum_list) > len(k_list):
            unscram = list(zip(jum_list, cycle(k_list)))
        else:
            unscram = list(zip(cycle(jum_list), k_list))
        list1, list2 = zip(*unscram)
        done = ([x - y for x, y in zip(list1, list2)])
        for x in done:
            print(assoc[x], end='')
        print("")
        print("")   
    elif a == "q":
        print("Goodbye!")
    else: 
        print("Did not understand command, try again.")
        

