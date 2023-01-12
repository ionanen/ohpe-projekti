import os
import json

def lisaa_kirja(paivakirja: list):
    """Pyytää käyttäjältä lisättävän kirjan tiedot, tallettaa ne sanakirjaksi 
    sekä lisää sanakirjan listaan
    """
    nimi = input("Kirjan nimi: ")
    while True:
        kirjoittaja = input("Kirjoittaja (Sukunimi, Etunimi): ")
        if not ", " in kirjoittaja:
            print("Anna kirjailijan nimi muodossa Sukunimi, Etunimi")
        else:
            break
    vuosi = input("Julkaisuvuosi: ")
    arvio = input("Arvio kirjasta (1-5): ")
    kommentti = input("Lisää kommentti kirjasta: ")
    paivakirja.append({"nimi": nimi, "kirjoittaja": kirjoittaja, "vuosi": \
        vuosi, "arvio": arvio, "kommentti": kommentti})
    print()

def hae_kirja(paivakirja: list):
    """Pyytää käyttäjältä valinnan, haetaanko kirjan nimen, kirjailijan nimen
    vai kirjan saaman arvion mukaan
    """
    tulosta_hakuvalikko()
    valinta = input("Valitse: ")
    if valinta == "n":
        syote = input("Kirjan nimi: ")
        print()
        tulosta_loydetyt(syote, "nimi", paivakirja)    
    elif valinta == "k":
        syote = input("Kirjoittajan nimi: ")
        print()
        tulosta_loydetyt(syote, "kirjoittaja", paivakirja)   
    elif valinta == "a":
        syote = input("Arvio: ")
        print()
        tulosta_loydetyt(syote, "arvio", paivakirja)
    else:
        print()
        print("Virheellinen valinta!")
        print()

def tulosta_loydetyt(syote: str, hakukohde: str, paivakirja: list):
    """Apufunktio hakutoimintoon, tulostaa näytölle listasta syötteen ja 
    hakukohteen mukaiset kirjat kirjailijan mukaan aakkosjärjestyksessä
    """
    loydetyt = []
    for kirja in paivakirja:
        if syote.lower() in kirja[hakukohde].lower():
            loydetyt.append(kirja)
    if len(loydetyt) == 0:
        print("Hakusanalla ei löytynyt yhtään kirjaa.")
        print()
    else:
        tulokset = aakkosta(loydetyt)
        if len(tulokset) == 1:
            print("Löydettiin yksi kirja:")
        else:
            print("Löydettiin seuraavat kirjat:")
        for kirja in tulokset:
            tulosta_kirja(kirja) 
        print()

def tulosta_kaikki(paivakirja: list):
    """Tulostaa kaikki lukupäiväkirjaan tallennetut kirjat kirjailijan mukaan
    aakkosjärjestyksessä
    """
    print()
    print("Kaikki tallennetut kirjat:")
    kokolista = aakkosta(paivakirja)
    for kirja in kokolista:
        tulosta_kirja(kirja)
    print()

def aakkosta(lista: list):
    """Aakkostaa parametrinä välitetyn kirjalistan kirjoittajan mukaan 
    aakkosjärjestykseen
    """
    return sorted(lista, key=lambda d: d['kirjoittaja'])

def tulosta_kirja(kirja: dict):
    """Apufunktio kirjan tietojen muotoilemiseen ja tulostamiseen näytölle"""
    print(f"{kirja['kirjoittaja']:20} {kirja['nimi']:25}{kirja['vuosi']:4}\
        {int(kirja['arvio']) * '*':5} - {kirja['kommentti']}")

def tallennapk(paivakirja: list):
    """Tallentaa päiväkirjan json-tiedostoksi ylikirjoittaen aikaisemman
    tiedoston, jos sellainen on
    """
    with open("luetut.json", "w") as f:
        json.dump(paivakirja, f, indent=4)
        
def tulosta_valikko():
    """Tulostaa päävalikon"""
    print("📕 (u)usi kirja")
    print("📗 (h)ae kirjaa...")
    print("📘 (t)ulosta kaikki")
    print("📙 (l)opeta")
    print()

def tulosta_hakuvalikko():
    """Tulostaa hakutoiminnon valikon"""
    print("Hae...")
    print("📕 kirjan (n)imellä tai sen osalla")
    print("📗 (k)irjoittajan nimellä tai sen osalla")
    print("📘 valitun (a)rvion saaneet kirjat")
    print()

def main(paivakirja: dict):
    """Pääohjelma"""
    os.system('clear') # Tyhjentää konsolin tekstistä ohjelman aluksi
    print("📚 S I V U H I S T O R I A 📚")
    print("Tallenna lukuharrastuksesi!")
    print()

    while True:
        tulosta_valikko()
        valinta = input("Valitse: ")
        if valinta == "l":
            tallennapk(paivakirja)
            break
        elif valinta == "u":
            lisaa_kirja(paivakirja)
        elif valinta == "h":
            hae_kirja(paivakirja)
        elif valinta == "t":
            tulosta_kaikki(paivakirja)
        else:
            tulosta_valikko()

try:
    with open("luetut.json") as f:
        paivakirja = json.load(f)
except:
    paivakirja = [] #jos annettua tiedostoa ei löydy, luodaan tyhjä lista
main(paivakirja)