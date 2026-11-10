#!/usr/bin/env python3
"""Génère les fichiers Jimdo à partir de site/multipage/build.py :
  - style.css         : CSS du Custom Template (scopé sous #container + corrections Jimdo)
  - template.html     : structure (à coller dans l'onglet HTML du Custom Template)
  - pages/*.html      : contenu de chaque rubrique (à coller dans l'élément HTML de la page)
Usage : python3 make_template.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "multipage"))
import build  # noqa: E402

# Adresses des pages Jimdo (générées par Jimdo d'après les noms des rubriques)
JIMDO_URL = {
    "index.html": "/",
    "about.html": "/a-propos-de-moi/",
    "works.html": "/mes-travaux/",
    "skills.html": "/mes-competences/",
    "contact.html": "/contact/",
}
PAGE_FILE = {
    "index.html": "accueil.html",
    "about.html": "a-propos-de-moi.html",
    "works.html": "mes-travaux.html",
    "skills.html": "mes-competences.html",
    "contact.html": "contact.html",
}


def scope_sel(sel):
    out = []
    for s in sel.split(","):
        s = s.strip()
        if not s:
            continue
        if s == ":root" or s in ("html", "body"):
            out.append("#container")
        elif s == "*":
            out.append("#container *")
        elif s.startswith("#container"):
            out.append(s)
        else:
            out.append("#container " + s)
    return ", ".join(out)


def scope_css(text):
    res, i, n = [], 0, len(text)
    while i < n:
        j = text.find("{", i)
        if j < 0:
            res.append(text[i:])
            break
        head = text[i:j].strip()
        depth, k = 0, j
        while k < n:
            if text[k] == "{":
                depth += 1
            elif text[k] == "}":
                depth -= 1
                if depth == 0:
                    break
            k += 1
        body = text[j + 1:k]
        if head.startswith("@media"):
            res.append(f"{head}{{\n{scope_css(body)}}}\n")
        elif head.startswith("@keyframes") or head.startswith("@font-face"):
            res.append(f"{head}{{{body}}}\n")
        else:
            res.append(f"{scope_sel(head)}{{{body}}}\n")
        i = k + 1
    return "".join(res)


OVERRIDES = """
/* ---- Corrections pour Jimdo ---- */
html,body{background:#F5F2EA!important;margin:0!important;padding:0!important}
#container{min-height:100vh;background:#F5F2EA;color:#1C1812}
#container *{box-sizing:border-box}
#container a{color:inherit;text-decoration:none}
#container img{max-width:100%;height:auto}
/* Navigation Jimdo : pilules au lieu de liens bruts */
#navigation{max-width:1160px;margin:18px auto 0;padding:0 5%;text-align:center}
#navigation ul{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;list-style:none;padding:0;margin:0}
#navigation li{list-style:none;margin:0;padding:0}
#navigation a{display:inline-block;padding:9px 16px;border-radius:999px;background:#fff;box-shadow:0 8px 20px rgba(28,24,18,.08);font-weight:700;font-size:.92rem;color:#1C1812;transition:background .25s}
#navigation a:hover,#navigation a.current,#navigation a.active,#navigation li.current a,#navigation li.active a{background:#FFA41B}
/* Contenu : pas de masquage à l'apparition (le JS n'est pas garanti dans Jimdo) */
#content{max-width:1160px;margin:0 auto}
.reveal{opacity:1!important;transform:none!important;transition:none!important}
/* Pied de page */
#footer{text-align:center;color:#6E6759;padding:30px 5% 30px;font-size:.9rem;margin-top:50px}
#footer .social{margin-top:16px}
#footer .social a{font-size:1.05rem;width:46px;height:46px}
#footer .gutter{padding-bottom:14px}
"""


def build_css():
    head = (
        "@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');\n"
        "@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');\n"
    )
    return head + scope_css(build.CSS) + OVERRIDES


PAGE_SCRIPT = """<script>
(function(){
  document.querySelectorAll('.svc').forEach(function(item){
    function toggle(){
      var open = item.classList.contains('open');
      document.querySelectorAll('.svc.open').forEach(function(o){ o.classList.remove('open'); });
      if (!open) item.classList.add('open');
    }
    item.addEventListener('click', toggle);
  });
  var form = document.getElementById('contactForm');
  if (form) form.addEventListener('submit', function(ev){
    ev.preventDefault();
    var n = form.name.value, m = form.email.value, t = form.message.value;
    var body = 'Nom: ' + n + '\\nE-mail: ' + m + '\\n\\n' + t;
    window.location.href = 'mailto:%s?subject=' + encodeURIComponent('Contact via portfolio - ' + n) + '&body=' + encodeURIComponent(body);
  });
})();
</script>""" % build.EMAIL


def jimdo_links(html):
    for src, dst in JIMDO_URL.items():
        html = html.replace(f'href="{src}"', f'href="{dst}"')
    return html


def main():
    # 1) CSS
    with open(os.path.join(HERE, "style.css"), "w", encoding="utf-8") as f:
        f.write(build_css())

    # 2) Template (structure)
    template = f"""<div id="container">

  <div id="header">
    <div class="topbar">
      <nav class="navbar">
        <a class="logo" href="/"><span class="logo-dot">K</span>Karou.</a>
        <div class="navright">
          <a class="cta-nav" href="/contact/">Me contacter</a>
        </div>
      </nav>
    </div>
  </div>

  <div id="navigation">
    <var>navigation[1|2|3]</var>
  </div>

  <div id="sidebar"><var>sidebar</var></div>

  <div id="content">
    <var>content</var>
  </div>

  <div id="footer">
    <div class="gutter"><var>footer</var></div>
    <div class="social">
      <a href="{build.INSTAGRAM}" target="_blank" rel="noopener" title="Instagram"><i class="fa-brands fa-instagram">&#xf16d;</i></a>
      <a href="{build.FACEBOOK}" target="_blank" rel="noopener" title="Facebook"><i class="fa-brands fa-facebook-f">&#xf39e;</i></a>
      <a href="{build.LINKEDIN}" target="_blank" rel="noopener" title="LinkedIn"><i class="fa-brands fa-linkedin-in">&#xf0e1;</i></a>
      <a href="{build.YOUTUBE}" target="_blank" rel="noopener" title="YouTube"><i class="fa-brands fa-youtube">&#xf167;</i></a>
    </div>
    <p>&copy; 2026 Karou Mosaab</p>
  </div>

</div>
"""
    with open(os.path.join(HERE, "template.html"), "w", encoding="utf-8") as f:
        f.write(template)

    # 3) Contenu des rubriques (une fois collé dans la page Jimdo correspondante)
    os.makedirs(os.path.join(HERE, "pages"), exist_ok=True)
    for src, fname in PAGE_FILE.items():
        body = build.BODY[src]
        body = jimdo_links(body)
        body = build.fix_icons(body)
        with open(os.path.join(HERE, "pages", fname), "w", encoding="utf-8") as f:
            f.write(body + "\n" + PAGE_SCRIPT + "\n")
    print("OK : style.css, template.html, pages/*.html")


if __name__ == "__main__":
    main()
