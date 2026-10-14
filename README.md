# Éditions Licht · maquette « Lumière dans l'ombre »

Maquette statique (HTML, CSS, JavaScript sans dépendance) pour le site des Éditions Licht.
Aucune étape de construction : le dossier se déploie tel quel sur Vercel.

## Pages

| Adresse | Contenu |
|---|---|
| `/` | Accueil : héros au faisceau lumineux, nouveautés, meilleures ventes, dossiers d'espionnage, auteur, catalogue filtrable (19 titres), la maison, lettre d'information |
| `/livre/la-vengeance-de-poutine` | Fiche livre : couverture en volume, résumé caviardé qui se déclassifie, protagonistes, plan de Paris, presse, fiche technique, autres dossiers |
| `/404` | Page introuvable, dans le même esprit |

## Images

- **Couvertures** : les 19 couvertures réelles, reprises du site actuel (`assets/couvertures/`, format WebP). Elles sont un peu compressées par Wix : des fichiers en haute définition de l'éditeur rendraient la fiche livre plus nette.
- **Images d'ambiance** (`assets/img/`) : bureau sous la lampe, photos de filature des dossiers, toits de Paris, lampe de la maison, enveloppe de la lettre. Ce sont des illustrations générées, pas des photos réelles.

## Ce qui reste provisoire

- **Photos** : silhouettes « Photo à venir » sur la carte de l'auteur et les fiches personnages.
- **ISBN de La vengeance de Poutine** : marqué « à compléter ».
- **Titre à vérifier** : le site actuel indique « Dieu l'homme », la couverture « Dieu et l'homme » ; la maquette suit la couverture.
- **Auteurs** : relevés sur les couvertures quand le site ne les affichait pas.
- **Panier** : simulé (sessionStorage). Le bouton « Commander » affiche un message, aucun paiement n'est branché.
- **Lettre d'information** : inscription simulée.

## Fichiers

```
index.html, 404.html, livre/…      pages générées
css/licht.css                      toute la mise en forme
js/licht.js                        faisceau, animations, filtres, panier, fiche livre
assets/couvertures/                couvertures des livres
assets/img/                        images d'ambiance
assets/fonts/                      Bodoni Moda, Schibsted Grotesk, Courier Prime, Big Shoulders (licence OFL)
_outils/generer.py                 générateur des pages (données des livres en tête de fichier)
vercel.json                        adresses propres (sans .html)
```

Pour modifier un prix, un titre ou ajouter un livre : éditer la liste en haut de `_outils/generer.py`, puis lancer `python3 _outils/generer.py`.

## Sources du contenu

- Site actuel : editions-licht.com (titres, prix, résumés, coordonnées, slogan).
- Entretien avec Mouftaou Badarou, camer.be, septembre 2025 (genèse du roman, personnages, citations).
- « J'ai lu pour vous » de Calvin Djouari, camer.be, septembre 2025 (citation de presse, lieux de l'intrigue).
