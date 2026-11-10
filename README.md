# jimdo

Site personnel de Karou Mosaab (Master 2 Marketing Digital, EHEC) - version trilingue (AR / FR / EN).

## Fichiers
- `site/index.html` : page complète (CSS + JS intégrés, aucune dépendance externe).

## Mise en ligne sur Jimdo
1. Dans Jimdo, créer 5 pages avec ces noms exacts : Accueil, A propos de moi, Mes travaux, Mes compétences, Contact.
2. Ajouter un élément **Code / HTML (Embed code)** sur la page Accueil et y coller tout le contenu de `site/index.html`.
3. Remplacer `CV_URL` (bouton « Mon CV ») par l'adresse de la sous-page CV protégée par mot de passe créée dans Jimdo.
4. Remplacer `CODE_COMPTEUR_COMPTEURDEVISITE` par le code généré sur compteurdevisite.com (compteur de visiteurs).
5. Remplacer les liens Instagram / LinkedIn / e-mail par les vrais liens.

## Version multi-pages (`site/multipage/`)
- `build.py` : générateur. Modifier les textes ici, puis lancer `python3 build.py`.
- `index.html`, `about.html`, `works.html`, `skills.html`, `contact.html` : pages autonomes (CSS et JS intégrés).
- Dans Jimdo : une page par rubrique, et dans chaque page un élément « Code / HTML (Embed code) » avec le contenu du fichier correspondant.
- Les liens du menu (`works.html`, etc.) sont relatifs : sur Jimdo, utilisez le menu Jimdo à la place, ou remplacez-les par les adresses des pages Jimdo.
- Placeholders à remplacer : `REMPLACER_PAR_URL_MON_CV` (bouton CV, page about).
