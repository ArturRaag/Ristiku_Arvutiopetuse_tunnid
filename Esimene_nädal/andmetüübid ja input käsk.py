
tekst="Tere maailm!"
print(tekst)

nimi=input("Mis on sinu nimi? : ")
print("Tere "+ nimi)

vanus=input("Mis on sinu vanus? : ")

print("Tere "+nimi + ". Sina oled "+vanus+" aastat vana.")

vanus_int=int(input("Sisesta uuesti enda vanus: "))
vanus_sõber_int=int(input("Sisesta enda sõbra vanus: "))
print("Sa oled oma sõbrast "+str(vanus_int-vanus_sõber_int)+" aastat vanem.")

print("Meie andmetüübid on järgmised:")
print("'tekst' andmetüüp on: " + str(type(tekst)))
print("'nimi' andmetüüp on: "+str(type(nimi)))
print("'vanus' andmetüüp on: "+str(type(vanus)))
print("'vanus_int' andmetüüp on: "+str(type(vanus_int)))
print("'vanus_sõber_int' andmetüüp on: "+str(type(vanus_sõber_int)))

arv_pi=3.14
print("'arv_pi' andmetüüp on: "+str(type(arv_pi)))
