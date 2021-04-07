
pikkus=float(input("Sisesta enda pikkus: "))
sugu=input("Sisesta enda sugu: ")

sugu=sugu.strip()
sugu=sugu.capitalize()

if sugu=="Mees" and pikkus>=180:
    print("Kasutaja on MEESSOOST ja PIKKA kasvu.")
elif sugu=="Mees" and pikkus <= 180:
    print("Kasutaja on MEESSOOST ja LÜHEMAT kasvu. ")
elif sugu=="Naine" and pikkus >= 165:
    print("Kasutaja on NAISSOOST ja PIKKA kasvu.")
elif sugu=="Naine" and pikkus <= 165:
    print("Kasutaja on NAISSOOST ja LÜHEMAT kasvu.")
else:
    print("Vigased andmed.")
    
