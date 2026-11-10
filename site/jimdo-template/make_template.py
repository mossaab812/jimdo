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


HOME_T = {
    "fr": {"welcome": "Bienvenue sur mon portfolio", "badge": "Master 2 Marketing Digital · EHEC",
           "sub": "Étudiant en Master 2 Marketing Digital, je combine stratégie marketing, développement web, automatisation et photographie automobile.",
           "btn1": "Voir mes travaux", "btn2": "Me contacter",
           "marquee": "Marketing digital ✦ Développement web ✦ Automatisation ✦ Photo automobile ✦ ",
           "c1t": "Marketing digital", "c1d": "Stratégie de contenu et présence en ligne.",
           "c2t": "Développement web", "c2d": "Sites simples, rapides et adaptés au mobile.",
           "c3t": "Automatisation", "c3d": "Automatiser les tâches répétitives pour gagner du temps.",
           "dt": "Qui est Karou ?",
           "dp": "Étudiant à l'EHEC, membre du département RH & Communication de HUC Alumni (Company Discovery). Passionné par le web, les réseaux sociaux et la photographie automobile.",
           "dbtn": "En savoir plus", "counter": "Compteur de visiteurs"},
    "ar": {"welcome": "مرحباً بكم في البورتفوليو تاعي", "badge": "ماستر 2 تسويق رقمي · EHEC",
           "sub": "طالب ماستر 2 تسويق رقمي، أجمع بين الاستراتيجية التسويقية وتطوير الويب والأتمتة وتصوير السيارات.",
           "btn1": "شوف أعمالي", "btn2": "اتصل بي",
           "marquee": "التسويق الرقمي ✦ تطوير الويب ✦ الأتمتة ✦ تصوير السيارات ✦ ",
           "c1t": "التسويق الرقمي", "c1d": "استراتيجية المحتوى وحضور قوي على الإنترنت.",
           "c2t": "تطوير الويب", "c2d": "مواقع بسيطة وسريعة ومتجاوبة مع الهاتف.",
           "c3t": "الأتمتة", "c3d": "أتمتة المهام المتكررة باش توفر الوقت.",
           "dt": "من هو كارو؟",
           "dp": "طالب في EHEC، عضو قسم الموارد البشرية والاتصال في نادي HUC Alumni (Company Discovery). شغوف بالويب ومواقع التواصل وتصوير السيارات.",
           "dbtn": "تعرف عليا أكثر", "counter": "عداد الزوار"},
    "en": {"welcome": "Welcome to my portfolio", "badge": "Master 2 Digital Marketing · EHEC",
           "sub": "Master 2 Digital Marketing student, I combine marketing strategy, web development, automation and car photography.",
           "btn1": "See my work", "btn2": "Contact me",
           "marquee": "Digital marketing ✦ Web development ✦ Automation ✦ Car photography ✦ ",
           "c1t": "Digital marketing", "c1d": "Content strategy and online presence.",
           "c2t": "Web development", "c2d": "Simple, fast, mobile-friendly websites.",
           "c3t": "Automation", "c3d": "Automating repetitive tasks to save time.",
           "dt": "Who is Karou?",
           "dp": "EHEC student, member of the HR & Communication department at HUC Alumni (Company Discovery). Passionate about web, social media and car photography.",
           "dbtn": "Learn more", "counter": "Visitor counter"},
}

HOME_CSS = """
.km-home{background:#F5F2EA;color:#1C1812;font-family:'Plus Jakarta Sans','Cairo',system-ui,sans-serif;line-height:1.6;padding:0 0 30px;overflow:hidden}
.km-home *{box-sizing:border-box}
.km-home a{color:inherit;text-decoration:none}
.km-home p{color:#6E6759;margin:0}
.km-wrap{max-width:1160px;margin:0 auto;padding:0 5%}
.km-lang{display:flex;justify-content:flex-end;gap:6px;padding-top:24px;max-width:1160px;margin:0 auto;padding-left:5%;padding-right:5%}
.km-lang button{background:#fff;border:1px solid #E4DDCC;color:#1C1812;padding:6px 12px;border-radius:999px;cursor:pointer;font-weight:700;font-size:.8rem}
.km-lang button.on{background:#FFA41B;border-color:#FFA41B}
.km-hero{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;padding:30px 0 40px}
.km-hero h1{font-size:3.4rem;line-height:1.08;font-weight:800;letter-spacing:-.8px;margin-bottom:14px;color:#1C1812}
.km-hl{color:#FFA41B}
.km-badge{display:inline-block;background:#fff;box-shadow:0 8px 20px rgba(28,24,18,.08);padding:8px 16px;border-radius:999px;font-weight:600;font-size:.88rem;margin-bottom:20px}
.km-sub{font-size:1.08rem;max-width:520px;margin-bottom:26px}
.km-btns{display:flex;gap:12px;flex-wrap:wrap}
.km-btn{display:inline-block;padding:14px 26px;border-radius:999px;font-weight:700;font-size:1rem;transition:transform .25s}
.km-btn:hover{transform:translateY(-3px)}
.km-btn-amber{background:#FFA41B;color:#1C1812;box-shadow:0 10px 24px rgba(255,164,27,.35)}
.km-btn-dark{background:#1C1812;color:#fff}
.km-photo{position:relative;max-width:440px;width:100%;justify-self:center;aspect-ratio:4/5}
.km-photo .blob{position:absolute;inset:6% 4% 0 8%;background:#FFA41B;border-radius:48% 52% 46% 54%/40% 42% 58% 60%}
.km-photo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 15%;border-radius:36px;box-shadow:0 12px 32px rgba(28,24,18,.12)}
.km-marquee{background:#1C1812;border-top:3px solid #FFA41B;border-bottom:3px solid #FFA41B;overflow:hidden;white-space:nowrap;padding:16px 0}
.km-track{display:inline-block;animation:km-scroll 26s linear infinite}
.km-track span{font-size:1.4rem;font-weight:800;color:#fff;padding-right:14px}
.km-track span:nth-child(even){color:#FFA41B}
@keyframes km-scroll{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.km-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:22px;padding:60px 0 20px}
.km-card{background:#fff;border-radius:28px;padding:28px;box-shadow:0 12px 32px rgba(28,24,18,.08);transition:transform .3s}
.km-card:hover{transform:translateY(-6px)}
.km-ico{width:56px;height:56px;border-radius:50%;background:#1C1812;color:#FFA41B;display:grid;place-items:center;margin-bottom:14px;font-size:1.2rem}
.km-card h3{font-size:1.25rem;font-weight:700;margin-bottom:8px;color:#1C1812}
.km-dark{background:#1C1812;border-radius:36px;padding:56px 48px;display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;margin-top:50px}
.km-dark h2{font-size:2.4rem;font-weight:800;margin-bottom:14px;color:#fff}
.km-dark h2 span{color:#FFA41B}
.km-dark p{color:#CFC8B8;font-size:1.02rem;margin-bottom:24px}
.km-dark-photo{position:relative;max-width:300px;width:100%;justify-self:center;aspect-ratio:4/5}
.km-dark-photo .frame{position:absolute;inset:0;background:#FFA41B;border-radius:32px;transform:rotate(-4deg)}
.km-dark-photo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 15%;border-radius:28px}
.km-social{display:flex;gap:12px;justify-content:center;margin:44px 0 0;flex-wrap:wrap}
.km-social a{width:52px;height:52px;border-radius:50%;background:#1C1812;color:#fff;display:grid;place-items:center;font-size:1.1rem;transition:.25s}
.km-social a:hover{background:#FFA41B;color:#1C1812}
.km-counter{max-width:520px;margin:30px auto 0;background:#fff;border-radius:28px;padding:22px;text-align:center;box-shadow:0 12px 32px rgba(28,24,18,.08)}
@media (max-width:860px){
  .km-hero,.km-dark{grid-template-columns:1fr;text-align:center}
  .km-hero h1{font-size:2.5rem}
  .km-btns{justify-content:center}
  .km-sub{margin-left:auto;margin-right:auto}
  .km-dark{padding:36px 26px}
  .km-dark h2{font-size:2rem}
}
"""

HOME_SCRIPT = """<script>
(function(){
  var DICT = __DICT__;
  var root = document.querySelector('.km-home');
  function setLang(l){
    var d = DICT[l]; if (!d || !root) return;
    root.setAttribute('dir', l === 'ar' ? 'rtl' : 'ltr');
    root.querySelectorAll('[data-i18n]').forEach(function(el){
      var k = el.getAttribute('data-i18n'); if (d[k] !== undefined) el.textContent = d[k];
    });
    root.querySelectorAll('.km-lang button').forEach(function(b){ b.classList.toggle('on', b.dataset.lang === l); });
  }
  root.querySelectorAll('.km-lang button').forEach(function(b){
    b.addEventListener('click', function(){ setLang(b.dataset.lang); });
  });
  setLang('fr');
})();
</script>"""


def build_home():
    import base64
    import json
    photo = "data:image/jpeg;base64," + base64.b64encode(
        open(build.PHOTO, "rb").read()).decode()
    t = HOME_T["fr"]
    dict_js = json.dumps(HOME_T, ensure_ascii=False)
    script = HOME_SCRIPT.replace("__DICT__", dict_js)
    return f"""<style>{HOME_CSS}</style>
<div class="km-home">
  <div class="km-lang">
    <button data-lang="fr" class="on">FR</button>
    <button data-lang="ar">عربي</button>
    <button data-lang="en">EN</button>
  </div>

  <section class="km-wrap km-hero">
    <div>
      <span class="km-badge" data-i18n="badge">{t['badge']}</span>
      <h1><span data-i18n="welcome">{t['welcome']}</span> <span class="km-hl">Karou Mosaab</span></h1>
      <p class="km-sub" data-i18n="sub">{t['sub']}</p>
      <div class="km-btns">
        <a class="km-btn km-btn-amber" href="/mes-travaux/" data-i18n="btn1">{t['btn1']}</a>
        <a class="km-btn km-btn-dark" href="/contact/" data-i18n="btn2">{t['btn2']}</a>
      </div>
    </div>
    <div class="km-photo">
      <div class="blob"></div>
      <img src="{photo}" alt="Karou Mosaab">
    </div>
  </section>

  <div class="km-marquee"><div class="km-track"><span data-i18n="marquee">{t['marquee']}</span><span data-i18n="marquee">{t['marquee']}</span></div></div>

  <section class="km-wrap">
    <div class="km-cards">
      <div class="km-card"><div class="km-ico"><i class="fa-solid fa-bullhorn">&#xf0a1;</i></div><h3 data-i18n="c1t">{t['c1t']}</h3><p data-i18n="c1d">{t['c1d']}</p></div>
      <div class="km-card"><div class="km-ico"><i class="fa-solid fa-code">&#xf121;</i></div><h3 data-i18n="c2t">{t['c2t']}</h3><p data-i18n="c2d">{t['c2d']}</p></div>
      <div class="km-card"><div class="km-ico"><i class="fa-solid fa-gears">&#xf085;</i></div><h3 data-i18n="c3t">{t['c3t']}</h3><p data-i18n="c3d">{t['c3d']}</p></div>
    </div>

    <div class="km-dark">
      <div>
        <h2 data-i18n="dt">{t['dt']}</h2>
        <p data-i18n="dp">{t['dp']}</p>
        <a class="km-btn km-btn-amber" href="/a-propos-de-moi/" data-i18n="dbtn">{t['dbtn']}</a>
      </div>
      <div class="km-dark-photo"><div class="frame"></div><img src="{photo}" alt="Karou Mosaab"></div>
    </div>

    <div class="km-social">
      <a href="{build.INSTAGRAM}" target="_blank" rel="noopener" title="Instagram"><i class="fa-brands fa-instagram">&#xf16d;</i></a>
      <a href="{build.FACEBOOK}" target="_blank" rel="noopener" title="Facebook"><i class="fa-brands fa-facebook-f">&#xf39e;</i></a>
      <a href="{build.LINKEDIN}" target="_blank" rel="noopener" title="LinkedIn"><i class="fa-brands fa-linkedin-in">&#xf0e1;</i></a>
      <a href="{build.YOUTUBE}" target="_blank" rel="noopener" title="YouTube"><i class="fa-brands fa-youtube">&#xf167;</i></a>
    </div>

    <div class="km-counter">
      <p data-i18n="counter" style="margin-bottom:10px">{t['counter']}</p>
      {build.COUNTER}
    </div>
  </section>
</div>
{script}
"""


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
    with open(os.path.join(HERE, "pages", "accueil.html"), "w", encoding="utf-8") as f:
        f.write(build_home())
    for src, fname in PAGE_FILE.items():
        if src == "index.html":
            continue
        body = build.BODY[src]
        body = jimdo_links(body)
        body = build.fix_icons(body)
        with open(os.path.join(HERE, "pages", fname), "w", encoding="utf-8") as f:
            f.write(body + "\n" + PAGE_SCRIPT + "\n")
    print("OK : style.css, template.html, pages/*.html")


if __name__ == "__main__":
    main()
