# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 08:24:19 2021

@author: artur
"""

password="imelik"

for i in range(10):
    kasutaja_sisend = input("Arva ära, mis sõna ma arvan: ")
    if kasutaja_sisend == "imelik":
        print("Arvasid sõna ära!")
        break
    # elif kasutaja_sisend != "parool":
    #     print("Proovi uuesti.")
    else:
        print("Proovi uuesti.")
    if i == 9:
        print("Sul said katsed otsa.")
    

