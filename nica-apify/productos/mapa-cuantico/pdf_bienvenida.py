"""PDF de bienvenida (entregable de Hotmart) · Obtén tu Mapa Cuántico. Línea galaxia + dorado."""
import sys, types
from pathlib import Path
from PIL import Image, ImageDraw
src = Path("landing/checkout_roboticas_galaxia.py").read_text().split("# 1 HERO")[0]
m = types.ModuleType("g"); sys.argv = ["x", "/tmp/_g"]; exec(src, m.__dict__)
FORM = "https://docs.google.com/forms/d/e/1FAIpQLScNF6hY-jTNJXgc5p8XUPUl02XdktFJdB4xoszE0KvdHbFP_A/viewform"
W, H = 1240, 1754; m.W = W
bg = m.galaxia(W, H, 11); d = ImageDraw.Draw(bg)
ORO = (255, 200, 60); CAFE = (70, 30, 10)
def c(t, f, y, col=m.BLANCO, sol=False):
    x = (W - d.textlength(t, font=f)) / 2
    if sol: d.text((x, y), t, font=f, fill=ORO, stroke_width=4, stroke_fill=CAFE)
    else: d.text((x, y), t, font=f, fill=col)
m.atomo(d, W // 2, 110, 34)
c("BNQ Method™ · Mabel Soriano", m.F(m.SB, 34), 170)
c("¡GRACIAS!", m.F(m.SER, 110), 260, sol=True)
c("Ya activaste tu", m.F(m.SER, 52), 410)
c("MAPA CUÁNTICO", m.F(m.SER, 96), 480, sol=True)
c("Carta Natal + Matriz del Destino con Numerología", m.F(m.SB, 36), 610, ORO)
y = 720
d.text((110, y), "Para preparar tu Mapa necesito tus datos de nacimiento:", font=m.F(m.SB, 38), fill=m.BLANCO); y += 90
pasos = ["1. Llena el formulario (2 minutos): nombre, fecha,", "    hora y lugar de nacimiento.",
         "2. Preparo tu Mapa Cuántico personalmente.",
         "3. Lo recibes en PDF en tu correo en un máximo", "    de 72 horas hábiles.",
         "Si elegiste la SESIÓN 1 A 1, te escribo para agendar", "    tu sesión en vivo conmigo."]
for p in pasos:
    d.text((110, y), p, font=m.F(m.SB, 38), fill=m.BLANCO); y += 62
y += 40
bx = (110, y, W - 110, y + 120); d.rounded_rectangle(bx, 40, fill=(255, 205, 90))
t = "LLENA TU FORMULARIO AQUÍ"; f = m.F(m.B, 50)
d.text(((W - d.textlength(t, font=f)) / 2, y + 32), t, font=f, fill=(60, 25, 90)); boton = bx
y += 160
c("o copia este link:", m.F(m.SB, 30), y); y += 50
c("docs.google.com/forms/d/e/1FAIpQLScNF6hY-jTNJXgc5p8XUPUl02XdktFJdB4xoszE0KvdHbFP_A", m.F(m.SB, 20), y, ORO)
c("Lo que no se ACTIVA, no CAMBIA. Y lo que no se REPITE, no se INSTALA.", m.F(m.SB, 30), H - 170)
c("Mabel Soriano · BNQ Method™", m.F(m.SB, 32), H - 115, ORO)
out = Path("productos/mapa-cuantico/MAPA-CUANTICO-BIENVENIDA.pdf")
bg.save(out, "PDF", resolution=150)
# link clickeable sobre el botón
try:
    import pypdf
    from pypdf.generic import DictionaryObject, NameObject, ArrayObject, FloatObject, TextStringObject, NumberObject
    r = pypdf.PdfReader(str(out)); w = pypdf.PdfWriter(); w.append(r)
    pg = w.pages[0]; sc = 72 / 150; ph = float(pg.mediabox.height)
    rect = [boton[0]*sc, ph - boton[3]*sc, boton[2]*sc, ph - boton[1]*sc]
    from pypdf.annotations import Link
    w.add_annotation(0, Link(rect=rect, url=FORM)); w.write(str(out)); print("link ok")
except Exception as e:
    print("sin link clickeable:", e)
bg.convert("RGB").resize((620, 877)).save("/tmp/claude-0/-home-user-markitdown-mcp-serve/de17578c-0c23-5361-aec3-0e1cdc8677f7/scratchpad/bienv.jpg")
