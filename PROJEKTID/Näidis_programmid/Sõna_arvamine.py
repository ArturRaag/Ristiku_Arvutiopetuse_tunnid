
import numpy as np

sõnad = ["Liivatera","Olevik","Programmeerimine"]
vastus = np.random.choice(sõnad)
elud=3

def kontroll(täht, õige_sõna):
    if täht in õige_sõna:
        print("Tubli! Arvasid õigesti!")
        return True
    else:
        print("Jama...Arvasid valesti.")
        return False

print("Arva sõna ära. Sõnas on", len(vastus), "tähte.\n")
praegune_seis=len(vastus)*"_ "

while True:
    print("Praegune seis: ", praegune_seis)
    pakkumine = input("Sisesta sõna arvamiseks mõni täht.\nVõi kui arvad, et tead mis sõna on, siis sisesta õige sõna: ").upper()
    
    if len(pakkumine)>1:
        if pakkumine.upper() == vastus.upper():
            print("Tubli! Oled mängu võitja!")
            print("Sul oli jäänud ", elud, " elu. Sõna oli: ", vastus.upper())
            break
        elif pakkumine.upper() != vastus.upper():
            elud = elud-1
            print("Arvasid valesti. Kaotasid ühe elu.")
            print("Sul on jäänud ", elud, " elu.")
            print("Praegune seis: ", praegune_seis)
    elif len(pakkumine)==1:
        if kontroll(pakkumine, vastus.upper())==True:
            print("Sul on jäänud", elud, "elu.")
            #-------------------SEDA SAAKS TEGELIKULT KA MEETODIKS TEHA--------------------------
            indeksid=[]
            iteratsioonid=0
            for i in vastus.upper():
                if i == pakkumine:
                    indeksid.append(iteratsioonid)
                iteratsioonid = iteratsioonid+1
            praegune_seis_listina = praegune_seis.split()
            for indeks in indeksid:
                praegune_seis_listina[indeks]=pakkumine
            praegune_seis=" ".join(praegune_seis_listina)
            #----------------------------ET TAASKASUTADA------------------------
            print("Praegune seis: ", praegune_seis)
        else:
            elud = elud-1
            print("Arvasid valesti. Kaotasid ühe elu.")
            print("Sul on jäänud ", elud, " elu.")
            print("Praegune seis: ", praegune_seis)
        print("----------------------------------------------------------------------------")
    if elud<=0:
        print("Sul on elud otsas. Mäng läbi...")
        print("Õige sõna oli: ", vastus.upper())
        print("Praegune seis: ", praegune_seis)
        break            
    if praegune_seis.replace(" ","").upper() == vastus.upper():
        break    


            

















