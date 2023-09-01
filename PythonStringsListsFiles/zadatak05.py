### Zadatak 5. Napiši program koji kombinuje sadržaj dva fajla i snima ga u treći fajl. U prvom fajlu se nalaze
### korisnička imena i lozinke prodavaca, a u drugom fajlu se nalaze nizovi cena artikala koje su prodavci
### prodali. Pri tome prvom redu u fajlu sa korisničkim imenima i lozinkama odgovara prvi red u fajlu sa
### računima, drugom redu u fajlu sa korisničkim imeni i lozinkama odgovara drugi red u fajlu sa računima
### itd. Svaki red trećeg fajla treba da sadrži korisničko ime prodavca, ukupnu cenu robe koju je prodao i
### prosečnu cenu artikla koji je prodao.
### Primer izvršavanja programa:
### Ako su dati fajlovi
### korisnici.txt
### pera|peric
### jova|jovic
### steva|stevic
### i racuni.txt
### 100|200|150|150|300|100
### 50|100|100|50
### 300|400|200|100|400
### Formirani fajl treba da bude:
### statistika.txt
### pera|1000.0|166.66666666666666
### jova|300.0|75.0
### steva|1400.0|280.0
# otvaranje fajlova
def calculateStatistics():
    with open('korisnici.txt', 'r') as korisnici_fajl, open('racuni.txt', 'r') as racuni_fajl, open('statistika.txt', 'w') as statistika_fajl:
    
        # iteracija kroz linije u oba fajla
        for korisnik_line, racuni_line in zip(korisnici_fajl, racuni_fajl):
        
            # parsiranje korisničkog imena i lozinke
            korisnik, lozinka = korisnik_line.strip().split('|')
        
            # parsiranje računa kao niza brojeva
            racuni = [int(cena) for cena in racuni_line.strip().split('|')]
        
            # izračunavanje ukupne i prosečne cene
            ukupno = round(sum(racuni), 2)
            prosecno = round(ukupno / len(racuni), 2)
        
            # pisanje statistike u novi fajl
            statistika_fajl.write("{}|{}|{}\n".format(korisnik, ukupno, prosecno))

    # zatvaranje fajlova
    korisnici_fajl.close()
    racuni_fajl.close()
    statistika_fajl.close()

calculateStatistics()