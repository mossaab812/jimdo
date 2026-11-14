#!/usr/bin/env python3
"""Génère le CV PDF (noir & or, comme le site) : Mosaab_Karou_CV.pdf
Dépendances : reportlab, pillow.  Usage : python3 make_cv.py
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Spacer, Image, Table, TableStyle, KeepTogether

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "Mosaab_Karou_CV.pdf")

BLACK = colors.HexColor("#0E0D0B")
CARD = colors.HexColor("#171512")
GOLD = colors.HexColor("#C9A45C")
CREAM = colors.HexColor("#F5F2EA")
CREAM_TXT = colors.HexColor("#F3EDE2")
MUTED_TXT = colors.HexColor("#A39B8B")
INK = colors.HexColor("#1C1812")
MUTED = colors.HexColor("#6E6759")

W, H = A4
SIDE_W = 66 * mm
M = 9 * mm

# ---------- styles ----------
SCALE = 1.0

def st(name, **kw):
    base = dict(fontName="Helvetica", fontSize=8.6, leading=11.6, textColor=INK, spaceAfter=0)
    base.update(kw)
    for k in ("fontSize", "leading", "spaceBefore", "spaceAfter"):
        if k in base:
            base[k] = base[k] * SCALE
    return ParagraphStyle(name, **base)

def _make_styles():
    global S_SIDE_H, S_SIDE, S_SIDE_MUTED, S_NAME, S_TITLE, S_LEAD, S_H, S_CASE_K, S_CASE_T, S_CASE_O, S_BODY, S_JOB, S_ORG, S_BUL, S_DATE, S_EDU_T, S_EDU_O, S_EDU_B, S_FOOT
    S_SIDE_H = st("sh", fontName="Helvetica-Bold", fontSize=8, leading=10, textColor=GOLD, spaceBefore=9, spaceAfter=4)
    S_SIDE = st("s", fontSize=8.2, leading=10.8, textColor=CREAM_TXT)
    S_SIDE_MUTED = st("sm", fontSize=7.4, leading=9.6, textColor=MUTED_TXT)
    S_NAME = st("nm", fontName="Helvetica-Bold", fontSize=25, leading=28, textColor=INK, spaceAfter=3)
    S_TITLE = st("tt", fontName="Helvetica-Bold", fontSize=9.4, leading=12, textColor=GOLD, spaceAfter=6)
    S_LEAD = st("ld", fontSize=8.6, leading=12, textColor=MUTED)
    S_H = st("h", fontName="Helvetica-Bold", fontSize=9.2, leading=12, textColor=INK, spaceBefore=10, spaceAfter=5)
    S_CASE_K = st("ck", fontName="Helvetica-Bold", fontSize=6.6, leading=8.5, textColor=GOLD)
    S_CASE_T = st("ct", fontName="Helvetica-Bold", fontSize=8.8, leading=11, textColor=INK, spaceAfter=1)
    S_CASE_O = st("co", fontName="Helvetica-Oblique", fontSize=7.6, leading=10, textColor=MUTED, spaceAfter=2)
    S_BODY = st("b", fontSize=7.9, leading=10.6, textColor=MUTED)
    S_JOB = st("j", fontName="Helvetica-Bold", fontSize=9, leading=11.6, textColor=INK)
    S_ORG = st("o", fontName="Helvetica-Bold", fontSize=7.8, leading=10, textColor=GOLD, spaceAfter=3)
    S_BUL = st("bu", fontSize=7.9, leading=10.4, textColor=MUTED, leftIndent=9, bulletIndent=0)
    S_DATE = st("dt", fontName="Helvetica-Bold", fontSize=7.4, leading=9, textColor=BLACK, alignment=2)
    S_EDU_T = st("et", fontName="Helvetica-Bold", fontSize=8.6, leading=11, textColor=INK)
    S_EDU_O = st("eo", fontName="Helvetica-Bold", fontSize=7.8, leading=10, textColor=GOLD)
    S_EDU_B = st("eb", fontSize=7.6, leading=10, textColor=MUTED, spaceAfter=5)
    S_FOOT = st("ft", fontName="Helvetica-Oblique", fontSize=7.4, leading=9.5, textColor=MUTED)


_make_styles()

def chip_main(text):
    return f'<font backColor="#0E0D0B" color="#F3EDE2">&nbsp;{text}&nbsp;</font>'

def chip_side(text):
    return f'<font backColor="#2A241B" color="#F3EDE2">&nbsp;{text}&nbsp;</font>'

def bar(label, level, frac):
    """Libellé + niveau (repris du CV d'origine) et barre de progression."""
    full = SIDE_W - 2 * M
    t = Table([[Paragraph(label, S_SIDE),
                Paragraph(level, st("lv", fontName="Helvetica-Bold", fontSize=7, leading=9, alignment=2, textColor=GOLD))]],
              colWidths=[full - 22 * mm, 22 * mm])
    t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                           ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    track = Table([[""]], colWidths=[full], rowHeights=[2.2])
    track.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#2A241B")),
                               ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                               ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    fill = Table([[""]], colWidths=[full * frac], rowHeights=[2.2])
    fill.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), GOLD),
                              ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                              ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return [t, Spacer(1, 1.5), fill, Spacer(1, 5)]

# ---------- contenu ----------
def sidebar():
    f = []
    f.append(Image(os.path.join(HERE, "photo_circle.png"), width=40 * mm, height=40 * mm))
    f.append(Spacer(1, 4 * mm))

    f.append(Paragraph("CONTACT", S_SIDE_H))
    for line in [
        "karmoyoyo@gmail.com",
        "mossaabmanant19@gmail.com",
        "Algeria · Remote worldwide",
        "drive.google.com/portfolio",
        "karoumosaab.jimdofree.com",
        "Instagram : mk.venatus",
        "LinkedIn : mosaab~karou",
        "YouTube : @kazunari812",
        "Facebook",
    ]:
        f.append(Paragraph(line, S_SIDE))
        f.append(Spacer(1, 2.2))

    f.append(Paragraph("CORE EXPERTISE", S_SIDE_H))
    for label, level, frac in [
        ("Blender · 3D Motion", "Expert", 0.96),
        ("After Effects", "Expert", 0.92),
        ("DaVinci Resolve · Premiere Pro", "Pro", 0.90),
        ("Photoshop · Illustrator", "Pro", 0.86),
        ("AI Voice Synthesis", "Advanced", 0.82),
        ("LLM Translation Frameworks", "Advanced", 0.80),
    ]:
        f.extend(bar(label, level, frac))

    f.append(Paragraph("MARKETING &amp; WEB", S_SIDE_H))
    f.append(Paragraph("Digital marketing · strategy &amp; content", S_SIDE))
    f.append(Spacer(1, 2.2))
    f.append(Paragraph("Web development · HTML, CSS, JavaScript", S_SIDE))
    f.append(Spacer(1, 2.2))
    f.append(Paragraph("Task automation", S_SIDE))
    f.append(Spacer(1, 2.2))
    f.append(Paragraph("Car photography &amp; retouching", S_SIDE))

    f.append(Paragraph("TOOLKIT", S_SIDE_H))
    tools = ["Blender", "After Effects", "DaVinci Resolve", "Premiere Pro", "Photoshop",
             "Illustrator", "AI Voice Synthesis", "LLM Frameworks"]
    f.append(Paragraph(" ".join(chip_side(t) for t in tools), st("tk", fontSize=7.4, leading=13, textColor=CREAM_TXT)))

    f.append(Paragraph("LANGUAGES", S_SIDE_H))
    for lang, note in [("Arabic", "Native · Primary"), ("English", "AI Localization"),
                       ("French", "AI Localization"), ("Spanish", "AI Localization")]:
        f.append(Paragraph(f'<b>{lang}</b> <font color="#A39B8B">— {note}</font>', S_SIDE))
        f.append(Spacer(1, 2.2))

    f.append(Spacer(1, 4 * mm))
    box = Table([[Paragraph('<font color="#C9A45C"><b>PORTFOLIO</b></font><br/>'
                            '<font color="#F3EDE2">drive.google.com/portfolio</font><br/>'
                            '<font color="#F3EDE2">karoumosaab.jimdofree.com</font>',
                            st("pb", fontSize=7.6, leading=11, alignment=TA_CENTER))]],
                colWidths=[SIDE_W - 2 * M])
    box.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.8, GOLD), ("TOPPADDING", (0, 0), (-1, -1), 7),
                             ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))
    f.append(box)
    return f

def main_col():
    f = []
    f.append(Paragraph("MOSAAB KAROU", S_NAME))
    f.append(Paragraph("CINEMATIC MOTION DESIGNER &amp; AI-DRIVEN MEDIA STRATEGIST", S_TITLE))
    f.append(Paragraph(
        "Bespoke digital asset creator specializing in high-end cinematic 3D motion graphics, professional product "
        "media production, and automated multilingual localization. Expert in AI prompt engineering to deliver "
        "premium visual assets across global markets.", S_LEAD))
    f.append(Spacer(1, 4))
    f.append(Paragraph(
        "Master 2 Digital Marketing student at EHEC. I combine marketing strategy, web development, automation "
        "and car photography.", S_LEAD))

    f.append(Paragraph("SELECTED CASE STUDIES", S_H))
    cases = [
        ("CASE 01 — YOUTUBE CHANNEL OPTIMIZATION", "Visual Layout Optimization",
         "Objective: Re-engineer channel branding layouts to capture algorithmic traction and enhance organic visibility.",
         "Applied advanced composition techniques to construct high-contrast, narrative-driven thumbnails, resulting in "
         "sustained organic channel reach and improved audience alignment."),
        ("CASE 02 — E-COMMERCE BRAND MEDIA", "Commercial Product Visual Assets",
         "Objective: Create high-end visual assets for digital campaigns to lift target audience engagement.",
         "Engineered clean, photorealistic product setups with dynamic studio lighting and distraction-free backgrounds, "
         "elevating the product's perceived market value."),
        ("CASE 03 — CUSTOM 3D BRAND ANIMATION", "Ahmed's Pizzeria — Visual Identity",
         "Objective: Modernize a local restaurant's visual identity for digital displays and social media.",
         "Modeled and animated a custom 3D cinematic logo reveal featuring warm lighting and realistic textures — no "
         "pre-made templates, delivering a unique brand asset."),
    ]
    for k, t, o, b in cases:
        block = [Paragraph(k, S_CASE_K), Paragraph(t, S_CASE_T), Paragraph(o, S_CASE_O), Paragraph(b, S_BODY)]
        tb = Table([[block]], colWidths=[W - SIDE_W - M - 9 * mm])
        tb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.white),
                                ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                                ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                                ("LINEBEFORE", (0, 0), (0, -1), 2.2, GOLD)]))
        f.append(tb)
        f.append(Spacer(1, 4))

    f.append(Paragraph("PROFESSIONAL EXPERIENCE", S_H))
    exp = [
        ("Freelance Motion Designer &amp; AI Media Contractor", "2023 — Present",
         "Self-Employed · Global Remote Clients",
         ["Deploy custom 3D animations, product visuals, and localized media assets for international clients across "
          "e-commerce and digital media sectors.",
          "Manage a 100% remote global client pipeline through Agent AI translation models, ensuring fluent professional "
          "negotiations across multiple language barriers.",
          "Produce realistic localized voice-overs and audio tracks for multi-regional marketing campaigns via automated "
          "vocal synthesis pipelines."]),
        ("Visual Content Creator", "2021 — 2023", "Freelance · Regional Digital Commerce",
         ["Produced professional marketing graphics, product mockups, and corporate video banners for regional digital "
          "commerce shops.",
          "Maintained strict delivery schedules while adapting creative briefs into high-impact, clean visual formats — "
          "streamlining workflows, reducing revision rounds by 30%."]),
    ]
    for title, date, org, bullets in exp:
        head = Table([[Paragraph(title, S_JOB), Paragraph(date, S_DATE)]],
                     colWidths=[W - SIDE_W - M - 9 * mm - 34 * mm, 34 * mm])
        head.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                  ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                                  ("BACKGROUND", (1, 0), (1, 0), GOLD), ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
        f.append(head)
        f.append(Paragraph(org, S_ORG))
        for b in bullets:
            f.append(Paragraph(b, S_BUL, bulletText="•"))
        f.append(Spacer(1, 6))

    f.append(Paragraph("EDUCATION &amp; KEY CAPABILITIES", S_H))
    edu = [
        ("Master 2 Digital Marketing", "EHEC", "Digital marketing: strategy, content, web development and automation."),
        ("Digital Media &amp; Visual Effects", "Self-Directed Advanced Studies",
         "3D production pipelines, cinematic lighting, color theory, and advanced post-production techniques."),
        ("AI Media Localization Specialist", "LLM Translation &amp; Voice Synthesis Frameworks",
         "AI prompt engineering, multilingual voice synthesis, and cross-cultural digital asset localization for global campaigns."),
    ]
    for t, o, b in edu:
        f.append(Paragraph(t, S_EDU_T))
        f.append(Paragraph(o, S_EDU_O))
        f.append(Paragraph(b, S_EDU_B))

    f.append(Paragraph("STUDENT LIFE", S_H))
    f.append(Paragraph("HUC Alumni", S_EDU_T))
    f.append(Paragraph("Member of the HR &amp; Communication department (Company Discovery)", S_EDU_O))
    f.append(Spacer(1, 6))

    f.append(Paragraph("KEY CAPABILITIES", S_H))
    caps = ["YouTube Thumbnail Design", "Cinematic Video Production", "3D Logo Animation", "Product Photography",
            "Multilingual Localization", "AI Voice Synthesis", "Brand Identity Design", "Remote Global Workflow",
            "Digital Marketing", "Web Development", "Automation", "Car Photography"]
    f.append(Paragraph(" ".join(chip_main(c) for c in caps), st("cp", fontSize=7.6, leading=15, textColor=CREAM_TXT)))

    f.append(Spacer(1, 10))
    f.append(Paragraph("Portfolio: drive.google.com/portfolio · karoumosaab.jimdofree.com · "
                       "karmoyoyo@gmail.com · mossaabmanant19@gmail.com", S_FOOT))
    return f

# ---------- mise en page ----------
class Overflow(Exception):
    pass

def draw_bg(c):
    c.setFillColor(BLACK)
    c.rect(0, 0, SIDE_W, H, stroke=0, fill=1)
    c.setFillColor(CREAM)
    c.rect(SIDE_W, 0, W - SIDE_W, H, stroke=0, fill=1)
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.6)
    c.line(SIDE_W, 0, SIDE_W, H)

def flow(c, items, x, width, top, bottom, gap=0):
    y = top
    for fl in items:
        w, h = fl.wrap(width, 10000)
        if y - h < bottom:
            raise Overflow()
        fl.drawOn(c, x, y - h)
        y -= h + gap
    return y

def build():
    global SCALE
    for scale in [1.0, 0.97, 0.94, 0.91, 0.88, 0.85, 0.82]:
        SCALE = scale
        _make_styles()
        c = canvas.Canvas(OUT, pagesize=A4)
        c.setTitle("Mosaab Karou — CV")
        c.setAuthor("Mosaab Karou")
        draw_bg(c)
        try:
            side_w = SIDE_W - 2 * M
            flow(c, sidebar(), M, side_w, H - 10 * mm, 10 * mm, gap=0)
            main_x = SIDE_W + 9 * mm
            flow(c, main_col(), main_x, W - SIDE_W - 18 * mm, H - 12 * mm, 12 * mm, gap=0)
        except Overflow:
            continue
        c.showPage()
        c.save()
        print("OK", OUT, "scale", scale)
        return
    raise SystemExit("Le contenu ne rentre pas sur une page")

if __name__ == "__main__":
    build()
