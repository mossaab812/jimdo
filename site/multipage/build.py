#!/usr/bin/env python3
"""Génère 5 pages HTML autonomes (une par rubrique Jimdo) au style « cream / noir / ambre ».
Chaque fichier contient son CSS et son JS : il suffit de coller le fichier complet
dans un élément « Code / HTML (Embed code) » de la page Jimdo correspondante.
Usage : python3 build.py
"""
import base64
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
EMAIL = "mossaabmanant19@gmail.com"
PHOTO = os.path.join(HERE, "..", "assets", "karou.jpg")
PHOTO_SRC = "data:image/jpeg;base64," + base64.b64encode(open(PHOTO, "rb").read()).decode()
INSTAGRAM = "https://www.instagram.com/mk.venatus/"
FACEBOOK = "https://www.facebook.com/share/18R3j19EPu/"
LINKEDIN = "https://www.linkedin.com/in/mosaab~karou"
YOUTUBE = "https://youtube.com/@kazunari812"
CV_URL = "REMPLACER_PAR_URL_MON_CV"
COUNTER = (
    '<div id="sfch4e1us4hpqpj9ym3sb2j3uf7bn8p5e3w"></div>\n'
    '<script type="text/javascript" src="https://counter6.optistats.ovh/private/counter.js?c=h4e1us4hpqpj9ym3sb2j3uf7bn8p5e3w&amp;down=async" async></script>\n'
    '<noscript><a href="https://www.compteurdevisite.com" title="compteur internet"><img src="https://counter6.optistats.ovh/private/compteurdevisite.php?c=h4e1us4hpqpj9ym3sb2j3uf7bn8p5e3w" border="0" title="compteur internet" alt="compteur internet"></a></noscript>'
)

# ---------------- Traductions (FR par défaut, AR, EN) ----------------
T = {
    "fr": {
        "badge": "Master 2 Marketing Digital · EHEC",
        "hero_a": "Je suis", "hero_b": "Karou Mosaab",
        "hero_role": "Étudiant en Master 2 Marketing Digital, passionné par le web et l'automatisation.",
        "hero_sub": "Je combine stratégie marketing, développement web, automatisation et photographie automobile.",
        "quote": "Marketing, web et contenu avec une vision créative et précise.",
        "btn_work": "Voir mes travaux", "btn_contact": "Me contacter",
        "ft1": "Marketing", "ft2": "Web", "ft3": "Automatisation", "ft4": "Photo auto",
        "marquee": "Marketing digital ✦ Développement web ✦ Automatisation ✦ Photo automobile ✦ Smartphones ✦ ",
        "svc_eyebrow": "Mes services", "svc_a": "Comment je donne", "svc_b": "vie aux idées", "btn_all": "Tous les services",
        "s1_t": "Marketing digital", "s1_d": "Stratégie de contenu, réseaux sociaux et analyse de la présence en ligne.",
        "s1_tag1": "Stratégie de contenu", "s1_tag2": "Réseaux sociaux", "s1_tag3": "Analyse",
        "s2_t": "Développement web", "s2_d": "Création de pages web rapides et adaptées au mobile avec HTML, CSS et JavaScript.",
        "s2_tag1": "HTML / CSS", "s2_tag2": "JavaScript", "s2_tag3": "Responsive",
        "s3_t": "Automatisation", "s3_d": "Automatiser les tâches répétitives pour gagner du temps et réduire les erreurs.",
        "s3_tag1": "Workflows", "s3_tag2": "Tâches répétitives", "s3_tag3": "Scripts",
        "s4_t": "Photographie automobile", "s4_d": "Prise de vue créative et retouche de véhicules, publiées sur Instagram.",
        "s4_tag1": "Prise de vue", "s4_tag2": "Retouche", "s4_tag3": "Instagram",
        "s5_t": "Maintenance smartphones", "s5_d": "Initiation au diagnostic et à la réparation des smartphones.",
        "s5_tag1": "Diagnostic", "s5_tag2": "Initiation", "s5_tag3": "Entretien",
        "about_eyebrow": "À propos", "about_a": "Qui est", "about_b": "Karou ?",
        "about_p1": "Étudiant en Master 2 Marketing Digital à l'EHEC, je m'intéresse à la façon dont la technologie et la stratégie se rencontrent pour créer de la valeur.",
        "about_p2": "Je pratique le développement web, l'automatisation et la photographie automobile, et je reste ouvert à de nouveaux apprentissages.",
        "exp_t": "Vie associative", "exp_d": "HUC Alumni : membre du département RH & Communication (Company Discovery).",
        "btn_cv": "Mon CV", "cv_note": "Le CV est protégé par mot de passe.",
        "works_a": "Mes", "works_b": "travaux",
        "works_sub": "Quelques réalisations et domaines dans lesquels je travaille.",
        "w1_t": "Photographie automobile", "w1_d": "Prises de vue et retouche de véhicules, publiées sur Instagram.",
        "w2_t": "Sites web", "w2_d": "Pages web simples, rapides et adaptées au mobile.",
        "w3_t": "Automatisation", "w3_d": "Scripts et workflows qui simplifient les tâches répétitives.",
        "btn_insta": "Voir la galerie sur Instagram",
        "skills_a": "Mes", "skills_b": "compétences",
        "skills_sub": "Les services et compétences que je développe, cliquez sur une ligne pour voir le détail.",
        "contact_a": "Parlons", "contact_b": "ensemble",
        "contact_sub": "Une collaboration, une question ? Écrivez-moi.",
        "f_name": "Votre nom", "f_email": "Votre e-mail", "f_msg": "Votre message", "f_send": "Envoyer",
        "cta_t": "Un projet ou une question ?",
        "counter_label": "Compteur de visiteurs",
        "footer": "© 2026 Karou Mosaab · Tous droits réservés",
    },
    "ar": {
        "badge": "ماستر 2 تسويق رقمي · EHEC",
        "hero_a": "أنا", "hero_b": "كارو مصعب",
        "hero_role": "طالب ماستر 2 تسويق رقمي، شغوف بالويب والأتمتة.",
        "hero_sub": "أجمع بين الاستراتيجية التسويقية وتطوير الويب والأتمتة وتصوير السيارات.",
        "quote": "تسويق وويب ومحتوى برؤية إبداعية ودقيقة.",
        "btn_work": "شوف أعمالي", "btn_contact": "اتصل بي",
        "ft1": "تسويق", "ft2": "ويب", "ft3": "أتمتة", "ft4": "تصوير",
        "marquee": "التسويق الرقمي ✦ تطوير الويب ✦ الأتمتة ✦ تصوير السيارات ✦ الهواتف ✦ ",
        "svc_eyebrow": "خدماتي", "svc_a": "كيفاش نحول", "svc_b": "الأفكار لواقع", "btn_all": "كل الخدمات",
        "s1_t": "التسويق الرقمي", "s1_d": "استراتيجية المحتوى، شبكات التواصل، وتحليل الحضور على الإنترنت.",
        "s1_tag1": "استراتيجية المحتوى", "s1_tag2": "شبكات التواصل", "s1_tag3": "التحليل",
        "s2_t": "تطوير الويب", "s2_d": "إنشاء صفحات ويب سريعة ومتجاوبة مع الهاتف بـ HTML وCSS وJavaScript.",
        "s2_tag1": "HTML / CSS", "s2_tag2": "JavaScript", "s2_tag3": "متجاوب",
        "s3_t": "الأتمتة", "s3_d": "أتمتة المهام المتكررة باش توفر الوقت وتقلل الأخطاء.",
        "s3_tag1": "Workflows", "s3_tag2": "مهام متكررة", "s3_tag3": "سكريبتات",
        "s4_t": "تصوير السيارات", "s4_d": "تصوير إبداعي وتحرير صور السيارات المنشورة على إنستغرام.",
        "s4_tag1": "تصوير", "s4_tag2": "تحرير", "s4_tag3": "إنستغرام",
        "s5_t": "صيانة الهواتف", "s5_d": "مبادئ أولية في تشخيص وإصلاح الهواتف الذكية.",
        "s5_tag1": "تشخيص", "s5_tag2": "مبادئ أولية", "s5_tag3": "صيانة",
        "about_eyebrow": "عني", "about_a": "من هو", "about_b": "كارو؟",
        "about_p1": "طالب ماستر 2 تسويق رقمي في EHEC، مهتم بكيفاش التكنولوجيا والاستراتيجية تتلاقاو باش يخلقو قيمة.",
        "about_p2": "نمارس تطوير الويب والأتمتة وتصوير السيارات، ونبقى مفتوحين لتعلم جديد.",
        "exp_t": "النشاط الجمعوي", "exp_d": "نادي HUC Alumni: عضو قسم الموارد البشرية والاتصال (Company Discovery).",
        "btn_cv": "سيرتي الذاتية", "cv_note": "السيرة الذاتية محمية بكلمة مرور.",
        "works_a": "أهم", "works_b": "أعمالي",
        "works_sub": "بعض الإنجازات ومجالات العمل اللي نخدم فيها.",
        "w1_t": "تصوير السيارات", "w1_d": "تصوير وتحرير صور السيارات المنشورة على إنستغرام.",
        "w2_t": "مواقع الويب", "w2_d": "صفحات ويب بسيطة وسريعة ومتجاوبة مع الهاتف.",
        "w3_t": "الأتمتة", "w3_d": "سكريبتات وworkflows تبسط المهام المتكررة.",
        "btn_insta": "شوف المعرض على إنستغرام",
        "skills_a": "مهاراتي", "skills_b": "وخدماتي",
        "skills_sub": "الخدمات والمهارات اللي نطورها، كليك على أي سطر باش تشوف التفاصيل.",
        "contact_a": "خلينا", "contact_b": "نتكلمو",
        "contact_sub": "تعاون ولا سؤال؟ كتبلي.",
        "f_name": "الاسم", "f_email": "الإيميل", "f_msg": "الرسالة", "f_send": "إرسال",
        "cta_t": "مشروع ولا سؤال؟",
        "counter_label": "عداد الزوار",
        "footer": "© 2026 كارو مصعب · جميع الحقوق محفوظة",
    },
    "en": {
        "badge": "Master 2 Digital Marketing · EHEC",
        "hero_a": "I'm", "hero_b": "Karou Mosaab",
        "hero_role": "Master 2 Digital Marketing student, passionate about web and automation.",
        "hero_sub": "I combine marketing strategy, web development, automation and automotive photography.",
        "quote": "Marketing, web and content with a creative, precise vision.",
        "btn_work": "See my work", "btn_contact": "Contact me",
        "ft1": "Marketing", "ft2": "Web", "ft3": "Automation", "ft4": "Car photo",
        "marquee": "Digital marketing ✦ Web development ✦ Automation ✦ Car photography ✦ Smartphones ✦ ",
        "svc_eyebrow": "My services", "svc_a": "How I bring", "svc_b": "ideas to life", "btn_all": "View all services",
        "s1_t": "Digital marketing", "s1_d": "Content strategy, social networks and online presence analysis.",
        "s1_tag1": "Content strategy", "s1_tag2": "Social networks", "s1_tag3": "Analysis",
        "s2_t": "Web development", "s2_d": "Fast, mobile-friendly web pages built with HTML, CSS and JavaScript.",
        "s2_tag1": "HTML / CSS", "s2_tag2": "JavaScript", "s2_tag3": "Responsive",
        "s3_t": "Automation", "s3_d": "Automating repetitive tasks to save time and reduce errors.",
        "s3_tag1": "Workflows", "s3_tag2": "Repetitive tasks", "s3_tag3": "Scripts",
        "s4_t": "Automotive photography", "s4_d": "Creative shooting and editing of cars, published on Instagram.",
        "s4_tag1": "Shooting", "s4_tag2": "Editing", "s4_tag3": "Instagram",
        "s5_t": "Smartphone repair", "s5_d": "Beginner-level diagnosis and repair of smartphones.",
        "s5_tag1": "Diagnosis", "s5_tag2": "Beginner level", "s5_tag3": "Maintenance",
        "about_eyebrow": "About me", "about_a": "Who is", "about_b": "Karou?",
        "about_p1": "Master 2 Digital Marketing student at EHEC, interested in where technology and strategy meet to create value.",
        "about_p2": "I practise web development, automation and car photography, and I am always eager to learn.",
        "exp_t": "Student life", "exp_d": "HUC Alumni: member of the HR & Communication department (Company Discovery).",
        "btn_cv": "Download CV", "cv_note": "The CV is password protected.",
        "works_a": "My", "works_b": "work",
        "works_sub": "Some achievements and areas I work in.",
        "w1_t": "Automotive photography", "w1_d": "Car shoots and editing, published on Instagram.",
        "w2_t": "Websites", "w2_d": "Simple, fast, mobile-friendly web pages.",
        "w3_t": "Automation", "w3_d": "Scripts and workflows that simplify repetitive tasks.",
        "btn_insta": "View the gallery on Instagram",
        "skills_a": "My", "skills_b": "skills",
        "skills_sub": "Services and skills I am developing. Click a row to see the details.",
        "contact_a": "Let's", "contact_b": "talk",
        "contact_sub": "A collaboration or a question? Write to me.",
        "f_name": "Your name", "f_email": "Your e-mail", "f_msg": "Your message", "f_send": "Send",
        "cta_t": "A project or a question?",
        "counter_label": "Visitor counter",
        "footer": "© 2026 Karou Mosaab · All rights reserved",
    },
}

PAGES = [
    ("index.html", "Accueil"),
    ("about.html", "A propos de moi"),
    ("works.html", "Mes travaux"),
    ("skills.html", "Mes compétences"),
    ("contact.html", "Contact"),
]

CSS = """
:root{
  --cream:#F5F2EA;--cream-2:#EFEBE0;--card:#FFFFFF;
  --dark:#1C1812;--dark-2:#2A241B;--amber:#FFA41B;--amber-2:#F7B23B;
  --ink:#1C1812;--muted:#6E6759;--line:#E4DDCC;
  --shadow:0 12px 32px rgba(28,24,18,.08);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Plus Jakarta Sans','Poppins','Cairo',system-ui,sans-serif;background:var(--cream);color:var(--ink);line-height:1.6;overflow-x:hidden}
[dir=rtl] body{font-family:'Cairo','Plus Jakarta Sans',system-ui,sans-serif}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}
button{font-family:inherit}
.wrap{max-width:1160px;margin:auto;padding:0 5%}
section{padding:90px 0;position:relative}
.hl{color:var(--amber)}
.eyebrow{display:inline-flex;align-items:center;gap:10px;font-size:.92rem;font-weight:600;color:var(--muted);margin-bottom:14px}
.eyebrow::before{content:"";width:22px;height:12px;border-radius:12px;background:linear-gradient(90deg,var(--dark) 50%,var(--amber) 50%)}
h1{font-size:4.1rem;line-height:1.05;font-weight:800;letter-spacing:-1px;margin-bottom:18px}
h2{font-size:3rem;line-height:1.1;font-weight:800;letter-spacing:-.8px;margin-bottom:18px}
h3{font-size:1.35rem;font-weight:700;line-height:1.25}
p{color:var(--muted);margin-bottom:14px}

/* ---------- Navigation : pilule sombre ---------- */
.topbar{position:sticky;top:14px;z-index:100;padding:0 5%}
.navbar{max-width:1100px;margin:auto;background:var(--dark);border-radius:999px;padding:9px 12px 9px 10px;display:flex;align-items:center;justify-content:space-between;gap:14px;box-shadow:0 14px 34px rgba(28,24,18,.25);position:relative}
.logo{display:flex;align-items:center;gap:10px;color:#fff;font-weight:800;font-size:1.05rem;padding-left:4px}
.logo-dot{width:36px;height:36px;border-radius:50%;background:var(--amber);display:grid;place-items:center;color:var(--dark);font-weight:800}
.menu{display:flex;gap:4px;list-style:none;flex-wrap:wrap}
.menu a{display:block;padding:8px 13px;border-radius:999px;font-size:.88rem;color:#CFC8B8;font-weight:500;transition:.25s}
.menu a:hover{color:#fff}
.menu a.on{color:var(--amber);font-weight:700}
.navright{display:flex;align-items:center;gap:8px}
.lang{display:flex;gap:4px;background:var(--dark-2);border-radius:999px;padding:4px}
.lang button{background:transparent;border:0;color:#CFC8B8;padding:6px 10px;border-radius:999px;cursor:pointer;font-size:.8rem;font-weight:700;transition:.2s}
.lang button.on{background:var(--amber);color:var(--dark)}
.cta-nav{background:#fff;color:var(--dark);padding:9px 16px;border-radius:999px;font-weight:700;font-size:.85rem;white-space:nowrap}
.burger{display:none;background:var(--dark-2);border:0;color:#fff;border-radius:999px;width:40px;height:40px;cursor:pointer}

/* ---------- Badges, boutons, puces ---------- */
.badge{display:inline-flex;align-items:center;gap:10px;background:#fff;box-shadow:var(--shadow);padding:7px 16px 7px 8px;border-radius:999px;font-size:.88rem;font-weight:600;margin-bottom:24px;animation:float 4s ease-in-out infinite}
.badge i{width:26px;height:26px;border-radius:50%;background:var(--dark);color:var(--amber);display:grid;place-items:center;font-size:.7rem}
.btns{display:flex;gap:12px;flex-wrap:wrap;margin-top:8px}
.btn{display:inline-flex;align-items:center;gap:10px;padding:10px 10px 10px 26px;border-radius:999px;font-weight:700;font-size:1rem;border:0;cursor:pointer;transition:transform .25s,box-shadow .25s;white-space:nowrap}
.btn .arr{width:34px;height:34px;border-radius:50%;display:grid;place-items:center;font-size:.85rem}
.btn-amber{background:var(--amber);color:var(--dark);box-shadow:0 10px 24px rgba(255,164,27,.35)}
.btn-amber .arr{background:var(--dark);color:var(--amber)}
.btn-dark{background:var(--dark);color:#fff;box-shadow:0 10px 24px rgba(28,24,18,.2)}
.btn-dark .arr{background:#fff;color:var(--dark)}
.btn-light{background:#fff;color:var(--dark);box-shadow:var(--shadow);padding:10px 10px 10px 22px}
.btn-light .arr{background:var(--amber);color:var(--dark)}
.btn:hover{transform:translateY(-3px)}
.btn-plain{padding:14px 26px}
.tag{display:inline-block;padding:8px 16px;border-radius:999px;font-size:.85rem;font-weight:600;white-space:nowrap}
.tag-dark{background:var(--dark);color:#fff}
.tag-amber{background:var(--amber);color:var(--dark)}
.tag-light{background:#fff;color:var(--dark);box-shadow:var(--shadow)}

/* ---------- Hero ---------- */
.hero{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;padding-top:70px;padding-bottom:40px}
.hero-text{text-align:left}
.role{font-size:1.05rem;font-weight:600;color:var(--ink);margin-bottom:8px}
.hero-text .sub{font-size:1.05rem;max-width:520px}
.quote{margin-top:26px;padding-left:16px;border-left:3px solid var(--amber);font-style:italic;color:var(--ink);max-width:420px}
.hero-photo{position:relative;justify-self:center;width:100%;max-width:480px;aspect-ratio:4/5}
.blob{position:absolute;inset:8% 4% 0 8%;background:var(--amber);border-radius:48% 52% 46% 54% / 40% 42% 58% 60%;z-index:0}
.hero-photo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 15%;border-radius:36px;z-index:1;filter:saturate(1.05)}
.ftag{position:absolute;z-index:2;font-size:.85rem;font-weight:700;padding:9px 16px;border-radius:999px;box-shadow:0 10px 24px rgba(28,24,18,.18);animation:float 5s ease-in-out infinite;white-space:nowrap}
.ft1{top:6%;left:-6%;background:var(--dark);color:#fff}
.ft2{top:34%;right:-8%;background:var(--amber);color:var(--dark);animation-delay:-1s}
.ft3{bottom:24%;left:-10%;background:#fff;color:var(--dark);animation-delay:-2s}
.ft4{bottom:6%;right:4%;background:var(--dark);color:var(--amber);animation-delay:-3s}
[dir=rtl] .ft1{left:auto;right:-6%}
[dir=rtl] .ft2{right:auto;left:-8%}
[dir=rtl] .ft3{left:auto;right:-10%}
[dir=rtl] .ft4{right:auto;left:4%}
.sticker{position:absolute;top:2%;right:-2%;width:124px;height:124px;z-index:3;border-radius:50%;background:var(--dark);display:grid;place-items:center}
.sticker svg{position:absolute;inset:0;width:100%;height:100%;animation:spin 14s linear infinite}
.sticker text{fill:#fff;font-size:11.5px;font-weight:700;letter-spacing:2.6px;font-family:'Plus Jakarta Sans',sans-serif}
.sticker .go{width:44px;height:44px;border-radius:50%;background:var(--amber);color:var(--dark);display:grid;place-items:center;font-size:.95rem;position:relative;z-index:1}
[dir=rtl] .sticker{right:auto;left:-2%}

/* ---------- Bandeau défilant ---------- */
.marquee{background:var(--dark);border-top:3px solid var(--amber);border-bottom:3px solid var(--amber);overflow:hidden;padding:18px 0;white-space:nowrap}
.track{display:inline-flex;animation:marquee 28s linear infinite}
.track span{font-size:1.5rem;font-weight:800;color:#fff;padding-right:14px;letter-spacing:.3px}
.track span:nth-child(even){color:var(--amber)}
@keyframes marquee{from{transform:translateX(0)}to{transform:translateX(-50%)}}

/* ---------- Services : liste en accordéon ---------- */
.svc-head-wrap{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap;margin-bottom:34px}
.svc-list{display:grid;gap:14px;max-width:880px}
.svc{background:#fff;border-radius:26px;padding:20px 22px 20px 20px;cursor:pointer;transition:background .35s,color .35s,transform .3s,box-shadow .3s;box-shadow:var(--shadow)}
.svc:hover{transform:translateX(-4px)}
[dir=rtl] .svc:hover{transform:translateX(4px)}
.svc-head{display:flex;align-items:center;gap:20px}
.num{min-width:58px;height:40px;border-radius:999px;background:var(--cream);display:grid;place-items:center;font-size:.85rem;font-weight:700;color:var(--amber)}
.svc h3{flex:1;font-size:1.45rem;font-weight:700;color:var(--ink);transition:color .3s}
.go-sm{width:42px;height:42px;border-radius:50%;background:var(--amber);color:var(--dark);display:grid;place-items:center;transition:transform .35s}
.svc-body{display:none;padding:16px 0 4px 78px}
.svc-body p{color:#CFC8B8;max-width:600px;margin-bottom:14px;font-size:.98rem}
.chips{display:flex;gap:8px;flex-wrap:wrap}
.chips span{background:#2F2820;color:#fff;padding:6px 14px;border-radius:999px;font-size:.82rem;font-weight:600;border:1px solid #3B3328}
.svc.open{background:var(--dark);color:#fff;transform:none}
.svc.open h3{color:#fff}
.svc.open .num{background:var(--dark-2);color:var(--amber)}
.svc.open .go-sm{transform:rotate(45deg)}
.svc.open .svc-body{display:block}
[dir=rtl] .svc-body{padding:16px 78px 4px 0}

/* ---------- Teaser à propos (accueil) & page À propos : fond noir ---------- */
.dark{background:var(--dark);color:#fff}
.dark h2,.dark h3{color:#fff}
.dark p{color:#CFC8B8}
.dark .eyebrow{color:#BDB5A4}
.about{display:grid;grid-template-columns:.9fr 1.1fr;gap:70px;align-items:center}
.about-photo{position:relative;max-width:420px;width:100%;justify-self:center;aspect-ratio:4/5}
.about-photo .frame{position:absolute;inset:0;background:var(--amber);border-radius:36px;transform:rotate(-4deg)}
.about-photo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 15%;border-radius:32px;z-index:1}
.about-photo .tagwrap{position:absolute;inset:auto 0 -18px 0;display:flex;gap:8px;flex-wrap:wrap;justify-content:center;z-index:2;padding:0 10px}
.about-photo .tagwrap .tag{font-size:.8rem;padding:7px 12px;box-shadow:0 8px 20px rgba(0,0,0,.25)}
.about-text p.big{font-size:1.12rem;color:#E6E0D2}
.exp{margin-top:24px;background:var(--dark-2);border-radius:24px;padding:24px;border:1px solid #3B3328}
.exp h3{color:var(--amber);font-size:1.1rem;margin-bottom:6px}
.exp p{margin:0}
.about-actions{display:flex;gap:14px;align-items:center;flex-wrap:wrap;margin-top:28px}
.sign{font-family:'Brush Script MT','Segoe Script',cursive;font-size:1.9rem;color:#fff}
.about-actions .sign{margin-left:4px}
[dir=rtl] .about-actions .sign{margin-left:0;margin-right:4px}

/* ---------- Cartes ---------- */
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:24px}
.card{background:#fff;border-radius:30px;padding:30px;box-shadow:var(--shadow);transition:transform .3s,box-shadow .3s;display:flex;flex-direction:column;gap:6px}
.card:hover{transform:translateY(-6px);box-shadow:0 22px 44px rgba(28,24,18,.12)}
.ico{width:58px;height:58px;border-radius:50%;display:grid;place-items:center;background:var(--dark);color:var(--amber);font-size:1.25rem;margin-bottom:14px}
.card p{margin-bottom:auto}
.card .btn{align-self:flex-start;margin-top:14px}
.card .go-card{width:46px;height:46px;border-radius:50%;background:var(--amber);color:var(--dark);display:grid;place-items:center;margin-top:12px;align-self:flex-start}

/* ---------- Contact ---------- */
.head{text-align:center;max-width:720px;margin:0 auto 40px}
.head p{font-size:1.05rem}
.form{max-width:660px;margin:0 auto;background:#fff;border-radius:34px;padding:38px;box-shadow:var(--shadow);display:grid;gap:14px}
.form input,.form textarea{width:100%;padding:16px 20px;border-radius:20px;border:1.5px solid var(--line);background:var(--cream);font:inherit;color:var(--ink);transition:.2s}
.form input:focus,.form textarea:focus{outline:none;border-color:var(--amber);background:#fff;box-shadow:0 0 0 4px rgba(255,164,27,.18)}
.form textarea{min-height:140px;resize:vertical}
.form .btn{justify-self:center}
.social{display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin-top:30px}
.social a{width:56px;height:56px;border-radius:50%;background:var(--dark);color:#fff;display:grid;place-items:center;font-size:1.2rem;transition:.25s}
.social a:hover{background:var(--amber);color:var(--dark);transform:translateY(-4px)}
.counter{max-width:660px;margin:36px auto 0;text-align:center;background:#fff;border-radius:30px;padding:24px;box-shadow:var(--shadow)}
.cta{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;background:var(--amber);color:var(--dark);border-radius:36px;padding:38px 44px}
.cta h2{color:var(--dark);font-size:2.3rem;margin:0}
.cta .btn-dark .arr{background:var(--amber);color:var(--dark)}

/* ---------- Pied de page ---------- */
footer{background:var(--dark);color:#CFC8B8;text-align:center;padding:40px 5% 34px;font-size:.9rem}
footer .social{margin-top:16px}
footer .social a{background:var(--dark-2);width:46px;height:46px;font-size:1rem}
footer .social a:hover{background:var(--amber);color:var(--dark)}

/* ---------- Animations ---------- */
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}
@keyframes spin{to{transform:rotate(360deg)}}
html.js .reveal{opacity:0;transform:translateY(26px);transition:opacity .7s ease,transform .7s ease}
html.js .reveal.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto!important}html.js .reveal{opacity:1;transform:none}}

/* ---------- Responsive ---------- */
@media (max-width:1000px){
  h1{font-size:3.2rem}h2{font-size:2.4rem}
  .cta-nav{display:none}
}
@media (max-width:860px){
  .hero,.about{grid-template-columns:1fr;gap:50px}
  .hero{padding-top:40px;text-align:center}
  .hero-text{text-align:center}
  .hero-text .sub,.quote{margin-left:auto;margin-right:auto}
  .quote{border-left:none;border-top:3px solid var(--amber);padding:14px 0 0;text-align:center}
  .btns{justify-content:center}
  .hero-photo{max-width:400px}
  .about-text{text-align:center}
  .about-actions{justify-content:center}
  .svc-body{padding-left:0}
  [dir=rtl] .svc-body{padding-right:0}
  section{padding:64px 0}
}
@media (max-width:760px){
  .burger{display:block}
  .menu{display:none;position:absolute;top:calc(100% + 10px);left:0;right:0;background:var(--dark);border-radius:26px;flex-direction:column;padding:12px;gap:4px}
  .menu.open{display:flex}
  .menu a{padding:12px 16px}
  .navbar{flex-wrap:wrap}
  h1{font-size:2.6rem}h2{font-size:2rem}
  .ft1,.ft2,.ft3,.ft4{font-size:.75rem;padding:7px 12px}
  .cta{padding:30px 26px;text-align:center;justify-content:center}
  .form{padding:26px}
  .svc h3{font-size:1.15rem}
}
"""

JS = """
(function(){
  var DICT = __DICT__;
  var EMAIL = "__EMAIL__";
  document.documentElement.classList.add('js');

  var burger = document.getElementById('burger'), menu = document.getElementById('menu');
  if (burger) burger.addEventListener('click', function(){ menu.classList.toggle('open'); });

  function setLang(l){
    var d = DICT[l]; if (!d) return;
    document.documentElement.lang = l;
    document.documentElement.dir = (l === 'ar') ? 'rtl' : 'ltr';
    document.querySelectorAll('[data-i18n]').forEach(function(el){
      var k = el.getAttribute('data-i18n'); if (d[k] !== undefined) el.textContent = d[k];
    });
    document.querySelectorAll('[data-i18n-ph]').forEach(function(el){
      var k = el.getAttribute('data-i18n-ph'); if (d[k] !== undefined) el.setAttribute('placeholder', d[k]);
    });
    document.querySelectorAll('.lang button').forEach(function(b){ b.classList.toggle('on', b.dataset.lang === l); });
    try { localStorage.setItem('km_lang', l); } catch(e){}
  }
  document.querySelectorAll('.lang button').forEach(function(b){
    b.addEventListener('click', function(){ setLang(b.dataset.lang); });
  });
  var saved = null; try { saved = localStorage.getItem('km_lang'); } catch(e){}
  setLang(DICT[saved] ? saved : 'fr');

  // Accordéon des services
  document.querySelectorAll('.svc').forEach(function(item){
    function toggle(){
      var open = item.classList.contains('open');
      document.querySelectorAll('.svc.open').forEach(function(o){ o.classList.remove('open'); });
      if (!open) item.classList.add('open');
    }
    item.addEventListener('click', toggle);
    item.addEventListener('keydown', function(e){ if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); } });
  });

  // Apparition au scroll
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    items.forEach(function(el){ io.observe(el); });
  } else { items.forEach(function(el){ el.classList.add('in'); }); }

  // Formulaire : ouvre le client e-mail (pas de serveur nécessaire)
  var form = document.getElementById('contactForm');
  if (form) form.addEventListener('submit', function(ev){
    ev.preventDefault();
    var n = form.name.value, m = form.email.value, t = form.message.value;
    var body = 'Nom: ' + n + '\\nE-mail: ' + m + '\\n\\n' + t;
    window.location.href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent('Contact via portfolio - ' + n) + '&body=' + encodeURIComponent(body);
  });
})();
"""


ICON_CODES = {'fa-instagram': 'f16d', 'fa-facebook-f': 'f39e', 'fa-linkedin-in': 'f0e1', 'fa-youtube': 'f167', 'fa-envelope': 'f0e0', 'fa-arrow-right': 'f061', 'fa-arrow-up-right': 'f08e', 'fa-bars': 'f0c9', 'fa-graduation-cap': 'f19d', 'fa-bullhorn': 'f0a1', 'fa-code': 'f121', 'fa-camera': 'f030', 'fa-globe': 'f0ac', 'fa-robot': 'f544', 'fa-gears': 'f085', 'fa-mobile-screen-button': 'f3cd', 'fa-lock': 'f023', 'fa-key': 'f084', 'fa-paper-plane': 'f1d8'}


def fix_icons(html):
    """Remplace les <i> vides par le glyphe Font Awesome (sinon Tidy/Jimdo les supprime)."""
    import re

    def rep(m):
        cls = m.group(1)
        for name, cp in ICON_CODES.items():
            if name in cls.split():
                return '<i class="%s">&#x%s;</i>' % (cls, cp)
        return m.group(0)

    return re.sub(r'<i class="([^"]*)"></i>', rep, html)


def dict_js():
    return JS.replace("__DICT__", json.dumps(T, ensure_ascii=False)).replace("__EMAIL__", EMAIL)


def tx(key, tag="span", extra=""):
    """Élément traduisible ; le texte FR est mis par défaut."""
    return f'<{tag} data-i18n="{key}"{extra}>{T["fr"][key]}</{tag}>'


def social_links(cls="social"):
    return f"""<div class="{cls}">
    <a href="{INSTAGRAM}" target="_blank" rel="noopener" title="Instagram"><i class="fa-brands fa-instagram"></i></a>
    <a href="{FACEBOOK}" target="_blank" rel="noopener" title="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
    <a href="{LINKEDIN}" target="_blank" rel="noopener" title="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
    <a href="{YOUTUBE}" target="_blank" rel="noopener" title="YouTube"><i class="fa-brands fa-youtube"></i></a>
  </div>"""


def page_shell(title, desc, active, body):
    nav_items = "".join(
        '<li><a href="%s"%s>%s</a></li>' % (href, ' class="on"' if href == active else "", label)
        for href, label in PAGES)
    return f"""<!DOCTYPE html>
<html lang="fr" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>{CSS}</style>
</head>
<body>
<header class="topbar">
  <nav class="navbar">
    <a class="logo" href="index.html"><span class="logo-dot">K</span>Karou.</a>
    <button class="burger" id="burger" aria-label="Menu"><i class="fa-solid fa-bars"></i></button>
    <ul class="menu" id="menu">{nav_items}</ul>
    <div class="navright">
      <a class="cta-nav" href="contact.html" data-i18n="btn_contact">{T['fr']['btn_contact']}</a>
      <div class="lang">
        <button data-lang="fr" class="on">FR</button>
        <button data-lang="ar">عربي</button>
        <button data-lang="en">EN</button>
      </div>
    </div>
  </nav>
</header>
{body}
<footer>
  <div><span data-i18n="footer">{T['fr']['footer']}</span></div>
  {social_links()}
</footer>
<script>{dict_js()}</script>
</body>
</html>
"""


def ico(c):
    return f'<div class="ico"><i class="fa-solid {c}"></i></div>'


def svc_item(i, key, open_=False):
    cls = "svc open" if open_ else "svc"
    return f"""<div class="{cls}" tabindex="0" role="button" aria-expanded="{str(open_).lower()}">
        <div class="svc-head">
          <span class="num">0{i}.</span>
          {tx(key + '_t', 'h3')}
          <span class="go-sm"><i class="fa-solid fa-arrow-up-right"></i></span>
        </div>
        <div class="svc-body">
          {tx(key + '_d', 'p')}
          <div class="chips">{tx(key + '_tag1')}{tx(key + '_tag2')}{tx(key + '_tag3')}</div>
        </div>
      </div>"""


def services_list():
    return '<div class="svc-list">' + "".join(
        svc_item(i, f"s{i}", open_=(i == 2)) for i in range(1, 6)) + "</div>"


def marquee():
    txt = T["fr"]["marquee"]
    span = f'<span data-i18n="marquee">{txt}</span>'
    return f'<div class="marquee"><div class="track">{span}{span}</div></div>'


BODY = {}

BODY["index.html"] = f"""
<main>
<section class="hero wrap">
  <div class="hero-text reveal">
    <span class="badge"><i class="fa-solid fa-graduation-cap"></i>{tx('badge')}</span>
    <h1>{tx('hero_a')} <span class="hl">{tx('hero_b')}</span></h1>
    <p class="role">{tx('hero_role')}</p>
    <p class="sub">{tx('hero_sub')}</p>
    <div class="btns">
      <a class="btn btn-amber" href="works.html">{tx('btn_work')}<span class="arr"><i class="fa-solid fa-arrow-right"></i></span></a>
      <a class="btn btn-dark" href="contact.html">{tx('btn_contact')}<span class="arr"><i class="fa-solid fa-arrow-right"></i></span></a>
    </div>
    <p class="quote">{tx('quote')}</p>
  </div>
  <div class="hero-photo reveal">
    <div class="blob"></div>
    <img src="{PHOTO_SRC}" alt="Karou Mosaab">
    <span class="ftag ft1" data-i18n="ft1">{T['fr']['ft1']}</span>
    <span class="ftag ft2" data-i18n="ft2">{T['fr']['ft2']}</span>
    <span class="ftag ft3" data-i18n="ft3">{T['fr']['ft3']}</span>
    <span class="ftag ft4" data-i18n="ft4">{T['fr']['ft4']}</span>
    <div class="sticker">
      <svg viewBox="0 0 124 124"><defs><path id="circ" d="M62,62 m-46,0 a46,46 0 1,1 92,0 a46,46 0 1,1 -92,0"/></defs>
        <text><textPath href="#circ">KAROU • MOSAAB • KAROU • MOSAAB • </textPath></text></svg>
      <span class="go"><i class="fa-solid fa-arrow-right"></i></span>
    </div>
  </div>
</section>
{marquee()}
<section>
  <div class="wrap">
    <div class="svc-head-wrap reveal">
      <div>
        {tx('svc_eyebrow', 'span', ' class="eyebrow"')}
        <h2>{tx('svc_a')} <span class="hl">{tx('svc_b')}</span></h2>
      </div>
      <a class="btn btn-dark" href="skills.html">{tx('btn_all')}<span class="arr"><i class="fa-solid fa-arrow-right"></i></span></a>
    </div>
    <div class="reveal">{services_list()}</div>
  </div>
</section>
<section class="dark">
  <div class="wrap about">
    <div class="about-photo reveal">
      <div class="frame"></div>
      <img src="{PHOTO_SRC}" alt="Karou Mosaab">
      <div class="tagwrap">
        <span class="tag tag-dark" data-i18n="ft1">{T['fr']['ft1']}</span>
        <span class="tag tag-amber" data-i18n="ft3">{T['fr']['ft3']}</span>
        <span class="tag tag-light" data-i18n="ft2">{T['fr']['ft2']}</span>
      </div>
    </div>
    <div class="about-text reveal">
      {tx('about_eyebrow', 'span', ' class="eyebrow"')}
      <h2>{tx('about_a')} <span class="hl">{tx('about_b')}</span></h2>
      <p class="big">{tx('about_p1', 'p')}</p>
      <div class="about-actions">
        <a class="btn btn-amber" href="about.html">{tx('btn_cv')}<span class="arr"><i class="fa-solid fa-arrow-right"></i></span></a>
      </div>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="cta reveal">
      <h2>{tx('cta_t')}</h2>
      <a class="btn btn-dark" href="contact.html">{tx('btn_contact')}<span class="arr"><i class="fa-solid fa-arrow-right"></i></span></a>
    </div>
  </div>
</section>
</main>"""

BODY["about.html"] = f"""
<main>
<section class="dark" style="padding-top:80px">
  <div class="wrap about">
    <div class="about-photo reveal">
      <div class="frame"></div>
      <img src="{PHOTO_SRC}" alt="Karou Mosaab">
      <div class="tagwrap">
        <span class="tag tag-dark" data-i18n="ft1">{T['fr']['ft1']}</span>
        <span class="tag tag-amber" data-i18n="ft3">{T['fr']['ft3']}</span>
        <span class="tag tag-light" data-i18n="ft4">{T['fr']['ft4']}</span>
      </div>
    </div>
    <div class="about-text reveal">
      {tx('about_eyebrow', 'span', ' class="eyebrow"')}
      <h2>{tx('about_a')} <span class="hl">{tx('about_b')}</span></h2>
      <p class="big">{tx('about_p1', 'p')}</p>
      <p>{tx('about_p2', 'p')}</p>
      <div class="exp">
        <h3 data-i18n="exp_t">{T['fr']['exp_t']}</h3>
        <p data-i18n="exp_d">{T['fr']['exp_d']}</p>
      </div>
      <div class="about-actions">
        <!-- Remplacer REMPLACER_PAR_URL_MON_CV par l'URL de la page « Mon CV » protégée par mot de passe dans Jimdo -->
        <a class="btn btn-amber" href="{CV_URL}">{tx('btn_cv')}<span class="arr"><i class="fa-solid fa-lock"></i></span></a>
        <span class="sign">Karou</span>
      </div>
      <small data-i18n="cv_note" style="display:block;margin-top:10px;color:#BDB5A4">{T['fr']['cv_note']}</small>
    </div>
  </div>
</section>
</main>"""

BODY["works.html"] = f"""
<main>
<section style="padding-top:80px">
  <div class="wrap">
    <div class="head reveal">
      {tx('works_a', 'span', ' class="eyebrow"')}
      <h2>{tx('works_a')} <span class="hl">{tx('works_b')}</span></h2>
      <p>{tx('works_sub', 'p')}</p>
    </div>
    <div class="grid">
      <div class="card reveal">
        <div class="ico"><i class="fa-brands fa-instagram"></i></div>
        {tx('w1_t', 'h3')}
        {tx('w1_d', 'p')}
        <a class="btn btn-amber" href="{INSTAGRAM}" target="_blank" rel="noopener">{tx('btn_insta')}<span class="arr"><i class="fa-solid fa-arrow-up-right"></i></span></a>
      </div>
      <div class="card reveal">
        {ico('fa-globe')}
        {tx('w2_t', 'h3')}
        {tx('w2_d', 'p')}
      </div>
      <div class="card reveal">
        {ico('fa-robot')}
        {tx('w3_t', 'h3')}
        {tx('w3_d', 'p')}
      </div>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="cta reveal">
      <h2>{tx('cta_t')}</h2>
      <a class="btn btn-dark" href="contact.html">{tx('btn_contact')}<span class="arr"><i class="fa-solid fa-arrow-right"></i></span></a>
    </div>
  </div>
</section>
</main>"""

BODY["skills.html"] = f"""
<main>
<section style="padding-top:80px">
  <div class="wrap">
    <div class="svc-head-wrap reveal">
      <div>
        {tx('svc_eyebrow', 'span', ' class="eyebrow"')}
        <h2>{tx('skills_a')} <span class="hl">{tx('skills_b')}</span></h2>
        <p style="margin:0;max-width:560px">{tx('skills_sub')}</p>
      </div>
    </div>
    <div class="reveal">{services_list()}</div>
  </div>
</section>
</main>"""

BODY["contact.html"] = f"""
<main>
<section style="padding-top:80px">
  <div class="wrap">
    <div class="head reveal">
      {tx('btn_contact', 'span', ' class="eyebrow"')}
      <h2>{tx('contact_a')} <span class="hl">{tx('contact_b')}</span></h2>
      <p>{tx('contact_sub', 'p')}</p>
    </div>
    <form class="form reveal" id="contactForm">
      <input name="name" required placeholder="Votre nom" data-i18n-ph="f_name">
      <input name="email" type="email" required placeholder="Votre e-mail" data-i18n-ph="f_email">
      <textarea name="message" required placeholder="Votre message" data-i18n-ph="f_msg"></textarea>
      <button class="btn btn-amber" type="submit"><span data-i18n="f_send">{T['fr']['f_send']}</span><span class="arr"><i class="fa-solid fa-paper-plane"></i></span></button>
    </form>
    <div class="reveal">
      {social_links()}
    </div>
    <!-- Compteur de visiteurs (compteurdevisite.com) -->
    <div class="counter reveal">
      <p data-i18n="counter_label" style="margin-bottom:10px">{T['fr']['counter_label']}</p>
      {COUNTER}
    </div>
  </div>
</section>
</main>"""

DESCS = {
    "index.html": "Karou Mosaab - Master 2 Marketing Digital, EHEC. Accueil.",
    "about.html": "A propos de moi - Karou Mosaab, Master 2 Marketing Digital à l'EHEC.",
    "works.html": "Mes travaux - photographie automobile, sites web, automatisation.",
    "skills.html": "Mes compétences - marketing digital, web, automatisation, photo, smartphones.",
    "contact.html": "Contact - Karou Mosaab.",
}

if __name__ == "__main__":
    for href, label in PAGES:
        html = fix_icons(page_shell(f"{label} | Karou Mosaab", DESCS[href], href, BODY[href]))
        with open(os.path.join(HERE, href), "w", encoding="utf-8") as f:
            f.write(html)
        print("écrit", href, len(html))
