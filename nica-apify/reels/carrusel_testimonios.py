"""Carrusel dorado de testimonios reales (capturas) + imagen única para WhatsApp."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from carrusel import fondo, bloque, envolver, firma, cierre, W, H, SER, SAN, SANR, CAFE, ORO, ORO2
T = Path(__file__).parent / "banco" / "testimonios"
CAPS = ["escrito-158.png", "escrito-159.png", "escrito-160.png", "escrito-161.png"]
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/user/CARRUSEL-TESTIMONIOS")
OUT.mkdir(exist_ok=True)
FOTO = "mabel-sonrisa.jpg"

def tarjeta(bg, cap, x, y, ancho):
    im = Image.open(T / cap).convert("RGB")
    from PIL import ImageChops
    bb = ImageChops.difference(im, Image.new("RGB", im.size, (255, 255, 255))).point(lambda v: 255 if v > 30 else 0).getbbox()
    im = im.crop((max(0, bb[0] - 12), max(0, bb[1] - 12), min(im.width, bb[2] + 12), min(im.height, bb[3] + 12))); k = (ancho - 40) / im.width
    im = im.resize((int(im.width * k), int(im.height * k)), Image.LANCZOS)
    w, h = im.width + 40, im.height + 40
    sh = Image.new("RGBA", bg.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((x + 6, y + 14, x + w + 6, y + h + 14), 28, fill=(170, 100, 0, 90))
    bg.paste(Image.alpha_composite(bg.convert("RGBA"), sh.filter(ImageFilter.GaussianBlur(16))).convert("RGB"))
    d = ImageDraw.Draw(bg)
    d.rounded_rectangle((x - 4, y - 4, x + w + 4, y + h + 4), 30, fill=ORO2)
    d.rounded_rectangle((x, y, x + w, y + h), 26, fill=(255, 255, 255))
    bg.paste(im, (x + 20, y + 20)); return y + h

def pastilla(d, txt, y, f=None):
    f = f or ImageFont.truetype(SAN, 30); w = d.textlength(txt, font=f)
    d.rounded_rectangle(((W - w) / 2 - 30, y, (W + w) / 2 + 30, y + 58), 29, fill=ORO)
    d.text(((W - w) / 2, y + 12), txt, font=f, fill=(255, 250, 225))

def estrellas(d, y):
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 46); s = "★ ★ ★ ★ ★"
    d.text(((W - d.textlength(s, font=f)) / 2, y), s, font=f, fill=(230, 160, 0))

# 1 PORTADA
bg = fondo(); d = ImageDraw.Draw(bg)
pastilla(d, "MENSAJES REALES", 90)
y = bloque(d, "Lo pusieron al dormir…", ImageFont.truetype(SER, 84), 190, CAFE)
y = bloque(d, "y esto les pasó", ImageFont.truetype(SER, 96), y, ORO, stroke=(255, 250, 225))
yy = y + 40
for i, c in enumerate(CAPS[:3]):
    yy = tarjeta(bg, c, 70 + i * 0, yy, 940) + 22 if i < 2 else tarjeta(bg, c, 70, yy, 940)
d = ImageDraw.Draw(bg)
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
for k in range(H - 470, H):
    a = int(255 * min(1, (k - (H - 470)) / 170)); od.line([(0, k), (W, k)], fill=(255, 236, 170, a))
bg = Image.alpha_composite(bg.convert("RGBA"), ov).convert("RGB"); d = ImageDraw.Draw(bg)
bloque(d, "Desliza y lee cada una  →", ImageFont.truetype(SAN, 44), H - 190, CAFE)
bloque(d, "Programa la Riqueza mientras Duermes", ImageFont.truetype(SANR, 32), H - 115, ORO)
bg.save(OUT / "1-PORTADA.jpg", quality=93)

# 2-5 TESTIMONIOS
heads = [("Cerró la venta más", "grande del año"), ("“Yo misma era", "mi propio bloqueo”"),
         ("Un bono inesperado", "y pagó su deuda"), ("Una clienta enorme", "en una semana")]
subs = ["Solo lo dejó sonando las 8 horas mientras dormía.", "Era súper escéptica. Hoy le llegan oportunidades que ni buscó.",
        "Dejó de esforzarse tanto… y el dinero llegó por otro lado.", "Llevaba meses estancada. Su energía cambió por completo."]
citas = ["“No tengo que hacer nada, solo ponerlo al dormir”", "“Me llegan oportunidades de negocio que ni siquiera busqué”",
         "“Recibí un bono inesperado y pude pagar una deuda”", "“Siento que mi energía cambió por completo”"]
for i, c in enumerate(CAPS):
    bg = fondo(); d = ImageDraw.Draw(bg)
    pastilla(d, f"TESTIMONIO REAL  {i+1}/4", 90)
    y = bloque(d, heads[i][0], ImageFont.truetype(SER, 80), 195, CAFE)
    y = bloque(d, heads[i][1], ImageFont.truetype(SER, 88), y, ORO, stroke=(255, 250, 225))
    y = bloque(d, subs[i], ImageFont.truetype(SANR, 36), y + 20, CAFE, ancho=880)
    y = tarjeta(bg, c, 30, y + 45, 1020); d = ImageDraw.Draw(bg)
    estrellas(d, y + 35)
    fq = ImageFont.truetype(SER, 54); lns = envolver(d, citas[i], fq, 860); hh = len(lns) * 66 + 50
    yq = y + 120 + max(0, ((H - 240) - (y + 120) - hh) // 2)
    d.rounded_rectangle((70, yq, W - 70, yq + hh), 30, fill=(255, 250, 225), outline=ORO2, width=5)
    bloque(d, citas[i], fq, yq + 25, ORO, ancho=860, inter=1.22)
    firma(bg, d, FOTO); bg.save(OUT / f"{i+2}-TESTIMONIO-{i+1}.jpg", quality=93)

# 6 CIERRE
cierre("Ninguno se esforzó más. Reprogramaron su mente mientras dormían. ¿Y tú?", OUT / "6-CIERRE.jpg", FOTO)

# WHATSAPP: todos juntos
WH = 1700
bg = fondo().resize((W, WH)); d = ImageDraw.Draw(bg)
pastilla(d, "MENSAJES REALES", 60)
y = bloque(d, "Lo que pasa cuando reprogramas", ImageFont.truetype(SER, 60), 150, CAFE)
y = bloque(d, "tu mente mientras duermes", ImageFont.truetype(SER, 68), y, ORO, stroke=(255, 250, 225)) + 25
for c in [CAPS[0], CAPS[1], CAPS[2], CAPS[3]]:
    y = tarjeta(bg, c, 60, y, 960) + 30
d = ImageDraw.Draw(bg)
yy = bloque(d, "Programa la Riqueza mientras Duermes", ImageFont.truetype(SAN, 38), y + 5, CAFE)
bloque(d, "21 noches · Mabel Soriano · BNQ Method™", ImageFont.truetype(SANR, 30), yy + 8, ORO)
bg = bg.crop((0, 0, W, min(WH, y + 140)))
bg.save(OUT / "WHATSAPP-TESTIMONIOS-JUNTOS.jpg", quality=93)
print("ok", y)
