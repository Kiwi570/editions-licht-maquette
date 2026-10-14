# Éditions Licht · maquette « Lumière dans l'ombre »

Maquette statique (HTML, CSS, JavaScript sans dépendance) pour le site des Éditions Licht.
Aucune étape de construction : le dossier se déploie tel quel sur Vercel.

## Pages

| Adresse | Contenu |
|---|---|
| `/` | Accueil : héros au faisceau lumineux, nouveautés, meilleures ventes, dossiers d'espionnage, auteur, catalogue filtrable (19 titres), la maison, lettre d'information |
| `/livre/la-vengeance-de-poutine` | Fiche livre : couverture en volume, résumé caviardé qui se déclassifie, protagonistes, plan de Paris, presse, fiche technique, autres dossiers |
| `/404` | Page introuvable, dans le même esprit |

## Ce qui est provisoire

- **Couvertures** : dessinées en HTML/CSS en attendant les vraies. Pour les remplacer, mettre l'image dans `.livre__face` (ou adapter la fonction `couv()` du générateur).
- **Photos** : silhouettes « Photo à venir » sur la carte de l'auteur et les fiches personnages.
- **ISBN de La vengeance de Poutine** : marqué « à compléter ».
- **Auteurs inconnus** : plusieurs titres du catalogue n'ont pas d'auteur affiché sur le site actuel ; la maquette n'en invente pas.
- **Panier** : simulé (sessionStorage). Le bouton « Commander » affiche un message, aucun paiement n'est branché.
- **Lettre d'information** : inscription simulée.

## Fichiers

```
index.html, 404.html, livre/…      pages générées
css/licht.css                      toute la mise en forme
js/licht.js                        faisceau, animations, filtres, panier, fiche livre
assets/fonts/                      Bodoni Moda, Schibsted Grotesk, Courier Prime, Big Shoulders (licence OFL)
_outils/generer.py                 générateur des pages (données des livres en tête de fichier)
vercel.json                        adresses propres (sans .html)
```

Pour modifier un prix, un titre ou ajouter un livre : éditer la liste en haut de `_outils/generer.py`, puis lancer `python3 _outils/generer.py`.

## Sources du contenu

- Site actuel : editions-licht.com (titres, prix, résumés, coordonnées, slogan).
- Entretien avec Mouftaou Badarou, camer.be, septembre 2025 (genèse du roman, personnages, citations).
- « J'ai lu pour vous » de Calvin Djouari, camer.be, septembre 2025 (citation de presse, lieux de l'intrigue).
