
import numpy as np
import matplotlib.pyplot as plt

def ütle_tere(kordused):
    print(kordused*"Tere!")

#ütle_tere(10)

def funk1(x):
    y=3*x+15
    return y

def funk2(x):
    return 3*x+15

#funk1(-10)
#print(funk2(-10), funk2(-5), funk2(0), funk2(5), funk2(10))

x_1 = np.arange(-10, 11, 5) #Loome massiivi, kus (algus, lõpp, samm). 
# NB! "LÕPP" on väljaarvatud. Sellepärast on 10 asemel ka 11.
# Kui 11 asemel oleks hoopis 10, siis ta jääks 10 peal küll pidama, aga seda välja ta ei trükkiks.

print("X-id: ", x_1) # Siin trükkime massiivid välja. Ehk X-i väärtustega massiiv. (matemaatikas tuntud kui väärtuste tabel)
print("Y-id: ", funk2(x_1)) # Siin trükkime funktsiooni, ehk Y-i väärtustega massiivi.

plt.plot(x_1, funk2(x_1)) # See on matplotlib moodulist graafika joonestamiseks meetod. Põhjalikumalt uurime seda kunagi hiljem. Iseseisvaks uurimiseks Googelda: Matplotlib
