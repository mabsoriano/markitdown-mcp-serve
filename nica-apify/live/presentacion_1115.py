"""Presentación del LIVE del domingo 15 nov 2026 (Zoom, gente nueva por pauta).
Probadita de hipnosis (no completa) + oferta Buen Fin: Programa la Riqueza mientras Duermes $500 + impuestos,
regalo: activación en vivo martes 17 · 11 AM. Reutiliza el estilo aprobado de presentacion_1110.py.
"""
from PIL import Image, ImageDraw
import presentacion as P
import presentacion_1110 as Q
from presentacion import (W, H, ORO, ORO_CLARO, BLANCO, GRIS, SERIF, SANS, SANS_REG, f, universo, parrafo, caja,
                          circulo_num, pie, encabezado, qr)

LINK = "https://pay.hotmart.com/U104269730G?off=dwbelu1i"
ARTE = P.AQUI / "artes" / "buenfin-riqueza-mientras-duermes-4x5.jpg"
SALIDA = P.AQUI / "presentacion-1115"
CIERRE = "Precio Buen Fin · solo hasta el lunes 16 de noviembre"


def s_puerta():
    return Q.s_capas(["✓ abriste la puerta", "✓ hoy", "✓ abriste la puerta"],
                     "LO QUE NO SE REPITE, NO SE INSTALA", "Hoy abriste la puerta. La repetición instala.")


def s_oferta():
    img = universo(37)
    arte = Image.open(ARTE).convert("RGB")
    h = 760
    arte = arte.resize((int(arte.width * h / arte.height), h), Image.LANCZOS)
    x0 = W - arte.width - 90
    caja(img, (x0 - 10, 150, x0 + arte.width + 10, 160 + h), 20)
    img.paste(arte, (x0, 155))
    d = ImageDraw.Draw(img)
    d.text((90, 70), "PARA QUE SE INSTALE · 21 NOCHES", font=f(SANS, 32), fill=ORO)
    y = parrafo(d, "Programa la Riqueza mientras Duermes", f(SERIF, 66), 90, 115, x0 - 150, ORO_CLARO, inter=1.05)
    d.text((90, y + 25), "BNQ Method™ · BIO · NEURO · QUANTUM", font=f(SANS, 32), fill=ORO)
    y += 95
    items = ["Audio de activación de 8 horas · 21 noches", "Fórmula Cuántica CEI™",
             "Fórmula Cuántica ADN · reprograma tus células",
             "Fórmula Cuántica para desbloquear la riqueza",
             "REGALO: activación en vivo · martes 17 · 11 AM"]
    for i, t in enumerate(items, 1):
        d.ellipse([92, y + 14, 112, y + 34], fill=ORO)
        y = max(parrafo(d, t, f(SANS, 36), 135, y, x0 - 200, ORO_CLARO if i == 5 else BLANCO), y + 50) + 16
    d.text((90, y + 20), "Antes $1,200", font=f(SANS, 44), fill=GRIS)
    w = d.textlength("Antes $1,200", font=f(SANS, 44))
    d.line([(90, y + 47), (90 + w, y + 47)], fill=(230, 90, 90), width=5)
    d.text((90, y + 75), "$500 + impuestos", font=f(SERIF, 80), fill=ORO_CLARO)
    d.text((90, H - 150), CIERRE, font=f(SANS, 38), fill=ORO)
    pie(d)
    return img


def s_decide():
    img = universo(39)
    d = ImageDraw.Draw(img)
    y = encabezado(d, "SI DECIDES HOY", "Programa la Riqueza · $500", ancho=1050)
    for t in ["+ impuestos · antes $1,200", "REGALO: activación en vivo martes 17 · 11 AM",
              "Garantía Hotmart de 7 días", CIERRE, "Al entrar, escribe ACTIVADA en el chat"]:
        d.ellipse([92, y + 18, 112, y + 38], fill=ORO)
        y = max(parrafo(d, t, f(SANS, 42), 135, y, 960, BLANCO), y + 55) + 30
    caja(img, (1260, 180, 1800, 880), 24, ORO_CLARO)
    img.paste(qr(460, LINK), (1300, 220))
    d = ImageDraw.Draw(img)
    for i, t in enumerate(["Escanea y activa", "Precio Buen Fin"]):
        d.text((1530 - d.textlength(t, font=f(SANS, 40)) / 2, 710 + i * 60), t, font=f(SANS, 40), fill=ORO_CLARO)
    pie(d)
    return img


def s_probadita():
    img = Q.s_hipnosis()
    d = ImageDraw.Draw(img)
    t = "Una probadita: abre la puerta. La repetición la instala."
    d.text((W / 2 - d.textlength(t, font=f(SANS, 44)) / 2, 820), t, font=f(SANS, 44), fill=ORO_CLARO)
    return img


SLIDES = [("01_portada", P.d01_portada), ("02_cuidados", P.d02_cuidados), ("03_programas", Q.s_programas),
          ("04_capas", Q.s_capas), ("05_bio", Q.s_bio), ("06_duke", Q.s_duke), ("07_hebb", Q.s_hebb),
          ("08_quantum", Q.s_quantum), ("09_taxistas", Q.s_taxistas), ("10_quien_soy", P.d17_quien_soy),
          ("11_preparate", P.d18_preparate), ("12_probadita", s_probadita), ("13_sentiste", P.d20_sentiste),
          ("14_puerta", s_puerta), ("15_oferta", s_oferta), ("16_razones", Q.s_razones), ("17_decide", s_decide),
          ("18_comunidad", P.d26_comunidad), ("19_cierre", P.d27_cierre)]


def armar():
    from pptx import Presentation
    from pptx.util import Emu
    SALIDA.mkdir(exist_ok=True)
    rutas = []
    for nombre, fn in SLIDES:
        r = SALIDA / f"{nombre}.png"
        fn().save(r)
        rutas.append(r)
    pres = Presentation()
    pres.slide_width, pres.slide_height = Emu(12192000), Emu(6858000)
    for r in rutas:
        s = pres.slides.add_slide(pres.slide_layouts[6])
        s.shapes.add_picture(str(r), 0, 0, pres.slide_width, pres.slide_height)
    pres.save(P.AQUI / "presentacion-live-2026-11-15.pptx")
    imgs = [Image.open(r).convert("RGB") for r in rutas]
    imgs[0].save(P.AQUI / "presentacion-live-2026-11-15.pdf", save_all=True, append_images=imgs[1:])
    # versión ligera para Google Slides
    pres2 = Presentation()
    pres2.slide_width, pres2.slide_height = Emu(12192000), Emu(6858000)
    for r in rutas:
        j = r.with_suffix(".jpg")
        Image.open(r).convert("RGB").save(j, quality=80)
        s = pres2.slides.add_slide(pres2.slide_layouts[6])
        s.shapes.add_picture(str(j), 0, 0, pres2.slide_width, pres2.slide_height)
    pres2.save("/home/user/PRESENTACION-LIVE-15-NOV-GOOGLE.pptx")
    print(len(rutas), "láminas")


if __name__ == "__main__":
    armar()
