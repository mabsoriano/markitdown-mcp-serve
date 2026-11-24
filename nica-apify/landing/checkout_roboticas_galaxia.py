"""Checkout Robóticas · LÍNEA DE MABEL: universo morado/azul + dorado + su foto real (como sus artes de Grok)."""
import sys, random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
SER = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
B = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"; SB = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
W = 1200; ORO = (255, 205, 90); BLANCO = (255, 255, 255)
def F(p, s): return ImageFont.truetype(p, s)
def galaxia(w, h, seed=3):
    random.seed(seed)
    bg = Image.new("RGB", (w, h)); d = ImageDraw.Draw(bg)
    for y in range(h):
        t = y / h; d.line([(0, y), (w, y)], fill=(int(48 + 20 * t), int(24 + 10 * t), int(92 + 30 * (1 - t))))
    neb = Image.new("RGB", (w, h), (0, 0, 0)); nd = ImageDraw.Draw(neb)
    for _ in range(7):
        x, y, r = random.randint(0, w), random.randint(0, h), random.randint(180, 420)
        col = random.choice([(150, 70, 200), (70, 90, 220), (210, 90, 180), (255, 170, 60)])
        nd.ellipse((x - r, y - r, x + r, y + r), fill=col)
    bg = Image.blend(bg, neb.filter(ImageFilter.GaussianBlur(120)), 0.45)
    d = ImageDraw.Draw(bg)
    for _ in range(int(w * h / 7000)):
        x, y = random.randint(0, w), random.randint(0, h); r = random.choice([1, 1, 1, 2, 2, 3])
        d.ellipse((x - r, y - r, x + r, y + r), fill=random.choice([(255, 255, 255), (255, 215, 120), (255, 230, 170)]))
    return bg
def oro_txt(bg, xy, t, f):
    d = ImageDraw.Draw(bg); m = Image.new("L", bg.size, 0); ImageDraw.Draw(m).text(xy, t, font=f, fill=255)
    bg.paste((255, 170, 40), (0, 0), m.filter(ImageFilter.GaussianBlur(9)).point(lambda v: int(v * .8)))
    bb = d.textbbox(xy, t, font=f); g = Image.new("RGB", bg.size); gd = ImageDraw.Draw(g)
    for y in range(bb[1], bb[3] + 1):
        k = (y - bb[1]) / max(1, bb[3] - bb[1]); gd.line([(bb[0], y), (bb[2], y)], fill=(255, int(240 - 70 * k), int(170 - 120 * k)))
    bg.paste(g, (0, 0), m)
def centro_oro(bg, t, f, y):
    d = ImageDraw.Draw(bg); oro_txt(bg, ((W - d.textlength(t, font=f)) / 2, y), t, f)
def centro(d, t, f, y, col=BLANCO):
    d.text(((W - d.textlength(t, font=f)) / 2, y), t, font=f, fill=col)
def atomo(d, cx, cy, r, col=ORO):
    for a in (0, 60, 120):
        import math
        bb = (cx - r, cy - r * .38, cx + r, cy + r * .38)
        im = Image.new("L", (2 * r + 4, 2 * r + 4), 0); ImageDraw.Draw(im).ellipse((2, r - r * .38 + 2, 2 * r + 2, r + r * .38 + 2), outline=255, width=3)
        im = im.rotate(a); d._image.paste(col, (cx - r - 2, cy - r - 2), im)
    d.ellipse((cx - 6, cy - 6, cx + 6, cy + 6), fill=col)
def foto(bg, x0, y0, aw, ah):
    im = Image.open("reels/banco/fotos/mabel-brazos.png").convert("RGB").crop((60, 40, 708, 1344))
    im = im.resize((aw, int(im.height * aw / im.width)), Image.LANCZOS).crop((0, 0, aw, ah))
    mk = Image.new("L", (aw, ah), 0); ImageDraw.Draw(mk).rounded_rectangle((0, 0, aw, ah + 300), aw // 2, fill=255)
    g = Image.new("L", bg.size, 0); ImageDraw.Draw(g).rounded_rectangle((x0 - 26, y0 - 26, x0 + aw + 26, y0 + ah + 26), aw // 2 + 26, fill=255)
    bg.paste((255, 190, 70), (0, 0), g.filter(ImageFilter.GaussianBlur(24)))
    ImageDraw.Draw(bg).rounded_rectangle((x0 - 6, y0 - 6, x0 + aw + 6, y0 + ah + 6), aw // 2 + 6, fill=ORO)
    bg.paste(im, (x0, y0), mk)
def caja(d, box, gold=False):
    d.rounded_rectangle(box, 26, fill=(255, 205, 90) if gold else (40, 22, 80), outline=ORO, width=3)

# 1 HERO
H = 1000; bg = galaxia(W, H, 4); foto(bg, 770, 300, 370, 640); d = ImageDraw.Draw(bg)
atomo(d, 395, 62, 26); d.text((435, 42), "BNQ Method™ · Mabel Soriano", font=F(SB, 30), fill=BLANCO)
centro_oro(bg, "Activaciones Robóticas", F(SER, 74), 100); centro_oro(bg, "Millonarias", F(SER, 92), 190)
d = ImageDraw.Draw(bg)
d.multiline_text((60, 330), "1 minuto antes de cobrar\npuede cambiar tu dinero.", font=F(SER, 44), fill=ORO, spacing=12)
yy = 470
for t in ["Tu subconsciente lo aprendió.", "Tu memoria celular lo heredó.", "Tu energía lo repite", "cada vez que tocas dinero."]:
    d.text((60, yy), t, font=F(SB, 34), fill=BLANCO); yy += 48
caja(d, (60, 700, 700, 800), gold=True)
d.text((90, 712), "10 audios de 1 minuto", font=F(B, 40), fill=(60, 30, 90))
d.text((90, 760), "el interruptor del dinero", font=F(SB, 28), fill=(60, 30, 90))
d.text((60, 840), "Escúchalo, repítelo, instálalo.", font=F(SB, 32), fill=BLANCO)
d.text((60, 900), "Lo que no se ACTIVA, no CAMBIA.", font=F(SB, 26), fill=ORO)
d.text((60, 936), "Y lo que no se REPITE, no se INSTALA.", font=F(SB, 26), fill=ORO)
bg.save(OUT / "1-HERO.jpg", quality=92)

# 2 ES PARA TI
items = ["Te tiembla la voz cuando cobras lo que vales.", "Pagas y sientes que el dinero se va para siempre.",
         "Vendes con miedo a que te digan que no.", "No tienes tiempo para meditaciones largas.", "Quieres algo práctico para usar TODOS los días."]
H = 150 + len(items) * 92 + 50; bg = galaxia(W, H, 7); d = ImageDraw.Draw(bg)
d.rounded_rectangle((30, 20, W - 30, H - 20), 34, outline=ORO, width=5)
centro_oro(bg, "Esto es para ti si:", F(SER, 60), 45); d = ImageDraw.Draw(bg); y = 155
for t in items:
    d.ellipse((90, y + 4, 140, y + 54), fill=ORO); d.text((102, y + 6), "✓", font=F(B, 36), fill=(60, 30, 90))
    d.text((170, y + 10), t, font=F(SB, 34), fill=BLANCO); y += 92
bg.save(OUT / "2-ES-PARA-TI.jpg", quality=92)

# 3 BOTON
H = 300; bg = galaxia(W, H, 9); g = Image.new("RGB", (W - 120, H - 60)); gd = ImageDraw.Draw(g)
for y in range(H - 60):
    t = y / (H - 60); gd.line([(0, y), (W, y)], fill=(255, int(225 - 70 * t), int(120 - 90 * t)))
m = Image.new("L", g.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, g.width - 1, g.height - 1), 50, fill=255)
gl = Image.new("L", (W, H), 0); ImageDraw.Draw(gl).rounded_rectangle((50, 20, W - 50, H - 20), 56, fill=255)
bg.paste((255, 170, 60), (0, 0), gl.filter(ImageFilter.GaussianBlur(16))); bg.paste(g, (60, 30), m); d = ImageDraw.Draw(bg)
centro(d, "¡QUIERO ACTIVAR", F(B, 62), 70, (60, 30, 90)); centro(d, "MI INTERRUPTOR DEL DINERO!", F(B, 56), 148, (60, 30, 90))
bg.save(OUT / "3-BOTON.jpg", quality=92)

# 4 QUE INCLUYE
inc = [("10 audios de activación de 1 minuto", "Para antes de cobrar, pagar, vender o abrir la app del banco."),
       ("Método BNQ™ en simultáneo", "Subconsciente, memoria celular y energía al mismo tiempo."),
       ("Úsalos donde estés", "En el celular, con audífonos, las veces que quieras."),
       ("Tus audios siempre en tu cuenta de Hotmart", "Escúchalos todos los días: lo que se repite, se instala."),
       ("REGALO: entrada a NeurohackersVIP", "Mi comunidad privada de activaciones y hackeos.")]
H = 170 + len(inc) * 130 + 300; bg = galaxia(W, H, 11)
centro_oro(bg, "¿Qué incluye tu compra?", F(SER, 64), 50); d = ImageDraw.Draw(bg); y = 170
for a, b in inc:
    gold = a.startswith("REGALO"); caja(d, (60, y, W - 60, y + 110), gold)
    c1 = (60, 30, 90) if gold else ORO; c2 = (60, 30, 90) if gold else BLANCO
    d.text((95, y + 16), a, font=F(B, 34), fill=c1); d.text((95, y + 64), b, font=F(SB, 26), fill=c2); y += 130
d.text((60, y + 20), "Precio público $500 + impuestos", font=F(SB, 34), fill=BLANCO)
d.text((60, y + 74), "Comunidad: 20% con el cupón COMUNIDAD", font=F(B, 42), fill=ORO)
oro_txt(bg, (60, y + 134), "= $400 + impuestos", F(B, 60)); d = ImageDraw.Draw(bg)
d.text((60, y + 225), "Garantía de 7 días de Hotmart · Compra segura", font=F(SB, 28), fill=BLANCO)
bg.save(OUT / "4-QUE-INCLUYE.jpg", quality=92)
print("ok")
