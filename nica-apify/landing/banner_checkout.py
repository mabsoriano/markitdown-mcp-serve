"""Banner de cabecera para el checkout de Hotmart (muestra). Uso: python3 landing/banner_checkout.py salida.jpg"""
import sys, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H = 1200, 420
SER = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SAN = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
CAFE, ORO, ORO2 = (90, 48, 5), (170, 100, 0), (255, 214, 90)
bg = Image.new("RGB", (W, H)); d = ImageDraw.Draw(bg)
for x in range(W):
    t = x / W; d.line([(x, 0), (x, H)], fill=(255, int(250 - 40 * t), int(222 - 120 * t)))
g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).ellipse((700, -150, 1300, 600), fill=230)
bg = Image.composite(Image.new("RGB", (W, H), (255, 252, 230)), bg, g.filter(ImageFilter.GaussianBlur(120)))
d = ImageDraw.Draw(bg); random.seed(3)
for _ in range(120):
    x, y, r = random.randint(0, W), random.randint(0, H), random.choice([1, 1, 2, 3])
    d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 240))
# Mabel en arco dorado
im = Image.open("reels/banco/fotos/mabel-brazos.png").convert("RGB").crop((60, 40, 708, 900))
aw, ah = 300, 400; im = im.resize((aw, int(im.height * aw / im.width)), Image.LANCZOS).crop((0, 0, aw, ah))
mk = Image.new("L", (aw, ah), 0); ImageDraw.Draw(mk).rounded_rectangle((0, 0, aw, ah + 200), 150, fill=255)
x0, y0 = W - aw - 70, 30
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(glow).rounded_rectangle((x0 - 18, y0 - 18, x0 + aw + 18, H + 200), 168, fill=(255, 200, 60, 150))
bg = Image.alpha_composite(bg.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(18))).convert("RGB")
ImageDraw.Draw(bg).rounded_rectangle((x0 - 7, y0 - 7, x0 + aw + 7, H + 200), 157, fill=ORO2)
bg.paste(im, (x0, y0), mk)
d = ImageDraw.Draw(bg)
d.text((48, 34), "BNQ Method™ · Mabel Soriano", font=ImageFont.truetype(SAN, 24), fill=ORO)
f = ImageFont.truetype(SER, 62)
d.text((46, 70), "Programa la Riqueza", font=f, fill=CAFE)
d.text((46, 136), "mientras Duermes", font=f, fill=ORO, stroke_width=2, stroke_fill=(255, 248, 220))
d.text((48, 214), "21 noches reprogramando tu subconsciente mientras duermes", font=ImageFont.truetype(SANR, 25), fill=CAFE)
# precio
d.rounded_rectangle((46, 262, 470, 330), 34, fill=ORO)
d.text((70, 274), "$500", font=ImageFont.truetype(SAN, 42), fill=(255, 250, 225))
d.text((190, 278), "+ impuestos", font=ImageFont.truetype(SANR, 22), fill=(255, 245, 210))
fa = ImageFont.truetype(SANR, 20); d.text((190, 302), "antes ", font=fa, fill=(255, 230, 180))
x0 = 190 + d.textlength("antes ", font=fa); d.text((x0, 302), "$1,200", font=fa, fill=(255, 230, 180))
d.line((x0, 315, x0 + d.textlength("$1,200", font=fa), 315), fill=(255, 230, 180), width=2)
f2 = ImageFont.truetype(SAN, 22)
d.text((48, 350), "REGALO: hipnosis COMPLETA en vivo · domingo 22 · 11 AM", font=f2, fill=CAFE)
d.text((48, 382), "Lo que no se ACTIVA, no CAMBIA. Y lo que no se REPITE, no se INSTALA.", font=ImageFont.truetype(SANR, 18), fill=ORO)
bg.save(sys.argv[1], quality=93)
