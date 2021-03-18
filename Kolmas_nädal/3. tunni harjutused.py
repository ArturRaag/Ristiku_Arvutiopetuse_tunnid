nimi="Artur"
vanus="23"

tekst="Tere {}! Sa oled {} aastat vana."
uus_tekst=tekst.format(nimi,vanus)
print(uus_tekst)
teksti_pikkus=len(uus_tekst)
print(teksti_pikkus)

A_indeks=uus_tekst[5] # Väljastab 5ndal kohal oleva sümboli. NB!!! Pythonis ja paljudes muudes keeltes, algab loendamine 0-st mitte 1-st!
print(A_indeks)

print(uus_tekst.index("A"))

asendus1=uus_tekst.replace("23", "1000000") # Teeme esimese asenduse
asendus2=asendus1.replace("Artur","Urtur") # Teeme uuesti asenduse, kuid mitte originiaalses lauses, vaid uuendatud (asendus1) lauses.
print(asendus2)

