# Vaatimusmäärittely

## Sovelluksen tarkoitus

Harjoitustyössä on tarkoituksena toteuttaa ristinollapeli, jota pelataan vuoropohjaisesti saman tietokoneen ääressä. Myöhemmässä vaiheessa sovellus tallentaa pelaajien tilastotietoja, joita pääsee tarkastelemaan esimerkiksi pelaajakohtaisesti tai listauksena prosentuaalisesti eniten pelejä voittaneista käyttäjistä.

## Käyttäjät

Sovelluksella on näillä näkymin vain yksi käyttäjärooli eli pelaaja. Jos kurssin puitteissa jää aikaan, voidaan luoda lisätä myös ylläpitäjäkäyttäjä, jolla on oikeus poistaa pelaajia tai nollata pistelistat.

## Perusversion tarjoama toiminnallisuus

- Aivan ensimmäisessä kurssin puitteissa tehtävässä palautuksessa palautetaan minimalistinen versio, joka tarjoaa mahdollisuuden pelata erän ristinollaa yhden kokoisella ruudukolla. Peli päättyy jommankumman pelaajan voittoon tai tasapeliin, kun kaikki ruudut ovat täynnä. **tehty!**
- Käyttöliittymä voi ainakin alkuvaiheessa olla tekstipohjainen, mutta muuttuu toivottavasti graafiseksi kurssin edetessä. **osittain tehty!**
- Perusversiota laajennetaan kurssin aikana tarjoamaan pelaajille mahdollisuus valita peliruudukon koko. **tehty!**
- Lisäksi toteutetaan tilastointi ja parhaiden pelaajien listaus, jotka vaativat alkeellisen käyttäjähallinnan.

## Jatkokehitysideoita

Mikäli aikaa (ja ohjelmoinnin pariin tauon jälkeen palanneella opiskelijalla kärsivällisyyttä) riittää, voidaan toteuttaa lisäominaisuuksia:

- Ylläpitäjän käyttäjärooli monipuolisemmin oikeuksin
- Kesken jääneen pelin tallentaminen ja avaaminen ohjelman seuraavalla käyttökerralla
- Etenkin suuremmissa ruudukoissa hyödyllinen tarkistus siitä, onko kummallakaan pelaajalla enää mahdollisuutta voittaa peliä. Mikäli voitto ei ole enää mahdollinen, peli päättyy tasatilanteeseen tai mahdollisesti jonkinlaisin kriteerein määritettävään jommankumman pelaajan voittoon.

