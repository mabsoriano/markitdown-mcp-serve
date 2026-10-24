"""Artes del LIVE con la foto real de Mabel y su estilo (fondo espacial morado, acentos dorados).

Uso:  python3 artes_live.py
Sale en live/artes/: <variante>_<uso>_<ancho>x<alto>.png, web_banner_1920x700.png y, para
TikTok Ads, un video de 10 s a partir de cada arte vertical de anuncio.
"""
import random
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

AQUI = Path(__file__).parent
FOTO = AQUI.parent / "marca" / "mabel-foto.jpg"
SALIDA = AQUI / "artes"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
ORO, ORO_CLARO, BLANCO, OSCURO = (212, 162, 60), (246, 205, 110), (255, 255, 255), (18, 10, 40)

ETIQUETA = "LIVE GRATIS POR ZOOM"
SUBTITULO = "MARTES 27 DE OCTUBRE · 10 AM y 7 PM (CDMX)"
TITULO = "Hipnosis para hackear bloqueos con el dinero"
GANCHO = "¿EL DINERO LLEGA Y SE VA?"
AUTORA = ["Mabel Soriano", "Autora del libro Las Fórmulas Cuánticas", "para Hackear tu Mente y la Matrix"]
HORARIOS = [  # (país, sesión mañana, sesión noche)
    ("CDMX (México)", "10:00 AM", "7:00 PM"),
    ("Pacific Time", "9:00 AM", "6:00 PM"),
    ("Eastern Time", "12:00 PM", "9:00 PM"),
    ("Colombia", "11:00 AM", "8:00 PM"),
    ("Venezuela", "12:00 PM", "9:00 PM"),
    ("Argentina", "1:00 PM", "10:00 PM"),
    ("España", "5:00 PM", "—"),
]
CTA = {"organico": "REGÍSTRATE GRATIS · LINK EN MI PERFIL", "ads": "REGÍSTRATE GRATIS"}
FIRMA = "@mabradiante"
TAMANOS = [(1080, 1350), (1080, 1920), (1080, 1080)]


def f(ruta, px):
    return ImageFont.truetype(ruta, int(px))


def fondo(w, h, semilla=7):
    """Fondo espacial: degradado morado, nebulosa difusa, estrellas y polvo dorado."""
    rnd = random.Random(semilla)
    img = Image.new("RGB", (w, h), (10, 8, 30))
    neb = Image.new("RGB", (w, h), (10, 8, 30))
    d = ImageDraw.Draw(neb)
    for _ in range(14):
        x, y, r = rnd.uniform(0.3, 1.1) * w, rnd.uniform(-0.1, 1.0) * h, rnd.uniform(0.15, 0.45) * max(w, h)
        c = rnd.choice([(70, 40, 130), (40, 30, 110), (110, 60, 140), (30, 40, 90)])
        d.ellipse((x - r, y - r, x + r, y + r), fill=c)
    img = Image.blend(img, neb.filter(ImageFilter.GaussianBlur(max(w, h) * 0.08)), 0.65)
    d = ImageDraw.Draw(img, "RGBA")
    for _ in range(int(w * h / 2500)):
        x, y = rnd.uniform(0, w), rnd.uniform(0, h)
        r = rnd.choice([0.6, 0.8, 1, 1.2, 1.8])
        d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 255, rnd.randint(60, 220)))
    return img.convert("RGBA")


def polvo_dorado(img, cx, cy, rx, ry, semilla=3):
    rnd = random.Random(semilla)
    capa = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    import math
    for i in range(900):
        t = rnd.uniform(0, 2 * math.pi)
        x = cx + rx * math.cos(t) + rnd.gauss(0, rx * 0.04)
        y = cy + ry * math.sin(t) + rnd.gauss(0, ry * 0.06)
        r = rnd.choice([0.8, 1.2, 1.6, 2.4])
        d.ellipse((x - r, y - r, x + r, y + r), fill=ORO_CLARO + (rnd.randint(80, 230),))
    img.alpha_composite(capa.filter(ImageFilter.GaussianBlur(0.6)))
    img.alpha_composite(capa)


def foto_arco(ancho, alto):
    """La foto de Mabel recortada en arco con borde dorado."""
    foto = Image.open(FOTO).convert("RGB")
    foto = foto.crop((0, 0, foto.width, int(foto.width * alto / ancho)))
    foto = foto.resize((ancho, alto), Image.LANCZOS).convert("RGBA")
    m = Image.new("L", (ancho, alto), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle((0, 0, ancho, alto + ancho // 2), ancho // 2, fill=255)
    marco = Image.new("RGBA", (ancho + 16, alto + 16), (0, 0, 0, 0))
    dm = ImageDraw.Draw(marco)
    dm.rounded_rectangle((0, 0, ancho + 15, alto + 15 + ancho // 2), ancho // 2 + 8, fill=ORO + (255,))
    marco.paste(foto, (8, 8), m)
    return marco


def ajustar(d, txt, fuente, px, maximo):
    while px > 10 and d.textlength(txt, font=f(fuente, px)) > maximo:
        px -= 1
    return f(fuente, px)


def partir(d, txt, fu, maximo):
    lineas, actual = [], ""
    for p in txt.split():
        prueba = (actual + " " + p).strip()
        if d.textlength(prueba, font=fu) <= maximo or not actual:
            actual = prueba
        else:
            lineas.append(actual)
            actual = p
    return lineas + [actual]


def escribir(img, x, y, txt, fuente, px, color, maximo, centrado=False, interlineado=1.12):
    d = ImageDraw.Draw(img)
    fu = f(fuente, px)
    for linea in partir(d, txt, fu, maximo):
        xx = x + (maximo - d.textlength(linea, font=fu)) / 2 if centrado else x
        d.text((xx + 2, y + 3), linea, font=fu, fill=(0, 0, 0, 160))
        d.text((xx, y), linea, font=fu, fill=color)
        y += px * interlineado
    return y


def pastilla(img, x, y, txt, px, centrado_en=None):
    d = ImageDraw.Draw(img)
    fu = f(SANS_B, px)
    w = d.textlength(txt, font=fu) + px * 2.2
    if centrado_en is not None:
        x = centrado_en - w / 2
    d.rounded_rectangle((x, y, x + w, y + px * 1.9), px, fill=ORO)
    d.text((x + w / 2, y + px * 0.95), txt, font=fu, fill=OSCURO, anchor="mm")
    return y + px * 1.9


def tabla(img, x0, y0, x1, px):
    capa = Image.new("RGBA", img.size, (0, 0, 0, 0))
    alto = px * (1.5 + 1.38 * len(HORARIOS)) + px
    ImageDraw.Draw(capa).rounded_rectangle((x0, y0, x1, y0 + alto), 22, fill=(12, 8, 34, 210), outline=ORO + (255,), width=2)
    img.alpha_composite(capa)
    d = ImageDraw.Draw(img)
    ancho = x1 - x0
    c1, c2, c3 = x0 + ancho * 0.06, x0 + ancho * 0.60, x0 + ancho * 0.84
    y = y0 + px * 0.6
    d.text((c2, y), "MAÑANA", font=f(SANS_B, px * 0.78), fill=ORO_CLARO, anchor="ma")
    d.text((c3, y), "NOCHE", font=f(SANS_B, px * 0.78), fill=ORO_CLARO, anchor="ma")
    y += px * 1.4
    for pais, m, n in HORARIOS:
        col = ORO_CLARO if pais.startswith("CDMX") else BLANCO
        d.text((c1, y), pais, font=f(SANS_B if col == ORO_CLARO else SANS, px), fill=col)
        d.text((c2, y), m, font=f(SANS_B, px), fill=col, anchor="ma")
        d.text((c3, y), n, font=f(SANS_B, px), fill=col, anchor="ma")
        y += px * 1.38
    return y0 + alto


def boton(img, txt, y, px, w_max):
    d = ImageDraw.Draw(img)
    fu = ajustar(d, txt, SANS_B, px, w_max)
    w = d.textlength(txt, font=fu) + fu.size * 2.4
    x = (img.width - w) / 2
    d.rounded_rectangle((x, y, x + w, y + fu.size * 2.2), fu.size * 1.1, fill=ORO, outline=ORO_CLARO, width=3)
    d.text((img.width / 2, y + fu.size * 1.1), txt, font=fu, fill=OSCURO, anchor="mm")
    return y + fu.size * 2.2


def autora(img, cx, y, px, ancho):
    d = ImageDraw.Draw(img)
    for i, linea in enumerate(AUTORA):
        fu = ajustar(d, linea, SANS_B if i == 0 else SANS, px * (1.15 if i == 0 else 0.9), ancho)
        d.text((cx, y), linea, font=fu, fill=ORO_CLARO if i == 0 else BLANCO, anchor="ma")
        y += fu.size * 1.25
    return y


def arte(variante, uso, w, h):
    img = fondo(w, h)
    m = 70 if w >= 1080 else 50
    cuadrado, alto = h <= 1100, h >= 1900
    y = 60 if not cuadrado else 45
    y = pastilla(img, m, y, ETIQUETA, 30)
    y += 22
    if variante == "dolor":
        y = escribir(img, m, y, GANCHO, SANS_B, 40, BLANCO, w - 2 * m) + 6
    y = escribir(img, m, y, SUBTITULO, SANS_B, 30, ORO_CLARO, w - 2 * m) + 10
    y = escribir(img, m, y, TITULO, SANS_B, 74 if alto else (60 if cuadrado else 66), BLANCO, w - 2 * m, interlineado=1.08)
    y += 20 if not alto else 40
    # fila: foto (izquierda) + horarios (derecha); en 9:16 la foto va arriba y la tabla abajo
    if alto:
        fw = 560
        fh = int(fw * 1.2)
        fa = foto_arco(fw, fh)
        img.alpha_composite(fa, (int((w - fa.width) / 2), int(y)))
        y = autora(img, w / 2, y + fa.height + 14, 28, w - 2 * m) + 26
        y = tabla(img, m, y, w - m, 30) + 34
    else:
        fw = 380 if not cuadrado else 300
        fh = int(fw * (1.3 if not cuadrado else 1.15))
        fa = foto_arco(fw, fh)
        img.alpha_composite(fa, (m, int(y)))
        yt_fin = tabla(img, m + fw + 50, y + 10, w - m, 23 if cuadrado else 25)
        ya = autora(img, m + fa.width / 2, y + fa.height + 10, 20 if cuadrado else 22, fa.width + 40)
        y = max(yt_fin, ya) + (22 if cuadrado else 34)
    y = boton(img, CTA[uso], y, 32, w - 2 * m)
    ImageDraw.Draw(img).text((w / 2, y + 22), FIRMA, font=f(SANS_B, 30), fill=ORO_CLARO, anchor="ma")
    return img.convert("RGB")


def banner_web(w=1920, h=700):
    """Banner para www.mabradiante.com: texto a la izquierda, horarios al centro, foto a la derecha."""
    img = fondo(w, h, semilla=11)
    x0, ancho = 80, 700
    y = pastilla(img, x0, 60, ETIQUETA, 28) + 22
    y = escribir(img, x0, y, SUBTITULO, SANS_B, 28, ORO_CLARO, ancho) + 8
    y = escribir(img, x0, y, TITULO, SANS_B, 64, BLANCO, ancho, interlineado=1.06) + 26
    d = ImageDraw.Draw(img)
    fu = f(SANS_B, 30)
    wb = d.textlength(CTA["ads"], font=fu) + 70
    d.rounded_rectangle((x0, y, x0 + wb, y + 66), 33, fill=ORO, outline=ORO_CLARO, width=3)
    d.text((x0 + wb / 2, y + 33), CTA["ads"], font=fu, fill=OSCURO, anchor="mm")
    d.text((x0, y + 90), FIRMA, font=f(SANS_B, 28), fill=ORO_CLARO)
    tabla(img, 830, 150, 1390, 24)
    fw, fh = 380, 470
    fa = foto_arco(fw, fh)
    img.alpha_composite(fa, (1650 - fa.width // 2, 40))
    autora(img, 1650, 40 + fa.height + 12, 22, 470)
    return img.convert("RGB")


def video(png, mp4):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", png, "-vf",
                    "scale=2160:-1,zoompan=z='min(zoom+0.0006,1.06)':d=300:s=1080x1920:fps=30",
                    "-t", "10", "-c:v", "libx264", "-pix_fmt", "yuv420p", mp4], check=True)


if __name__ == "__main__":
    SALIDA.mkdir(exist_ok=True)
    for viejo in SALIDA.glob("*"):
        viejo.unlink()
    for variante in ("principal", "dolor"):
        for uso in ("organico", "ads"):
            for w, h in TAMANOS:
                p = SALIDA / f"{variante}_{uso}_{w}x{h}.png"
                arte(variante, uso, w, h).save(p, "PNG")
                if uso == "ads" and h == 1920:
                    video(str(p), str(p.with_suffix(".mp4")))
    banner_web().save(SALIDA / "web_banner_1920x700.png", "PNG")
    print(len(list(SALIDA.glob("*.png"))), "artes ·", len(list(SALIDA.glob("*.mp4"))), "videos")
