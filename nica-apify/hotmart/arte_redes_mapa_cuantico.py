"""Arte de redes · Obtén tu Mapa Cuántico con las 2 opciones (PDF / sesión 1 a 1). Misma línea que la portada aprobada."""
import sys, types
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
src = Path("landing/checkout_roboticas_galaxia.py").read_text().split("# 1 HERO")[0]
m = types.ModuleType("g"); sys.argv = ["x", "/tmp/_g"]; exec(src, m.__dict__)
ORO = (255, 200, 60); CAFE = (70, 30, 10); MOR = (60, 25, 90)

def arte(W, H, out):
    m.W = W
    bg = m.galaxia(W, H, 9)
    geo = Image.open("marca/geo-metatron.png").convert("RGBA").resize((820, 820))
    bg.paste((255, 205, 90), (W - 760, int(H * .28)), geo.split()[3].point(lambda v: int(v * .25)))
    # foto
    ft = Image.open("marca/mabel-foto.jpg").convert("RGB"); mk = Image.open("marca/mabel-mascara.png").convert("L")
    fh = int(H * .58); fw = int(ft.width * fh / ft.height)
    ft = ft.resize((fw, fh), Image.LANCZOS); mk = mk.resize((fw, fh), Image.LANCZOS)
    x0, y0 = W - fw + 70, H - fh - (150 if H > 1500 else 110)
    halo = Image.new("L", bg.size, 0); halo.paste(mk, (x0, y0))
    bg.paste((255, 190, 70), (0, 0), halo.filter(ImageFilter.GaussianBlur(26)).point(lambda v: int(v * .8)))
    bg.paste(ft, (x0, y0), mk)
    d = ImageDraw.Draw(bg)
    top = 60 if H < 1500 else 150
    m.atomo(d, W // 2 - 230, top + 20, 22); d.text((W // 2 - 195, top), "BNQ Method™ · Mabel Soriano", font=m.F(m.SB, 28), fill=m.BLANCO)
    def sol(t, f, y):
        d.text(((W - d.textlength(t, font=f)) / 2, y), t, font=f, fill=ORO, stroke_width=4, stroke_fill=CAFE)
    sol("OBTÉN TU", m.F(m.SER, 84), top + 60); sol("MAPA CUÁNTICO", m.F(m.SER, 100), top + 150)
    m.centro(d, "Con tu Carta Natal + tu Matriz del Destino", m.F(m.SB, 34), top + 275)
    m.centro(d, "con Numerología", m.F(m.SB, 34), top + 318)
    # tarjetas
    cx, cw = 50, 600; y = top + 400
    def tarjeta(y, etiqueta, titulo, lineas, precio, gold):
        h = 110 + 46 * len(lineas) + 92
        d.rounded_rectangle((cx, y, cx + cw, y + h), 28, fill=(255, 205, 90) if gold else (38, 20, 78), outline=ORO, width=4)
        tc = MOR if gold else ORO; bc = MOR if gold else m.BLANCO
        d.text((cx + 30, y + 22), etiqueta, font=m.F(m.SB, 26), fill=tc)
        d.text((cx + 30, y + 54), titulo, font=m.F(m.B, 40), fill=bc)
        yy = y + 112
        for l in lineas:
            d.ellipse((cx + 34, yy + 13, cx + 46, yy + 25), fill=tc); d.text((cx + 60, yy), l, font=m.F(m.SB, 30), fill=bc); yy += 46
        d.text((cx + 30, yy + 10), precio, font=m.F(m.B, 46), fill=tc)
        return y + h
    y = tarjeta(y, "OPCIÓN 1", "TU MAPA EN PDF", ["Carta Natal", "Matriz del Destino", "Tu diagnóstico personal"], "$390 + impuestos", False) + 28
    y = tarjeta(y, "OPCIÓN 2", "SESIÓN 1 A 1 CONMIGO", ["Tu Mapa en PDF", "20 min de lectura en vivo", "Activación simultánea", "Acceso a mi comunidad VIP"], "$2,000 + impuestos", True) + 34
    # CTA
    t = "Comenta MAPA y te mando el link"; f = m.F(m.B, 40); tw = d.textlength(t, font=f)
    d.rounded_rectangle(((W - tw) / 2 - 40, y, (W + tw) / 2 + 40, y + 76), 38, fill=ORO)
    d.text(((W - tw) / 2, y + 14), t, font=f, fill=MOR)
    bg.save(out, quality=93)

Path("hotmart/redes").mkdir(exist_ok=True)
arte(1080, 1350, "hotmart/redes/MAPA-CUANTICO-4x5.jpg")
arte(1080, 1920, "hotmart/redes/MAPA-CUANTICO-9x16.jpg")
print("ok")
