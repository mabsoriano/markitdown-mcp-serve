"""Portada diaria (800x800 PNG) para el audio de WhatsApp de @mabradiante.

Uso:  python3 portada.py "Nombre de la activación" [AAAA-MM-DD]
Sale en whatsapp/portadas/AAAA-MM-DD_<nombre>.png
"""
import math, random, re, sys, unicodedata
from datetime import date
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONDO, ORO, BLANCO, MORADO = (7, 7, 15), (201, 168, 76), (255, 255, 255), (91, 44, 160)
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
F = "/usr/share/fonts/truetype/dejavu/"
S, K = 800, 2          # tamaño final y supermuestreo (bordes suaves)
W = S * K


def fuente(nombre, px):
    return ImageFont.truetype(F + nombre, px * K)


def ancho(d, txt, f, esp=0):
    return d.textlength(txt, font=f) + esp * K * max(len(txt) - 1, 0)


def centrado(d, y, txt, f, color, esp=0):
    x = (W - ancho(d, txt, f, esp)) / 2
    if not esp:
        d.text((x, y), txt, font=f, fill=color)
        return
    for c in txt:
        d.text((x, y), c, font=f, fill=color)
        x += d.textlength(c, font=f) + esp * K


def partir(d, txt, f, maximo):
    lineas, actual = [], ""
    for p in txt.split():
        prueba = (actual + " " + p).strip()
        if ancho(d, prueba, f) <= maximo or not actual:
            actual = prueba
        else:
            lineas.append(actual)
            actual = p
    return lineas + [actual]


def portada(titulo, dia):
    rnd = random.Random(dia.toordinal())          # mismo día = mismas estrellas
    img = Image.new("RGB", (W, W), FONDO)

    # Resplandor morado al centro
    brillo = Image.new("RGB", (W, W), FONDO)
    g = ImageDraw.Draw(brillo)
    for r in range(int(W * 0.55), 0, -6 * K):
        t = 1 - r / (W * 0.55)
        c = tuple(int(FONDO[i] + (MORADO[i] - FONDO[i]) * t ** 2 * 0.55) for i in range(3))
        g.ellipse((W / 2 - r, W * 0.52 - r, W / 2 + r, W * 0.52 + r), fill=c)
    img = brillo.filter(ImageFilter.GaussianBlur(40 * K))
    d = ImageDraw.Draw(img, "RGBA")

    # Estrellas y partículas
    for _ in range(170):
        x, y = rnd.uniform(0, W), rnd.uniform(0, W)
        r = rnd.choice([0.6, 0.8, 1, 1, 1.4, 2]) * K
        col = ORO if rnd.random() < 0.3 else BLANCO
        d.ellipse((x - r, y - r, x + r, y + r), fill=col + (rnd.randint(70, 230),))
    for _ in range(6):                             # destellos de 4 puntas
        x, y, L = rnd.uniform(60, W - 60) * 1, rnd.uniform(60, W - 60), rnd.uniform(7, 13) * K
        if W * 0.2 < y < W * 0.8 and W * 0.15 < x < W * 0.85:
            continue
        d.line((x - L, y, x + L, y), fill=ORO + (200,), width=K)
        d.line((x, y - L, x, y + L), fill=ORO + (200,), width=K)

    # Anillo dorado y luna creciente
    R = W * 0.40
    d.ellipse((W / 2 - R, W * 0.52 - R, W / 2 + R, W * 0.52 + R), outline=ORO + (90,), width=K)
    R2 = R + 10 * K
    d.ellipse((W / 2 - R2, W * 0.52 - R2, W / 2 + R2, W * 0.52 + R2), outline=ORO + (35,), width=K)
    lx, ly, lr = W / 2, 92 * K, 26 * K
    d.ellipse((lx - lr, ly - lr, lx + lr, ly + lr), fill=ORO)
    d.ellipse((lx - lr + 13 * K, ly - lr - 6 * K, lx + lr + 13 * K, ly + lr - 6 * K), fill=FONDO)

    # Etiqueta
    centrado(d, 170 * K, "ACTIVACIÓN DEL DÍA", fuente("DejaVuSans.ttf", 15), ORO, esp=5)

    # Título: lo más grande que quepa en 3 líneas
    txt = titulo.strip().upper()
    for px in range(76, 30, -2):
        f = fuente("DejaVuSans-Bold.ttf", px)
        lineas = partir(d, txt, f, W * 0.72)
        if len(lineas) <= 3 and all(ancho(d, l, f) <= W * 0.72 for l in lineas):
            break
    alto = px * K * 1.18
    y = W * 0.50 - alto * len(lineas) / 2
    for l in lineas:
        centrado(d, y, l, f, BLANCO)
        y += alto

    # Separador con rombo
    yS = y + 26 * K
    d.line((W / 2 - 120 * K, yS, W / 2 - 14 * K, yS), fill=ORO, width=K)
    d.line((W / 2 + 14 * K, yS, W / 2 + 120 * K, yS), fill=ORO, width=K)
    r = 6 * K
    d.polygon([(W / 2, yS - r), (W / 2 + r, yS), (W / 2, yS + r), (W / 2 - r, yS)], fill=ORO)

    # Fecha y firma
    fecha = f"{dia.day} de {MESES[dia.month - 1]}, {dia.year}"
    centrado(d, yS + 22 * K, fecha, fuente("DejaVuSerif.ttf", 24), (235, 225, 200))
    centrado(d, W - 70 * K, "@mabradiante · Método BNQ™", fuente("DejaVuSans-Bold.ttf", 20), ORO)

    return img.resize((S, S), Image.LANCZOS)


def slug(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:40]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit('Uso: python3 portada.py "Nombre de la activación" [AAAA-MM-DD]')
    dia = date.fromisoformat(sys.argv[2]) if len(sys.argv) > 2 else date.today()
    sal = Path(__file__).parent / "portadas" / f"{dia.isoformat()}_{slug(sys.argv[1])}.png"
    sal.parent.mkdir(exist_ok=True)
    portada(sys.argv[1], dia).save(sal, "PNG")
    print(sal)
