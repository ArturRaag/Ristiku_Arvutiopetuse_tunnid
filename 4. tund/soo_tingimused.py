
sugu = input("Sisesta enda sugu: ")
sugu = sugu.strip() # eemaldame sõna eest ja tagant üleliigsed tühikud. Võid eraldi konsoolis katsetada nt: " abc   ".strip() väljastab: "abc"
sugu = sugu.capitalize() # Teeme esimese tähe suureks ja muu tähed väikseks.

if sugu == "Mees":
    print("Sa oled mees.")
elif sugu == "Naine":
    print("Sa oled naine.")
elif sugu== "Laps":
    print("Sa oled laps.")
else:
    print("Sa oled mingi imelik elukas.")
