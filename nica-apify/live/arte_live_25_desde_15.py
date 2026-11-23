"""Arte aprobada del live 15-nov (dorada, dinero) con fecha nueva: MIÉRCOLES 25 NOV · 11 AM · HORA MX.
Salidas: 4:5 (1080x1350) para feed y 9:16 (1080x1920) para historias/TikTok."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
SRC = "live/artes/anuncio-live-2026-11-15-4x5.jpg"
TXT = "MIÉRCOLES 25 NOV · 11 AM · HORA MX"
im = Image.open(SRC).convert("RGB")
d = ImageDraw.Draw(im)
# tapar el texto viejo dentro del recuadro (interior oscuro)
d.rectangle((158, 1381, 1128, 1434), fill=(18, 15, 26))
f = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Bold.otf", 40)
w = d.textlength(TXT, font=f)
x = (1264 - w) / 2
d.text((x, 1386), TXT, font=f, fill=(255, 255, 255))
im.save("live/artes/anuncio-live-2026-11-25-4x5-original.jpg", quality=95)
# 4:5 exacto 1080x1350
a45 = im.resize((1080, int(1568 * 1080 / 1264)), Image.LANCZOS)  # 1080x1340
c45 = Image.new("RGB", (1080, 1350), (18, 15, 26)); c45.paste(a45, (0, 5))
c45.save("/home/user/LIVE-25-NOV-11AM-4x5.jpg", quality=93)
# 9:16: arte centrada sobre fondo desenfocado de la misma arte
bg = im.resize((1080, 1920)).filter(ImageFilter.GaussianBlur(30))
bg = Image.blend(bg, Image.new("RGB", bg.size, (10, 8, 20)), 0.35)
bg.paste(a45, (0, (1920 - a45.height) // 2))
bg.save("/home/user/LIVE-25-NOV-11AM-9x16.jpg", quality=93)
print("ok")
