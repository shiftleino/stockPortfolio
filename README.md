# Ohjelmistotekniikka - Helsingin yliopisto

Tämä repositorio sisältää <I>Ohjelmistotekniikka</I>-kurssin kurssiprojektin ja harjoitusten vastaukset.

## Stock Portfolio
Sovellus on graafisella käyttöliittymällä toteutettu osakeportfolion hallinointityökalu. Sovelluksen avulla käyttäjä voi tarkastella omaa osakesalkkuaan, lisätä sinne uusia osakkeita, saada tiedon osakkeen päivän kurssista ja tutkia osakkeen historiallista käyttäytymistä havainnollisen aikasarjakuvaajan avulla. Sovellusta voi käyttää usea rekisteröitynyt käyttäjä kirjautumalla sisään omalle tililleen.

Lisää tietoa sovelluksesta voi löytää Dokumentaatio-kohdan sisältämistä linkeistä.

## Dokumentaatio
[Työtunnit](https://github.com/shiftleino/stockPortfolio/blob/main/documentation/tuntikirjanpito.md)<br>
[Vaatimusmäärittely](https://github.com/shiftleino/stockPortfolio/blob/main/documentation/vaatimusmaarittely.md)</br>
[Arkkitehtuurikuvaus](https://github.com/shiftleino/stockPortfolio/blob/main/documentation/arkkitehtuuri.md)

## Python-versio
Sovellus on suunniteltu Python-versiolle 3.8. Uudemmista versioista tuskin on haittaa, vanhempien versioiden kanssa saattaa tulla ongelmia.

## Huomautuksia toiminnasta
- Lisätessä osakkeen tai muuttaessa taulukon tietoja täytyy taulukko päivittää "refresh"-napista.
- Ohjelmisto on tällä hetkellä hyvin hidas ohjelmiston käyttämän ulkoisen datalähteen (Yahoo Finance, yfinance-kirjasto) takia.

## Käynnistys
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
