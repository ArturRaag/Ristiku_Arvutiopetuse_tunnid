# Kodutöö järgmiseks korraks

Kirjutada programm, mis küsib kasutajalt tema pikkust sentimeetrites kui ka tema sugu.

1. Kui kasutaja on meestsoost ning pikkem kui näiteks 180cm, siis väljastada: "Kasutaja on meestsoost ja pikka kasvu.".
2. Kui kasutaja on meestsoost ning lühem kui 180cm, siis väljastada: "Kasutaja on meestsoost ja lühemat kasvu.".
3. Kui kasutaja on naissoost ning pikkem kui näiteks 165cm, siis väljastada: "Kasutaja on naissoost ja pikka kasvu."
4. Kui kasutaja on naissoost ning lühem kui 165cm, siis väljastada: "Kasutaja on naissoost ja lühemat kasvu.".

Vihjed:

1) Suurem või võrdne: ">=".
Väiksem või võrdne: "<=".
2) Tingimuste kontrollimiseks kasuta "if" lauseid. Nt: "if pikkus >=180:" jne...
3) Mõlema tingimuse kontrollimiseks tohib kasutada if-lausetes "and" funktsiooni.
Näiteks: 
```python
if pikkus > 180 and sugu =="Mees":
    print("tekst")
``` 
   vms... See võtab mõlemad tingimused korraga arvesse.

4) veendu ka, et programm töötaks hoolimata tähe suurusest. (st peab töötama kui sisestada nt MEES/Mees/mees).
Selle jaoks soovitan kasutada "string".capitalize() funktsiooni.
Samuti võiks ta ka töötada olukorras, kui kasutaja kogemata sisestab sõna ette või järgi mingid tühikud.
Tühikute eemaldamiseks (vaid eest ja tagant) saab kasutada nt "string".split()
https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.strip

Kui on mõtteid või küsimusi mida soovite arutada, siis kirjutage meilile: a.raag@ristiku.tln.edu.ee
