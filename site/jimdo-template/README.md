# Template Jimdo (Design > Advanced > Custom Template)

Fichiers générés par `python3 make_template.py` (à relancer après chaque modification de `site/multipage/build.py`) :

- `template.html` : onglet **HTML** du Custom Template. Garder les `<var>` (navigation, sidebar, content, footer).
- `style.css` : onglet **CSS** du Custom Template.
- `karou.jpg` : onglet **Files** (photo).
- `pages/*.html` : contenu de chaque rubrique. Dans Jimdo, sur la page correspondante, ajouter un élément **Code / HTML (Embed code)** et coller le fichier :
  - `accueil.html` → Accueil
  - `a-propos-de-moi.html` → A propos de moi
  - `mes-travaux.html` → Mes travaux
  - `mes-competences.html` → Mes compétences
  - `contact.html` → Contact

Ordre : 1) coller `template.html` et `style.css` dans Custom Template, 2) envoyer `karou.jpg` dans Files, 3) coller chaque fichier `pages/` dans sa page.
