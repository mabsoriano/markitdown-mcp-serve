"""Genera un fondo cósmico (morado/azul + dorado, flor de la vida) 2160x3840 sin texto ni rostro."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFilter

def fondo(salida, semilla=7):
    random.seed(semilla)
    W, H = 2160, 3840
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        t = y / H
        r, g, b = int(20 + 40 * t), int(8 + 10 * t), int(50 + 30 * (1 - t))
        for x in range(0, W):
            px[x, y] = (r, g, b)
    neb = Image.new("RGB", (W, H)); d = ImageDraw.Draw(neb)
    for _ in range(14):
        cx, cy, rr = random.randint(0, W), random.randint(0, H), random.randint(400, 1100)
        col = random.choice([(120, 40, 160), (40, 60, 170), (190, 130, 40), (90, 30, 120)])
        d.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), fill=col)
    neb = neb.filter(ImageFilter.GaussianBlur(260))
    img = Image.blend(img, neb, 0.55)
    d = ImageDraw.Draw(img)
    for _ in range(2600):
        x, y, s = random.randint(0, W), random.randint(0, H), random.choice([1, 1, 2, 2, 3, 4])
        c = random.choice([(255, 255, 255), (255, 230, 160), (250, 210, 120)])
        d.ellipse((x, y, x + s, y + s), fill=c)
    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dc = ImageDraw.Draw(capa)
    cx, cy, R = W // 2, int(H * 0.47), 330
    centros = [(cx, cy)] + [(cx + R * math.cos(a), cy + R * math.sin(a)) for a in [i * math.pi / 3 for i in range(6)]]
    for (x, y) in centros:
        dc.ellipse((x - R, y - R, x + R, y + R), outline=(235, 195, 110, 150), width=7)
    dc.ellipse((cx - 2 * R - 40, cy - 2 * R - 40, cx + 2 * R + 40, cy + 2 * R + 40), outline=(235, 195, 110, 170), width=10)
    glow = capa.filter(ImageFilter.GaussianBlur(14))
    img = img.convert("RGBA"); img.alpha_composite(glow); img.alpha_composite(capa)
    halo = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dh = ImageDraw.Draw(halo)
    dh.ellipse((cx - 600, cy - 600, cx + 600, cy + 600), fill=(255, 200, 110, 70))
    img.alpha_composite(halo.filter(ImageFilter.GaussianBlur(200)))
    img.convert("RGB").save(salida, quality=92)

if __name__ == "__main__":
    fondo(sys.argv[1])
