"""Arte LIVE 25-nov (Hackeo Simultáneo), luminosa, sin precio. 4:5 y 9:16."""
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
FOTO = "/home/user/markitdown-mcp-serve/nica-apify/reels/banco/fotos/mabel-brazos.png"
SER = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SAN = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
CAFE, ORO, ORO2, CREMA, ROJO = (90, 48, 5), (170, 100, 0), (255, 214, 90), (255, 250, 225), (200, 40, 30)
def F(p, s): return ImageFont.truetype(p, s)

def fondo(w, h, seed=11):
    bg = Image.new("RGB", (w, h)); d = ImageDraw.Draw(bg)
    for y in range(h):
        t = y / h; d.line([(0, y), (w, y)], fill=(255, int(247 - 45 * t), int(205 - 105 * t)))
    g = Image.new("L", (w, h), 0); ImageDraw.Draw(g).ellipse((w*.05, h*.08, w*.95, h*.9), fill=215)
    bg = Image.composite(Image.new("RGB", (w, h), (255, 253, 234)), bg, g.filter(ImageFilter.GaussianBlur(170)))
    # rayos de luz suaves
    ray = Image.new("L", (w, h), 0); rd = ImageDraw.Draw(ray); cx, cy = w/2, h*.42
    for k in range(18):
        import math; a = k * math.pi / 9; L = max(w, h)
        rd.polygon([(cx, cy), (cx + L*math.cos(a-.05), cy + L*math.sin(a-.05)), (cx + L*math.cos(a+.05), cy + L*math.sin(a+.05))], fill=60)
    bg = Image.composite(Image.new("RGB", (w, h), (255, 255, 240)), bg, ray.filter(ImageFilter.GaussianBlur(25)))
    d = ImageDraw.Draw(bg); random.seed(seed)
    for _ in range(int(w*h/7000)):
        x, y, r = random.randint(0, w), random.randint(0, h), random.choice([1, 1, 2, 3])
        d.ellipse((x-r, y-r, x+r, y+r), fill=(255, 255, 238))
    for _ in range(14):  # destellos
        x, y, s = random.randint(30, w-30), random.randint(30, h-30), random.randint(8, 18)
        d.line((x-s, y, x+s, y), fill=(255, 236, 160), width=2); d.line((x, y-s, x, y+s), fill=(255, 236, 160), width=2)
    return bg

def envolver(d, txt, f, ancho):
    out, cur = [], ""
    for w in txt.split():
        if d.textlength((cur+" "+w).strip(), font=f) > ancho and cur: out.append(cur); cur = w
        else: cur = (cur+" "+w).strip()
    return out + [cur]

def centro(d, txt, f, y, color, x0, w, inter=1.15, stroke=None, ancho=None):
    for ln in envolver(d, txt, f, ancho or w):
        kw = dict(stroke_width=3, stroke_fill=stroke) if stroke else {}
        d.text((x0 + (w - d.textlength(ln, font=f))/2, y), ln, font=f, fill=color, **kw); y += int(f.size*inter)
    return y

def pill(d, txt, f, cx, y, fill, color, padx=40, pady=18, outline=None):
    tw = d.textlength(txt, font=f); bb = d.textbbox((0, 0), txt, font=f); th = bb[3] - bb[1]
    box = (cx - tw/2 - padx, y, cx + tw/2 + padx, y + th + 2*pady)
    d.rounded_rectangle(box, (th + 2*pady)//2, fill=fill, outline=outline, width=3 if outline else 0)
    d.text((cx - tw/2, y + pady - bb[1]), txt, font=f, fill=color); return box

def foto_arco(bg, x0, y0, aw, ah):
    im = Image.open(FOTO).convert("RGB").crop((60, 140, 708, 1344))
    im = im.resize((aw, int(im.height*aw/im.width)), Image.LANCZOS).crop((0, 0, aw, ah))
    mk = Image.new("L", (aw, ah), 0); ImageDraw.Draw(mk).rounded_rectangle((0, 0, aw, ah+400), aw//2, fill=255)
    glow = Image.new("RGBA", bg.size, (0, 0, 0, 0))
    ImageDraw.Draw(glow).rounded_rectangle((x0-30, y0-30, x0+aw+30, y0+ah+30), aw//2+30, fill=(255, 200, 60, 170))
    bg = Image.alpha_composite(bg.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(24))).convert("RGB")
    ImageDraw.Draw(bg).rounded_rectangle((x0-9, y0-9, x0+aw+9, y0+ah+9), aw//2+9, fill=ORO2)
    bg.paste(im, (x0, y0), mk); return bg

def comunes(d, W, y_badge):
    pill(d, "● LIVE GRATIS", F(SAN, 40), W/2, y_badge, ROJO, (255, 255, 255), padx=46)

def niveles_col(d, x0, y, w, f):
    for i, t in enumerate(["Subconsciente", "Memoria celular", "Energía"], 1):
        h = 92; d.rounded_rectangle((x0, y, x0+w, y+h), 46, fill=(255, 246, 214), outline=ORO, width=3)
        d.ellipse((x0+14, y+14, x0+78, y+78), fill=ORO); n = str(i)
        d.text((x0+46 - d.textlength(n, font=F(SAN, 36))/2, y+22), n, font=F(SAN, 36), fill=CREMA)
        d.text((x0+96, y+(h - f.size)/2 - 4), t, font=f, fill=CAFE); y += h + 22
    return y

# ---------- 4:5 ----------
W, H = 1080, 1350
bg = fondo(W, H); bg = foto_arco(bg, 610, 470, 410, 610); d = ImageDraw.Draw(bg)
comunes(d, W, 46)
y = centro(d, "Hackea tus bloqueos", F(SER, 88), 150, CAFE, 40, W-80)
y = centro(d, "con el dinero", F(SER, 88), y, CAFE, 40, W-80)
y = centro(d, "en simultáneo", F(SER, 108), y+4, ORO, 40, W-80, stroke=CREMA)
yt = y
d.text((60, 480), "3 niveles, al mismo tiempo:", font=F(SANR, 32), fill=CAFE)
y = niveles_col(d, 60, 535, 510, F(SAN, 38))
d.rounded_rectangle((60, y+8, 570, y+188), 28, fill=ORO)
d.text((90, y+28), "Miércoles 25 de noviembre", font=F(SAN, 30), fill=CREMA)
d.text((90, y+82), "8 PM", font=F(SER, 72), fill=(255, 238, 180))
d.text((280, y+108), "(CDMX)", font=F(SAN, 34), fill=CREMA)
ycta = 1118
pill(d, "Escríbeme ABUNDANCIA", F(SAN, 52), W/2, ycta, CAFE, ORO2, padx=60, pady=24, outline=ORO2)
centro(d, "Mabel Soriano · BNQ Method™", F(SAN, 34), 1262, CAFE, 0, W)
print("4x5 title_end", yt, "date_end", y+188)
bg.save("/home/user/LIVE-25-ARTE-4x5.jpg", quality=93)

# ---------- 9:16 ----------
W, H = 1080, 1920
bg = fondo(W, H, seed=17); bg = foto_arco(bg, 290, 650, 500, 640); d = ImageDraw.Draw(bg)
comunes(d, W, 190)
y = centro(d, "Hackea tus bloqueos", F(SER, 94), 290, CAFE, 40, W-80)
y = centro(d, "con el dinero", F(SER, 94), y, CAFE, 40, W-80)
y = centro(d, "en simultáneo", F(SER, 116), y+4, ORO, 40, W-80, stroke=CREMA)
print("9x16 title_end", y)
# niveles en fila
f = F(SAN, 34); xs = []; items = ["Subconsciente", "Memoria celular", "Energía"]
tot = sum(d.textlength(t, font=f) + 60 for t in items) + 2*20; x = (W - tot)/2; yr = 1330
for t in items:
    tw = d.textlength(t, font=f)
    d.rounded_rectangle((x, yr, x+tw+60, yr+76), 38, fill=(255, 246, 214), outline=ORO, width=3)
    d.text((x+30, yr+18), t, font=f, fill=CAFE); x += tw + 60 + 20
d.rounded_rectangle((150, 1430, 930, 1592), 30, fill=ORO)
centro(d, "Miércoles 25 de noviembre", F(SAN, 40), 1450, CREMA, 150, 780)
centro(d, "8 PM (CDMX)", F(SER, 60), 1504, (255, 238, 180), 150, 780)
pill(d, "Escríbeme ABUNDANCIA", F(SAN, 54), W/2, 1618, CAFE, ORO2, padx=60, pady=24, outline=ORO2)
centro(d, "Mabel Soriano · BNQ Method™", F(SAN, 34), 1748, CAFE, 0, W)
bg.save("/home/user/LIVE-25-ARTE-9x16.jpg", quality=93)
