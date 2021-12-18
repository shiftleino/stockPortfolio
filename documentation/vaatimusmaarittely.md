# Vaatimusmäärittely

## Sovelluksen yleiskuva ja tarkoitus
Sovellus on graafisella käyttöliittymällä toteutettu osakeportfolion hallinointityökalu. Sovelluksen avulla käyttäjä voi tarkastella omaa osakesalkkuaan, lisätä sinne uusia osakkeita, saada tiedon osakkeen päivän kurssista ja tutkia osakkeen historiallista käyttäytymistä havainnollisen aikasarjakuvaajan avulla. Sovellusta voi käyttää usea rekisteröitynyt käyttäjä kirjautumalla sisään omalle tililleen.

## Sovelluksen käyttäjät
Sovelluksella on ainoastaan yksi käyttäjärooli, normaali käyttäjä. Pääkäyttäjäroolia ei sovelluksessa ole.

## Suunnitellut toiminnallisuudet

### Perusversio
- Käyttäjä voi rekisteröityä käyttäjäksi ja siten luoda oman tilin
    - Käyttäjätunnus uniikki
- Käyttäjä voi kirjautua sisään sovellukseen omalle tililleen
    - Jos syötettyä käyttäjää ei ole olemassa tai salasana on virheellinen, ilmoittaa sovellus tästä virhetekstillä, joka on molemmissa tapauksissa sama.
- Käyttäjä voi kirjautua ulos sovelluksesta
    - Tällöin sovellus palauttaa käyttäjän takaisin aloitusikkunaan
- Käyttäjä voi lisätä osakkeita portfolioonsa
    - Ticker täytyy olla samassa muodossa kuin YAHOO! Financessä. 
- Käyttäjä voi poistaa osakkeita omasta portfoliosta
    - Jos osaketta ei ole portfoliossa, mitään ei tapahdu
- Käyttäjä voi tarkastella taulukosta osakkeidensa ostohintaa, tuottoa ja päivittäistä kurssia 
    - Päivittäinen kurssi ei päivity automaattisesti, vaan se täytyy erikseen päivittää sille osoitetulla napilla
- Käyttäjä pystyy järjestää taulukkoa eri sarakkeiden avulla. 
- Käyttäjä voi tarkastella osakkeiden historiallista hintakehitystä kuvaajasta
    - Kuvaaja on interaktiivinen ja sitä pystyy esimerkiksi zoomata.
    - Käyttäjä ei pysty tarkastella esimerkiksi muiden käyttäjien osakkeiden historiallista hintakehitystä.

### Jatkokehitysideat
- Muita rahoitusalan laskuja osakkeisiin liittyen: beta, alfa jne.
- Koko portfolioon liittyvät kuvaajat: kynttiläkaavio, Pareto-diagrammi jne.

## Käyttöliittymäluonnos (tekstinä)
- Sovellus aukeaa aloitusikkunaa, josta käyttäjä voi siirtyä kirjautumis- ja rekisteröitymisikkunoihin.
- Kirjautumisikkunassa käyttäjä voi kirjautua sisään ja siten päästä tarkastelemaan omaa salkkuaan. Avautuvalla ikkunalla käyttäjä näkee taulukon salkkunsa osakkeista ja esimerkiksi niiden sen hetkisestä kurssista (päivittämällä napista).
- Tässä ikkunassa käyttäjä voi painamalla alla olevaa nappia siirtyä uuteen ikkunaan, joka näyttää osakkeen historiallisen hinnan kuvaajan. Nappia painamalla käyttäjä pääsee takaisin edelliseen pääikkunaan.
- Kirjautumalla ulos pääikkunassa käyttäjä pääsee takaisin aloitusikkunaan.
