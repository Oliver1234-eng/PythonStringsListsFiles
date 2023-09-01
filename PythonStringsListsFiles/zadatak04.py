### Zadatak 4. Napiši program koji učitava iz tekstulanog fajla korisnička imena i ispisuje ih. Za fajl
### korisnici.txt iz prethodnog zadatka nakon izvršavanja programa treba da bude prikazano:
### korisnicko ime: pera
### lozinka: peric
### korisnicko ime: jova
### lozinka: jovic
### korisnicko ime: steva
### lozinka: stevic
def readData():
    with open("korisnici.txt", "r") as file:
        for line in file:
            username, password = line.strip().split("|")
            print("Korisnicko ime: {}".format(username))
            print("Lozinka: {}".format(password))

readData()