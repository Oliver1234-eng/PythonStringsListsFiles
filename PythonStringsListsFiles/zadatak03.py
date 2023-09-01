### Zadatak 3. Napiši program za registrovanje korisnika. Program teba da omogući korisniku da unese
### korisničko ime i lozinku. Informacije o korisniku čuvaju se u tekstualnom fajlu.
### Primer izvršavanja programa:
### Nakon 3 navedena izvršavanja programa:
### korisnicko ime: pera
### lozinka: peric
### >>> ================================ RESTART
### ================================
### >>>
### korisnicko ime: jova
### lozinka: jovic
### >>> ================================ RESTART
### ================================
### >>>
### korisnicko ime: steva
### lozinka: stevic
### >>>
### Fajl korisnici.txt treba da sadrži sledeće podatke:
### pera|peric
### jova|jovic
### steva|stevic
def register():
    username = input("korisnicko ime: ")
    password = input("lozinka: ")
    
    with open("korisnici.txt", "a") as f:
        f.write(username + "|" + password + "\n")

register()