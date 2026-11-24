"""Portada Hotmart · Tu Mapa Cuántico (Carta Natal + Matriz del Destino + Protocolo CEI™).
Línea de productos de Mabel: galaxia morada/azul + dorado + su foto real. Reusa funciones de landing/checkout_roboticas_galaxia.py."""
import sys, types
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
src = Path("landing/checkout_roboticas_galaxia.py").read_text().split("# 1 HERO")[0]
m = types.ModuleType("g"); sys.argv = ["x", "/tmp/_g"]; exec(src, m.__dict__)
W = 1200; m.W = W
bg = m.galaxia(W, W, 9)
geo = Image.open("marca/geo-metatron.png").convert("RGBA").resize((900, 900))
a = geo.split()[3].point(lambda v: int(v * .28)); bg.paste((255, 205, 90), (330, 210), a)
# foto real recortada con su máscara + halo dorado
ft = Image.open("marca/mabel-foto.jpg").convert("RGB"); mk = Image.open("marca/mabel-mascara.png").convert("L")
h = 760; w = int(ft.width * h / ft.height); ft = ft.resize((w, h), Image.LANCZOS); mk = mk.resize((w, h), Image.LANCZOS)
x0, y0 = W - w + 40, W - h
halo = Image.new("L", bg.size, 0); halo.paste(mk, (x0, y0)); bg.paste((255, 190, 70), (0, 0), halo.filter(ImageFilter.GaussianBlur(28)).point(lambda v: int(v * .85)))
bg.paste(ft, (x0, y0), mk)
d = ImageDraw.Draw(bg)
m.atomo(d, 360, 70, 26); d.text((400, 50), "BNQ Method™ · Mabel Soriano", font=m.F(m.SB, 32), fill=m.BLANCO)
m.centro_oro(bg, "Tu Mapa", m.F(m.SER, 120), 120); m.centro_oro(bg, "Cuántico", m.F(m.SER, 150), 245)
d = ImageDraw.Draw(bg)
m.centro(d, "Carta Natal + Matriz del Destino + Protocolo CEI™", m.F(m.SB, 36), 430, m.ORO)
d.multiline_text((70, 540), "Descubre con qué\nprograma llegaste…", font=m.F(m.SER, 54), fill=m.BLANCO, spacing=14)
d.multiline_text((70, 700), "y cómo reescribirlo\nen simultáneo.", font=m.F(m.SER, 54), fill=m.ORO, spacing=14)
y = 880
for t in ("Tus talentos y tu misión", "Dónde se fuga tu dinero", "Qué Fórmula activar primero"):
    d.ellipse((80, y + 14, 96, y + 30), fill=m.ORO); d.text((112, y), t, font=m.F(m.SB, 36), fill=m.BLANCO); y += 58
m.caja(d, (60, 1080, 700, 1160), gold=True)
d.text((95, 1097), "Decodificación personalizada", font=m.F(m.B, 40), fill=(60, 25, 90))
out = Path("hotmart"); bg.save(out / "portada-mapa-cuantico-1200x1200.jpg", quality=93)
for s in (800, 600): bg.resize((s, s), Image.LANCZOS).save(out / f"portada-mapa-cuantico-{s}x{s}.jpg", quality=92)
print("ok")
