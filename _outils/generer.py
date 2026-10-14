#!/usr/bin/env python3
"""Génère la maquette Éditions Licht : accueil + fiche « La vengeance de Poutine »."""
import json, os, re

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = '1'

# ---------------------------------------------------------------- Livres
# style : serie (sombre, bande), poesie (clair), essai, roman
L = {}
def livre_def(slug, **k):
    L[slug] = k

livre_def('poutine', titre='La vengeance de Poutine', cv='<small>La vengeance de</small>Poutine', auteur='Mouftaou Badarou',
          prix=1600, genre='espionnage', lib='Espionnage', style='serie', c='#d8402a', fond='#0c0e12', emb='kremlin',
          bande='Une enquête de Jimmy Boris', page='livre/la-vengeance-de-poutine.html')
livre_def('conspiration', titre='La conspiration des anges', cv='<small>La conspiration</small>des anges', auteur='Mouftaou Badarou',
          prix=2300, genre='espionnage', lib='Espionnage', style='serie', c='#e3a43a', fond='#101210', emb='ailes',
          bande='Une enquête de Jimmy Boris', etiquette='Nouveauté')
livre_def('aicha', titre='La vengeance d’Aïcha Kadhafi', cv='<small>La vengeance d’</small>Aïcha Kadhafi', auteur='Mouftaou Badarou',
          prix=1600, genre='espionnage', lib='Espionnage', style='serie', c='#d9b48a', fond='#15110d', emb='horloge',
          bande='Espionnage', etiquette='Réédition')
livre_def('gabon', titre='Coup d’État au Gabon', cv='<small>Coup d’État</small>au Gabon', auteur='Mouftaou Badarou',
          prix=1000, genre='espionnage', lib='Espionnage', style='serie', c='#45ab72', fond='#0b100d', emb='repere',
          bande='Espionnage')
livre_def('taupe', titre='Une taupe à l’Élysée', cv='<small>Une taupe à</small>l’Élysée', auteur='Mouftaou Badarou',
          prix=1000, genre='espionnage', lib='Espionnage', style='serie', c='#5b8fdc', fond='#0b0e15', emb='serrure',
          bande='Une enquête de Jimmy Boris')
livre_def('conversations', titre='Conversations avec le diable', cv='Conversations avec le diable', auteur='Mouftaou Badarou',
          prix=1000, genre='poesie', lib='Poésie', style='poesie', c='#8a2a1c', emb='flamme', mention='Poèmes')
livre_def('amour', titre='De l’amour et des larmes', cv='De l’amour et des larmes', auteur='Julie Martinet',
          prix=1200, genre='roman', lib='Roman', style='roman', c='#e7a5a0', fond='#1d2846', emb='larme', etiquette='Nouveauté')
livre_def('afrique', titre='L’Afrique dans la peau', cv='L’Afrique dans la peau', auteur='Litsé K. Janvier',
          auteur_long='Litsé K. Janvier, entretiens avec Roch Sosthène Nepo', sous='Pour une pédagogie du développement',
          prix=2300, genre='essai', lib='Essai', style='essai', c='#f8eedf', fond='#b4532f', emb='soleil', etiquette='Nouveauté')
livre_def('reussir2', titre='Réussir mon projet d’entreprise, tome 2', cv='Réussir mon projet d’entreprise', sous='Tome 2',
          auteur='Hippolyte d’Almeida', prix=2100, genre='entreprendre', lib='Entreprendre', style='essai', c='#9fd3c7',
          fond='#1e4d5c', emb='escalier', etiquette='Nouveauté')
livre_def('reussir1', titre='Réussir mon projet d’entreprise, tome 1', cv='Réussir mon projet d’entreprise', sous='Tome 1',
          auteur='', prix=2300, genre='entreprendre', lib='Entreprendre', style='essai', c='#9fd3c7', fond='#173f4b', emb='escalier')
livre_def('esprit', titre='L’esprit au service de l’entreprise', cv='L’esprit au service de l’entreprise', auteur='',
          prix=1850, genre='entreprendre', lib='Entreprendre', style='essai', c='#f5cf7a', fond='#23344a', emb='ampoule')
livre_def('passion', titre='La passion de servir', cv='La passion de servir', auteur='', prix=2300, genre='essai', lib='Essai',
          style='essai', c='#f1c9a5', fond='#5c2733', emb='arcs')
livre_def('covid', titre='L’Afrique face au Covid-19', cv='L’Afrique face au Covid-19', auteur='', prix=1800, genre='essai',
          lib='Essai', style='essai', c='#d8ecd0', fond='#2c5a45', emb='virus')
livre_def('mokoko', titre='Si le Général Mokoko m’était conté', cv='Si le Général Mokoko m’était conté', auteur='', prix=850,
          genre='essai', lib='Essai', style='essai', c='#e9d39b', fond='#4d4126', emb='etoile')
livre_def('croix', titre='La croix et la bannière', cv='La croix et la bannière', auteur='', prix=1850, genre='essai',
          lib='Essai', style='essai', c='#e8d6f0', fond='#3b3150', emb='croix')
livre_def('amourhaine', titre='L’amour plus fort que la haine', cv='L’amour plus fort que la haine', auteur='', prix=1850,
          genre='roman', lib='Roman', style='roman', c='#f0a1a8', fond='#3a1626', emb='coeur')
livre_def('papillon', titre='Ce que le papillon doit à la chenille', cv='Ce que le papillon doit à la chenille', auteur='',
          prix=1800, genre='autres', lib='Littérature', style='roman', c='#f3c37a', fond='#2f3d5c', emb='papillon')
livre_def('dieu', titre='Dieu l’homme', cv='Dieu l’homme', auteur='', prix=900, genre='autres', lib='Religion',
          style='poesie', c='#7a5a1c', emb='rayons', mention='Religion')
livre_def('horizon', titre='Aller plus loin que l’horizon', cv='Aller plus loin que l’horizon', auteur='', prix=1850,
          genre='autres', lib='Autobiographie', style='roman', c='#ffd9a0', fond='#7a4a22', emb='horizon')

ORDRE_CATALOGUE = ['poutine', 'conspiration', 'aicha', 'gabon', 'taupe', 'conversations', 'amour', 'amourhaine', 'afrique',
                   'passion', 'covid', 'mokoko', 'croix', 'reussir2', 'reussir1', 'esprit', 'papillon', 'dieu', 'horizon']
assert sorted(ORDRE_CATALOGUE) == sorted(L), set(L) ^ set(ORDRE_CATALOGUE)

GENRES = [('tous', 'Tous'), ('espionnage', 'Espionnage'), ('roman', 'Romans'), ('poesie', 'Poésie'),
          ('essai', 'Essais'), ('entreprendre', 'Entreprendre'), ('autres', 'Récits et spiritualité')]

# ---------------------------------------------------------------- Emblèmes (traits, couleur --c)
EMB = {
    'kremlin': '<circle cx="50" cy="52" r="36"/><circle cx="50" cy="52" r="23" opacity=".55"/><path d="M50 6v20M50 78v20M4 52h20M76 52h20"/><path d="M41 76V50l9-15 9 15v26M36 76h28M44 50h12M50 35v-9M46.5 27 50 22l3.5 5"/>',
    'ailes': '<path d="M50 60C40 40 24 32 6 34c8 6 12 13 14 21 7-3 14-2 19 2-6 3-10 7-12 13 9-4 16-6 23-10z"/><path d="M50 60c10-20 26-28 44-26-8 6-12 13-14 21-7-3-14-2-19 2 6 3 10 7 12 13-9-4-16-6-23-10z"/><circle cx="50" cy="62" r="5"/><path d="M50 70v20M42 82h16" opacity=".6"/>',
    'horloge': '<circle cx="50" cy="50" r="30"/><path d="M50 26v5M50 69v5M26 50h5M69 50h5M50 50V35M50 50l10 7"/><path d="M50 6v8M50 86v8M6 50h8M86 50h8M19 19l6 6M75 75l6 6M81 19l-6 6M25 75l-6 6" opacity=".6"/>',
    'repere': '<path d="M8 62h84M8 72h84M8 82h84" opacity=".45"/><path d="M50 76C37 59 31 48 31 37a19 19 0 0 1 38 0c0 11-6 22-19 39z"/><circle cx="50" cy="37" r="7"/><path d="M14 30h10M76 30h10" opacity=".6"/>',
    'serrure': '<circle cx="50" cy="50" r="36"/><circle cx="50" cy="50" r="28" opacity=".45"/><circle cx="50" cy="42" r="9"/><path d="M45 50 40 72h20l-5-22"/>',
    'flamme': '<path d="M50 92C34 86 28 72 32 58c3-10 11-14 12-25 8 6 11 15 9 24 5-3 8-8 8-15 10 9 13 21 10 32-3 10-10 16-21 18z"/><path d="M50 92c-6-4-8-10-6-17 2-5 6-7 7-12 5 5 7 11 5 18-1 5-3 8-6 11z" opacity=".6"/>',
    'larme': '<path d="M50 12C40 33 29 46 29 61a21 21 0 0 0 42 0c0-15-11-28-21-49z"/><path d="M40 62a10 10 0 0 0 9 11" opacity=".6"/>',
    'soleil': '<path d="M6 78h88"/><path d="M20 78a30 30 0 0 1 60 0"/><path d="M33 78a17 17 0 0 1 34 0"/><path d="M50 30v-14M27 40l-9-9M73 40l9-9M15 60H4M85 60h11" opacity=".7"/>',
    'escalier': '<path d="M12 86h18V70h18V54h18V38h18V22"/><path d="M68 22h16v16" opacity=".6"/><path d="M12 92h76" opacity=".4"/>',
    'ampoule': '<path d="M37 64c0-9-11-14-11-30a24 24 0 0 1 48 0c0 16-11 21-11 30z"/><path d="M38 72h24M40 80h20M45 88h10"/><path d="M44 50l6-10 6 10" opacity=".6"/>',
    'arcs': '<path d="M14 84a36 36 0 0 1 72 0"/><path d="M26 84a24 24 0 0 1 48 0"/><path d="M38 84a12 12 0 0 1 24 0"/><path d="M8 84h84" opacity=".5"/>',
    'virus': '<circle cx="50" cy="50" r="22"/><path d="M50 28V14M50 72v14M28 50H14M72 50h14M34 34l-9-9M66 66l9 9M66 34l9-9M34 66l-9 9"/><circle cx="50" cy="12" r="3"/><circle cx="50" cy="88" r="3"/><circle cx="12" cy="50" r="3"/><circle cx="88" cy="50" r="3"/>',
    'etoile': '<path d="M50 14l10 23 25 2-19 16 6 25-22-13-22 13 6-25-19-16 25-2z"/><circle cx="50" cy="50" r="42" opacity=".4"/>',
    'croix': '<path d="M38 10v82M24 30h28"/><path d="M38 40h44l-10 10 10 10H38" opacity=".75"/>',
    'coeur': '<path d="M50 84C24 64 14 50 14 36a17 17 0 0 1 36-6 17 17 0 0 1 36 6c0 14-10 28-36 48z"/><path d="M50 30v54" opacity=".5"/>',
    'papillon': '<path d="M50 34C40 16 14 14 14 30c0 14 18 20 36 22-18 2-32 8-30 22 2 12 22 10 30-10z"/><path d="M50 34c10-18 36-20 36-4 0 14-18 20-36 22 18 2 32 8 30 22-2 12-22 10-30-10z"/><path d="M50 30v40M50 30l-6-12M50 30l6-12" opacity=".7"/>',
    'rayons': '<path d="M50 8v22M50 30 22 80M50 30 78 80M50 30 36 86M50 30 64 86M50 30 10 64M50 30 90 64"/><circle cx="50" cy="30" r="6"/>',
    'horizon': '<path d="M6 64h88"/><path d="M28 64a22 22 0 0 1 44 0"/><path d="M18 74h64M30 84h40M42 92h16" opacity=".55"/><path d="M50 30V18M30 38l-7-8M70 38l7-8" opacity=".7"/>',
}

def esc(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')

def couv(s):
    b = L[s]
    st = b['style']
    v = [f"--c:{b['c']}"]
    if b.get('fond'):
        v.append(f"--fond-couv:{b['fond']}")
    out = []
    if b['auteur']:
        out.append(f'<span class="couv__auteur">{b["auteur"]}</span>')
    if st == 'serie' and b.get('bande'):
        out.append(f'<span class="couv__bande">{b["bande"]}</span>')
    out.append(f'<svg class="couv__embleme" viewBox="0 0 100 100" aria-hidden="true">{EMB[b["emb"]]}</svg>')
    out.append(f'<span class="couv__titre">{b["cv"]}</span>')
    if b.get('sous'):
        out.append(f'<span class="couv__sous">{b["sous"]}</span>')
    if st == 'poesie' and b.get('mention'):
        out.append(f'<span class="couv__genre">{b["mention"]}</span>')
    out.append('<span class="couv__editeur">Licht</span>')
    return f'<div class="couv couv--{st}" data-couv="{s}" style="{";".join(v)}">{"".join(out)}</div>'

def livre(s, ep=14, style='', cls=''):
    b = L[s]
    fond = b.get('fond') or '#efe8da'
    tr = (b['auteur'].split()[-1] + ' · ' if b['auteur'] else '') + b['titre']
    st = f"--epx:{ep}px;--fond-dos:{fond};--c-tranche:{b['c']}" + (';' + style if style else '')
    return (f'<div class="livre{(" " + cls) if cls else ""}" style="{st}" aria-hidden="true"><div class="livre__objet">'
            f'<div class="livre__face">{couv(s)}</div><div class="livre__dos"></div>'
            f'<div class="livre__tranche"><span>{tr}</span></div><div class="livre__pages"></div></div></div>')

def prix(c):
    e, ct = divmod(c, 100)
    return f'{e},{ct:02d} €'

def ajouter(s, libelle='Ajouter', cls='btn-panier'):
    return f'<button class="{cls}" type="button" data-ajout="{s}">{libelle}</button>'

# ---------------------------------------------------------------- Gabarit
SILHOUETTE = '<svg viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="38" r="18"/><path d="M12 100c0-23 17-37 38-37s38 14 38 37z"/></svg>'
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230a0e14'/%3E"
           "%3Ccircle cx='32' cy='17' r='7' fill='%23f5cf7a'/%3E%3Cpath d='M22 28h11v22h11v6H22z' fill='%23ece4d3'/%3E%3C/svg%3E")

def entete(p, h):
    liens = [('nouveautes', 'Nouveautés'), ('meilleures-ventes', 'Meilleures ventes'), ('dossiers', 'Espionnage'),
             ('catalogue', 'Catalogue'), ('maison', 'La maison'), ('contact', 'Contact')]
    nav = ''.join(f'<li><a href="{h}#{i}">{t}</a></li>' for i, t in liens)
    return f'''<header class="tete">
  <a class="marque" href="{p or './'}" aria-label="Éditions Licht, accueil"><span class="marque__mot" aria-hidden="true">L<i>i</i>cht</span><span class="marque__lieu" aria-hidden="true">Éditions · Paris</span></a>
  <nav class="nav" id="nav" aria-label="Navigation principale"><ul>{nav}</ul></nav>
  <div class="outils">
    <button class="panier-bouton" type="button" aria-controls="panier" aria-expanded="false" aria-label="Panier, 0 livre"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 8h14l-1.2 12H6.2z"/><path d="M9 8V6.5a3 3 0 0 1 6 0V8"/></svg><span class="panier-bouton__texte" aria-hidden="true">Panier</span><span class="panier-bouton__n" aria-hidden="true">0</span></button>
    <button class="menu-bouton" type="button" aria-controls="nav" aria-expanded="false"><span class="menu-bouton__traits" aria-hidden="true"></span><span class="menu-bouton__texte">Menu</span></button>
  </div>
</header>'''

def pied(p, h):
    return f'''<footer class="pied">
  <div class="cadre">
    <div class="pied__haut">
      <div><p class="pied__mot" aria-hidden="true">L<i>i</i>cht</p><p>Éditions Licht, Paris.<br>« Cultivons-nous, lisons ! »</p></div>
      <div><h2>Lire</h2><ul><li><a href="{h}#nouveautes">Nouveautés</a></li><li><a href="{h}#meilleures-ventes">Meilleures ventes</a></li><li><a href="{h}#dossiers">Espionnage</a></li><li><a href="{h}#catalogue">Catalogue</a></li></ul></div>
      <div><h2>La maison</h2><ul><li><a href="{h}#maison">Qui sommes-nous</a></li><li><a href="{h}#auteur">Mouftaou Badarou</a></li><li><a href="#lettre">Lettre d’information</a></li><li><a href="{p}livre/la-vengeance-de-poutine.html">La vengeance de Poutine</a></li></ul></div>
      <div><h2>Nous écrire</h2><ul><li>54 avenue Hoche<br>75008 Paris</li><li><a href="mailto:leseditionslicht@yahoo.com">leseditionslicht@yahoo.com</a></li><li><a href="tel:+33784612551">+33 7 84 61 25 51</a></li></ul></div>
    </div>
    <div class="pied__bas"><p>© Éditions Licht</p><p>Maquette de démonstration · couvertures provisoires</p></div>
  </div>
</footer>'''

PANIER = '''<aside class="panier" id="panier" role="dialog" aria-modal="true" aria-labelledby="panier-titre" aria-hidden="true">
  <div class="panier__tete"><h2 id="panier-titre">Votre panier</h2><button class="panier__fermer" type="button" aria-label="Fermer le panier">×</button></div>
  <p class="panier__vide">Votre panier est vide. Les livres vous attendent sous la lampe.</p>
  <ul class="panier__liste"></ul>
  <div class="panier__pied">
    <p class="panier__total"><span>Total</span><output class="prix">0,00 €</output></p>
    <button class="btn btn--lumiere" type="button" data-commander disabled>Commander</button>
    <p class="panier__note">Livraison en France métropolitaine : 7,00 €. Paiement non activé sur cette maquette.</p>
  </div>
</aside>
<div class="panier__voile" aria-hidden="true"></div>'''

LETTRE = '''<section class="section" id="lettre" aria-labelledby="lettre-titre">
  <div class="cadre lettre">
    <div>
      <p class="surtitre">Lettre d’information</p>
      <h2 class="titre-section" id="lettre-titre" data-mots>Une parution, <em>une lettre.</em></h2>
    </div>
    <form class="lettre__form" novalidate>
      <p class="chapeau">Chaque nouveau livre, dès sa sortie. Rien d’autre.</p>
      <label class="sr-only" for="courriel">Votre adresse électronique</label>
      <div class="champ-ligne"><input id="courriel" type="email" name="courriel" placeholder="votre@adresse.fr" autocomplete="email" required><button type="submit">S’inscrire →</button></div>
      <label class="case"><input type="checkbox" name="accord"> <span>Oui, je souhaite souscrire à votre newsletter.</span></label>
      <p class="lettre__message" role="status"></p>
    </form>
  </div>
</section>'''

def typo(s):
    """Espaces fines insécables de la typographie française (hors balises et scripts)."""
    morceaux = re.split(r'(<script[\s\S]*?</script>|<[^>]+>)', s)
    for i, m in enumerate(morceaux):
        if m.startswith('<'):
            continue
        m = re.sub(r' ([;!?»])', ' \\1', m)
        m = re.sub(r' :', ' :', m)
        m = re.sub(r'« ', '« ', m)
        morceaux[i] = m
    return ''.join(morceaux)

def page(titre, desc, corps, p=''):
    h = p
    donnees = {s: {'t': b['titre'], 'a': b.get('auteur_long') or b['auteur'], 'p': b['prix']} for s, b in L.items()}
    modeles = ''.join(couv(s) for s in ORDRE_CATALOGUE)
    contenu = typo(f'''<a class="evitement" href="#contenu">Aller au contenu</a>
{entete(p, h)}
<main id="contenu" tabindex="-1">
{corps}
{LETTRE}
</main>
{pied(p, h)}
{PANIER}
<template id="couvertures">{modeles}</template>''')
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titre}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#0a0e14">
<link rel="icon" href="{FAVICON}">
<link rel="preload" href="{p}assets/fonts/bodoni-moda.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" href="{p}assets/fonts/schibsted-grotesk.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="{p}css/licht.css?v={V}">
<script>document.documentElement.classList.add('js')</script>
</head>
<body>
{contenu}
<script type="application/json" id="catalogue-donnees">{json.dumps(donnees, ensure_ascii=False)}</script>
<script src="{p}js/licht.js?v={V}" defer></script>
</body>
</html>
'''

# ---------------------------------------------------------------- Accueil
def lien_livre(s, p=''):
    return (p + L[s]['page']) if L[s].get('page') else None

def rayon(s, etiquette, p=''):
    b = L[s]
    u = lien_livre(s, p)
    vol = livre(s, ep=13)
    objet = f'<a class="rayon__lien" href="{u}" tabindex="-1" aria-hidden="true">{vol}</a>' if u else f'<div class="rayon__lien">{vol}</div>'
    titre = f'<a href="{u}">{b["titre"]}</a>' if u else b['titre']
    auteur = f'<span class="rayon__auteur">{b["auteur"]}</span>' if b['auteur'] else ''
    return f'''<li class="rayon">
      <span class="rayon__spot" aria-hidden="true"></span>
      {objet}
      <div class="rayon__info">
        <span class="rayon__etiquette">{etiquette}</span>
        <h3 class="rayon__titre">{titre}</h3>
        {auteur}
        <div class="rayon__achat"><span class="prix">{prix(b["prix"])}</span>{ajouter(s)}</div>
      </div>
    </li>'''

def classement(s, href, sous):
    b = L[s]
    return f'''<li><a href="{href}">{livre(s, ep=5)}<span><span class="classement__titre">{b["titre"]}</span><span class="classement__auteur">{sous}</span></span><span class="prix">{prix(b["prix"])}</span></a></li>'''

def dossier(s, ident, nom, lignes, p=''):
    b = L[s]
    u = lien_livre(s, p)
    interieur = ''.join(f'<p class="dossier__ligne"><b>{k} :</b> <span class="caviar">{v}</span></p>' for k, v in lignes)
    chemise = f'''<div class="dossier__chemise">
          <div class="dossier__interieur">{interieur}{livre(s, ep=5)}</div>
          <div class="dossier__rabat" aria-hidden="true"><span class="dossier__code">Dossier · Espionnage</span><span class="dossier__nom">{nom}</span><span class="tampon">Confidentiel</span></div>
        </div>'''
    enveloppe = f'<a class="dossier__lien" href="{u}" tabindex="-1">{chemise}</a>' if u else f'<div class="dossier__lien">{chemise}</div>'
    titre = f'<a href="{u}">{b["titre"]}</a>' if u else b['titre']
    return f'''<li class="dossier" id="{ident}">
        {enveloppe}
        <div class="dossier__legende">
          <h3 class="dossier__titre">{titre}</h3>
          <p class="dossier__meta">{b["auteur"]} · {b.get("etiquette", "Espionnage")}</p>
          <div class="dossier__achat"><span class="prix">{prix(b["prix"])}</span>{ajouter(s)}</div>
        </div>
      </li>'''

def fiche_cat(s):
    b = L[s]
    u = lien_livre(s)
    vol = livre(s, ep=11)
    objet = f'<a class="fiche-cat__lien" href="{u}" tabindex="-1" aria-hidden="true">{vol}</a>' if u else f'<div class="fiche-cat__lien">{vol}</div>'
    titre = f'<a href="{u}">{b["titre"]}</a>' if u else b['titre']
    auteur = f'<p class="fiche-cat__auteur">{b.get("auteur_long") or b["auteur"]}</p>' if b['auteur'] else '<p class="fiche-cat__auteur">Éditions Licht</p>'
    etiq = (' · ' + b['etiquette']) if b.get('etiquette') else ''
    return f'''<li class="fiche-cat" data-genre="{b["genre"]}" style="view-transition-name:fc-{s}">
        {objet}
        <p class="fiche-cat__genre">{b["lib"]}{etiq}</p>
        <h3 class="fiche-cat__titre">{titre}</h3>
        {auteur}
        <div class="fiche-cat__achat"><span class="prix">{prix(b["prix"])}</span>{ajouter(s)}</div>
      </li>'''

def accueil():
    lettres = ''.join(f'<span style="--k:{i}">{c}</span>' for i, c in enumerate('Licht'))
    nouveautes = ''.join([
        rayon('conspiration', 'Nouveauté · Espionnage'),
        rayon('amour', 'Nouveauté · Roman'),
        rayon('reussir2', 'Nouveauté · Entreprendre'),
        rayon('aicha', 'Réédition · Espionnage'),
    ])
    ventes = ''.join([
        classement('poutine', L['poutine']['page'], 'Mouftaou Badarou · Espionnage'),
        classement('gabon', '#dossier-gabon', 'Mouftaou Badarou · Espionnage'),
        classement('afrique', '#catalogue', 'Litsé K. Janvier · Essai'),
    ])
    dossiers = ''.join([
        dossier('conspiration', 'dossier-cotonou', 'Cotonou', [('Lieu', 'Cotonou, Bénin'), ('Année', '2014'), ('Menace', 'un attentat contre la France')]),
        dossier('aicha', 'dossier-saint-lazare', 'Saint-<br>Lazare', [('Lieu', 'Paris, quartier Saint-Lazare'), ('Année', '2015'), ('Menace', 'un second terroriste en France')]),
        dossier('gabon', 'dossier-gabon', 'Libreville', [('Lieu', 'une villa de Libreville'), ('Date', '27 octobre 2019'), ('Objet', 'un coup d’État en préparation')]),
        dossier('poutine', 'dossier-mest', 'Mest’', [('Lieu', 'Paris, 17<sup>e</sup> arrondissement'), ('Opération', '« Mest’ »'), ('Cible', 'l’Élysée')]),
    ])
    compte = {g: sum(1 for s in ORDRE_CATALOGUE if g == 'tous' or L[s]['genre'] == g) for g, _ in GENRES}
    filtres = ''.join(f'<button type="button" data-filtre="{g}" aria-pressed="{"true" if g == "tous" else "false"}">{t} <span>{compte[g]}</span></button>' for g, t in GENRES)
    catalogue = ''.join(fiche_cat(s) for s in ORDRE_CATALOGUE)
    hauteurs = [96, 88, 92, 84, 90, 80, 94, 86, 100, 82, 90, 78, 95, 87, 87, 83, 91, 79, 93]
    rangee = ''.join(
        f'<span class="rangee__dos" style="--fond:{L[s].get("fond") or "#efe8da"};--c:{L[s]["c"]};--h:{hauteurs[i]}%"><b>{L[s]["titre"]}</b></span>'
        for i, s in enumerate(ORDRE_CATALOGUE))

    corps = f'''<section class="heros" aria-labelledby="heros-titre">
  <div class="heros__scene" aria-hidden="true">
    <div class="objet objet--livre" style="left:15%;top:34%;--rot:-9deg">{livre('poutine', ep=16, style='--ry:-26deg')}</div>
    <div class="objet objet--loupe" style="left:38%;top:24%;--rot:20deg"></div>
    <div class="objet objet--feuille" style="left:56%;top:40%;--rot:5deg"><b>NOTE DE SYNTHÈSE</b>Objet : opération <span class="caviar-fixe" style="width:4.6em"></span><br>Origine : <span class="caviar-fixe" style="width:6.5em"></span><br>Lieu : Paris, 17<sup>e</sup> arr.<br><br>Plusieurs témoins <span class="caviar-fixe" style="width:8em"></span> en moins d’un mois. Le Service recommande <span class="caviar-fixe" style="width:10em"></span> et la plus grande discrétion. <span class="caviar-fixe" style="width:12em"></span> <span class="caviar-fixe" style="width:7em"></span> l’Élysée.<br><br>Agent : J. B.</div>
    <div class="objet objet--chemise" style="left:82%;top:30%;--rot:-6deg">DOSSIER<b>J. BORIS</b>DGSE<span class="tampon">Confidentiel</span></div>
    <div class="objet objet--livre" style="left:88%;top:68%;--rot:8deg">{livre('conversations', ep=10, style='--ry:22deg')}</div>
    <div class="objet objet--livre" style="left:33%;top:66%;--rot:4deg">{livre('afrique', ep=16, style='--ry:30deg')}</div>
  </div>
  <div class="heros__nuit" aria-hidden="true"></div>
  <div class="heros__halo" aria-hidden="true"></div>
  <span class="heros__point" aria-hidden="true"></span>
  <p class="heros__consigne" aria-hidden="true" data-consigne>Promenez la lampe</p>
  <div class="heros__contenu">
    <h1 class="heros__mot" id="heros-titre"><span class="sr-only">Éditions Licht</span><span aria-hidden="true">{lettres}</span></h1>
    <p class="heros__texte"><em>Licht</em> veut dire lumière. Nous publions des romans d’espionnage, de la poésie, des essais et des récits qui éclairent le monde tel qu’il va.</p>
    <div class="heros__cote">
      <p class="heros__slogan">« Cultivons-nous, lisons ! »</p>
      <div class="heros__actions"><a class="btn btn--lumiere" href="#nouveautes">Les nouveautés</a><a class="btn" href="#catalogue">Tout le catalogue</a></div>
    </div>
  </div>
</section>

<section class="section" id="nouveautes" aria-labelledby="nouv-titre">
  <div class="cadre">
    <div class="tete-section">
      <div><p class="surtitre">Nouveautés</p><h2 class="titre-section" id="nouv-titre" data-mots>Sous la lampe, <em>les dernières parutions</em></h2></div>
      <p class="chapeau">Un thriller à Cotonou, un roman sur le pardon, un guide pour entreprendre et une réédition attendue : la lumière se pose sur chacun.</p>
    </div>
    <ul class="etagere">{nouveautes}</ul>
  </div>
</section>

<section class="section" id="meilleures-ventes" aria-labelledby="ventes-titre">
  <div class="cadre">
    <div class="tete-section">
      <div><p class="surtitre">Meilleures ventes</p><h2 class="titre-section" id="ventes-titre" data-mots>Ceux qu’on <em>s’arrache</em></h2></div>
      <p class="chapeau">Deux romans d’espionnage et un livre d’entretiens sur l’Afrique : le trio de tête de la maison.</p>
    </div>
    <ol class="classement">{ventes}</ol>
  </div>
</section>

<section class="section serie" id="dossiers" aria-labelledby="dos-titre">
  <div class="cadre">
    <div class="agent">
      <div>
        <p class="surtitre">Espionnage</p>
        <h2 class="titre-section" id="dos-titre" data-mots>Les dossiers <em>Badarou</em></h2>
        <p class="chapeau">Cotonou, Paris, Libreville : Mouftaou Badarou tire ses intrigues de l’actualité et lance la DGSE sur la piste des complots de notre temps. Son agent fétiche s’appelle Jimmy Boris.</p>
      </div>
      <div>
        <div class="agent__fiche">
          <span class="tampon">Confidentiel</span>
          <dl data-machine>
            <dt>Nom</dt><dd>BORIS, Jimmy</dd>
            <dt>Service</dt><dd>DGSE</dd>
            <dt>Signes</dt><dd>élégant, fin gourmet, amateur de bière blanche</dd>
            <dt>Proches</dt><dd>Eva Randet, sa fiancée ; le colonel Arnaud Cyazinski</dd>
            <dt>Enquêtes</dt><dd>Une taupe à l’Élysée ; La conspiration des anges ; La vengeance de Poutine</dd>
          </dl>
        </div>
        <p class="agent__citation">« Mon roman est une fiction inspirée de faits réels. »<small>Mouftaou Badarou, entretien, septembre 2025</small></p>
      </div>
    </div>
    <ul class="dossiers">{dossiers}</ul>
  </div>
</section>

<section class="section" id="auteur" aria-labelledby="auteur-titre">
  <div class="cadre auteur">
    <div class="auteur__texte">
      <p class="surtitre">L’auteur à la une</p>
      <h2 class="auteur__nom" id="auteur-titre">Mouftaou <span>Badarou</span></h2>
      <p>Romancier béninois installé en France, Mouftaou Badarou a publié une dizaine de livres, du roman d’espionnage à la poésie. Il a reçu le prix de la radio Africa N° 1 en 1990, puis le prix Francophonie – Union européenne en 1996.</p>
      <p>Ses romans partent de faits réels : un contrat d’armement annulé, un coup d’État, un attentat. La fiction fait le reste.</p>
      <ul class="citations">
        <li data-revele>On ne se venge jamais sans raison.<small>Entretien, camer.be, septembre 2025</small></li>
        <li data-revele style="--d:150">Un roman n’est jamais figé : il évolue au rythme du monde qui l’entoure.<small>Entretien, camer.be, septembre 2025</small></li>
      </ul>
    </div>
    <div class="carte-presse" data-revele>
      <p class="carte-presse__entete">Auteur <small>Éditions Licht</small></p>
      <div class="carte-presse__photo"><small>Photo à venir</small>{SILHOUETTE}</div>
      <dl>
        <div><dt>Nom</dt><dd>Mouftaou Badarou</dd></div>
        <div><dt>Nationalité</dt><dd>Béninoise</dd></div>
        <div><dt>Distinctions</dt><dd>Africa N° 1 (1990), Francophonie – UE (1996)</dd></div>
        <div><dt>Signe particulier</dt><dd>Champion du Bénin de Scrabble (1992)</dd></div>
      </dl>
      <span class="carte-presse__puce" aria-hidden="true"></span>
    </div>
  </div>
</section>

<section class="section section--jour" id="catalogue" data-jour aria-labelledby="cat-titre">
  <div class="cadre">
    <div class="tete-section">
      <div><p class="surtitre">Catalogue</p><h2 class="titre-section" id="cat-titre" data-mots>Et la lumière <em>fut.</em></h2></div>
      <p class="chapeau">Dix-neuf titres, du roman d’espionnage à la poésie, de l’essai aux livres pour entreprendre.</p>
    </div>
    <div class="filtres" role="group" aria-label="Filtrer par genre">{filtres}</div>
    <p class="filtres__compte" aria-live="polite">{len(ORDRE_CATALOGUE)} titres</p>
    <ul class="grille-catalogue">{catalogue}</ul>
  </div>
</section>

<section class="section section--jour" id="maison" data-jour aria-labelledby="maison-titre">
  <div class="cadre maison">
    <h2 class="maison__mot" id="maison-titre">Licht<small>lumière, en allemand</small></h2>
    <div class="maison__texte">
      <p class="surtitre">La maison</p>
      <p>Les Éditions Licht publient, depuis Paris, des romans d’espionnage, de la poésie, des essais, des récits de vie et des livres pour entreprendre. Des voix d’ici et d’Afrique, des sujets qui éclairent le monde tel qu’il va.</p>
      <p class="maison__slogan">« Cultivons-nous, lisons ! »</p>
      <ul class="coordonnees" id="contact">
        <li><span>Adresse</span><span>54 avenue Hoche, 75008 Paris</span></li>
        <li><span>Courriel</span><a href="mailto:leseditionslicht@yahoo.com">leseditionslicht@yahoo.com</a></li>
        <li><span>Téléphone</span><a href="tel:+33784612551">+33 7 84 61 25 51</a></li>
        <li><span>Livraison</span><span>France métropolitaine : 7,00 €</span></li>
      </ul>
    </div>
  </div>
  <div class="cadre">
    <div class="rangee" aria-hidden="true">{rangee}</div>
    <p class="rangee__legende">Le fonds Licht, dix-neuf titres sur une seule étagère.</p>
  </div>
</section>'''
    return page('Éditions Licht', 'Éditions Licht, maison d’édition à Paris : romans d’espionnage, poésie, essais. « Cultivons-nous, lisons ! »', corps)

# ---------------------------------------------------------------- Fiche livre
def carte_id(nom, rot, lignes, tampon):
    dl = ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in lignes)
    return f'''<li class="carte-id" style="--rot:{rot}" data-revele>
        <div class="carte-id__photo"><span>Photo non communiquée</span>{SILHOUETTE}</div>
        <h3>{nom}</h3>
        <dl>{dl}</dl>
        <span class="tampon">{tampon}</span>
      </li>'''

def plan_svg():
    grille = ''.join(f'M{x} 0V560' for x in range(40, 800, 40)) + ''.join(f'M0 {y}H800' for y in range(40, 560, 40))
    return f'''<svg viewBox="0 0 800 560" role="img" aria-label="Plan de Paris : du 17e arrondissement à l’Élysée, puis Saint-Denis">
      <path class="plan__grille" d="{grille}"/>
      <ellipse class="plan__perif" cx="410" cy="300" rx="300" ry="205"/>
      <path class="plan__seine" d="M800 470C690 430 570 372 478 330S340 268 278 318 196 430 128 404 44 262 92 150 262 52 340 0"/>
      <text class="plan__seine-nom" x="560" y="372" transform="rotate(24 560 372)">la Seine</text>
      <text class="plan__ville" x="372" y="452">PARIS</text>
      <g class="plan__boussole" transform="translate(740 70)"><circle r="22"/><path d="M0-16 6 6 0 2-6 6z"/><text x="-5" y="-28">N</text></g>
      <path class="plan__trajet" pathLength="1" d="M300 172Q296 222 342 252Q440 170 472 52"/>
      <g class="plan__lieu" data-t="0"><circle class="onde" cx="300" cy="172" r="9"/><circle cx="300" cy="172" r="6"/><text x="196" y="160">Paris 17e</text></g>
      <g class="plan__lieu" data-t=".42"><circle class="onde" cx="342" cy="252" r="9"/><circle cx="342" cy="252" r="6"/><text x="360" y="268">Élysée</text></g>
      <g class="plan__lieu" data-t=".96"><circle class="onde" cx="472" cy="52" r="9"/><circle cx="472" cy="52" r="6"/><text x="490" y="57">Saint-Denis</text></g>
    </svg>'''

def fiche_poutine():
    p = '../'
    b = L['poutine']
    autres = ''.join([
        rayon('conspiration', 'Nouveauté · Une enquête de Jimmy Boris', p),
        rayon('taupe', 'Première version, 2022', p),
        rayon('aicha', 'Réédition · Espionnage', p),
        rayon('gabon', 'Espionnage', p),
    ])
    protagonistes = ''.join([
        carte_id('Jimmy Boris', '-2deg', [('Service', 'DGSE'), ('Rôle', 'chargé de l’enquête'), ('Goûts', 'l’élégance, la bonne table, la bière blanche')], 'Agent'),
        carte_id('Vladimir Orlov', '1.6deg', [('Poste', 'attaché militaire russe à Paris'), ('Mission', 'infiltrer l’Élysée')], 'Cible'),
        carte_id('Michel de Closets', '-1deg', [('Fonction', 'conseiller du président'), ('Dernière position', 'Paris 17e, de nuit')], 'Témoin'),
        carte_id('Arnaud Cyazinski', '2.2deg', [('Grade', 'colonel'), ('Service', 'DGSE'), ('Profil', 'rugueux, direct, redoutablement efficace')], 'DGSE'),
    ])
    corps = f'''<section class="fiche-tete" aria-labelledby="titre-livre">
  <div class="cadre fiche-tete__grille">
    <div class="fiche-tete__livre">{livre('poutine', ep=24)}</div>
    <div>
      <ol class="fil-ariane"><li><a href="../">Accueil</a></li><li><a href="../#catalogue">Catalogue</a></li><li><a href="../#dossiers">Espionnage</a></li><li aria-current="page">La vengeance de Poutine</li></ol>
      <p class="fiche-tete__serie">Roman d’espionnage · Une enquête de Jimmy Boris</p>
      <h1 class="fiche-tete__titre" id="titre-livre" data-mots>La vengeance <em>de Poutine</em></h1>
      <p class="fiche-tete__auteur">par <a href="../#auteur">Mouftaou Badarou</a></p>
      <p class="chapeau">Des témoins tombent un à un dans Paris. Derrière eux, une opération russe validée au plus haut niveau. La DGSE lance Jimmy Boris sur sa piste.</p>
      <ul class="infos"><li>196 pages</li><li>Septembre 2025</li><li>Éditions Licht</li></ul>
      <div class="achat">
        <span class="prix">{prix(b["prix"])}</span>
        <div class="quantite" role="group" aria-label="Quantité"><button type="button" data-pas="-1" aria-label="Un exemplaire de moins">−</button><output id="qte" aria-live="polite">1</output><button type="button" data-pas="1" aria-label="Un exemplaire de plus">+</button></div>
        <button class="btn btn--lumiere" type="button" data-ajout="poutine" data-quantite="#qte">Ajouter au panier</button>
        <p class="achat__note">Livraison en France métropolitaine : 7,00 €.</p>
      </div>
    </div>
  </div>
</section>

<section class="section dossier-resume" id="resume" aria-labelledby="resume-titre">
  <div class="cadre dossier-resume__grille">
    <div>
      <p class="surtitre">Le résumé</p>
      <h2 class="dossier-resume__titre" id="resume-titre">Opération<br>« Mest’ »</h2>
      <p class="dossier-resume__note">« Mest’ » : vengeance, en russe.</p>
    </div>
    <div class="dossier-resume__texte">
      <p>Paris, une nuit, dans le <span class="caviar surligne">17<sup>e</sup> arrondissement</span>. Un conseiller du président de la République est <span class="caviar surligne">braqué en pleine rue</span>. Ce n’est pas un fait divers.</p>
      <p>D’autres témoins tombent, un à un. Pour la DGSE, ces morts dessinent une même opération : <span class="caviar surligne">« Mest’ »</span>, montée par les services de renseignement russes et validée <span class="caviar surligne">par le président russe lui-même</span>.</p>
      <p>L’affaire est confiée à <span class="caviar surligne">Jimmy Boris</span>. En face, un attaché militaire en poste à Paris, <span class="caviar surligne">Vladimir Orlov</span>, a reçu une mission impensable : <span class="caviar surligne">infiltrer l’Élysée</span>.</p>
      <p>Plus Jimmy Boris avance, plus la conspiration s’étend. Ceux qui l’ont montée ne reculeront devant rien. Pas même devant l’idée <span class="caviar surligne">d’abattre un conseiller du président français</span> en plein Paris.</p>
    </div>
    <aside class="dossier-resume__etat" aria-label="Niveau de classification">
      <p>Classification du dossier</p>
      <div class="dossier-resume__tampons"><span class="tampon tampon--secret">Secret défense</span><span class="tampon tampon--declasse">Déclassifié</span></div>
      <div class="jauge"><i></i></div>
      <p class="compte"><span data-pourcent>0</span> % du dossier levé</p>
      <button class="btn btn--petit" type="button" data-tout-lever>Tout déclassifier</button>
      <p class="dossier-resume__genese">Écrit entre 2017 et 2019, publié une première fois en 2022 sous le titre <i>Une taupe à l’Élysée</i>, le roman a été repris après l’invasion de l’Ukraine.</p>
    </aside>
  </div>
</section>

<section class="section" id="protagonistes" aria-labelledby="proto-titre">
  <div class="cadre">
    <div class="tete-section">
      <div><p class="surtitre">Les protagonistes</p><h2 class="titre-section" id="proto-titre" data-mots>Qui est <em>qui</em></h2></div>
      <p class="chapeau">Quatre fiches sorties des archives. Les photos, elles, sont restées au coffre.</p>
    </div>
    <ul class="protagonistes">{protagonistes}</ul>
  </div>
</section>

<section class="section" id="terrain" aria-labelledby="terrain-titre">
  <div class="cadre">
    <div class="tete-section">
      <div><p class="surtitre">Le terrain</p><h2 class="titre-section" id="terrain-titre" data-mots>Paris, <em>de nuit</em></h2></div>
      <p class="chapeau">Faites défiler : le trajet de l’enquête se trace sur le plan.</p>
    </div>
    <div class="terrain">
      <div class="plan">{plan_svg()}</div>
      <ul class="lieux">
        <li><b>Paris 17<sup>e</sup></b><span>Rue Ampère, de nuit : un conseiller du président est braqué.</span></li>
        <li><b>Palais de l’Élysée</b><span>La cible : un homme de Moscou doit s’y infiltrer.</span></li>
        <li><b>Saint-Denis</b><span>Un rendez-vous qui tourne au guet-apens.</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="presse-titre">
  <div class="cadre presse">
    <p class="surtitre" id="presse-titre">Ils l’ont lu</p>
    <blockquote data-revele>Un roman d’espionnage particulièrement prometteur.</blockquote>
    <cite>Calvin Djouari, « J’ai lu pour vous », camer.be, septembre 2025</cite>
    <p class="presse__second" data-revele>« On ne se venge jamais sans raison. »<br><small>Mouftaou Badarou, entretien, septembre 2025</small></p>
  </div>
</section>

<section class="section" id="fiche-technique" aria-labelledby="ft-titre">
  <div class="cadre">
    <p class="surtitre">Fiche technique</p>
    <h2 class="sr-only" id="ft-titre">Fiche technique</h2>
    <dl class="fiche-technique">
      <div><dt>Auteur</dt><dd>Mouftaou Badarou</dd></div>
      <div><dt>Éditeur</dt><dd>Éditions Licht, Paris</dd></div>
      <div><dt>Genre</dt><dd>Roman d’espionnage</dd></div>
      <div><dt>Parution</dt><dd>Septembre 2025</dd></div>
      <div><dt>Pages</dt><dd>196</dd></div>
      <div><dt>Prix</dt><dd>16,00 €</dd></div>
      <div><dt>Livraison</dt><dd>7,00 € (France métropolitaine)</dd></div>
      <div><dt>ISBN</dt><dd class="a-venir">à compléter</dd></div>
    </dl>
  </div>
</section>

<section class="section" id="autres" aria-labelledby="autres-titre">
  <div class="cadre">
    <div class="tete-section">
      <div><p class="surtitre">Du même auteur</p><h2 class="titre-section" id="autres-titre" data-mots>Les autres <em>dossiers</em></h2></div>
      <p class="chapeau">Cotonou, Saint-Lazare, Libreville, l’Élysée : quatre enquêtes à lire dans l’ordre que vous voudrez.</p>
    </div>
    <ul class="etagere">{autres}</ul>
  </div>
</section>'''
    return page('La vengeance de Poutine · Éditions Licht',
                'La vengeance de Poutine, roman d’espionnage de Mouftaou Badarou : une enquête de Jimmy Boris (DGSE). Éditions Licht, 196 pages, 16 €.',
                corps, p)

# ---------------------------------------------------------------- 404
def page_404():
    corps = '''<section class="heros" aria-labelledby="heros-titre" style="min-height:80svh">
  <div class="heros__scene" aria-hidden="true"></div>
  <div class="heros__nuit" aria-hidden="true"></div>
  <div class="heros__halo" aria-hidden="true"></div>
  <span class="heros__point" aria-hidden="true"></span>
  <p class="heros__consigne" aria-hidden="true" data-consigne>Promenez la lampe</p>
  <div class="heros__contenu">
    <h1 class="heros__mot" id="heros-titre"><span class="sr-only">Page introuvable</span><span aria-hidden="true"><span style="--k:0">4</span><span style="--k:1">0</span><span style="--k:2">4</span></span></h1>
    <p class="heros__texte">Cette page est restée <em>dans l’ombre</em>. Le dossier a peut-être été déplacé.</p>
    <div class="heros__cote"><div class="heros__actions"><a class="btn btn--lumiere" href="/">Retour à l’accueil</a></div></div>
  </div>
</section>'''
    return page('Page introuvable · Éditions Licht', 'Cette page n’existe pas ou plus.', corps, '/')

# ---------------------------------------------------------------- Écriture
def ecrire(chemin, texte):
    chemin = os.path.join(RACINE, chemin)
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write(texte)

ecrire('index.html', accueil())
ecrire('livre/la-vengeance-de-poutine.html', fiche_poutine())
ecrire('404.html', page_404())
ecrire('vercel.json', json.dumps({'cleanUrls': True, 'trailingSlash': False,
                                  'headers': [{'source': '/assets/(.*)', 'headers': [{'key': 'Cache-Control', 'value': 'public, max-age=31536000, immutable'}]}]}, indent=2) + '\n')
print('ok', len(L), 'livres')
