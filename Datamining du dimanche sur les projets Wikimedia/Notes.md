# Datamining du dimanche sur les projets Wikimedia

## Données

* Date : dimanche 21 août 2016
* Heure :10 h 00 – 11 h 30
* Durée : 1 h 30
* Salle : Nation
* Spectateurs : 55

## Plan

### API
* wget / curl / httpie
* jq
* xmlstarlet
* sparql
* Exemple : articles créés / les plus modifiés
* Exemple : ancienneté des administrateurs
* Exemple : drapeaux des pays par continent
* Exemple : détection de copyvio
* Exemples avec graphiques ?
### Dump
* wget | bunzip
* lxml / page parser
* Exemple : dictionnaires de synonymes / antonymes à partir du wikt (+ comparaison avec WOLF)
* Exemple : articles sans portails / UTF-8 invalide
### Dump cyrrus search
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
