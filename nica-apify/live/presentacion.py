"""Diapositivas del LIVE (1920x1080): fondo universo azul y morado, letras doradas y blancas.

Uso: python3 live/presentacion.py  -> live/presentacion/muestra_quien_soy.png
"""
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

AQUI = Path(__file__).resolve().parent
MARCA = AQUI.parent / "marca"
SALIDA = AQUI / "presentacion"
W, H = 1920, 1080

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
ORO = (232, 190, 92)
ORO_CLARO = (250, 222, 150)
BLANCO = (255, 255, 255)


def f(ruta, px):
    return ImageFont.truetype(ruta, px)


def universo(semilla=7):
    """Degradado azul noche a morado, nebulosas suaves y estrellas."""
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)], fill=(int(12 + 22 * t), int(10 + 4 * t), int(38 + 30 * t)))
    neb = Image.new("RGB", (W, H), (0, 0, 0))
    nd = ImageDraw.Draw(neb)
    for (cx, cy, r, color) in [(1450, 300, 420, (90, 40, 150)), (1650, 800, 380, (30, 60, 150)),
                               (300, 950, 300, (70, 30, 120)), (1200, 650, 260, (140, 100, 40))]:
        nd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    neb = neb.filter(ImageFilter.GaussianBlur(160))
    img = Image.blend(img, Image.composite(neb, img, Image.new("L", (W, H), 255)), 0.55)
    d = ImageDraw.Draw(img)
    rnd = random.Random(semilla)
    for _ in range(420):
        x, y, b = rnd.randrange(W), rnd.randrange(H), rnd.randrange(140, 255)
        r = rnd.choice([1, 1, 1, 2])
        d.ellipse([x - r, y - r, x + r, y + r], fill=(b, b, min(255, b + 20)))
    return img


def foto_derecha(img, ancho=760):
    """Foto real de Mabel recortada con su máscara, pegada abajo a la derecha con brillo dorado."""
    foto = Image.open(MARCA / "mabel-foto.jpg").convert("RGB")
    mascara = Image.open(MARCA / "mabel-mascara.png").convert("L")
    alto = int(foto.height * ancho / foto.width)
    foto = foto.resize((ancho, alto), Image.LANCZOS)
    mascara = mascara.resize((ancho, alto), Image.LANCZOS).filter(ImageFilter.GaussianBlur(3))
    x, y = W - ancho - 40, H - alto + 260
    brillo = Image.new("L", (W, H), 0)
    ImageDraw.Draw(brillo).ellipse([x + 80, y + 120, x + ancho - 80, y + 900], fill=255)
    brillo = brillo.filter(ImageFilter.GaussianBlur(120))
    img.paste(Image.new("RGB", (W, H), (200, 150, 60)), (0, 0), brillo.point(lambda v: v * 0.55))
    img.paste(foto, (x, y), mascara)
    return img


def linea_oro(d, x, y, largo):
    d.line([(x, y), (x + largo, y)], fill=ORO, width=3)
    d.ellipse([x + largo - 6, y - 6, x + largo + 6, y + 6], fill=ORO)


def pie(d):
    d.text((90, H - 80), "@mabradiante · Método BNQ™", font=f(SANS, 30), fill=ORO)


def quien_soy():
    img = foto_derecha(universo())
    d = ImageDraw.Draw(img)
    d.text((90, 90), "QUIÉN TE VA A GUIAR HOY", font=f(SANS, 34), fill=ORO)
    d.text((90, 140), "Mabel Soriano", font=f(SERIF, 104), fill=ORO_CLARO)
    linea_oro(d, 92, 275, 520)
    puntos = [
        ("Terapeuta cuántica", "y activadora de Kundalini"),
        ("Creadora del Método BNQ™", "Bio Neuro Quantum"),
        ("Metodología CEI™", "registrada ante INDAUTOR"),
        ("Autora del libro", "Las Fórmulas Cuánticas para Hackear tu Mente y la Matrix"),
        ("+5 años", "activando consciencias"),
    ]
    y = 320
    for titulo, detalle in puntos:
        d.ellipse([92, y + 16, 112, y + 36], fill=ORO)
        d.text((140, y), titulo, font=f(SANS, 44), fill=BLANCO)
        d.text((140, y + 56), detalle, font=f(SANS_REG, 30), fill=ORO_CLARO)
        y += 128
    pie(d)
    return img


if __name__ == "__main__":
    SALIDA.mkdir(exist_ok=True)
    quien_soy().save(SALIDA / "muestra_quien_soy.png")
    print(SALIDA / "muestra_quien_soy.png")
