
arv = float(input("Sisesta number: "))

if arv%2==0:
    print("Arv on paaris.")
#elif arv%2 != 0:
  #print("Tegemist on paaritu arvuga")
else:
    print("Tegemist on paaritu arvuga.")
 
# NB! elif lause jätsime ära, kuna meil ei ole selle jaoks eraldi tingimust tegelikult vaja.
# Kui me näiteks juba teame, et arv on paaris, siis teame juba automaatselt, et paaritu ta olla ei saa.
# Samuti juhul kui teaksime, et arv on paaritu, siis ei ole mõttet kontrollida kas ta on paaris, sest mõlemad korraga ta olla ei saa.
