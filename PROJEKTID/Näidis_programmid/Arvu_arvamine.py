
import numpy as np

arv=np.random.randint(100)
kasutaja_arv=int(input("Mõtlen arvu vahemikus 1-100. Arva ära, mis arv see on: ").strip())

for i in range(10):
    if kasutaja_arv > arv:
        kasutaja_arv=int(input("Sinu arv oli liiga suur. Vali VÄIKSEM: ").strip())
    elif kasutaja_arv < arv:
        kasutaja_arv=int(input("Sinu arv oli liiga väike. Vali SUUREM: ").strip())
    elif kasutaja_arv==arv:
        print("Arvasid ära!")
        break
    else:
        print("Midagi läks valesti...")
        break
