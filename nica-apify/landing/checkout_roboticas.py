"""Piezas del checkout Hotmart · ACTIVACIONES ROBÓTICAS MILLONARIAS (comunidad). Uso: python3 landing/checkout_roboticas.py carpeta"""
import sys, random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
SER = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SAN = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
CAFE, ORO, ORO2, CREMA = (90, 48, 5), (170, 100, 0), (255, 214, 90), (255, 250, 225)
W = 1200
def F(p, s): return ImageFont.truetype(p, s)
def fondo(w, h, seed=5):
    bg = Image.new("RGB", (w, h)); d = ImageDraw.Draw(bg)
    for y in range(h):
        t = y / h; d.line([(0, y), (w, y)], fill=(255, int(248 - 40 * t), int(215 - 110 * t)))
    g = Image.new("L", (w, h), 0); ImageDraw.Draw(g).ellipse((w * .1, h * .05, w * .9, h * .95), fill=210)
    bg = Image.composite(Image.new("RGB", (w, h), (255, 253, 235)), bg, g.filter(ImageFilter.GaussianBlur(150)))
    d = ImageDraw.Draw(bg); random.seed(seed)
    for _ in range(int(w * h / 6000)):
        x, y, r = random.randint(0, w), random.randint(0, h), random.choice([1, 1, 2, 3])
        d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 240))
    return bg
def envolver(d, txt, f, ancho):
    out, cur = [], ""
    for w in txt.split():
        if d.textlength((cur + " " + w).strip(), font=f) > ancho and cur: out.append(cur); cur = w
        else: cur = (cur + " " + w).strip()
    return out + [cur]
def centro(d, txt, f, y, color, ancho=1080, inter=1.2, x0=0, w=W, stroke=None):
    for ln in envolver(d, txt, f, ancho):
        kw = dict(stroke_width=2, stroke_fill=stroke) if stroke else {}
        d.text((x0 + (w - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=color, **kw); y += int(f.size * inter)
    return y
def foto_arco(bg, x0, y0, aw, ah):
    im = Image.open("reels/banco/fotos/mabel-brazos.png").convert("RGB").crop((60, 40, 708, 1344))
    im = im.resize((aw, int(im.height * aw / im.width)), Image.LANCZOS).crop((0, 0, aw, ah))
    mk = Image.new("L", (aw, ah), 0); ImageDraw.Draw(mk).rounded_rectangle((0, 0, aw, ah + 300), aw // 2, fill=255)
    glow = Image.new("RGBA", bg.size, (0, 0, 0, 0)); ImageDraw.Draw(glow).rounded_rectangle((x0 - 22, y0 - 22, x0 + aw + 22, y0 + ah + 22), aw // 2 + 22, fill=(255, 200, 60, 160))
    bg2 = Image.alpha_composite(bg.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(20))).convert("RGB")
    ImageDraw.Draw(bg2).rounded_rectangle((x0 - 8, y0 - 8, x0 + aw + 8, y0 + ah + 8), aw // 2 + 8, fill=ORO2)
    bg2.paste(im, (x0, y0), mk); return bg2

# 1 HERO
H = 1000; bg = fondo(W, H); bg = foto_arco(bg, 770, 300, 370, 640); d = ImageDraw.Draw(bg)
centro(d, "BNQ Method™ · Mabel Soriano", F(SAN, 30), 40, ORO)

# 1 HERO
H = 1000; bg = fondo(W, H, 21); bg = foto_arco(bg, 770, 300, 370, 640); d = ImageDraw.Draw(bg)
centro(d, "BNQ Method™ · Mabel Soriano", F(SAN, 30), 40, ORO)
y = centro(d, "1 minuto antes de cobrar", F(SER, 78), 100, CAFE)
y = centro(d, "puede cambiar tu dinero", F(SER, 82), y, ORO, stroke=CREMA)
d.multiline_text((60, 330), "Cobras con miedo, pagas con culpa…\ny el dinero se te escapa.", font=F(SER, 46), fill=CAFE, spacing=14)
yy = 480
for t in ["Tu subconsciente lo aprendió.", "Tu memoria celular lo heredó.", "Tu energía lo repite", "cada vez que tocas dinero."]:
    d.text((60, yy), t, font=F(SANR, 36), fill=CAFE); yy += 50
d.rounded_rectangle((60, 720, 700, 830), 30, fill=ORO)
d.text((90, 735), "Activaciones Robóticas", font=F(SER, 44), fill=CREMA)
d.text((90, 782), "Millonarias · 10 audios de 1 min", font=F(SAN, 30), fill=(255, 238, 190))
d.text((60, 858), "El interruptor del dinero:", font=F(SANR, 30), fill=CAFE)
d.text((60, 898), "escúchalo, repítelo, instálalo.", font=F(SANR, 30), fill=CAFE)
d.text((60, 948), "Lo que no se ACTIVA, no CAMBIA. Y lo que no se REPITE, no se INSTALA.", font=F(SANR, 21), fill=ORO)
bg.save(OUT / "1-HERO.jpg", quality=92)

# 2 ESTO ES PARA TI SI
items = ["Te tiembla la voz cuando cobras lo que vales.", "Pagas y sientes que el dinero se va para siempre.",
         "Vendes con miedo a que te digan que no.", "No tienes tiempo para meditaciones largas.", "Quieres algo práctico para usar TODOS los días."]
H = 140 + len(items) * 92 + 50; bg = fondo(W, H, 23); d = ImageDraw.Draw(bg)
d.rounded_rectangle((30, 20, W - 30, H - 20), 34, fill=(255, 246, 214), outline=ORO2, width=6)
centro(d, "Esto es para ti si:", F(SER, 62), 50, CAFE)
y = 150
for t in items:
    d.ellipse((90, y + 4, 140, y + 54), fill=ORO); d.text((101, y + 4), "✓", font=F(SAN, 38), fill=CREMA)
    d.text((170, y + 8), t, font=F(SANR, 34), fill=CAFE); y += 92
bg.save(OUT / "2-ES-PARA-TI.jpg", quality=92)

# 3 BOTON
H = 300; bg = Image.new("RGB", (W, H), (255, 255, 255))
grad = Image.new("RGB", (W - 120, H - 60)); gd = ImageDraw.Draw(grad)
for y in range(H - 60):
    t = y / (H - 60); gd.line([(0, y), (W, y)], fill=(int(255 - 60 * t), int(222 - 90 * t), int(120 - 100 * t)))
mk = Image.new("L", grad.size, 0); ImageDraw.Draw(mk).rounded_rectangle((0, 0, grad.width - 1, grad.height - 1), 50, fill=255)
sh = Image.new("L", (W, H), 0); ImageDraw.Draw(sh).rounded_rectangle((66, 42, W - 54, H - 18), 50, fill=140)
bg.paste((200, 150, 60), mask=sh.filter(ImageFilter.GaussianBlur(10))); bg.paste(grad, (60, 30), mk); d = ImageDraw.Draw(bg)
d.rounded_rectangle((60, 30, W - 60, H - 30), 50, outline=(150, 90, 0), width=5)
centro(d, "¡QUIERO ACTIVAR", F(SAN, 64), 70, CAFE)
centro(d, "MI INTERRUPTOR DEL DINERO!", F(SAN, 58), 150, CAFE)
bg.save(OUT / "3-BOTON.jpg", quality=92)

# 4 QUE INCLUYE
inc = [("10 audios de activación de 1 minuto", "Para antes de cobrar, pagar, vender o abrir la app del banco."),
       ("Voz guiada con el Método BNQ™", "Subconsciente, memoria celular y energía, en simultáneo."),
       ("Úsalos donde estés", "En el celular, con audífonos, las veces que quieras."),
       ("Tus audios siempre en tu cuenta de Hotmart", "Escúchalos todos los días: lo que se repite, se instala."),
       ("REGALO: entrada a NeurohackersVIP", "Mi comunidad privada de activaciones y hackeos.")]
H = 170 + len(inc) * 130 + 300; bg = fondo(W, H, 29); d = ImageDraw.Draw(bg)
centro(d, "¿Qué incluye tu compra?", F(SER, 68), 50, CAFE)
y = 170
for a, b in inc:
    regalo = a.startswith("REGALO")
    d.rounded_rectangle((60, y, W - 60, y + 110), 26, fill=ORO2 if regalo else (255, 248, 222), outline=ORO, width=3)
    d.text((95, y + 16), a, font=F(SAN, 36), fill=CAFE)
    d.text((95, y + 64), b, font=F(SANR, 27), fill=CAFE); y += 130
d.text((60, y + 20), "Precio público $500 + impuestos", font=F(SANR, 36), fill=ORO)
d.text((60, y + 74), "Comunidad: 20% con el cupón COMUNIDAD", font=F(SAN, 44), fill=CAFE)
d.text((60, y + 140), "= $400 + impuestos", font=F(SAN, 54), fill=CAFE)
d.text((60, y + 220), "Garantía de 7 días de Hotmart · Compra segura", font=F(SAN, 30), fill=ORO)
bg.save(OUT / "4-QUE-INCLUYE.jpg", quality=92)
print("ok")
