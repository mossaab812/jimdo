#!/usr/bin/env python3
"""Génère les fichiers Jimdo à partir de site/multipage/build.py :
  - style.css         : CSS du Custom Template (scopé sous #container + corrections + style de l'accueil)
  - template.html     : structure (onglet HTML du Custom Template)
  - pages/accueil.html: page d'accueil complète (sans <style> : le CSS vient de style.css)
  - pages/*.html      : contenu des autres rubriques
Usage : python3 make_template.py
"""
import base64
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "multipage"))
import build  # noqa: E402

JIMDO_URL = {
    "index.html": "/",
    "about.html": "/a-propos-de-moi/",
    "works.html": "/mes-travaux/",
    "skills.html": "/mes-competences/",
    "contact.html": "/contact/",
}
PAGE_FILE = {
    "about.html": "a-propos-de-moi.html",
    "works.html": "mes-travaux.html",
    "skills.html": "mes-competences.html",
    "contact.html": "contact.html",
}

GOLD = "#C9A45C"
BLACK = "#0E0D0B"

# ---------- Style de la page d'accueil (dans style.css, pas dans l'embed) ----------
HOME_CSS = """
/* ===== Accueil : style premium noir & or ===== */
.km-home{background:#0E0D0B;color:#F3EDE2;font-family:'Plus Jakarta Sans','Cairo',system-ui,sans-serif;line-height:1.7;width:100vw;position:relative;left:50%;margin-left:-50vw;padding:0 0 70px;overflow:hidden;text-align:center}
.km-home *{box-sizing:border-box}
.km-home a{color:inherit;text-decoration:none}
.km-home p{margin:0}
.km-inner{max-width:1100px;margin:0 auto;padding:0 6%}
.km-lang{display:flex;justify-content:flex-end;gap:8px;padding-top:26px}
.km-lang button{background:transparent;border:1px solid rgba(201,164,92,.4);color:#C9A45C;padding:6px 12px;cursor:pointer;font-size:.72rem;letter-spacing:1.5px;font-weight:600;font-family:inherit}
.km-lang button.on,.km-lang button:hover{background:#C9A45C;color:#0E0D0B}
.km-hero{padding:34px 0 0}
.km-kicker{font-size:.76rem;letter-spacing:4px;text-transform:uppercase;color:#C9A45C;margin-bottom:22px}
.km-title{font-family:'Playfair Display',Georgia,serif;font-size:3.5rem;font-weight:400;line-height:1.12;color:#F3EDE2;margin:0}
.km-name{font-family:'Playfair Display',Georgia,serif;font-style:italic;font-size:2rem;color:#C9A45C;margin:8px 0 30px}
.km-orbit{position:relative;width:min(380px,88vw);height:min(380px,88vw);margin:0 auto 34px}
.km-ring{position:absolute;inset:58px;border-radius:50%;border:1px solid #C9A45C;padding:8px;background:#0E0D0B;overflow:hidden}
.km-ring img{display:block!important;width:100%!important;height:100%!important;border-radius:50%;object-fit:cover;object-position:center 15%;max-width:none!important}
.km-o{position:absolute;width:52px;height:52px;border-radius:50%;background:#0E0D0B;border:1px solid #C9A45C;color:#C9A45C;display:grid;place-items:center;font-size:1.05rem;transition:background .3s,color .3s}
.km-o:hover{background:#C9A45C;color:#0E0D0B}
.km-o-top{top:0;left:50%;transform:translateX(-50%)}
.km-o-right{right:0;top:50%;transform:translateY(-50%)}
.km-o-bottom{bottom:0;left:50%;transform:translateX(-50%)}
.km-o-left{left:0;top:50%;transform:translateY(-50%)}
.km-sub{max-width:640px;margin:0 auto 34px;color:#A39B8B;font-size:1.04rem}
.km-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.km-btn{display:inline-block;padding:14px 34px;font-weight:600;letter-spacing:.6px;font-size:.9rem;border:1px solid #C9A45C;transition:background .3s,color .3s}
.km-btn-gold{background:#C9A45C;color:#0E0D0B}
.km-btn-gold:hover{background:#E4C98A;border-color:#E4C98A}
.km-btn-line{color:#C9A45C}
.km-btn-line:hover{background:#C9A45C;color:#0E0D0B}
.km-marquee{margin:70px 0 0;border-top:1px solid rgba(201,164,92,.3);border-bottom:1px solid rgba(201,164,92,.3);overflow:hidden;white-space:nowrap;padding:16px 0}
.km-track{display:inline-block;animation:km-scroll 32s linear infinite}
.km-track span{font-family:'Playfair Display',Georgia,serif;font-size:1.25rem;font-style:italic;color:#C9A45C;padding-right:20px}
@keyframes km-scroll{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.km-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:22px;padding:64px 0 0}
.km-card{background:#171512;border:1px solid rgba(201,164,92,.22);padding:36px 28px;transition:border-color .3s,transform .3s;text-align:center}
.km-card:hover{border-color:#C9A45C;transform:translateY(-4px)}
.km-ico{color:#C9A45C;font-size:1.4rem;margin-bottom:20px}
.km-card h3{font-family:'Playfair Display',Georgia,serif;font-size:1.35rem;font-weight:500;margin-bottom:10px;color:#F3EDE2}
.km-card p{color:#A39B8B;font-size:.97rem}
.km-about{max-width:760px;margin:70px auto 0;padding:52px 40px;border:1px solid rgba(201,164,92,.3);background:#171512}
.km-about h2{font-family:'Playfair Display',Georgia,serif;font-size:2.3rem;font-weight:400;margin-bottom:18px;color:#F3EDE2}
.km-about h2 em{color:#C9A45C;font-style:italic}
.km-about p{color:#A39B8B;line-height:1.9;margin-bottom:30px}
.km-counter{max-width:460px;margin:56px auto 0;border:1px solid rgba(201,164,92,.3);padding:24px;text-align:center}
.km-counter p{color:#C9A45C;letter-spacing:2.5px;text-transform:uppercase;font-size:.74rem;margin-bottom:12px}
.km-home[dir=rtl] .km-title,.km-home[dir=rtl] .km-name,.km-home[dir=rtl] .km-card h3,.km-home[dir=rtl] .km-about h2,.km-home[dir=rtl] .km-track span{font-family:'Cairo',Georgia,serif;font-style:normal}
.km-home[dir=rtl] .km-kicker{letter-spacing:0}
@media (max-width:760px){
  .km-title{font-size:2.4rem}
  .km-name{font-size:1.6rem}
  .km-about{padding:36px 22px}
  .km-about h2{font-size:1.9rem}
}
"""

HOME_T = {
    "fr": {"welcome": "Bienvenue sur mon portfolio", "badge": "Master 2 Marketing Digital · EHEC",
           "sub": "Étudiant en Master 2 Marketing Digital, je combine stratégie marketing, développement web, automatisation et photographie automobile.",
           "btn1": "Voir mes travaux", "btn2": "Me contacter",
           "marquee": "Marketing digital ✦ Développement web ✦ Automatisation ✦ Photographie automobile ✦ ",
           "c1t": "Marketing digital", "c1d": "Stratégie de contenu et présence en ligne.",
           "c2t": "Développement web", "c2d": "Sites simples, rapides et adaptés au mobile.",
           "c3t": "Automatisation", "c3d": "Automatiser les tâches répétitives pour gagner du temps.",
           "dt": "Qui est <em>Karou</em> ?",
           "dp": "Étudiant à l'EHEC, membre du département RH & Communication de HUC Alumni (Company Discovery). Passionné par le web, les réseaux sociaux et la photographie automobile.",
           "dbtn": "En savoir plus", "counter": "Compteur de visiteurs"},
    "ar": {"welcome": "مرحباً بكم في البورتفوليو تاعي", "badge": "ماستر 2 تسويق رقمي · EHEC",
           "sub": "طالب ماستر 2 تسويق رقمي، أجمع بين الاستراتيجية التسويقية وتطوير الويب والأتمتة وتصوير السيارات.",
           "btn1": "شوف أعمالي", "btn2": "اتصل بي",
           "marquee": "التسويق الرقمي ✦ تطوير الويب ✦ الأتمتة ✦ تصوير السيارات ✦ ",
           "c1t": "التسويق الرقمي", "c1d": "استراتيجية المحتوى وحضور قوي على الإنترنت.",
           "c2t": "تطوير الويب", "c2d": "مواقع بسيطة وسريعة ومتجاوبة مع الهاتف.",
           "c3t": "الأتمتة", "c3d": "أتمتة المهام المتكررة باش توفر الوقت.",
           "dt": "من هو <em>كارو</em>؟",
           "dp": "طالب في EHEC، عضو قسم الموارد البشرية والاتصال في نادي HUC Alumni (Company Discovery). شغوف بالويب ومواقع التواصل وتصوير السيارات.",
           "dbtn": "تعرف عليا أكثر", "counter": "عداد الزوار"},
    "en": {"welcome": "Welcome to my portfolio", "badge": "Master 2 Digital Marketing · EHEC",
           "sub": "Master 2 Digital Marketing student, I combine marketing strategy, web development, automation and car photography.",
           "btn1": "See my work", "btn2": "Contact me",
           "marquee": "Digital marketing ✦ Web development ✦ Automation ✦ Car photography ✦ ",
           "c1t": "Digital marketing", "c1d": "Content strategy and online presence.",
           "c2t": "Web development", "c2d": "Simple, fast, mobile-friendly websites.",
           "c3t": "Automation", "c3d": "Automating repetitive tasks to save time.",
           "dt": "Who is <em>Karou</em>?",
           "dp": "EHEC student, member of the HR & Communication department at HUC Alumni (Company Discovery). Passionate about web, social media and car photography.",
           "dbtn": "Learn more", "counter": "Visitor counter"},
}

HOME_SCRIPT = """<script>
(function(){
  var DICT = __DICT__;
  var root = document.querySelector('.km-home');
  if (!root) return;
  function setLang(l){
    var d = DICT[l]; if (!d) return;
    root.setAttribute('dir', l === 'ar' ? 'rtl' : 'ltr');
    root.querySelectorAll('[data-i18n]').forEach(function(el){
      var k = el.getAttribute('data-i18n'); if (d[k] !== undefined) el.innerHTML = d[k];
    });
    root.querySelectorAll('.km-lang button').forEach(function(b){ b.classList.toggle('on', b.dataset.lang === l); });
  }
  root.querySelectorAll('.km-lang button').forEach(function(b){
    b.addEventListener('click', function(){ setLang(b.dataset.lang); });
  });
})();
</script>"""


def build_home():
    photo = "data:image/jpeg;base64," + base64.b64encode(open(build.PHOTO, "rb").read()).decode()
    t = HOME_T["fr"]
    script = HOME_SCRIPT.replace("__DICT__", json.dumps(HOME_T, ensure_ascii=False))
    return f"""<div class="km-home">
  <div class="km-inner">
    <div class="km-lang">
      <button data-lang="fr" class="on">FR</button>
      <button data-lang="ar">عربي</button>
      <button data-lang="en">EN</button>
    </div>

    <section class="km-hero">
      <p class="km-kicker" data-i18n="badge">{t['badge']}</p>
      <h1 class="km-title" data-i18n="welcome">{t['welcome']}</h1>
      <p class="km-name">Karou Mosaab</p>

      <div class="km-orbit">
        <div class="km-ring"><img src="{photo}" alt="Karou Mosaab"></div>
        <a class="km-o km-o-top" href="{build.INSTAGRAM}" target="_blank" rel="noopener" title="Instagram"><i class="fa-brands fa-instagram">&#xf16d;</i></a>
        <a class="km-o km-o-right" href="{build.FACEBOOK}" target="_blank" rel="noopener" title="Facebook"><i class="fa-brands fa-facebook-f">&#xf39e;</i></a>
        <a class="km-o km-o-bottom" href="{build.LINKEDIN}" target="_blank" rel="noopener" title="LinkedIn"><i class="fa-brands fa-linkedin-in">&#xf0e1;</i></a>
        <a class="km-o km-o-left" href="{build.YOUTUBE}" target="_blank" rel="noopener" title="YouTube"><i class="fa-brands fa-youtube">&#xf167;</i></a>
      </div>

      <p class="km-sub" data-i18n="sub">{t['sub']}</p>
      <div class="km-btns">
        <a class="km-btn km-btn-gold" href="/mes-travaux/" data-i18n="btn1">{t['btn1']}</a>
        <a class="km-btn km-btn-line" href="/contact/" data-i18n="btn2">{t['btn2']}</a>
      </div>
    </section>

    <div class="km-marquee"><div class="km-track"><span data-i18n="marquee">{t['marquee']}</span><span data-i18n="marquee">{t['marquee']}</span></div></div>

    <div class="km-cards">
      <div class="km-card"><div class="km-ico"><i class="fa-solid fa-bullhorn">&#xf0a1;</i></div><h3 data-i18n="c1t">{t['c1t']}</h3><p data-i18n="c1d">{t['c1d']}</p></div>
      <div class="km-card"><div class="km-ico"><i class="fa-solid fa-code">&#xf121;</i></div><h3 data-i18n="c2t">{t['c2t']}</h3><p data-i18n="c2d">{t['c2d']}</p></div>
      <div class="km-card"><div class="km-ico"><i class="fa-solid fa-gears">&#xf085;</i></div><h3 data-i18n="c3t">{t['c3t']}</h3><p data-i18n="c3d">{t['c3d']}</p></div>
    </div>

    <div class="km-about">
      <h2 data-i18n="dt">{t['dt']}</h2>
      <p data-i18n="dp">{t['dp']}</p>
      <a class="km-btn km-btn-gold" href="/a-propos-de-moi/" data-i18n="dbtn">{t['dbtn']}</a>
    </div>

    <div class="km-counter">
      <p data-i18n="counter">{t['counter']}</p>
      {build.COUNTER}
    </div>
  </div>
</div>
{script}
"""


# ---------- CSS scopé sous #container ----------
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
#container .logo-dot{background:#C9A45C!important;color:#0E0D0B!important}
#navigation{max-width:1160px;margin:18px auto 0;padding:0 5%;text-align:center}
#navigation ul{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;list-style:none;padding:0;margin:0}
#navigation li{list-style:none;margin:0;padding:0}
#navigation a{display:inline-block;padding:9px 16px;border-radius:999px;background:#fff;box-shadow:0 8px 20px rgba(28,24,18,.08);font-weight:700;font-size:.92rem;color:#1C1812;transition:background .25s}
#navigation a:hover,#navigation a.current,#navigation a.active,#navigation li.current a,#navigation li.active a{background:#C9A45C}
#content{max-width:1160px;margin:0 auto}
.reveal{opacity:1!important;transform:none!important;transition:none!important}
#footer{text-align:center;color:#6E6759;padding:30px 5% 30px;font-size:.9rem;margin-top:50px}
#footer .social{margin-top:16px}
#footer .social a{font-size:1.05rem;width:46px;height:46px}
#footer .gutter{padding-bottom:14px}
"""


def build_css():
    head = (
        "@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,500;1,400&display=swap');\n"
        "@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');\n"
    )
    return head + scope_css(build.CSS) + OVERRIDES + HOME_CSS


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
    with open(os.path.join(HERE, "style.css"), "w", encoding="utf-8") as f:
        f.write(build_css())

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

    os.makedirs(os.path.join(HERE, "pages"), exist_ok=True)
    with open(os.path.join(HERE, "pages", "accueil.html"), "w", encoding="utf-8") as f:
        f.write(build_home())
    for src, fname in PAGE_FILE.items():
        body = build.fix_icons(jimdo_links(build.BODY[src]))
        with open(os.path.join(HERE, "pages", fname), "w", encoding="utf-8") as f:
            f.write(body + "\n" + PAGE_SCRIPT + "\n")
    print("OK : style.css, template.html, pages/*.html")


if __name__ == "__main__":
    main()
