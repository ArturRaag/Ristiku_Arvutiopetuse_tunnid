# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 09:16:47 2021

@author: artur
"""

sõna = "text"
sisend = ""

while sisend != sõna:
    sisend = input("Sisesta sõna: ")
    if sisend==sõna:
        print("Tubli! Arvasid ära!")
    else:
        print("Proovi uuesti.")