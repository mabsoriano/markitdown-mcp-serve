"""Portada diaria (800x800 PNG) para el audio de WhatsApp de @mabradiante.

Usa la imagen base de Mabel (base-portada.jpg): cambia el título de arriba y
pone abajo el logo con "Las Fórmulas Cuánticas para Hackear tu Mente y la
Matrix · BNQ METHOD".

Uso:  python3 portada.py "Nombre de la activación" [AAAA-MM-DD]
Sale en whatsapp/portadas/AAAA-MM-DD_<nombre>.png
"""
import re, sys, unicodedata
from datetime import date
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

AQUI = Path(__file__).parent
BASE = AQUI / "base-portada.jpg"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
N = 1024                       # se trabaja al tamaño de la base y se reduce a 800
TOPE, PIE = 315, 700           # zona del título (0..TOPE) y del pie (PIE..N)
PIE_TEXTO = ["LAS FÓRMULAS CUÁNTICAS", "PARA HACKEAR TU", "MENTE Y LA MATRIX"]


def degradado_oro(w, h):
    g = Image.new("RGB", (1, h))
    paradas = [(0, (255, 244, 205)), (0.45, (232, 196, 110)), (0.7, (201, 168, 76)), (1, (140, 100, 35))]
    for y in range(h):
        t = y / max(h - 1, 1)
        for (a, ca), (b, cb) in zip(paradas, paradas[1:]):
            if a <= t <= b:
                k = (t - a) / (b - a)
                g.putpixel((0, y), tuple(int(ca[i] + (cb[i] - ca[i]) * k) for i in range(3)))
                break
    return g.resize((w, h))


def texto_oro(img, lineas, tamanos, y, interlineado=1.05):
    """Escribe líneas centradas en oro con sombra; devuelve la y final."""
    capa = Image.new("L", img.size, 0)
    d = ImageDraw.Draw(capa)
    for linea, px in zip(lineas, tamanos):
        f = ImageFont.truetype(SERIF, px)
        x = (N - d.textlength(linea, font=f)) / 2
        d.text((x, y), linea, font=f, fill=255)
        y += px * interlineado
    sombra = capa.filter(ImageFilter.GaussianBlur(6)).point(lambda v: min(255, v * 2))
    oscuro = Image.new("RGB", img.size, (25, 12, 0))
    img.paste(oscuro, (4, 6), sombra)
    borde = capa.filter(ImageFilter.MaxFilter(5))
    img.paste(Image.new("RGB", img.size, (70, 40, 5)), (0, 0), borde)
    img.paste(degradado_oro(N, N), (0, 0), capa)
    return y


def suavizar_franja(img, y0, y1, desde_arriba):
    """Cubre una franja con la misma imagen muy difuminada (brillo dorado)."""
    difusa = img.filter(ImageFilter.GaussianBlur(80))
    mascara = Image.new("L", img.size, 0)
    d = ImageDraw.Draw(mascara)
    transicion = 55
    for y in range(N):
        if desde_arriba:
            v = 255 if y < y1 - transicion else max(0, int(255 * (y1 - y) / transicion))
        else:
            v = 255 if y > y0 + transicion else max(0, int(255 * (y - y0) / transicion))
        d.line((0, y, N, y), fill=v)
    img.paste(difusa, (0, 0), mascara)


def partir(titulo, f, maximo):
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    lineas, actual = [], ""
    for p in titulo.split():
        prueba = (actual + " " + p).strip()
        if d.textlength(prueba, font=f) <= maximo or not actual:
            actual = prueba
        else:
            lineas.append(actual)
            actual = p
    return lineas + [actual]


def atomo(img, cx, cy, r):
    d = ImageDraw.Draw(img, "RGBA")
    oro = (232, 196, 110, 255)
    for ang in (0, 60, 120):
        orb = Image.new("RGBA", (r * 2 + 8, r * 2 + 8), (0, 0, 0, 0))
        ImageDraw.Draw(orb).ellipse((4, r * 0.62 + 4, r * 2 + 4, r * 1.38 + 4), outline=oro, width=3)
        orb = orb.rotate(ang, resample=Image.BICUBIC)
        img.paste(orb, (cx - r - 4, cy - r - 4), orb)
    d.ellipse((cx - r * 0.22, cy - r * 0.22, cx + r * 0.22, cy + r * 0.22), fill=(255, 236, 170, 255))


def portada(titulo):
    img = Image.open(BASE).convert("RGB")
    suavizar_franja(img, 0, TOPE, desde_arriba=True)
    suavizar_franja(img, PIE, N, desde_arriba=False)

    # Título: lo más grande que quepa en 3 líneas
    txt = titulo.strip().upper()
    for px in range(118, 40, -2):
        lineas = partir(txt, ImageFont.truetype(SERIF, px), N * 0.88)
        if len(lineas) <= 3 and px * 1.05 * len(lineas) <= TOPE - 40:
            break
    alto = px * 1.05 * len(lineas)
    texto_oro(img, lineas, [px] * len(lineas), (TOPE - 25 - alto) / 2 + 10)

    # Pie: frase del libro + logo + BNQ METHOD
    y = texto_oro(img, PIE_TEXTO, [48, 48, 48], PIE + 45, interlineado=1.0)
    atomo(img, N // 2, int(y + 30), 26)
    texto_oro(img, ["BNQ METHOD"], [32], y + 64)

    return img.resize((800, 800), Image.LANCZOS)


def slug(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:40]


def portada_real(titulo):
    """Portada con la FOTO REAL de Mabel y su estilo (espacio morado + dorado), segura para el
    recorte redondo de WhatsApp: título arriba, foto en arco al centro, @mabradiante abajo."""
    import math
    sys.path.insert(0, str(AQUI.parent / "live"))
    import artes_live as a
    from PIL import ImageDraw
    n, R = 1024, 512
    img = a.fondo(n, n, semilla=5)
    d = ImageDraw.Draw(img)
    def cabe(txt, px, y):
        while px > 24:
            fu = ImageFont.truetype(a.SANS_B, px)
            dy = max(abs(y - R), abs(y + px - R))
            if d.textlength(txt, font=fu) <= 2 * math.sqrt(max(R * R - dy * dy, 0)) * 0.86:
                return fu
            px -= 2
        return ImageFont.truetype(a.SANS_B, px)
    palabras, lineas, y = titulo.upper().split(), [], 150
    while palabras:   # llena cada renglón con lo que quepa en el círculo
        linea = palabras.pop(0)
        while palabras and cabe(linea + " " + palabras[0], 64, y).size >= 56:
            linea += " " + palabras.pop(0)
        lineas.append((linea, y))
        y += 70
    for linea, yy in lineas:
        fu = cabe(linea, 64, yy)
        d.text((R + 2, yy + 3), linea, font=fu, fill=(0, 0, 0), anchor="ma")
        d.text((R, yy), linea, font=fu, fill=a.ORO_CLARO if linea == lineas[-1][0] else a.BLANCO, anchor="ma")
    fa = a.foto_arco(330, 400)
    top = int(y + 15)
    img.alpha_composite(fa, (R - fa.width // 2, top))
    d = ImageDraw.Draw(img)
    d.text((R, top + fa.height + 12), "@mabradiante", font=ImageFont.truetype(a.SANS_B, 40), fill=a.ORO_CLARO, anchor="ma")
    return img.convert("RGB").resize((800, 800), Image.LANCZOS)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit('Uso: python3 portada.py "Nombre de la activación" [AAAA-MM-DD]')
    dia = date.fromisoformat(sys.argv[2]) if len(sys.argv) > 2 else date.today()
    sal = AQUI / "portadas" / f"{dia.isoformat()}_{slug(sys.argv[1])}.png"
    sal.parent.mkdir(exist_ok=True)
    portada_real(sys.argv[1]).save(sal, "PNG")
    print(sal)
