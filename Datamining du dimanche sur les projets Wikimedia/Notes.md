# Datamining du dimanche sur les projets Wikimedia

## Données

* Date : dimanche 21 août 2016
* Heure :10 h 00 – 11 h 30
* Durée : 1 h 30
* Salle : Nation
* Spectateurs : 55

## Préparation
* Fichiers et scripts en local
* Une page par outil / groups d'outils
 * wget / curl / httpie
 * xmlstarlet / XSLT
 * jq
 * grep
 * sed
 * awk
 * datamash
 * python
 * mysql

## Plan

### Scrapping
* wget / curl
* action=raw / render
* section=
* Special:Export

### Dump
* wget | bunzip
* lxml / page parser
* Exemple : dictionnaires de synonymes / antonymes à partir du wikt (+ comparaison avec WOLF) ; stats avec datamash
* Exemple : articles sans portails / UTF-8 invalide

### API
* api.php
* api.php?format=jsonfm&action=query&titles=LZMA&prop=revisions&rvprop=content&rvsection=0
* https://fr.wikipedia.org/wiki/Sp%C3%A9cial:ApiSandbox
* httpie
* jq
* xmlstarlet
* Exemple : articles créés / les plus modifiés
* Exemple : ancienneté des administrateurs
* Exemple : détection de copyvio
* SPARQL https://query.wikidata.org/
* Exemple : drapeaux des pays par continent
* Exemples avec graphiques ? Cf. blogs Poulpy & Coyau

### Dump cyrrus search

### DBPedia

### Réplicas SQL des Tool Labs
* Pour Wikimedia uniquement
SELECT
  page_title,
  COUNT(*)
  FROM revision_userindex
JOIN
  page
ON
  page_id = rev_page
JOIN
  user
ON
  user_id = rev_user
WHERE
  user_name = 'Arktest'
  AND page_namespace = 4
GROUP BY
  page_title
ORDER BY
  COUNT(*) DESC
LIMIT 25;
