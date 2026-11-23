"""Carruseles luminosos (4:5) con foto real de Mabel. Uso: python3 carrusel.py"""
import random, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H = 1080, 1350
FOT = Path(__file__).parent / "banco" / "fotos"
SER = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SAN = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
CAFE, ORO, ORO2 = (90, 48, 5), (170, 100, 0), (255, 214, 90)

def fondo():
    bg = Image.new("RGB", (W, H)); d = ImageDraw.Draw(bg)
    for y in range(H):
        t = y / H; d.line([(0, y), (W, y)], fill=(255, int(246 - 46 * t), int(200 - 100 * t)))
    g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).ellipse((90, 160, 990, 1150), fill=210)
    bg = Image.composite(Image.new("RGB", (W, H), (255, 253, 232)), bg, g.filter(ImageFilter.GaussianBlur(170)))
    d = ImageDraw.Draw(bg); random.seed(7)
    for _ in range(150):
        x, y, r = random.randint(0, W), random.randint(0, H), random.choice([1, 2, 2, 3, 4])
        d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 238))
    return bg

def envolver(d, txt, f, ancho):
    out, cur = [], ""
    for w in txt.split():
        if d.textlength((cur + " " + w).strip(), font=f) > ancho and cur: out.append(cur); cur = w
        else: cur = (cur + " " + w).strip()
    return out + [cur]

def bloque(d, txt, f, y, color, ancho=900, inter=1.18, stroke=None):
    for ln in envolver(d, txt, f, ancho):
        w = d.textlength(ln, font=f)
        kw = dict(stroke_width=3, stroke_fill=stroke) if stroke else {}
        d.text(((W - w) / 2, y), ln, font=f, fill=color, **kw); y += int(f.size * inter)
    return y

def circulo(foto, r):
    im = Image.open(FOT / foto).convert("RGB"); s = min(im.size)
    im = im.crop(((im.width - s) // 2, 0, (im.width + s) // 2, s)).resize((r, r))
    m = Image.new("L", (r, r), 0); ImageDraw.Draw(m).ellipse((0, 0, r, r), fill=255); return im, m

def firma(bg, d, foto):
    im, m = circulo(foto, 110)
    d.ellipse((W // 2 - 61, H - 205, W // 2 + 61, H - 83), fill=ORO2); bg.paste(im, (W // 2 - 55, H - 199), m)
    t = "Mabel Soriano · BNQ Method™"; f = ImageFont.truetype(SAN, 28)
    d.text(((W - d.textlength(t, font=f)) / 2, H - 70), t, font=f, fill=CAFE)

def portada(foto, arriba, caja, abajo, out):
    im = Image.open(FOT / foto).convert("RGB")
    k = max(W / im.width, H / im.height); im = im.resize((int(im.width * k), int(im.height * k)))
    bg = im.crop(((im.width - W) // 2, 0, (im.width - W) // 2 + W, H))
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
    for y in range(H // 2, H):
        a = int(170 * (y - H // 2) / (H // 2)); od.line([(0, y), (W, y)], fill=(120, 70, 0, a))
    bg = Image.alpha_composite(bg.convert("RGBA"), ov).convert("RGB"); d = ImageDraw.Draw(bg)
    y = bloque(d, arriba, ImageFont.truetype(SAN, 66), 820, (255, 255, 255), stroke=(110, 60, 0))
    f = ImageFont.truetype(SAN, 72); lns = envolver(d, caja, f, 880); hh = len(lns) * 84 + 30
    d.rounded_rectangle((70, y + 8, W - 70, y + 8 + hh), 18, fill=ORO2)
    yy = y + 22
    for ln in lns:
        d.text(((W - d.textlength(ln, font=f)) / 2, yy), ln, font=f, fill=(60, 30, 0)); yy += 84
    if abajo: bloque(d, abajo, ImageFont.truetype(SANR, 30), y + hh + 30, (255, 255, 255))
    bg.save(out, quality=92)

def lamina(texto, out, foto, sub=None, num=None):
    bg = fondo(); d = ImageDraw.Draw(bg)
    if num: bloque(d, num, ImageFont.truetype(SER, 120), 150, ORO, stroke=(255, 250, 220))
    f = ImageFont.truetype(SER, 74 if len(texto) < 90 else 62)
    lns = envolver(d, texto, f, 900); alto = len(lns) * int(f.size * 1.18)
    y = bloque(d, texto, f, max(330, (H - alto) // 2 - 80), CAFE)
    if sub: bloque(d, sub, ImageFont.truetype(SANR, 38), y + 40, ORO)
    firma(bg, d, foto); bg.save(out, quality=92)

def cierre(texto, out, foto):
    bg = fondo(); d = ImageDraw.Draw(bg)
    y = bloque(d, texto, ImageFont.truetype(SER, 70), 330, CAFE)
    d.rounded_rectangle((90, y + 50, W - 90, y + 230), 30, fill=ORO)
    bloque(d, "Programa la Riqueza mientras Duermes", ImageFont.truetype(SAN, 40), y + 75, (255, 240, 170))
    bloque(d, "21 noches · link en mi perfil", ImageFont.truetype(SAN, 36), y + 150, (255, 255, 255))
    firma(bg, d, foto); bg.save(out, quality=92)
