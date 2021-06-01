
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

valikud = ["Kivi", "Käärid", "Paber"]
x=[]
katsed=10
for i in range(katsed):
   tulemus=np.random.choice(valikud) 
   x.append(tulemus)

tulemused=Counter(x)
tulemused_2 = tulemused.most_common(3)


# -----------------sorteerime andmed, et oleks võimalik ka joonist luua------------------
variandid=[]
variantide_sagedused=[]
for i in tulemused_2:
    variandid.append(i[0])
    variantide_sagedused.append(i[1])
    
# ----------- Loome joonise, kus x-telje peal on võimalikud variandid ja y-telje peal variantide esinemise sagedused--------
plt.bar(variandid, variantide_sagedused)
plt.show()



