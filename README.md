# Ristinolla

Pelissä kaksi pelaajaa pystyy pelaamaan ristinollaa tämänhetkisessä versiossa 3x3-ruudukossa (myöhemmin pelaajan valitsemassa ruudukkokoossa). Kun jompikumpi pelaajista saa rivin täyteen, sovellus ilmoittaa voittajan.

## Python-versio

Sovellusta on testattu Pythonin versiolla 3.8, joten vanhemmilla versioilla toimintaa ei voida taata.

## Dokumentaatio

- Käyttöohje (tulossa)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- Arkkitehtuurikuvaus (tulossa)
- Testausdokumentti (tulossa)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

## Asennus

Kirjoita seuraavat komentorivikomennot sovelluksen asentamiseksi:

1. Riippuvuuksien asentaminen:

```bash
poetry install
```

2. Sovelluksen käynnistäminen:

```bash
poetry run invoke start
```

Sovellus kysyy ensin käyttäjältä haluttua pelilaudan kokoa, jonka jälkeen käynnistyy graafinen käyttöliittymä.

## Komentorivikomennot

### Ohjelman suorittaminen:

Peli käynnistyy komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin htmlcov-hakemistoon saa generoitua komennolla:

```bash
poetry run invoke coverage-report
```

### Pylint

Pylint-tarkistuksen voi suorittaa komennolla:

```bash
poetry run invoke lint
```


