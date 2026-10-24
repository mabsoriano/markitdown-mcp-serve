"""Portada de Hotmart del pack "Las 5 Hipnosis que Hackean tu Matrix" (600x600 JPG).

Híbrido aprobado por Mabel: fondo dorado + su foto real a la derecha, con todos los textos del
diseño de los 5 círculos, en letras negras para que se lean.
Uso:  python3 portada_pack.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

AQUI = Path(__file__).parent
MARCA = AQUI.parent / "marca"
BASE = AQUI.parent / "whatsapp" / "base-portada.jpg"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
NEGRO, CAFE, ORO, CREMA = (20, 12, 4), (95, 62, 10), (214, 168, 70), (255, 240, 205)
N = 1200

TEMAS = ["DINERO", "RELACIONES", "ANSIEDAD", "BURNOUT", "PROPÓSITO Y ÉXITO"]


def f(px):
    return ImageFont.truetype(SANS_B, int(px))


def fondo():
    """Fondo dorado de la línea (nubes, brillo), difuminado y aclarado a la izquierda para el texto."""
    img = Image.open(BASE).convert("RGB").resize((N, N), Image.LANCZOS).filter(ImageFilter.GaussianBlur(70))
    capa = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    for x in range(N):
        a = int(215 * max(0, 1 - x / (N * 0.72)) ** 0.8)
        d.line((x, 0, x, N), fill=CREMA + (a,))
    return Image.alpha_composite(img.convert("RGBA"), capa)


def mabel(img):
    foto = Image.open(MARCA / "mabel-foto.jpg").convert("RGB")
    mascara = Image.open(MARCA / "mabel-mascara.png").convert("L")
    mascara = mascara.point(lambda v: 255 if v > 140 else int(v * 1.6)).filter(ImageFilter.GaussianBlur(1.5))
    alto = 1350
    esc = alto / foto.height
    foto = foto.resize((int(foto.width * esc), alto), Image.LANCZOS)
    mascara = mascara.resize(foto.size, Image.LANCZOS)
    x, y = N - foto.width + 190, N - alto + 330
    halo = Image.new("L", (N, N), 0)
    halo.paste(mascara, (x, y))
    halo = halo.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(35))
    brillo = Image.new("RGBA", (N, N), (255, 220, 140, 0))
    brillo.putalpha(halo.point(lambda v: int(v * 0.8)))
    img.alpha_composite(brillo)
    persona = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    persona.paste(foto.convert("RGBA"), (x, y), mascara)
    img.alpha_composite(persona)


def texto(d, xy, txt, px, color, ancla="la"):
    d.text((xy[0] + 2, xy[1] + 2), txt, font=f(px), fill=CREMA, anchor=ancla)
    d.text(xy, txt, font=f(px), fill=color, anchor=ancla)


def portada():
    img = fondo()
    mabel(img)
    d = ImageDraw.Draw(img)
    x = 60
    texto(d, (x, 48), "MÉTODO BNQ™ · BIO NEURO QUANTUM", 30, NEGRO)
    texto(d, (x, 100), "LAS 5 HIPNOSIS", 104, NEGRO)
    texto(d, (x, 214), "QUE HACKEAN", 84, NEGRO)
    texto(d, (x, 306), "TU MATRIX", 118, NEGRO)
    y = 470
    for i, tema in enumerate(TEMAS, 1):
        r = 40
        d.ellipse((x, y, x + 2 * r, y + 2 * r), fill=NEGRO, outline=ORO, width=5)
        d.text((x + r, y + r), str(i), font=f(46), fill=ORO, anchor="mm")
        texto(d, (x + 2 * r + 24, y + r), tema, 44, NEGRO, "lm")
        y += 100
    y += 10
    fu = f(38)
    txt = "5 AUDIOS DE AUTOHIPNOSIS"
    w = d.textlength(txt, font=fu) + 70
    d.rounded_rectangle((x, y, x + w, y + 76), 38, fill=NEGRO, outline=ORO, width=4)
    d.text((x + w / 2, y + 38), txt, font=fu, fill=ORO, anchor="mm")
    texto(d, (x, y + 100), "Con la voz de Mabel Soriano", 36, NEGRO)
    texto(d, (x, y + 150), "@mabradiante", 34, NEGRO)
    return img.convert("RGB")


if __name__ == "__main__":
    img = portada()
    img.resize((600, 600), Image.LANCZOS).save(AQUI / "portada-hotmart-5-hipnosis-600x600.jpg", quality=92)
    img.save(AQUI / "portada-hotmart-5-hipnosis-1200x1200.jpg", quality=92)
    print("listo")
