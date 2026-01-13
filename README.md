# 🎓 Défi Text Mining & RI - M2 BI&A (2025-2026)

Bienvenue dans le dépôt du défi **Text Mining et Recherche d'Information**. Ce projet est réalisé dans le cadre du Master 2 Business Intelligence & Analytics à l'Université Lumière Lyon 2.

## 📝 Contexte du Projet

Ce défi s'inscrit dans le contexte de la recherche scientifique et s'inspire du **Défi EGC 2020** : *« 20 ans d'histoire pour quel avenir ? »*. L'objectif est d'analyser l'évolution de la communauté EGC (Extraction et Gestion des Connaissances) à travers ses publications.

> **Le mot d'ordre :** « Explorez, investiguez, surprenez-moi ! »

## 🎯 Objectifs

L'objectif principal est de fournir des éléments d'analyse à l'Association EGC concernant sa production scientifique.

* **Tableaux de bord :** Création de visuels décisionnels.
* **Compétences BI & Text Mining :** Articulation entre l'analyse de données structurées et l'analyse textuelle (fouille de textes).
* **Challenge :** Travail sur données réelles dans un temps limité.

## 📂 Données

Le projet s'appuie sur deux jeux de données principaux (fournis au format CSV) :

### 1. `edition_EGC.csv`
Recense les lieux et dates des conférences.
* `Year` : Année de l'édition
* `City` : Ville
* `Country` : Pays

### 2. `export_articles_EGC_2004_2018.csv`
Contient les métadonnées des articles publiés.
* `Series` : Nom de la revue
* `Booktitle` : Conférence (EGC)
* `Year` : Année
* `Title` : Titre de l'article
* `Abstract` : Résumé de l'article (Cœur de l'analyse textuelle)
* `Authors` : Liste des auteurs (séparés par des virgules)
* `Link pdf1page` & `Lien pdfarticle` : Liens vers les documents

## 🛠 Organisation & Contraintes

* **Groupe :** 4 à 5 personnes (mixité recommandée avec des profils ayant suivi le cours d'ingénierie des données).
* **Outils :** Choix libre (Solutions Open Source privilégiées).
* **Restitution :** Communication orale de 20 minutes.
* **Date de rendu :** Vendredi 16 janvier (après-midi).

## 🚀 Pistes d'exploration

* Analyse de l'évolution des thématiques au fil des années (Topic Modeling).
* Cartographie des collaborations entre auteurs (Graphes).
* Analyse géographique des éditions et des affiliations.
* Identification des tendances émergentes ou en déclin.

---
*Projet encadré par Cécile Favre, Professeure en informatique à l'Université Lumière Lyon 2.*
