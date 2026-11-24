"""Arte NEÓN (estilo aprobado 14-nov) para el LIVE GRATIS DOMINGO 29 nov · 11 AM. Sin precio. (copia de arte_live_25_neon.py, solo cambia la fecha)
Base: live/artes/buenfin-hipnosis-asistentes-4x5.jpg. Salidas 4:5 y 9:16."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
B = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
SB = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
im = Image.open("live/artes/buenfin-hipnosis-asistentes-4x5.jpg").convert("RGB")
W, H = im.size

def grad_text(base, xy, text, font, c1, c2, glow=None):
    d = ImageDraw.Draw(base)
    xy = (int(xy[0]), int(xy[1])); bbox = d.textbbox(xy, text, font=font)
    w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
    mask = Image.new("L", base.size, 0); ImageDraw.Draw(mask).text(xy, text, font=font, fill=255)
    if glow:
        g = Image.new("RGB", base.size, glow); gm = mask.filter(ImageFilter.GaussianBlur(10))
        base.paste(g, (0, 0), gm.point(lambda v: min(255, v*2)))
    gr = Image.new("RGB", base.size)
    gd = ImageDraw.Draw(gr)
    for x in range(bbox[0], bbox[2]+1):
        t = (x-bbox[0])/max(1, w)
        gd.line([(x, bbox[1]), (x, bbox[3])], fill=tuple(int(c1[i]+(c2[i]-c1[i])*t) for i in range(3)))
    base.paste(gr, (0, 0), mask)

def soft_band(base, box, color, r=0, blur=14, alpha=245):
    m = Image.new("L", base.size, 0); ImageDraw.Draw(m).rounded_rectangle(box, r, fill=alpha)
    base.paste(Image.new("RGB", base.size, color), (0, 0), m.filter(ImageFilter.GaussianBlur(blur)))

d = ImageDraw.Draw(im)
# 1) subtítulo nuevo
soft_band(im, (60, 455, 1204, 540), (18, 16, 40), 30, 10, 255)
f = ImageFont.truetype(SB, 36); t = "Subconsciente · Memoria celular · Energía"
d = ImageDraw.Draw(im); d.text(((W-d.textlength(t, font=f))/2, 474), t, font=f, fill=(255, 255, 255))
# 2) insignia: LIVE GRATIS en lugar del precio
cx, cy, r = 225, 802, 196
m = Image.new("L", im.size, 0); ImageDraw.Draw(m).ellipse((cx-r, cy-r, cx+r, cy+r), fill=255)
glow = Image.new("RGB", im.size, (255, 80, 200))
im.paste(glow, (0, 0), m.filter(ImageFilter.GaussianBlur(18)).point(lambda v: int(v*0.8)))
coin = Image.new("RGB", im.size)
cd = ImageDraw.Draw(coin)
for i in range(r, 0, -1):
    t = i/r; cd.ellipse((cx-i, cy-i, cx+i, cy+i), fill=(int(255-60*t), int(214-70*t), int(90-50*t)))
m2 = Image.new("L", im.size, 0); ImageDraw.Draw(m2).ellipse((cx-r+8, cy-r+8, cx+r-8, cy+r-8), fill=255)
im.paste(coin, (0, 0), m2)
d = ImageDraw.Draw(im)
for txt, sz, y, col in (("LIVE", 80, 680, (70, 30, 10)), ("GRATIS", 70, 765, (70, 30, 10)), ("EN VIVO", 38, 855, (150, 20, 70))):
    f = ImageFont.truetype(B, sz); d.text((cx-d.textlength(txt, font=f)/2, y), txt, font=f, fill=col)
# 3) franja inferior: fecha y hora
soft_band(im, (-40, 1250, W+40, 1495), (14, 12, 34), 0, 8, 255)
f = ImageFont.truetype(B, 92); t = "DOMINGO 29 NOV"
d = ImageDraw.Draw(im); x = (W-d.textlength(t, font=f))/2
grad_text(im, (x, 1270), t, f, (255, 205, 80), (255, 90, 190), glow=(255, 120, 160))
box = (170, 1390, W-170, 1462)
d = ImageDraw.Draw(im); d.rounded_rectangle(box, 10, outline=(255, 70, 150), width=4)
f = ImageFont.truetype(B, 44); t = "11 AM · HORA MX · REGÍSTRATE"
d.text(((W-d.textlength(t, font=f))/2, 1398), t, font=f, fill=(255, 255, 255))
im.save("live/artes/pauta-29/original-1264x1568.jpg", quality=95)
a = im.resize((1080, 1340), Image.LANCZOS)
c = Image.new("RGB", (1080, 1350), (14, 12, 34)); c.paste(a, (0, 5)); c.save("live/artes/pauta-29/LIVE-29-NOV-4x5-feed.jpg", quality=93)
bg = im.resize((1080, 1920)).filter(ImageFilter.GaussianBlur(30))
bg = Image.blend(bg, Image.new("RGB", bg.size, (10, 8, 24)), 0.3); bg.paste(a, (0, 290))
d = ImageDraw.Draw(bg); f = ImageFont.truetype(B, 50)
for t, y, fill, col in (("LIVE GRATIS · SIN COSTO", 120, (255, 205, 80), (20, 15, 30)), ("ESCRÍBEME ABUNDANCIA", 1700, (255, 205, 80), (20, 15, 30))):
    w = d.textlength(t, font=f); d.rounded_rectangle(((1080-w)/2-40, y-18, (1080+w)/2+40, y+72), 36, fill=fill); d.text(((1080-w)/2, y), t, font=f, fill=col)
bg.save("live/artes/pauta-29/LIVE-29-NOV-9x16-historias.jpg", quality=93)
# 1:1 (1080x1080): arte completa centrada sobre fondo desenfocado
sq = im.resize((1080, 1080)).filter(ImageFilter.GaussianBlur(30))
sq = Image.blend(sq, Image.new("RGB", sq.size, (10, 8, 24)), 0.3)
a11 = im.resize((int(W*1080/H), 1080), Image.LANCZOS); sq.paste(a11, ((1080-a11.width)//2, 0))
sq.save("live/artes/pauta-29/LIVE-29-NOV-1x1-cuadrado.jpg", quality=93)
print("ok")
