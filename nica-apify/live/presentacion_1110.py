"""Presentación del LIVE del 10 nov 2026 (mismo estilo aprobado: universo azul/morado + dorado + foto real).

Oferta: Hipnosis para Hackear tus Bloqueos con el Dinero · Activación Simultánea · $500 (antes $1,200), solo hoy.
Uso: python3 live/presentacion_1110.py → live/presentacion-1110/*.png + presentacion-live-2026-11-10.pptx/.pdf
"""
from pathlib import Path
from PIL import Image, ImageDraw

import presentacion as P
from presentacion import (W, H, ORO, ORO_CLARO, BLANCO, GRIS, SERIF, SANS, SANS_REG, f, universo, foto_derecha,
                          parrafo, linea_oro, caja, circulo_num, pie, encabezado, frase, numero, qr)

LINK = "https://hotmart.com/es/marketplace/productos/activacionadnmillonario/U104269730G"
P.COMUNIDAD = "https://chat.whatsapp.com/Lw9TQt73zFrEN1bGreqr29?s=cl&p=i&mlu=4&ilr=4&iam=2"
PORTADA = Path("/home/user/PORTADA-HOTMART-HIPNOSIS-DINERO.jpg")
SALIDA = P.AQUI / "presentacion-1110"
CIERRE = "Válido solo hoy, martes 10 de noviembre"


def s_programas():
    img = universo(30)
    d = ImageDraw.Draw(img)
    y = encabezado(d, "DIAGNÓSTICO", "Tus 4 programas del dinero")
    progs = ["Llega y se va", "Cuesta que llegue", "Llega con culpa", "Llega y se queda"]
    for i, t in enumerate(progs):
        x = 90 + (i % 2) * 880
        yy = y + 20 + (i // 2) * 230
        caja(img, (x, yy, x + 840, yy + 190), 28, ORO if i < 3 else ORO_CLARO)
        d = ImageDraw.Draw(img)
        d.text((x + 40, yy + 20), str(i + 1), font=f(SERIF, 140), fill=ORO)
        d.text((x + 170, yy + 62), t.upper(), font=f(SANS, 54), fill=BLANCO)
    t = "Escribe tu número en el chat"
    d.text((W / 2 - d.textlength(t, font=f(SANS, 48)) / 2, H - 150), t, font=f(SANS, 48), fill=ORO_CLARO)
    return img


def s_capas(marcar=None, kicker="EL MÉTODO BNQ™", titulo="Tu bloqueo vive en 3 capas"):
    img = universo(31)
    d = ImageDraw.Draw(img)
    y = encabezado(d, kicker, titulo)
    capas = [("BIO", "Tu cuerpo", "Lo que tu memoria celular heredó sobre el dinero"),
             ("NEURO", "Tu mente", "El programa del subconsciente: no merecimiento, deudas, autosabotaje"),
             ("QUANTUM", "Tu energía", "Tu frecuencia con el dinero")]
    for i, (n, sub, txt) in enumerate(capas):
        x = 90 + i * 590
        caja(img, (x, y + 10, x + 550, y + 520), 30)
        d = ImageDraw.Draw(img)
        d.text((x + 275 - d.textlength(n, font=f(SERIF, 80)) / 2, y + 60), n, font=f(SERIF, 80), fill=ORO_CLARO)
        d.text((x + 275 - d.textlength(sub, font=f(SANS, 44)) / 2, y + 170), sub, font=f(SANS, 44), fill=ORO)
        parrafo(d, txt, f(SANS_REG, 36), x + 40, y + 260, 470, BLANCO, centro=True)
        if marcar:
            et = marcar[i]
            d.text((x + 275 - d.textlength(et, font=f(SANS, 36)) / 2, y + 450), et, font=f(SANS, 36),
                   fill=ORO if et.startswith("✓") else GRIS)
    pie(d)
    return img


def s_bio():
    return frase(32, "CAPA 1 · BIO · TU CUERPO", "Memoria celular",
                 "Lo que tu cuerpo guarda desde que naciste (o antes): “el dinero cuesta”, “no alcanza”, "
                 "“los ricos son malos”.")


def s_duke():
    return numero(33, "CAPA 2 · NEURO · TU MENTE", "43%",
                  "de lo que haces en el día lo haces por hábito, mientras piensas en otra cosa.",
                  "Universidad de Duke, 2002")


def s_hebb():
    return frase(34, "LA BUENA NOTICIA", "Lo que repites, se instala.",
                 "“Neuronas que se activan juntas, se conectan juntas.” · Donald Hebb, 1949")


def s_quantum():
    return frase(35, "CAPA 3 · QUANTUM · TU ENERGÍA", "Coherencia Energética Integral (CEI™)",
                 "Cuando tu mente, tu emoción y tu acción van en la misma frecuencia.")


def s_taxistas():
    return frase(36, "TU CEREBRO PUEDE CAMBIAR", "El cerebro adulto se remodela con la práctica.",
                 "Taxistas de Londres · Eleanor Maguire, 2000. No importa tu edad.")


def s_puerta():
    return s_capas(["✓ abriste la puerta", "✓ hoy", "✓ abriste la puerta"],
                   "LO QUE ACABAS DE VIVIR", "Hoy abriste la puerta. La repetición instala.")


def s_oferta():
    img = universo(37)
    port = Image.open(PORTADA).convert("RGB").resize((640, 640), Image.LANCZOS)
    caja(img, (1170, 150, 1830, 810), 20)
    img.paste(port, (1180, 160))
    d = ImageDraw.Draw(img)
    d.text((90, 70), "PARA QUE SE INSTALE", font=f(SANS, 32), fill=ORO)
    y = parrafo(d, "Hipnosis para Hackear tus Bloqueos con el Dinero", f(SERIF, 64), 90, 110, 1040, ORO_CLARO,
                inter=1.05)
    d.text((90, y + 5), "ACTIVACIÓN SIMULTÁNEA · BIO · NEURO · QUANTUM", font=f(SANS, 34), fill=ORO)
    y += 75
    items = ["Fórmula Cuántica CEI™", "Hipnosis completa del dinero",
             "Audio subliminal de 8 horas · 21 noches", "Manual de activación de 21 días",
             "REGALO: Activaciones Robóticas Millonarias"]
    for i, t in enumerate(items, 1):
        d.ellipse([92, y + 14, 112, y + 34], fill=ORO)
        d.text((135, y), t, font=f(SANS, 40), fill=ORO_CLARO if i == 5 else BLANCO)
        y += 64
    d.text((1180, 840), "Antes $1,200", font=f(SANS, 46), fill=GRIS)
    w = d.textlength("Antes $1,200", font=f(SANS, 46))
    d.line([(1180, 868), (1180 + w, 868)], fill=(230, 90, 90), width=5)
    d.text((1180, 900), "HOY $500 MXN", font=f(SERIF, 92), fill=ORO_CLARO)
    d.text((90, H - 150), CIERRE, font=f(SANS, 40), fill=ORO)
    pie(d)
    return img


def s_razones():
    img = universo(38)
    d = ImageDraw.Draw(img)
    y = encabezado(d, "CON TODO MI CARIÑO", "Las 2 voces que aparecen")
    for i, t in enumerate(["“Ahorita no es el momento”", "“¿Y si a mí no me funciona?”"], 1):
        circulo_num(d, 140, y + 90, i, 44)
        d.text((220, y + 50), t, font=f(SERIF, 72), fill=BLANCO)
        y += 200
    parrafo(d, "¿Esta voz es mi realidad… o es mi programa?", f(SANS, 50), 90, y + 40, 1740, ORO_CLARO)
    pie(d)
    return img


def s_decide(kicker="SI DECIDES HOY", titulo="Activación Simultánea · $500"):
    img = universo(39)
    d = ImageDraw.Draw(img)
    y = encabezado(d, kicker, titulo, ancho=1050)
    for t in ["De regalo: Activaciones Robóticas Millonarias", "Garantía Hotmart de 7 días",
              CIERRE, "Al entrar, escribe ACTIVADA en el chat"]:
        d.ellipse([92, y + 18, 112, y + 38], fill=ORO)
        parrafo(d, t, f(SANS, 46), 135, y, 960, BLANCO)
        y += 120
    caja(img, (1260, 180, 1800, 880), 24, ORO_CLARO)
    img.paste(qr(460, LINK), (1300, 220))
    d = ImageDraw.Draw(img)
    for i, t in enumerate(["Escanea y activa", "$500 solo hoy"]):
        d.text((1530 - d.textlength(t, font=f(SANS, 40)) / 2, 710 + i * 60), t, font=f(SANS, 40), fill=ORO_CLARO)
    pie(d)
    return img


def s_preguntas():
    return s_decide("TUS PREGUNTAS", "Escríbelas en el chat")


def s_hipnosis():
    img = P.d19_hipnosis()
    d = ImageDraw.Draw(img)
    d.rectangle([0, 800, W, 880], fill=(9, 7, 25))
    return img


SLIDES = [("01_portada", P.d01_portada), ("02_cuidados", P.d02_cuidados), ("03_programas", s_programas),
          ("04_capas", s_capas), ("05_bio", s_bio), ("06_duke", s_duke), ("07_hebb", s_hebb),
          ("08_quantum", s_quantum), ("09_taxistas", s_taxistas), ("10_quien_soy", P.d17_quien_soy),
          ("11_preparate", P.d18_preparate), ("12_hipnosis", s_hipnosis), ("13_sentiste", P.d20_sentiste),
          ("14_puerta", s_puerta), ("15_oferta", s_oferta), ("16_razones", s_razones), ("17_decide", s_decide),
          ("18_comunidad", P.d26_comunidad), ("19_cierre", P.d27_cierre)]


def armar():
    from pptx import Presentation
    from pptx.util import Emu
    SALIDA.mkdir(exist_ok=True)
    rutas = []
    for nombre, fn in SLIDES:
        ruta = SALIDA / f"{nombre}.png"
        fn().save(ruta)
        rutas.append(ruta)
    pres = Presentation()
    pres.slide_width, pres.slide_height = Emu(12192000), Emu(6858000)
    for r in rutas:
        s = pres.slides.add_slide(pres.slide_layouts[6])
        s.shapes.add_picture(str(r), 0, 0, pres.slide_width, pres.slide_height)
    pres.save(P.AQUI / "presentacion-live-2026-11-10.pptx")
    imgs = [Image.open(r).convert("RGB") for r in rutas]
    imgs[0].save(P.AQUI / "presentacion-live-2026-11-10.pdf", save_all=True, append_images=imgs[1:])
    print(len(rutas), "láminas")


if __name__ == "__main__":
    armar()
