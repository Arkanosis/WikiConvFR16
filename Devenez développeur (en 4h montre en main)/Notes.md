# Devenez développeur (en 4 h montre en main)

## Données

* Date : dimanche 21 août 2016
* Heure :14 h 00 – 15 h 45 ; 16 h 15 – 18 h 00
* Durée : 1 h 45 + 1 h 45 (3 h 30)
* Salle : Denfer-Rochereau
* Spectateurs : 40

## Plan

### Schéma global
* Wikipédia
* ⇒ Projets Wikimedia
* MediaWiki
* + extensions
* + bots
* + tools
* Datacenters
* Wmflabs
* ⇒ Tools
* Git
* Devops / admin sys
* Puppet
* ⇒ Operations
* Phabricator
* Développeurs
* Gerrit
### Documentation
* MediaWiki
* Wikitech
* wikitech-l
* #wikitech
* Twitter
### Compte Wikitech + labs
* https://wikitech.wikimedia.org/wiki/Main_Page
* Création du compte
### Accès tools labs
* Avant la pause, pour créer les comptes pendant ?
* Voir avec un admin sur #wikimedia-labs
### Phabricator
* Sur la prod, MediaWiki, Extension:Scribunto, pywikibot
* Création de ticket,
* Commentaire dans un autre ticket
* Navigation dans les projets
### Installation git + git-review
### Clef SSH
* Génération
### Utilisation de Gerrit (test)
#### Sur la demo
* Choix du username, email
* Génération mot de passe HTTP
* git clone
* git config user.name "Arktest"
* git config user.email "arkanosis@gmail.com"
* git review -s
* …
#### Sur la prod
* Upload de la clef SSH
* git clone
* git review -s (ou wget https://gerrit.wikimedia.org/r/tools/hooks/commit-msg -O .git/hooks/commit-msg)
* git commit
* git review -R
* Review du commit d'un autre
### Utilisation des labs
* Création d'un outil: https://tools.wmflabs.org/ → Create New Tool
* ssh login.tools.wmflabs.or
* become $toolname
* /public/dumps/public
* sql frwiki
* SHOW TABLES
* DESCRIBE redirect
*
SELECT
  pt.page_namespace,
  pf.page_title,
  rd_title
FROM
  redirect,
  page AS pf,
  page AS pt
WHERE
  pf.page_namespace = 0
  AND rd_title = pt.page_title
  AND rd_namespace = pt.page_namespace
  AND pt.page_namespace != 0
  AND rd_from = pf.page_id
  AND pf.page_namespace = 0;
* Open grid
* mkdir public_html && echo "Hello world!" > public_html/index.htm && webservice start
* https://tools.wmflabs.org/$toolname
