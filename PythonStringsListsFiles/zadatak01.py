### Zadatak 1. Napiši program koji od korisnika traži da unese dva stringa i formira i ispisuje novi string koji
### se sastoji od dva puta ponovljena prva tri karaktera iz prvog stringa i poslednja tri karaktera prethodnog stringa.
### Primer izvršavanja programa:
### Unesite prvi string: abcdef
### Unesite drugi string: ghijkl
### abcabcjkl
prvi_string = input("Unesite prvi string: ")
drugi_string = input("Unesite drugi string: ")

novi_string = prvi_string[:3] * 2 + drugi_string[-3:]

print(novi_string)