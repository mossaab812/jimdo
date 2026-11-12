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

## Dossier `a-coller/` (à utiliser)

Tous les fichiers à coller, numérotés dans l'ordre :

| Fichier | Où le coller dans Jimdo |
|---|---|
| `1-template.html` | Custom Template → onglet **HTML** (remplacer tout) |
| `2-style.css` | Custom Template → onglet **CSS** (remplacer tout) |
| `karou.jpg` | Fichiers (Files) |
| `3-accueil.html` | Page **Accueil** → élément Embed/HTML (remplacer tout) |
| `4-a-propos-de-moi.html` | Page **A propos de moi** |
| `5-mes-travaux.html` | Page **Mes travaux** |
| `6-mes-competences.html` | Page **Mes compétences** |
| `7-contact.html` | Page **Contact** |
| `8-mon-cv.html` | Sous-page **Mon CV** (protégée par mot de passe) |

Avant de coller : supprimer l'ancien contenu de chaque élément (les anciennes versions mélangent les styles).
