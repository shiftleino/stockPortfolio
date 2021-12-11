# Ohjelmistotekniikka - Helsingin yliopisto

Tämä repositorio sisältää <I>Ohjelmistotekniikka</I>-kurssin kurssiprojektin ja harjoitusten vastaukset.

## Stock Portfolio
Sovellus on graafisella käyttöliittymällä toteutettu osakeportfolion hallinnointityökalu. Sovelluksen avulla käyttäjä voi tarkastella omaa osakesalkkuaan, lisätä sinne uusia osakkeita, saada tiedon osakkeen päivän kurssista ja tutkia osakkeen historiallista käyttäytymistä havainnollisen aikasarjakuvaajan avulla. Sovellusta voi käyttää usea rekisteröitynyt käyttäjä kirjautumalla sisään omalle tililleen.

Lisää tietoa sovelluksesta voi löytää Dokumentaatio-kohdan sisältämistä linkeistä.

## Dokumentaatio
[Työtunnit](https://github.com/shiftleino/stockPortfolio/blob/main/documentation/tuntikirjanpito.md)<br>
[Vaatimusmäärittely](https://github.com/shiftleino/stockPortfolio/blob/main/documentation/vaatimusmaarittely.md)</br>
[Arkkitehtuurikuvaus](https://github.com/shiftleino/stockPortfolio/blob/main/documentation/arkkitehtuuri.md)

## Python-versio
Sovellus on suunniteltu Python-versiolle 3.8. Uudemmista versioista tuskin on haittaa, vanhempien versioiden kanssa saattaa tulla ongelmia.

## Huomautuksia toiminnasta
- Taulukon osakkeiden hintojen päivittäminen voi viedä suhteellisen paljon aikaa sen käyttämän ulkoisen datalähteen (Yahoo Finance, yfinance-kirjasto) takia.
- HUOM. Linux-käyttäjät: Taulukon otsikot näkyvät tällä hetkellä jostain syystä harmaalla taustalla valkoisen sijasta. Windowsissa tätä ongelmaa ei ole. Ongelmaa pyritään ratkaisemaan.
- HUOM. Napin Portfolio Information toimintaa ei ole vielä tehty, joten se alkaa toimimaan vasta loppupalautuksessa.

## Julkaisut
[Viimeisin julkaisu](https://github.com/shiftleino/stockPortfolio/releases/tag/viikko5)<br>

## Käynnistys
Helpoin tapa käyttää sovellusta on asentaa ensiksi Poetry ([linkki](https://python-poetry.org/docs/#installation)), kloonata projekti itselleen ja tämän jälkeen seurata alla olevia ohjeita.<br>

1. Asenna riippuvuudet
```console 
poetry install
```

2. Käynnistä sovellus
```console
poetry run invoke start
```

## Testaus
1. Suorita testit
```console
poetry run invoke test
```

2. Testikattavuusraportti
```console
poetry run invoke coverage-report
```

3. Testaa tyyli
```console
poetry run invoke lint
```

<p align="center"><b>DO NOT COPY</b></p>
