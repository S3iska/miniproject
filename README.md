# Ohtu-kurssin miniprojekti

[![Workflow badge](https://github.com/S3iska/miniproject/actions/workflows/ci.yaml/badge.svg)](https://github.com/S3iska/miniproject/actions)

[Product backlog](https://docs.google.com/spreadsheets/d/1apMJDKGZPF-bFKYbJuen6lBlI-GctVNdVvS5p9Ai9UU/edit?usp=sharing)

## Ohjelman käyttöönotto

### Asennus

1. Kloonaa repositorio ja siirry luotuun hakemistoon:
   ```
   git clone https://github.com/S3iska/miniproject.git
   cd miniproject
   ```
2. Asenna riippuvuudet:
   ```
   poetry install
   ```
3. Luo .env-tiedosto:
   ```
    DATABASE_URL=postgresql://xxx
    TEST_ENV=true
    SECRET_KEY=satunnainen_merkkijono
   ```
4. Tietokannan alustus:
   ```
   poetry run python3 src/db_helper.py
   ```
   
### Ohjelman ajaminen
1. Siirry virtuaaliympäristöön:

   ```
   poetry shell
   ```
2. Käynnistä sovellus:
   ```
   python3 src/index.py
   ```

## Definition of done
  - User storyn taskit done tilassa
  - Asiakas näkee lähdekoodin ja testien tilanteen
  - Koodi noudattaa määriteltyjä tyylivaatimuksia
  - Testit automatisoitu
