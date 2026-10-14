/* =====================================================================
   Éditions Licht · maquette « Lumière dans l'ombre »
   Faisceau du héros, titres, étagère, dossiers, catalogue, panier,
   lettre, fiche livre (volume, déclassification, plan).
   Sans dépendance : tout tient dans ce fichier.
   ===================================================================== */
(() => {
  'use strict';

  const d = document, html = d.documentElement, body = d.body;
  const $ = (s, c = d) => c.querySelector(s);
  const $$ = (s, c = d) => [...c.querySelectorAll(s)];
  const mqReduit = matchMedia('(prefers-reduced-motion: reduce)');
  const reduit = () => mqReduit.matches;
  const souris = matchMedia('(hover: hover) and (pointer: fine)').matches;
  const borne = (v, a, b) => Math.min(b, Math.max(a, v));
  const euros = (c) => (c / 100).toLocaleString('fr-FR', { style: 'currency', currency: 'EUR' });

  /* Déclenche fn une seule fois quand l'élément entre dans la fenêtre. */
  const quandVisible = (els, fn, marge = '0px 0px -12% 0px') => {
    if (!('IntersectionObserver' in window)) { els.forEach(fn); return; }
    const io = new IntersectionObserver((entrees) => {
      entrees.forEach((e) => { if (e.isIntersecting) { io.unobserve(e.target); fn(e.target); } });
    }, { rootMargin: marge });
    els.forEach((el) => io.observe(el));
  };

  /* Un seul écouteur de défilement, cadencé sur l'image. */
  const auDefilement = [];
  let defilementPrevu = false;
  const defiler = () => { defilementPrevu = false; auDefilement.forEach((f) => f()); };
  addEventListener('scroll', () => { if (!defilementPrevu) { defilementPrevu = true; requestAnimationFrame(defiler); } }, { passive: true });
  addEventListener('resize', () => requestAnimationFrame(defiler));

  /* ---------- Annonce en bas d'écran ---------- */
  const annonce = (() => {
    const el = d.createElement('p');
    el.className = 'annonce-bas';
    el.setAttribute('role', 'status');
    body.appendChild(el);
    let minuteur;
    return (texte) => {
      el.textContent = texte;
      el.classList.add('visible');
      clearTimeout(minuteur);
      minuteur = setTimeout(() => el.classList.remove('visible'), 3400);
    };
  })();

  /* ---------- En-tête ---------- */
  const tete = $('.tete');
  let dernierY = scrollY;
  auDefilement.push(() => {
    if (!tete) return;
    const y = scrollY;
    tete.classList.toggle('tete--defile', y > 30);
    const bloque = html.classList.contains('menu-ouvert') || panierOuvert() || tete.contains(d.activeElement);
    if (!bloque) {
      if (y > dernierY + 6 && y > 520) tete.classList.add('tete--cachee');
      else if (y < dernierY - 6 || y <= 520) tete.classList.remove('tete--cachee');
    }
    dernierY = y;
  });
  tete?.addEventListener('focusin', () => tete.classList.remove('tete--cachee'));

  /* Menu plein écran (mobile) */
  const menuBouton = $('.menu-bouton');
  const ouvrirMenu = (oui) => {
    if (!menuBouton) return;
    html.classList.toggle('menu-ouvert', oui);
    menuBouton.setAttribute('aria-expanded', String(oui));
    const t = $('.menu-bouton__texte', menuBouton);
    if (t) t.textContent = oui ? 'Fermer' : 'Menu';
  };
  menuBouton?.addEventListener('click', () => ouvrirMenu(!html.classList.contains('menu-ouvert')));
  $$('.nav a').forEach((a) => a.addEventListener('click', () => ouvrirMenu(false)));

  /* Lien de navigation de la section en cours */
  const liensNav = $$('.nav a[href*="#"]');
  if (liensNav.length && 'IntersectionObserver' in window) {
    const parId = new Map();
    liensNav.forEach((a) => {
      const id = a.getAttribute('href').split('#')[1];
      const cible = id && d.getElementById(id);
      if (cible) parId.set(cible, a);
    });
    const io = new IntersectionObserver((entrees) => {
      entrees.forEach((e) => {
        const a = parId.get(e.target);
        if (!a) return;
        if (e.isIntersecting) { liensNav.forEach((l) => l.removeAttribute('aria-current')); a.setAttribute('aria-current', 'true'); }
        else if (a.hasAttribute('aria-current')) a.removeAttribute('aria-current');
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    parId.forEach((_, cible) => io.observe(cible));
  }

  /* ---------- La lumière se fait : fond clair sur les sections [data-jour] ---------- */
  const jours = $$('[data-jour]');
  if (jours.length && 'IntersectionObserver' in window) {
    const etat = new Map();
    const io = new IntersectionObserver((entrees) => {
      entrees.forEach((e) => etat.set(e.target, e.isIntersecting));
      const jour = [...etat.values()].some(Boolean);
      body.classList.toggle('jour', jour);
      $('meta[name="theme-color"]')?.setAttribute('content', jour ? '#f6f1e6' : '#0a0e14');
    }, { rootMargin: '-48% 0px -48% 0px' });
    jours.forEach((j) => io.observe(j));
  }

  /* ---------- Titres : les mots montent ---------- */
  const decouperMots = (el) => {
    let k = 0;
    const parcourir = (noeud) => {
      [...noeud.childNodes].forEach((n) => {
        if (n.nodeType === 3) {
          const frag = d.createDocumentFragment();
          n.textContent.split(/([ \t\n\r]+)/).forEach((m) => {
            if (!m) return;
            if (/^[ \t\n\r]+$/.test(m)) { frag.appendChild(d.createTextNode(' ')); return; }
            const o = d.createElement('span');
            o.className = 'm';
            const i = d.createElement('span');
            i.style.setProperty('--k', k++);
            i.textContent = m;
            o.appendChild(i);
            frag.appendChild(o);
          });
          n.replaceWith(frag);
        } else if (n.nodeType === 1 && !n.classList.contains('sr-only') && n.tagName !== 'BR') {
          parcourir(n);
        }
      });
    };
    parcourir(el);
  };
  $$('[data-mots]').forEach(decouperMots);
  quandVisible($$('[data-mots]'), (el) => el.classList.add('vu'));
  quandVisible($$('[data-revele]'), (el) => el.classList.add('vu'));

  /* Machine à écrire : chaque caractère apparaît à son tour, le texte reste lisible par les lecteurs d'écran. */
  $$('[data-machine]').forEach((bloc) => {
    let i = 0;
    const parcourir = (noeud) => {
      [...noeud.childNodes].forEach((n) => {
        if (n.nodeType === 3) {
          const frag = d.createDocumentFragment();
          [...n.textContent].forEach((ch) => {
            if (/\s/.test(ch)) { frag.appendChild(d.createTextNode(ch)); i++; return; }
            const s = d.createElement('span');
            s.className = 'c';
            s.style.setProperty('--i', i++);
            s.textContent = ch;
            frag.appendChild(s);
          });
          n.replaceWith(frag);
        } else if (n.nodeType === 1) parcourir(n);
      });
    };
    parcourir(bloc);
  });
  quandVisible($$('[data-machine]'), (el) => el.classList.add('vu'), '0px 0px -25% 0px');

  /* ---------- Héros : le faisceau de la lampe ---------- */
  const heros = $('.heros');
  if (heros) {
    const lettres = $$('.heros__mot > span[aria-hidden] > span', heros);
    let decalages = [];
    const consigne = $('[data-consigne]', heros);
    let l = 0, h = 0, rMax = 300, r = 0;
    let x = 0, y = 0, cx = 0, cy = 0;
    let dernierGeste = -1e9, enVue = true, rafId = 0, prete = false;
    const debut = performance.now();

    const mesurer = () => {
      const b = heros.getBoundingClientRect();
      l = b.width; h = b.height;
      decalages = lettres.map((lettre) => {
        const m = lettre.getBoundingClientRect();
        return { x: m.left - b.left, y: m.top - b.top };
      });
      rMax = Math.max(230, Math.min(l, h) * (l < 700 ? .66 : .5));
      if (!prete) { x = cx = l * .5; y = cy = h * .42; prete = true; }
    };

    /* Allumage : l'ampoule grésille avant de tenir. */
    const scenario = [[0, 0], [140, .5], [230, .04], [330, .72], [420, .12], [560, .9], [640, .55], [720, 1]];
    const niveauIntro = (t) => {
      let n = 0;
      for (const [debutEtape, v] of scenario) if (t >= debutEtape) n = v;
      return n;
    };

    const appliquer = () => {
      heros.style.setProperty('--x', x.toFixed(1) + 'px');
      heros.style.setProperty('--y', y.toFixed(1) + 'px');
      heros.style.setProperty('--r', r.toFixed(1) + 'px');
      lettres.forEach((lettre, i) => {
        lettre.style.setProperty('--lx', (x - decalages[i].x).toFixed(1) + 'px');
        lettre.style.setProperty('--ly', (y - decalages[i].y).toFixed(1) + 'px');
      });
    };

    const image = (t) => {
      rafId = 0;
      if (!enVue) return;
      const ecoule = t - debut;
      const auto = t - dernierGeste > 2600 && !reduit();
      if (auto) {
        const s = t / 1000;
        cx = l * (.5 + .34 * Math.sin(s * .42));
        cy = h * (.4 + .2 * Math.sin(s * .71 + 1.3));
      }
      const f = auto ? .03 : .14;
      x += (cx - x) * f;
      y += (cy - y) * f;
      if (ecoule < 760 && !reduit()) r = rMax * niveauIntro(ecoule);
      else r += (rMax - r) * .08;
      appliquer();
      rafId = requestAnimationFrame(image);
    };
    const relancer = () => { if (!rafId && enVue) rafId = requestAnimationFrame(image); };

    const viser = (e) => {
      const b = heros.getBoundingClientRect();
      cx = e.clientX - b.left;
      cy = e.clientY - b.top;
      dernierGeste = performance.now();
      relancer();
    };
    heros.addEventListener('pointermove', (e) => {
      viser(e);
      if (e.pointerType === 'mouse') heros.style.setProperty('--pt', '1');
    });
    heros.addEventListener('pointerdown', (e) => {
      viser(e);
      if (e.pointerType !== 'mouse') heros.classList.add('heros--touche');
    });
    heros.addEventListener('pointerleave', () => heros.style.setProperty('--pt', '0'));
    if (consigne && !souris) consigne.textContent = 'Touchez l’écran pour éclairer';

    mesurer();
    addEventListener('resize', mesurer);
    d.fonts?.ready.then(mesurer);
    if (reduit()) { r = rMax * 1.25; appliquer(); }
    setTimeout(() => heros.classList.add('allume'), reduit() ? 0 : 520);
    setTimeout(mesurer, 2600);
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(([e]) => { enVue = e.isIntersecting; relancer(); }).observe(heros);
    }
    relancer();
  }

  /* ---------- Étagère : les spots s'allument l'un après l'autre ---------- */
  $$('.etagere').forEach((etagere) => quandVisible([etagere], () => {
    $$('.rayon', etagere).forEach((rayon, i) => {
      setTimeout(() => rayon.classList.add('eclaire'), reduit() ? 0 : 250 + i * 380);
    });
  }, '0px 0px -30% 0px'));

  /* ---------- Dossiers : la chemise s'ouvre, l'encre noire se lève ---------- */
  $$('.dossiers').forEach((liste) => quandVisible([liste], () => {
    $$('.dossier', liste).forEach((dossier, i) => {
      setTimeout(() => {
        dossier.classList.add('ouvert');
        $$('.caviar', dossier).forEach((c, j) => setTimeout(() => c.classList.add('leve'), reduit() ? 0 : 900 + j * 280));
      }, reduit() ? 0 : i * 260);
    });
  }, '0px 0px -25% 0px'));

  /* ---------- Catalogue : filtres ---------- */
  const filtres = $('.filtres');
  if (filtres) {
    const fiches = $$('.fiche-cat');
    const compte = $('.filtres__compte');
    filtres.addEventListener('click', (e) => {
      const bouton = e.target.closest('button[data-filtre]');
      if (!bouton || bouton.getAttribute('aria-pressed') === 'true') return;
      const filtre = bouton.dataset.filtre;
      const faire = () => {
        $$('button[data-filtre]', filtres).forEach((b) => b.setAttribute('aria-pressed', String(b === bouton)));
        let n = 0;
        fiches.forEach((f) => {
          const garde = filtre === 'tous' || f.dataset.genre === filtre;
          f.classList.toggle('masque', !garde);
          if (garde) n++;
        });
        if (compte) compte.textContent = n + (n > 1 ? ' titres' : ' titre');
      };
      if (d.startViewTransition && !reduit()) d.startViewTransition(faire);
      else faire();
    });
  }

  /* ---------- Panier (sessionStorage : il suit la visite, pas plus) ---------- */
  const CLE = 'licht-panier';
  let donnees = {};
  try { donnees = JSON.parse($('#catalogue-donnees')?.textContent || '{}'); } catch (e) { donnees = {}; }
  const lire = () => { try { return JSON.parse(sessionStorage.getItem(CLE)) || {}; } catch (e) { return {}; } };
  const ecrire = () => { try { sessionStorage.setItem(CLE, JSON.stringify(panier)); } catch (e) { /* stockage indisponible : le panier vit le temps de la page */ } };
  let panier = lire();

  const tiroir = $('.panier');
  const liste = $('.panier__liste');
  const totalEl = $('.panier__total output');
  const vide = $('.panier__vide');
  const boutonPanier = $('.panier-bouton');
  const nombreEl = $('.panier-bouton__n');
  const commander = $('[data-commander]');
  const modeles = $('#couvertures');

  const couverture = (slug) => modeles?.content.querySelector(`[data-couv="${slug}"]`)?.cloneNode(true) || null;
  const nombre = () => Object.values(panier).reduce((a, b) => a + b, 0);

  function panierOuvert() { return !!tiroir && tiroir.classList.contains('panier--ouvert'); }

  const rendre = () => {
    if (!liste) return;
    liste.textContent = '';
    let total = 0;
    const slugs = Object.keys(panier).filter((s) => donnees[s] && panier[s] > 0);
    slugs.forEach((s) => {
      const q = panier[s], livre = donnees[s];
      total += q * livre.p;
      const li = d.createElement('li');
      li.className = 'panier__ligne';
      li.dataset.slug = s;
      const c = couverture(s);
      li.appendChild(c || d.createElement('span'));
      const info = d.createElement('div');
      const titre = d.createElement('b');
      titre.textContent = livre.t;
      const auteur = d.createElement('small');
      auteur.textContent = livre.a || 'Éditions Licht';
      const qte = d.createElement('div');
      qte.className = 'panier__qte';
      qte.innerHTML = '<button type="button" data-qte="-1"></button><output></output><button type="button" data-qte="1"></button>';
      const [moins, plus] = $$('button', qte);
      moins.textContent = '−'; moins.setAttribute('aria-label', 'Un exemplaire de moins : ' + livre.t);
      plus.textContent = '+'; plus.setAttribute('aria-label', 'Un exemplaire de plus : ' + livre.t);
      $('output', qte).textContent = q;
      info.append(titre, auteur, qte);
      const prix = d.createElement('span');
      prix.className = 'prix';
      prix.textContent = euros(q * livre.p);
      li.append(info, prix);
      liste.appendChild(li);
    });
    if (vide) vide.hidden = slugs.length > 0;
    if (totalEl) totalEl.textContent = euros(total);
    if (commander) commander.disabled = !slugs.length;
    const n = nombre();
    if (nombreEl) nombreEl.textContent = n;
    boutonPanier?.setAttribute('aria-label', `Panier, ${n} ${n > 1 ? 'livres' : 'livre'}`);
  };

  let focusAvant = null;
  const ouvrirPanier = () => {
    if (!tiroir) return;
    ouvrirMenu(false);
    focusAvant = d.activeElement;
    tiroir.classList.add('panier--ouvert');
    tiroir.removeAttribute('aria-hidden');
    boutonPanier?.setAttribute('aria-expanded', 'true');
    html.classList.add('panier-actif');
    setTimeout(() => $('.panier__fermer', tiroir)?.focus(), 60);
  };
  const fermerPanier = () => {
    if (!panierOuvert()) return;
    tiroir.classList.remove('panier--ouvert');
    tiroir.setAttribute('aria-hidden', 'true');
    boutonPanier?.setAttribute('aria-expanded', 'false');
    html.classList.remove('panier-actif');
    focusAvant?.focus?.();
  };
  boutonPanier?.addEventListener('click', ouvrirPanier);
  $('.panier__fermer')?.addEventListener('click', fermerPanier);
  $('.panier__voile')?.addEventListener('click', fermerPanier);
  tiroir?.addEventListener('keydown', (e) => {
    if (e.key !== 'Tab') return;
    const f = $$('button:not([disabled]), a[href]', tiroir);
    if (!f.length) return;
    if (e.shiftKey && d.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
    else if (!e.shiftKey && d.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
  });
  liste?.addEventListener('click', (e) => {
    const b = e.target.closest('[data-qte]');
    if (!b) return;
    const s = b.closest('.panier__ligne').dataset.slug;
    panier[s] = Math.max(0, (panier[s] || 0) + Number(b.dataset.qte));
    if (!panier[s]) delete panier[s];
    ecrire();
    rendre();
    const ligne = $(`.panier__ligne[data-slug="${s}"] [data-qte="${b.dataset.qte}"]`, liste);
    (ligne || $('.panier__fermer', tiroir))?.focus();
  });
  commander?.addEventListener('click', () => annonce('Maquette : le paiement n’est pas encore activé.'));

  const sauter = () => {
    if (!boutonPanier) return;
    boutonPanier.classList.remove('saute');
    void boutonPanier.offsetWidth;
    boutonPanier.classList.add('saute');
  };

  /* Le livre s'envole vers le panier. */
  const envoler = (bouton, slug) => {
    tete?.classList.remove('tete--cachee');
    const face = bouton.closest('.rayon, .fiche-cat, .dossier, .fiche-tete, li')?.querySelector('.livre__face');
    const clone = couverture(slug);
    if (reduit() || !face || !clone || !boutonPanier) { sauter(); return; }
    const a = face.getBoundingClientRect();
    const b = boutonPanier.getBoundingClientRect();
    clone.classList.add('vol-livre');
    Object.assign(clone.style, { left: a.left + 'px', top: a.top + 'px', width: a.width + 'px' });
    body.appendChild(clone);
    const dx = b.left + b.width / 2 - (a.left + a.width / 2);
    const dy = b.top + b.height / 2 - (a.top + a.height / 2);
    requestAnimationFrame(() => requestAnimationFrame(() => {
      clone.style.transform = `translate(${dx}px, ${dy}px) scale(.1) rotate(18deg)`;
      clone.style.opacity = '.3';
    }));
    setTimeout(() => { clone.remove(); sauter(); }, 820);
  };

  d.addEventListener('click', (e) => {
    const bouton = e.target.closest('[data-ajout]');
    if (!bouton) return;
    const slug = bouton.dataset.ajout;
    if (!donnees[slug]) return;
    const champ = bouton.dataset.quantite ? $(bouton.dataset.quantite) : null;
    const q = champ ? Math.max(1, parseInt(champ.textContent, 10) || 1) : 1;
    panier[slug] = (panier[slug] || 0) + q;
    ecrire();
    rendre();
    envoler(bouton, slug);
    if (!bouton.dataset.libelle) bouton.dataset.libelle = bouton.innerHTML;
    bouton.classList.add('ajoute');
    bouton.textContent = 'Ajouté ✓';
    clearTimeout(bouton._minuteur);
    bouton._minuteur = setTimeout(() => { bouton.classList.remove('ajoute'); bouton.innerHTML = bouton.dataset.libelle; }, 1700);
    annonce(`« ${donnees[slug].t} » ${q > 1 ? `(× ${q}) ` : ''}est dans votre panier.`);
  });
  rendre();

  d.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape') return;
    if (panierOuvert()) fermerPanier();
    else if (html.classList.contains('menu-ouvert')) { ouvrirMenu(false); menuBouton?.focus(); }
  });

  /* ---------- Lettre d'information (simulée) ---------- */
  $$('.lettre__form').forEach((form) => form.addEventListener('submit', (e) => {
    e.preventDefault();
    const champ = $('input[type="email"]', form);
    const accord = $('input[type="checkbox"]', form);
    const message = $('.lettre__message', form);
    if (!champ.value || !champ.checkValidity()) { message.textContent = 'Il manque une adresse électronique valide.'; champ.focus(); return; }
    if (accord && !accord.checked) { message.textContent = 'Cochez la case pour confirmer votre inscription.'; accord.focus(); return; }
    message.textContent = 'Merci ! Vous recevrez la prochaine parution. (Inscription simulée sur cette maquette.)';
    form.reset();
  }));

  /* =================== Fiche livre =================== */

  /* Le livre suit la main, la lampe aussi. */
  const ficheTete = $('.fiche-tete');
  if (ficheTete) {
    const livre = $('.fiche-tete__livre .livre', ficheTete);
    const objet = livre && $('.livre__objet', livre);
    if (objet && !reduit()) {
      objet.style.transition = 'transform 1.8s var(--courbe)';
      livre.style.setProperty('--ry', '-60deg');
      requestAnimationFrame(() => requestAnimationFrame(() => livre.style.removeProperty('--ry')));
      setTimeout(() => { objet.style.transition = ''; }, 1900);
    }
    if (livre && souris && !reduit()) {
      ficheTete.addEventListener('pointermove', (e) => {
        const b = ficheTete.getBoundingClientRect();
        const px = (e.clientX - b.left) / b.width, py = (e.clientY - b.top) / b.height;
        livre.style.setProperty('--ry', (34 - px * 44).toFixed(1) + 'deg');
        livre.style.setProperty('--rx', ((.5 - py) * 16).toFixed(1) + 'deg');
        ficheTete.style.setProperty('--x', (px * 100).toFixed(1) + '%');
        ficheTete.style.setProperty('--y', (py * 100).toFixed(1) + '%');
      });
      ficheTete.addEventListener('pointerleave', () => {
        livre.style.removeProperty('--ry');
        livre.style.removeProperty('--rx');
      });
    }
  }

  /* Quantité */
  $$('.quantite').forEach((q) => {
    const sortie = $('output', q);
    q.addEventListener('click', (e) => {
      const b = e.target.closest('[data-pas]');
      if (!b) return;
      sortie.textContent = borne((parseInt(sortie.textContent, 10) || 1) + Number(b.dataset.pas), 1, 20);
    });
  });

  /* Résumé caviardé : chaque passage se déclassifie en passant sous la ligne de lecture. */
  const resume = $('.dossier-resume');
  if (resume) {
    const caviars = $$('.dossier-resume__texte .caviar', resume);
    const etat = $('.dossier-resume__etat', resume);
    const jauge = $('.jauge i', resume);
    const pourcent = $('[data-pourcent]', resume);
    const majEtat = () => {
      const n = caviars.filter((c) => c.classList.contains('leve')).length;
      const p = caviars.length ? n / caviars.length : 1;
      jauge?.style.setProperty('--p', p.toFixed(3));
      if (pourcent) pourcent.textContent = Math.round(p * 100);
      etat?.classList.toggle('declasse', p === 1);
    };
    const lever = () => {
      const ligne = innerHeight * .64;
      let change = false;
      caviars.forEach((c) => {
        if (!c.classList.contains('leve') && c.getBoundingClientRect().top < ligne) { c.classList.add('leve'); change = true; }
      });
      if (change) majEtat();
    };
    $('[data-tout-lever]', resume)?.addEventListener('click', () => {
      caviars.forEach((c, i) => setTimeout(() => { c.classList.add('leve'); majEtat(); }, reduit() ? 0 : i * 140));
    });
    if (reduit()) caviars.forEach((c) => c.classList.add('leve'));
    majEtat();
    auDefilement.push(lever);
    lever();
  }

  /* Plan : le trajet se trace avec la lecture. */
  const terrain = $('.terrain');
  if (terrain) {
    const trajet = $('.plan__trajet', terrain);
    const lieux = $$('.plan__lieu', terrain);
    const items = $$('.lieux li', terrain);
    const tracer = () => {
      const b = terrain.getBoundingClientRect();
      const t = reduit() ? 1 : borne((innerHeight * .85 - b.top) / (b.height * .85), 0, 1);
      trajet?.style.setProperty('--t', t.toFixed(3));
      lieux.forEach((lieu, i) => {
        const allume = t >= Number(lieu.dataset.t || 0);
        lieu.classList.toggle('vu', allume);
        items[i]?.classList.toggle('actif', allume);
      });
    };
    auDefilement.push(tracer);
    tracer();
  }

  defiler();
})();
