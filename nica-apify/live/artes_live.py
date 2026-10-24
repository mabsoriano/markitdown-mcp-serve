"""Artes del LIVE (orgánico y anuncios) con la imagen base de Mabel.

Uso:  python3 artes_live.py
Sale en live/artes/<variante>_<uso>_<ancho>x<alto>.png y, para TikTok Ads,
un video de 10 s (zoom suave) a partir de cada arte vertical de anuncio.
"""
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

AQUI = Path(__file__).parent
BASE = AQUI.parent / "whatsapp" / "base-portada.jpg"
SALIDA = AQUI / "artes"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
ORO, ORO_CLARO, OSCURO = (201, 168, 76), (255, 236, 170), (20, 11, 3)

ETIQUETA = "LIVE GRATIS · ACTIVACIÓN EN TIEMPO REAL"
TITULO = ["HIPNOSIS PARA", "HACKEAR BLOQUEOS", "CON EL DINERO"]
GANCHO = "¿EL DINERO LLEGA Y SE VA?"
FECHA = "MARTES 27 DE OCTUBRE · LIVE EN TIKTOK"
HORARIOS = [  # (país, sesión mañana, sesión noche)
    ("CDMX (México)", "10:00 AM", "7:00 PM"),
    ("Pacific Time", "9:00 AM", "6:00 PM"),
    ("Eastern Time", "12:00 PM", "9:00 PM"),
    ("Colombia", "11:00 AM", "8:00 PM"),
    ("Venezuela", "12:00 PM", "9:00 PM"),
    ("Argentina", "1:00 PM", "10:00 PM"),
    ("España", "5:00 PM", "—"),
]
CTA = {"organico": "ÚNETE GRATIS · LINK EN MI PERFIL", "ads": "REGÍSTRATE GRATIS"}
FIRMA = "@mabradiante · Método BNQ™"
TAMANOS = [(1080, 1350), (1080, 1920), (1080, 1080)]


def f(ruta, px):
    return ImageFont.truetype(ruta, int(px))


def cubrir(img, w, h):
    e = max(w / img.width, h / img.height)
    img = img.resize((int(img.width * e) + 1, int(img.height * e) + 1), Image.LANCZOS)
    x, y = (img.width - w) // 2, (img.height - h) // 2
    return img.crop((x, y, x + w, y + h))


def oscurecer(img, y0, y1, desde_arriba, fuerza=235):
    capa = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    for y in range(y0, y1):
        t = (y - y0) / max(y1 - y0, 1)
        a = int(fuerza * ((1 - t) if desde_arriba else t))
        d.line((0, y, img.width, y), fill=OSCURO + (a,))
    return Image.alpha_composite(img, capa)


def ajustar(d, txt, fuente, px, maximo):
    while px > 10 and d.textlength(txt, font=f(fuente, px)) > maximo:
        px -= 2
    return f(fuente, px)


def texto(img, txt, fuente, px, y, color=ORO_CLARO, sombra=True, maximo=None):
    d = ImageDraw.Draw(img)
    fu = ajustar(d, txt, fuente, px, maximo or img.width * 0.9)
    x = (img.width - d.textlength(txt, font=fu)) / 2
    if sombra:
        s = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ImageDraw.Draw(s).text((x + 3, y + 4), txt, font=fu, fill=(0, 0, 0, 200))
        img.alpha_composite(s.filter(ImageFilter.GaussianBlur(5)))
        d = ImageDraw.Draw(img)
    d.text((x, y), txt, font=fu, fill=color, stroke_width=max(1, fu.size // 40), stroke_fill=(70, 40, 5))
    return y + fu.size * 1.12


def panel(img, caja, radio=28):
    capa = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    d.rounded_rectangle(caja, radio, fill=(12, 6, 2, 205), outline=ORO + (255,), width=3)
    img.alpha_composite(capa)


def tabla(img, x0, y0, x1, px):
    d = ImageDraw.Draw(img)
    ancho = x1 - x0
    c1, c2, c3 = x0 + ancho * 0.05, x0 + ancho * 0.56, x0 + ancho * 0.80
    fb, fn = f(SANS_B, px), f(SANS, px)
    d.text((c2, y0), "MAÑANA", font=f(SANS_B, px * 0.8), fill=ORO, anchor="ma")
    d.text((c3, y0), "NOCHE", font=f(SANS_B, px * 0.8), fill=ORO, anchor="ma")
    y = y0 + px * 1.4
    for pais, m, n in HORARIOS:
        destacado = pais.startswith("CDMX")
        col = ORO_CLARO if destacado else (245, 240, 230)
        d.text((c1, y), pais, font=fb if destacado else fn, fill=col)
        d.text((c2, y), m, font=fb, fill=col, anchor="ma")
        d.text((c3, y), n, font=fb, fill=col, anchor="ma")
        y += px * 1.35
    return y


def boton(img, txt, y, px):
    d = ImageDraw.Draw(img)
    fu = ajustar(d, txt, SANS_B, px, img.width * 0.78)
    w = d.textlength(txt, font=fu) + px * 2
    x0 = (img.width - w) / 2
    d.rounded_rectangle((x0, y, x0 + w, y + fu.size * 2.1), fu.size, fill=ORO, outline=ORO_CLARO, width=3)
    d.text((img.width / 2, y + fu.size * 1.05), txt, font=fu, fill=OSCURO, anchor="mm")
    return y + fu.size * 2.1


def base_limpia():
    """La imagen base sin el título ni el pie viejos (mismo método que las portadas)."""
    sys.path.insert(0, str(BASE.parent))
    import portada
    img = Image.open(BASE).convert("RGB")
    portada.suavizar_franja(img, 0, portada.TOPE, desde_arriba=True)
    portada.suavizar_franja(img, portada.PIE, portada.N, desde_arriba=False)
    return img


def fondo(w, h, difuso=False):
    img = cubrir(base_limpia(), w, h)
    if difuso:
        img = img.filter(ImageFilter.GaussianBlur(28))
    return img.convert("RGBA")


def arte(variante, uso, w, h):
    k = w / 1080            # escala de letra
    cuadrado = h <= 1100
    img = fondo(w, h, difuso=(variante == "horarios"))
    img = oscurecer(img, 0, int(h * 0.42), True)
    img = oscurecer(img, int(h * 0.45), h, False, 250)
    y = h * 0.035
    y = texto(img, ETIQUETA, SANS_B, 34 * k, y, color=ORO, sombra=False)
    if variante == "dolor":
        y = texto(img, GANCHO, SERIF, 64 * k, y + 8, color=(255, 255, 255))
    tam = 58 if cuadrado else (68 if variante == "dolor" else 78)
    for linea in TITULO:
        y = texto(img, linea, SERIF, tam * k, y)
    y = texto(img, FECHA, SANS_B, 32 * k, y + 6, color=(255, 255, 255))
    px_tabla = (25 if cuadrado else 30) * k
    alto_tabla = px_tabla * (1.4 + 1.35 * len(HORARIOS)) + 30 * k
    pie = 60 * k + px_tabla * 2.6
    y_tabla = h - pie - alto_tabla - 20 * k
    if variante == "foto" and not cuadrado:
        y_tabla = max(y_tabla, h * 0.55)
    panel(img, (w * 0.06, y_tabla, w * 0.94, y_tabla + alto_tabla))
    tabla(img, w * 0.06, y_tabla + 18 * k, w * 0.94, px_tabla)
    yb = y_tabla + alto_tabla + 18 * k
    yb = boton(img, CTA[uso], yb, 30 * k)
    texto(img, FIRMA, SANS_B, 26 * k, yb + 10 * k, color=ORO, sombra=False)
    return img.convert("RGB")


def video(png, mp4):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", png, "-vf",
                    "scale=2160:-1,zoompan=z='min(zoom+0.0006,1.06)':d=300:s=1080x1920:fps=30",
                    "-t", "10", "-c:v", "libx264", "-pix_fmt", "yuv420p", mp4], check=True)


if __name__ == "__main__":
    SALIDA.mkdir(exist_ok=True)
    for variante in ("foto", "horarios", "dolor"):
        for uso in ("organico", "ads"):
            for w, h in TAMANOS:
                p = SALIDA / f"{variante}_{uso}_{w}x{h}.png"
                arte(variante, uso, w, h).save(p, "PNG")
                if uso == "ads" and h == 1920:
                    video(str(p), str(p.with_suffix(".mp4")))
    print(len(list(SALIDA.glob("*.png"))), "artes ·", len(list(SALIDA.glob("*.mp4"))), "videos")


def banner_web(w=1920, h=700):
    """Banner horizontal para www.mabradiante.com: texto a la izquierda, horarios al centro, foto a la derecha."""
    img = Image.new("RGBA", (w, h), (14, 8, 3, 255))
    foto = base_limpia().resize((h, h), Image.LANCZOS).convert("RGBA")
    mascara = Image.new("L", (h, h), 255)
    d = ImageDraw.Draw(mascara)
    for x in range(int(h * 0.35)):
        d.line((x, 0, x, h), fill=int(255 * x / (h * 0.35)))
    img.paste(foto, (w - h, 0), mascara)
    d = ImageDraw.Draw(img)
    x0, ancho_txt = 70, 620
    y = 60
    for txt, fuente, px, color in [(ETIQUETA, SANS_B, 26, ORO)] + [(l, SERIF, 64, ORO_CLARO) for l in TITULO] + [
            ("MARTES 27 DE OCTUBRE", SANS_B, 30, (255, 255, 255)), ("LIVE EN TIKTOK · 10 AM y 7 PM CDMX", SANS_B, 26, ORO)]:
        fu = ajustar(d, txt, fuente, px, ancho_txt)
        d.text((x0 + 2, y + 3), txt, font=fu, fill=(0, 0, 0))
        d.text((x0, y), txt, font=fu, fill=color)
        y += fu.size * 1.18
    fu = f(SANS_B, 30)
    wb = d.textlength(CTA["ads"], font=fu) + 60
    d.rounded_rectangle((x0, y + 20, x0 + wb, y + 20 + 66), 33, fill=ORO, outline=ORO_CLARO, width=3)
    d.text((x0 + wb / 2, y + 53), CTA["ads"], font=fu, fill=OSCURO, anchor="mm")
    d.text((x0, y + 105), FIRMA, font=f(SANS_B, 22), fill=ORO)
    tx0, tx1 = 735, 1335
    alto = 24 * (1.4 + 1.35 * len(HORARIOS)) + 36
    ty = (h - alto) / 2
    panel(img, (tx0, ty, tx1, ty + alto))
    tabla(img, tx0, ty + 18, tx1, 24)
    return img.convert("RGB")


if __name__ == "__main__":
    banner_web().save(SALIDA / "web_banner_1920x700.png", "PNG")
    print("banners web listos")
