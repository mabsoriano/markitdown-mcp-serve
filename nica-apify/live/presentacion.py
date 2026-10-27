"""Presentación del LIVE (1920x1080): fondo universo azul y morado, letras doradas y blancas.

Uso: python3 live/presentacion.py
Sale: live/presentacion/NN_nombre.png, live/presentacion-live-2026-10-27.pptx y .pdf
"""
import random
from pathlib import Path

import qrcode
from PIL import Image, ImageDraw, ImageFilter, ImageFont

AQUI = Path(__file__).resolve().parent
MARCA = AQUI.parent / "marca"
PORTADA_PACK = AQUI.parent / "hotmart" / "portada-hotmart-5-hipnosis-1200x1200.jpg"
SALIDA = AQUI / "presentacion"
W, H = 1920, 1080
LINK = "https://pay.hotmart.com/T108210969W?bid=1793114479230"

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
ORO = (232, 190, 92)
ORO_CLARO = (250, 222, 150)
BLANCO = (255, 255, 255)
GRIS = (200, 196, 220)
PANEL = (20, 14, 48)


def f(ruta, px):
    return ImageFont.truetype(ruta, px)


def universo(semilla=7):
    """Degradado azul noche a morado, nebulosas suaves y estrellas."""
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)], fill=(int(12 + 22 * t), int(10 + 4 * t), int(38 + 30 * t)))
    neb = Image.new("RGB", (W, H), (0, 0, 0))
    nd = ImageDraw.Draw(neb)
    for (cx, cy, r, color) in [(1450, 300, 420, (90, 40, 150)), (1650, 800, 380, (30, 60, 150)),
                               (300, 950, 300, (70, 30, 120)), (1200, 650, 260, (140, 100, 40))]:
        nd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    neb = neb.filter(ImageFilter.GaussianBlur(160))
    img = Image.blend(img, Image.composite(neb, img, Image.new("L", (W, H), 255)), 0.55)
    d = ImageDraw.Draw(img)
    rnd = random.Random(semilla)
    for _ in range(420):
        x, y, b = rnd.randrange(W), rnd.randrange(H), rnd.randrange(140, 255)
        r = rnd.choice([1, 1, 1, 2])
        d.ellipse([x - r, y - r, x + r, y + r], fill=(b, b, min(255, b + 20)))
    return img


def foto_derecha(img, ancho=760):
    """Foto real de Mabel recortada con su máscara, pegada abajo a la derecha con brillo dorado."""
    foto = Image.open(MARCA / "mabel-foto.jpg").convert("RGB")
    mascara = Image.open(MARCA / "mabel-mascara.png").convert("L")
    alto = int(foto.height * ancho / foto.width)
    foto = foto.resize((ancho, alto), Image.LANCZOS)
    mascara = mascara.resize((ancho, alto), Image.LANCZOS).filter(ImageFilter.GaussianBlur(3))
    x, y = W - ancho - 40, H - alto + 260
    brillo = Image.new("L", (W, H), 0)
    ImageDraw.Draw(brillo).ellipse([x + 80, y + 120, x + ancho - 80, y + 900], fill=255)
    brillo = brillo.filter(ImageFilter.GaussianBlur(120))
    img.paste(Image.new("RGB", (W, H), (200, 150, 60)), (0, 0), brillo.point(lambda v: v * 0.55))
    img.paste(foto, (x, y), mascara)
    return img


def partir(d, txt, fuente, maximo):
    lineas, actual = [], ""
    for p in txt.split():
        prueba = (actual + " " + p).strip()
        if d.textlength(prueba, font=fuente) <= maximo or not actual:
            actual = prueba
        else:
            lineas.append(actual)
            actual = p
    return lineas + [actual]


def parrafo(d, txt, fuente, x, y, maximo, color=BLANCO, centro=False, inter=1.25):
    """Escribe texto partido en renglones; regresa la y final."""
    alto = fuente.size * inter
    for linea in partir(d, txt, fuente, maximo):
        xx = x + (maximo - d.textlength(linea, font=fuente)) / 2 if centro else x
        d.text((xx, y), linea, font=fuente, fill=color)
        y += alto
    return y


def linea_oro(d, x, y, largo):
    d.line([(x, y), (x + largo, y)], fill=ORO, width=3)
    d.ellipse([x + largo - 6, y - 6, x + largo + 6, y + 6], fill=ORO)


def caja(img, xy, radio=30, borde=ORO):
    capa = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(capa).rounded_rectangle(xy, radio, fill=PANEL + (190,), outline=borde + (255,), width=3)
    img.paste(capa, (0, 0), capa)


def circulo_num(d, cx, cy, n, r=34):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=ORO)
    fu = f(SANS, int(r * 1.1))
    t = str(n)
    d.text((cx - d.textlength(t, font=fu) / 2, cy - fu.size * 0.62), t, font=fu, fill=PANEL)


def pie(d):
    d.text((90, H - 80), "@mabradiante · Método BNQ™", font=f(SANS, 30), fill=ORO)


def encabezado(d, kicker, titulo, px=84, ancho=1740, x=90):
    d.text((x, 80), kicker, font=f(SANS, 32), fill=ORO)
    y = parrafo(d, titulo, f(SERIF, px), x, 128, ancho, ORO_CLARO, inter=1.08)
    linea_oro(d, x + 2, int(y) + 18, 520)
    return int(y) + 60


def qr(tam):
    q = qrcode.QRCode(border=2, box_size=10)
    q.add_data(LINK)
    return q.make_image(fill_color=(20, 14, 48), back_color=(255, 255, 255)).convert("RGB").resize((tam, tam))


# ---------- diapositivas ----------

def d01_portada():
    img = foto_derecha(universo(1))
    d = ImageDraw.Draw(img)
    d.text((90, 150), "LIVE GRATIS · ACTIVACIÓN EN TIEMPO REAL", font=f(SANS, 34), fill=ORO)
    y = parrafo(d, "HIPNOSIS PARA HACKEAR TUS BLOQUEOS CON EL DINERO", f(SERIF, 112), 90, 210, 1050,
                ORO_CLARO, inter=1.05)
    linea_oro(d, 92, int(y) + 20, 520)
    d.text((90, y + 60), "Método BNQ™ · Mabel Soriano", font=f(SANS, 46), fill=BLANCO)
    pie(d)
    return img


def d02_cuidados():
    img = universo(2)
    d = ImageDraw.Draw(img)
    y = encabezado(d, "ANTES DE EMPEZAR", "Prepárate para recibir")
    for i, t in enumerate(["No estés manejando", "Busca un lugar tranquilo y ponte audífonos",
                           "Ten a la mano agua y una libreta"], 1):
        circulo_num(d, 130, y + 70, i)
        d.text((200, y + 40), t, font=f(SANS, 50), fill=BLANCO)
        y += 140
    caja(img, (90, 820, 1830, 960), 24, (120, 100, 160))
    d = ImageDraw.Draw(img)
    parrafo(d, "Práctica de bienestar. No sustituye atención médica ni psicológica. "
               "Si lo necesitas: Línea de la Vida 800 911 2000 (gratis, 24 horas).",
            f(SANS_REG, 32), 130, 850, 1660, GRIS)
    return img


def d03_hoy():
    img = universo(3)
    d = ImageDraw.Draw(img)
    y = encabezado(d, "LO QUE VAS A VIVIR HOY", "Hoy vas a…")
    for i, t in enumerate(["Entender por qué tu fuerza de voluntad no alcanza",
                           "Ver lo que dice la neurociencia",
                           "Vivir una autohipnosis en vivo",
                           "Llevarte tu ancla de 3 palabras"], 1):
        circulo_num(d, 130, y + 70, i)
        d.text((200, y + 40), t, font=f(SANS, 52), fill=BLANCO)
        y += 150
    pie(d)
    return img


def frase(semilla, kicker, grande, chico):
    img = universo(semilla)
    d = ImageDraw.Draw(img)
    d.text((W / 2 - d.textlength(kicker, font=f(SANS, 34)) / 2, 200), kicker, font=f(SANS, 34), fill=ORO)
    y = parrafo(d, grande, f(SERIF, 130), 160, 280, W - 320, ORO_CLARO, centro=True, inter=1.05)
    linea_oro(d, W / 2 - 260, int(y) + 30, 520)
    parrafo(d, chico, f(SANS, 50), 200, y + 90, W - 400, BLANCO, centro=True)
    pie(d)
    return img


def d04_dolor():
    return frase(4, "¿TE SUENA?", "El dinero llega… y se va.",
                 "No es mala suerte. No es falta de disciplina. Es un PROGRAMA.")


def d05_culpa():
    img = frase(5, "LO QUE NADIE TE DIJO", "No es tu culpa. Pero sí es tu responsabilidad.", "")
    d = ImageDraw.Draw(img)
    fu = f(SANS, 34)
    chips = ["“El dinero cuesta”", "“No alcanza”", "“Los ricos son malos”", "“No lo merezco”"]
    anchos = [d.textlength(c, font=fu) + 60 for c in chips]
    x = (W - sum(anchos) - 24 * 3) / 2
    for c, a in zip(chips, anchos):
        caja(img, (x, 700, x + a, 790), 45)
        ImageDraw.Draw(img).text((x + 30, 725), c, font=fu, fill=ORO_CLARO)
        x += a + 24
    d = ImageDraw.Draw(img)
    t = "Programas que heredaste y aprendiste. Corren en automático."
    d.text((W / 2 - d.textlength(t, font=f(SANS_REG, 40)) / 2, 850), t, font=f(SANS_REG, 40), fill=GRIS)
    return img


def d06_sistema():
    img = universo(6)
    d = ImageDraw.Draw(img)
    y = encabezado(d, "ESPECIFICACIONES DEL SISTEMA", "Tu sistema operativo")
    cols = [("MENTE CONSCIENTE", "La pantalla", ["Lenta", "Se cansa", "Aquí vive la DECISIÓN"]),
            ("SUBCONSCIENTE", "La base de datos", ["Rápido", "Automático", "Aquí vive el HÁBITO"])]
    for i, (t, s, pts) in enumerate(cols):
        x0 = 90 + i * 890
        caja(img, (x0, y, x0 + 850, y + 440))
        d = ImageDraw.Draw(img)
        d.text((x0 + 50, y + 40), t, font=f(SANS, 52), fill=ORO_CLARO)
        d.text((x0 + 50, y + 110), s, font=f(SANS_REG, 38), fill=GRIS)
        yy = y + 190
        for p in pts:
            d.ellipse([x0 + 55, yy + 18, x0 + 73, yy + 36], fill=ORO)
            d.text((x0 + 100, yy), p, font=f(SANS, 44), fill=BLANCO)
            yy += 75
    caja(img, (90, 890, 1830, 1020), 24)
    d = ImageDraw.Draw(img)
    parrafo(d, "Decretar sin reprogramar es como querer cambiar un programa dibujando sobre el monitor.",
            f(SANS, 38), 130, 915, 1660, ORO_CLARO, centro=True)
    return img


def numero(semilla, kicker, cifra, texto, fuente):
    img = universo(semilla)
    d = ImageDraw.Draw(img)
    d.text((90, 80), kicker, font=f(SANS, 34), fill=ORO)
    d.text((90, 200), cifra, font=f(SERIF, 330), fill=ORO_CLARO)
    parrafo(d, texto, f(SANS, 56), 820, 300, 1010, BLANCO)
    linea_oro(d, 92, 620, 520)
    parrafo(d, fuente, f(SANS_REG, 34), 90, 660, 1700, GRIS)
    pie(d)
    return img


def d07_piloto():
    return numero(7, "EL PILOTO AUTOMÁTICO", "43%",
                  "de lo que haces en el día es hábito: lo haces mientras piensas en otra cosa.",
                  "Wood, Quinn y Kashy · Universidad de Duke, 2002")


def d08_bnq():
    img = universo(8)
    d = ImageDraw.Draw(img)
    y = encabezado(d, "DONDE VIVE EL BLOQUEO", "La Fórmula BNQ™")
    cartas = [("BIO", "Hardware", "Programas y memorias celulares", "Lo heredado"),
              ("NEURO", "Software", "Patrones, hábitos y lealtades", "Lo aprendido"),
              ("QUANTUM", "El salto", "Energía, nueva orden, nueva identidad", "Lo que eliges")]
    for i, (t, s, txt, pie_c) in enumerate(cartas):
        x0 = 90 + i * 590
        caja(img, (x0, y, x0 + 560, y + 470))
        d = ImageDraw.Draw(img)
        d.text((x0 + 45, y + 40), t, font=f(SERIF, 80), fill=ORO_CLARO)
        d.text((x0 + 45, y + 135), s, font=f(SANS, 38), fill=ORO)
        parrafo(d, txt, f(SANS, 40), x0 + 45, y + 210, 470, BLANCO)
        d.text((x0 + 45, y + 390), pie_c, font=f(SANS_REG, 34), fill=GRIS)
    t = "No evolucionas. TRANSMUTAS."
    d.text((W / 2 - d.textlength(t, font=f(SERIF, 64)) / 2, y + 520), t, font=f(SERIF, 64), fill=ORO_CLARO)
    return img


def d09_neuro():
    img = frase(9, "NEUROPLASTICIDAD", "Tu cerebro cambia su cableado según lo que repites.",
                "“Neuronas que se activan juntas, se conectan juntas.”")
    d = ImageDraw.Draw(img)
    t = "Donald Hebb, 1949"
    d.text((W / 2 - d.textlength(t, font=f(SANS_REG, 34)) / 2, 950), t, font=f(SANS_REG, 34), fill=GRIS)
    return img


def d10_taxistas():
    img = universo(10)
    d = ImageDraw.Draw(img)
    y = encabezado(d, "EVIDENCIA · NEUROPLASTICIDAD", "Los taxistas de Londres")
    caja(img, (90, y + 20, 1830, y + 420))
    d = ImageDraw.Draw(img)
    yy = parrafo(d, "Memorizar las 25,000 calles de Londres desarrolló más su hipocampo, "
                    "la zona de la orientación. Y entre más años de taxistas, más.",
                 f(SANS, 54), 150, y + 70, 1620, BLANCO)
    d.text((150, yy + 30), "El cerebro adulto SÍ se remodela con la práctica.", font=f(SANS, 46), fill=ORO_CLARO)
    d.text((90, H - 150), "Maguire y equipo · PNAS, 2000", font=f(SANS_REG, 34), fill=GRIS)
    pie(d)
    return img


def d11_aprovechar():
    img = universo(11)
    d = ImageDraw.Draw(img)
    y = encabezado(d, "CÓMO LO APROVECHAS", "3 pasos para reprogramar")
    pasos = [("DATE CUENTA", "del programa viejo"), ("INSTALA", "la orden nueva en estado relajado"),
             ("REPITE", "hasta que sea automático")]
    for i, (t, s) in enumerate(pasos):
        x0 = 90 + i * 590
        caja(img, (x0, y, x0 + 560, y + 380))
        d = ImageDraw.Draw(img)
        circulo_num(d, x0 + 90, y + 95, i + 1, 44)
        d.text((x0 + 45, y + 170), t, font=f(SANS, 50), fill=ORO_CLARO)
        parrafo(d, s, f(SANS_REG, 40), x0 + 45, y + 245, 470, BLANCO)
    t = "Eso es la autohipnosis BNQ™"
    d.text((W / 2 - d.textlength(t, font=f(SERIF, 70)) / 2, y + 440), t, font=f(SERIF, 70), fill=ORO_CLARO)
    return img


def d12_historia():
    img = universo(12)
    d = ImageDraw.Draw(img)
    y = encabezado(d, "DE LOS TEMPLOS A LA NEUROCIENCIA", "La hipnosis tiene historia")
    hitos = [("Antigüedad", "Templos del sueño en Egipto y Grecia"), ("1843", "James Braid la llama “hipnosis”"),
             ("1880s", "Charcot la estudia en París"), ("1950s", "Milton Erickson"),
             ("1955 · 1958", "La reconocen las asociaciones médicas británica y americana"),
             ("HOY", "La neurociencia la mide con resonancia magnética")]
    ly = y + 120
    d.line([(200, ly), (1720, ly)], fill=ORO, width=4)
    paso = 1520 / 5
    for i, (a, t) in enumerate(hitos):
        cx = 200 + i * paso
        d.ellipse([cx - 16, ly - 16, cx + 16, ly + 16], fill=ORO_CLARO if i == 5 else ORO)
        fa = f(SANS, 40)
        d.text((cx - d.textlength(a, font=fa) / 2, ly - 85), a, font=fa, fill=ORO_CLARO)
        parrafo(d, t, f(SANS_REG, 30), cx - 140, ly + 50, 280, BLANCO if i < 5 else ORO_CLARO, centro=True)
    pie(d)
    return img


def d13_kirsch():
    return numero(13, "EVIDENCIA · EL MULTIPLICADOR", "70%",
                  "Al sumar hipnosis a la terapia, la persona promedio mejoró más que el 70% de quienes no la usaron.",
                  "Kirsch, Montgomery y Sapirstein, 1995 · análisis de 18 estudios")


def d14_stanford():
    img = universo(14)
    d = ImageDraw.Draw(img)
    y = encabezado(d, "EVIDENCIA · NEUROCIENCIA EN TIEMPO REAL", "Tu cerebro en hipnosis")
    caja(img, (90, y + 20, 1830, y + 420))
    d = ImageDraw.Draw(img)
    yy = parrafo(d, "Baja la actividad de la zona que vigila y critica.", f(SANS, 56), 150, y + 70, 1620, BLANCO)
    parrafo(d, "Por eso la orden nueva entra sin pelear con tu juez interno.", f(SANS, 50), 150, yy + 40,
            1620, ORO_CLARO)
    d.text((90, H - 150), "Jiang, Spiegel y equipo · Universidad de Stanford, 2016", font=f(SANS_REG, 34), fill=GRIS)
    pie(d)
    return img


def d15_ecuacion():
    img = universo(15)
    d = ImageDraw.Draw(img)
    y = encabezado(d, "LA LLAVE", "Hipnosis + BNQ™ = Hackeo")
    piezas = [("HIPNOSIS", "abre la puerta del subconsciente"), ("FÓRMULAS CUÁNTICAS", "dicen QUÉ instalar"),
              ("HACKEO BNQ™", "reprogramas en los 3 niveles")]
    for i, (t, s) in enumerate(piezas):
        x0 = 90 + i * 610
        caja(img, (x0, y + 40, x0 + 520, y + 420), borde=ORO_CLARO if i == 2 else ORO)
        d = ImageDraw.Draw(img)
        parrafo(d, t, f(SANS, 48), x0 + 30, y + 120, 460, ORO_CLARO, centro=True)
        parrafo(d, s, f(SANS_REG, 38), x0 + 30, y + 260, 460, BLANCO, centro=True)
        if i < 2:
            sig = "+" if i == 0 else "="
            d.text((x0 + 545, y + 180), sig, font=f(SANS, 80), fill=ORO)
    pie(d)
    return img


def d16_todo():
    img = universo(16)
    d = ImageDraw.Draw(img)
    y = encabezado(d, "TODO LO QUE SE PUEDE REPROGRAMAR", "¿Qué más puedes hackear?")
    temas = ["Dinero y merecimiento", "Relaciones que se repiten", "Ansiedad y modo supervivencia",
             "Burnout y modo alarma", "Propósito, éxito y despertar de consciencia"]
    for i, t in enumerate(temas, 1):
        circulo_num(d, 130, y + 50, i, 30)
        d.text((190, y + 22), t, font=f(SANS, 48), fill=BLANCO)
        y += 105
    t = "Cambia el programa y cambia tu realidad."
    d.text((90, y + 40), t, font=f(SERIF, 64), fill=ORO_CLARO)
    return img


def d17_quien_soy():
    img = foto_derecha(universo())
    d = ImageDraw.Draw(img)
    d.text((90, 80), "QUIÉN TE VA A GUIAR HOY", font=f(SANS, 34), fill=ORO)
    d.text((90, 125), "Mabel Soriano", font=f(SERIF, 104), fill=ORO_CLARO)
    linea_oro(d, 92, 260, 520)
    puntos = [("Terapeuta cuántica", "y activadora de Kundalini"),
              ("Neurobiología", "con Mario Alonso Puig"),
              ("Hipnosis y Biodescodificación", "del Dr. Hamer"),
              ("Creadora del Método BNQ™", "y de la metodología CEI™, registrada ante INDAUTOR"),
              ("Autora del libro", "Las Fórmulas Cuánticas para Hackear tu Mente y la Matrix"),
              ("+5 años", "activando consciencias")]
    y = 300
    for titulo, detalle in puntos:
        d.ellipse([92, y + 14, 110, y + 32], fill=ORO)
        d.text((135, y), titulo, font=f(SANS, 40), fill=BLANCO)
        d.text((135, y + 50), detalle, font=f(SANS_REG, 28), fill=ORO_CLARO)
        y += 108
    pie(d)
    return img


def d18_preparate():
    img = universo(18)
    d = ImageDraw.Draw(img)
    y = encabezado(d, "VAMOS A LA ACTIVACIÓN", "Prepárate")
    for i, t in enumerate(["Ponte cómoda y suelta los hombros", "Audífonos puestos",
                           "Una mano en el pecho y otra en el estómago",
                           "Cierra los ojos cuando te lo indique"], 1):
        circulo_num(d, 130, y + 70, i)
        d.text((200, y + 40), t, font=f(SANS, 52), fill=BLANCO)
        y += 150
    pie(d)
    return img


def d19_hipnosis():
    img = universo(19)
    velo = Image.new("RGB", (W, H), (6, 4, 18))
    img = Image.blend(img, velo, 0.35)
    d = ImageDraw.Draw(img)
    for r, a in [(330, 60), (260, 90), (190, 130)]:
        capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(capa).ellipse([W / 2 - r, 420 - r, W / 2 + r, 420 + r], outline=ORO + (a,), width=3)
        img.paste(capa, (0, 0), capa)
    d = ImageDraw.Draw(img)
    for t, fu, y, c in [("AUTOHIPNOSIS EN VIVO", f(SANS, 40), 340, ORO),
                        ("Hackea tus bloqueos", f(SERIF, 76), 400, ORO_CLARO),
                        ("con el dinero", f(SERIF, 76), 480, ORO_CLARO),
                        ("F·05 Reprogramación de ADN · F·10 Reprogramar tu Subconsciente · F·08 Materializar",
                         f(SANS_REG, 32), 830, GRIS),
                        ("Cierra los ojos… y respira.", f(SANS, 46), 900, BLANCO)]:
        d.text((W / 2 - d.textlength(t, font=fu) / 2, y), t, font=fu, fill=c)
    return img


def d20_sentiste():
    return frase(20, "REGRESA AQUÍ", "¿Qué sentiste?", "Escríbelo en el chat en UNA palabra.")


def d21_uno_de_cinco():
    return frase(21, "ESTO APENAS EMPIEZA", "Esto fue 1 de 5.",
                 "Hoy hackeaste el dinero. El programa también vive en tus relaciones, "
                 "tu ansiedad, tu cansancio y tu propósito.")


def d22_pack():
    img = universo(22)
    portada = Image.open(PORTADA_PACK).convert("RGB").resize((700, 700), Image.LANCZOS)
    caja(img, (1110, 190, 1830, 910), 20)
    img.paste(portada, (1120, 200))
    d = ImageDraw.Draw(img)
    d.text((90, 80), "PARA SEGUIR HACKEANDO", font=f(SANS, 34), fill=ORO)
    y = parrafo(d, "LAS 5 HIPNOSIS QUE HACKEAN TU MATRIX", f(SERIF, 76), 90, 125, 960, ORO_CLARO, inter=1.05)
    y += 25
    for i, t in enumerate(["Dinero", "Relaciones tóxicas", "Ansiedad y modo supervivencia",
                           "Burnout y modo alarma", "Despertar, propósito y éxito"], 1):
        circulo_num(d, 120, y + 32, i, 28)
        d.text((175, y + 8), t, font=f(SANS, 42), fill=BLANCO)
        y += 88
    parrafo(d, "Método BNQ™ · con la voz de Mabel Soriano · cada una con los 3 procesos BNQ™ y su fórmula",
            f(SANS_REG, 30), 90, y + 25, 960, GRIS)
    pie(d)
    return img


def d23_regalo():
    img = universo(23)
    d = ImageDraw.Draw(img)
    y = encabezado(d, "Y ADEMÁS", "De regalo")
    regalos = [("Activaciones Robóticas Millonarias", "10 audios · 1 minuto para salir de la escasez"),
               ("Comunidad de WhatsApp", "Activaciones y acompañamiento con Mabel")]
    for i, (t, s) in enumerate(regalos):
        x0 = 90 + i * 890
        caja(img, (x0, y + 20, x0 + 850, y + 420))
        d = ImageDraw.Draw(img)
        d.text((x0 + 50, y + 70), "REGALO " + str(i + 1), font=f(SANS, 34), fill=ORO)
        yy = parrafo(d, t, f(SANS, 54), x0 + 50, y + 130, 750, ORO_CLARO)
        parrafo(d, s, f(SANS_REG, 38), x0 + 50, yy + 20, 750, BLANCO)
    pie(d)
    return img


def d24_precio():
    img = universo(24)
    d = ImageDraw.Draw(img)
    d.text((90, 80), "LAS 5 HIPNOSIS QUE HACKEAN TU MATRIX + REGALOS", font=f(SANS, 34), fill=ORO)
    d.text((90, 170), "Después del live:", font=f(SANS_REG, 46), fill=GRIS)
    fu = f(SANS, 70)
    d.text((540, 155), "$3,000", font=fu, fill=GRIS)
    d.line([(535, 200), (550 + d.textlength("$3,000", font=fu), 200)], fill=(230, 80, 90), width=7)
    d.text((90, 290), "SOLO HOY EN EL LIVE", font=f(SANS, 50), fill=ORO_CLARO)
    d.text((80, 350), "$2,500", font=f(SERIF, 250), fill=ORO_CLARO)
    d.text((820, 520), "MXN", font=f(SANS, 60), fill=ORO_CLARO)
    caja(img, (90, 690, 1060, 800), 24)
    d = ImageDraw.Draw(img)
    d.text((130, 718), "Cierra HOY a las 9:00 PM (CDMX)", font=f(SANS, 46), fill=BLANCO)
    d.text((90, 860), "pay.hotmart.com/T108210969W", font=f(SANS, 44), fill=ORO_CLARO)
    caja(img, (1260, 230, 1800, 830), 24, ORO_CLARO)
    img.paste(qr(460), (1300, 270))
    d = ImageDraw.Draw(img)
    t = "Escanea y entra"
    d.text((1530 - d.textlength(t, font=f(SANS, 40)) / 2, 755), t, font=f(SANS, 40), fill=ORO_CLARO)
    pie(d)
    return img


def d25_preguntas():
    img = universo(25)
    d = ImageDraw.Draw(img)
    d.text((90, 300), "¿Preguntas?", font=f(SERIF, 160), fill=ORO_CLARO)
    linea_oro(d, 92, 500, 520)
    parrafo(d, "El link está en el chat. Precio especial solo hasta hoy a las 9:00 PM (CDMX).",
            f(SANS, 46), 90, 550, 1000, BLANCO)
    caja(img, (1260, 230, 1800, 830), 24, ORO_CLARO)
    img.paste(qr(460), (1300, 270))
    d = ImageDraw.Draw(img)
    t = "pay.hotmart.com/T108210969W"
    d.text((1530 - d.textlength(t, font=f(SANS, 30)) / 2, 760), t, font=f(SANS, 30), fill=ORO_CLARO)
    pie(d)
    return img


def d26_cierre():
    img = foto_derecha(universo(26))
    d = ImageDraw.Draw(img)
    y = parrafo(d, "“La fórmula definitiva no es un decreto, es la BIO-NEUROABUNDANCIA: la reprogramación "
                   "simultánea de tu ADN, tu energía y tu subconsciente.”", f(SERIF, 58), 90, 170, 1060,
                ORO_CLARO, inter=1.15)
    linea_oro(d, 92, int(y) + 25, 520)
    parrafo(d, "Porque lo que no se ACTIVA, NO CAMBIA.", f(SANS, 54), 90, y + 70, 1060, BLANCO)
    d.text((90, H - 170), "@mabradiante", font=f(SANS, 60), fill=ORO)
    d.text((90, H - 90), "Gracias por activarte hoy", font=f(SANS_REG, 36), fill=GRIS)
    return img


DIAPOSITIVAS = [d01_portada, d02_cuidados, d03_hoy, d04_dolor, d05_culpa, d06_sistema, d07_piloto, d08_bnq,
                d09_neuro, d10_taxistas, d11_aprovechar, d12_historia, d13_kirsch, d14_stanford, d15_ecuacion,
                d16_todo, d17_quien_soy, d18_preparate, d19_hipnosis, d20_sentiste, d21_uno_de_cinco,
                d22_pack, d23_regalo, d24_precio, d25_preguntas, d26_cierre]


def armar():
    from pptx import Presentation
    from pptx.util import Emu

    SALIDA.mkdir(exist_ok=True)
    rutas = []
    for fn in DIAPOSITIVAS:
        ruta = SALIDA / (fn.__name__[1:3] + "_" + fn.__name__[4:] + ".png")
        fn().save(ruta)
        rutas.append(ruta)
    pres = Presentation()
    pres.slide_width, pres.slide_height = Emu(12192000), Emu(6858000)
    for ruta in rutas:
        s = pres.slides.add_slide(pres.slide_layouts[6])
        s.shapes.add_picture(str(ruta), 0, 0, pres.slide_width, pres.slide_height)
    pres.save(AQUI / "presentacion-live-2026-10-27.pptx")
    imgs = [Image.open(r).convert("RGB") for r in rutas]
    imgs[0].save(AQUI / "presentacion-live-2026-10-27.pdf", save_all=True, append_images=imgs[1:])
    return rutas


if __name__ == "__main__":
    for r in armar():
        print(r.name)
