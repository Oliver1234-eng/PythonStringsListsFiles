### Zadatak 6. Napisati program koji formatira tekstualni fajl prema sledećim uputsvima:
### · Svaka vezana pojava više razmaka između reči treba da bude zamenjena tačno jednim razmakom.
### · Naslov – Naslov je prvi red iz fajla i treba da bude poravnat na sredinu u string od 100 karakter i
### prvo slovo svake reči treba da bude veliko. Nakon naslova i pre prvog pasusa treba da bude jedan prazan red.
### · Paragrafi - Paragraf je svaki red u fajlu osim naslova. Paragraf treba da bude uvučen za pet
### praznih karaktera. Svaka rečenica u paragrafu treba da počinje velikim slovom.
### Primer izvršavanja programa:
### neformatiranTekst.txt
### THE ROTATION OF CROPS A Venture in a Theory of Social
### Prudence by Soren Kierkegaard
### people with experience maintain that proceeding from a basic
### principle is supposed to bevery reasonable; I yield to them and
### proceed from the basic principle that all people are boring. Or is
### there anyone who would be boring enough to contradict me in this
### regard? This basic principle has to the highest degree the repelling
### force always required in the negative, which is actually the principle of motion.
### It is not merely repelling but infinitely repulsive, and whoever has
### the basic principle behind him must necessarily have infinite momentum
### for making discoveries. If, then, my thesis is true, a person needs
### only to ponder how corrupting boredom is for people, tempering his
### reflections more or less according to his desire to diminish or
### increase his impetus, and if he wants to press the speed of the motion
### to the highest point, almost with danger to the locomotive, he needs
### only to say to himself: Boredom is the root of all evil.
### It is very curious that boredom, which itself has such a calm
### and sedate nature, can have such a capacity to initiate motion. the
### effect that boredom brings about is absolutely magical, but this
### effect is one not of attraction but of repulsion.
### formatiranTekst.txt
### The Rotation Of Crops A Venture In A Theory Of Social Prudence
### By Soren Kierkegaard
### People with experience maintain that proceeding from a basic
### principle is supposed to bevery reasonable; I yield to them and
### proceed from the basic principle that all people are boring. Or is
### there anyone who would be boring enough to contradict me in this
### regard? This basic principle has to the highest degree the repelling
### force always required in the negative, which is actually the principle of motion.
### It is not merely repelling but infinitely repulsive, and whoever
### has the basic principle behind him must necessarily have infinite
### momentum for making discoveries. If, then, my thesis is true, a person
### needs only to ponder how corrupting boredom is for people, tempering
### his reflections more or less according to his desire to diminish or
### increase his impetus, and if he wants to press the speed of the motion
### to the highest point, almost with danger to the locomotive, he needs
### only to say to himself: Boredom is the root of all evil.
### It is very curious that boredom, which itself has such a calm and
### sedate nature, can have such a capacity to initiate motion. the effect
### that boredom brings about is absolutely magical, but this effect is
### one not of attraction but of repulsion.
import re

def formatText():

    # Učitavanje fajla
    with open("neformatiranTekst.txt", "r") as f:
        text = f.read()

    # Formatiranje naslova
    title = text.split("\n")[0].strip()
    title = " ".join([word.capitalize() for word in title.split()])
    title = title.center(100) + "\n\n"

    # Formatiranje paragrafa
    paragraphs = re.findall("(?<=\n).+", text)
    paragraphs = [" "*5 + sentence.capitalize() for p in paragraphs for sentence in p.split(". ") if sentence]
    formatted_text = "\n".join(paragraphs)

    # Spajanje formatiranog teksta
    formatted_text = title + formatted_text

    # Ispisivanje formatiranog teksta
    print(formatted_text)

    # Upisivanje formatiranog teksta u novi fajl
    with open("formatiranTekst.txt", "w") as f:
        f.write(formatted_text)

formatText()