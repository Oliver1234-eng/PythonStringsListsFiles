### Zadatak 2. Napiši program koji formira akronim za zadatu frazu. Akronim se sastoji od kapitalizovanih
### prvih slova reči u frazi. Na primer RAM je akronim za frazu „random access memory“.
### Primer izvršavanja programa:
### Unesite frazu: random access memory
### Akronim za unetu frazu je: RAM
phrase = input("Unesite frazu: ")

# razdvajamo frazu na reči i uzimamo prvo slovo svake reči
acronym = "".join([word[0].upper() for word in phrase.split()])

print("Akronim za unetu frazu je: {}".format(acronym))