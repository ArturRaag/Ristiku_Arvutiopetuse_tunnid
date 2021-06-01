
import numpy as np
from time import sleep
import sys

arvuti_elud=3
kasutaja_elud=3
vahele_jätmis_võimalused = 3

täringu_võimalused=[1, 2, 3, 4, 5 ,6]
arvuti_täring = np.random.choice(täringu_võimalused)

        
while True:    
    tekst1 = (f"Arvuti poolt veeretatud arv on: {arvuti_täring}.\nKas jätad käigu vahele [A] või veeretad täringut [B]?\n")
    print(tekst1)
    otsus=input("").upper()
    if otsus == "A":
        if vahele_jätmis_võimalused == 0:
            print("Käigu jätmise võimalused on otsas.\nOled sunnitud oma täringut veeretama.")
            otsus=="B"
        else: 
            vahele_jätmis_võimalused = vahele_jätmis_võimalused-1
            print("Käigu vahele jätmis võimalusi jäänud: ", vahele_jätmis_võimalused)
            arvuti_täring = np.random.choice(täringu_võimalused)
            tekst2 = ("\nArvuti veeretab enda täringut uuesti ja saab...")
            print(tekst2)
            print(arvuti_täring,"!")
        
    elif otsus =="B":
        kasutaja_täring = np.random.randint(1,7)
        if kasutaja_täring > arvuti_täring:
            tekst3 ="Täringut veeretades said arvu..."
            print(tekst3)
            print(kasutaja_täring,"!")
            tekst4 = ("Kuna arvuti veeretas "+ str(arvuti_täring)+ " ning sina veeretasid "+ str(kasutaja_täring)+ " siis ühe elu kaotab... ARVUTI.\n")
            print(tekst4)
            arvuti_elud=arvuti_elud-1
            print(f"\nArvuti elud: {arvuti_elud}\nKasutaja elud: {kasutaja_elud}\n")
        elif kasutaja_täring < arvuti_täring:
            tekst5 = "Täringut veeretades said arvu..."
            print(tekst5, kasutaja_täring, "!")
            tekst6 = ("Kuna arvuti veeretas "+ str(arvuti_täring) + " ning sina veeretasid "+ str(kasutaja_täring) + " siis ühe elu kaotab... KASUTAJA.\n")
            print(tekst6)
            kasutaja_elud=kasutaja_elud-1
            print(f"\nArvuti elud: {arvuti_elud}\nKasutaja elud: {kasutaja_elud}")
        elif kasutaja_täring==arvuti_täring:
            tekst7="Täringut veeretades said arvu..."
            print(tekst7, kasutaja_täring, "!")
            print("Jäite viiki. Alustate mängu uuesti.")
            print(f"\nArvuti elud: {arvuti_elud}\nKasutaja elud: {kasutaja_elud}\n")
        else:
            print("Midagi läks väga valesti...")
        arvuti_täring = np.random.choice(täringu_võimalused)
    if arvuti_elud==0:
        print("Arvutil said elud otsa! KASUTAJA VÕITIS!")
        break
    elif kasutaja_elud==0:
        print("Kasutajal on elud otsas. ARVUTI VÕITIS!")
        break
  
        
        
