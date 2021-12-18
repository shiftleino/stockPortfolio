# Ohjelmistotekniikka - Helsingin yliopisto

Tämä repositorio sisältää <I>Ohjelmistotekniikka</I>-kurssin kurssiprojektin ja harjoitusten vastaukset.

## Stock Portfolio
Sovellus on graafisella käyttöliittymällä toteutettu osakeportfolion hallinnointityökalu. Sovelluksen avulla käyttäjä voi tarkastella omaa osakesalkkuaan, lisätä sinne uusia osakkeita, saada tiedon osakkeen päivän kurssista ja tutkia osakkeen historiallista käyttäytymistä havainnollisen aikasarjakuvaajan avulla. Sovellusta voi käyttää usea rekisteröitynyt käyttäjä kirjautumalla sisään omalle tililleen.

Lisää tietoa sovelluksesta voi löytää Dokumentaatio-kohdan sisältämistä linkeistä.

## Dokumentaatio
[Instructions in English](./documentation/instructions.md)<br>
[Työtunnit](./documentation/tuntikirjanpito.md)<br>
[Vaatimusmäärittely](./documentation/vaatimusmaarittely.md)<br>
[Arkkitehtuurikuvaus](./documentation/arkkitehtuuri.md)<br>
[Testausdokumentti](./documentation/testausdokumentti.md)<br>

## Python-versio
Sovellus on suunniteltu Python-versiolle 3.8. Uudemmista versioista tuskin on haittaa, vanhempien versioiden kanssa saattaa tulla ongelmia.

## Huomautuksia toiminnasta
- Taulukon osakkeiden hintojen päivittäminen voi viedä suhteellisen paljon aikaa sen käyttämän ulkoisen datalähteen (Yahoo Finance, yfinance-kirjasto) takia.
- Osakkeiden lyhenteet täytyy olla samassa muodossa kuin YAHOO! Finance -nettisivulla.

## Julkaisut
[Viimeisin julkaisu](https://github.com/shiftleino/stockPortfolio/releases)<br>

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
