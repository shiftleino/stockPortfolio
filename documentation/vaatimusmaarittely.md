# Vaatimusmäärittely

## Sovelluksen yleiskuva ja tarkoitus
Sovellus on graafisella käyttöliittymällä toteutettu osakeportfolion hallinointityökalu. Sovelluksen avulla käyttäjä voi tarkastella omaa osakesalkkuaan, lisätä sinne uusia osakkeita, saada tiedon osakkeen päivän kurssista ja tutkia osakkeen historiallista käyttäytymistä havainnollisen aikasarjakuvaajan avulla. Sovellusta voi käyttää usea rekisteröitynyt käyttäjä kirjautumalla sisään omalle tililleen.

## Sovelluksen käyttäjät
Sovelluksella on ainoastaan yksi käyttäjärooli, normaali käyttäjä. Pääkäyttäjäroolia ei sovelluksessa ole.

## Suunnitellut toiminnallisuudet

### Perusversio
- Käyttäjä voi rekisteröityä käyttäjäksi ja siten luoda tilin - tehty vko3
- Käyttäjä voi kirjautua sisään sovellukseen - tehty vko3
- Käyttäjä voi kirjautua ulos sovelluksesta - tehty vko4
- Käyttäjä voi lisätä osakkeita portfolioonsa - tehty vko4
- Käyttäjä voi poistaa osakkeita portfoliosta - tehty vko4
- Käyttäjä voi tarkastella osakkeidensa päivittäistä kurssia - tehty vko5
- Käyttäjä voi tarkastella osakkeiden historiallista hintakehitystä kuvaajasta

### Jatkokehitysideat
- Käyttäjä näkee osakkeen ostohinnan, prosentuaalisen tuoton ja rahamääräisen tuoton. - tehty vko4 ja vko5
- Muita rahoitusalan laskuja osakkeisiin liittyen: beta, alfa jne.
- Koko portfolioon liittyvät kuvaajat: kynttiläkaavio, Pareto-diagrammi jne.

## Käyttöliittymäluonnos (tekstinä)
- Sovellus aukeaa kirjautumisikkunaan, josta voi myös vaihtaa rekisteröitymisikkunaan. Nämä ikkunat ovat siis linkitetty toisiinsa napilla.
- Kirjautumisikkunassa käyttäjä voi kirjautua sisään ja siten päästä tarkastelemaan omaa salkkuaan. Avautuvalla ikkunalla käyttäjä näkee listan salkkunsa osakkeista ja niiden sen hetkisestä kurssista (päivän tarkkuudella). Lisäksi tähän ikkunaan voidaan lisää jokaiselle osakkeelle muutakin dataa, kuten esimerkiksi ostokurssi ja salkussa olevien osakkeiden lukumäärä.
- Tässä ikkunassa käyttäjä voi painamalla jotain osaketta siirtyä uuteen ikkunaan, joka näyttää osakkeen historiallisen hinnan kuvaajan. Nappia painamalla käyttäjä pääsee takaisin edelliseen pääikkunaan.
