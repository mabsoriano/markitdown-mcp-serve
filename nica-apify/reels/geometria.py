"""Geometrías sagradas doradas (PNG transparente 1400x1400) para los reels faceless.
Uso: python3 geometria.py nombre salida.png   nombres: flor, semilla, metatron, merkaba, sriyantra
"""
import math, sys
from PIL import Image, ImageDraw, ImageFilter

N, C = 1400, 700
ORO, ORO2 = (240, 200, 115, 235), (255, 225, 150, 200)

def circ(d, x, y, r, w=6, col=ORO):
    d.ellipse((x - r, y - r, x + r, y + r), outline=col, width=w)

def tri(d, cx, cy, r, ang, w=7, col=ORO):
    p = [(cx + r * math.cos(ang + k * 2 * math.pi / 3), cy + r * math.sin(ang + k * 2 * math.pi / 3)) for k in range(3)]
    d.line(p + [p[0]], fill=col, width=w, joint="curve")

def dibujar(nombre):
    img = Image.new("RGBA", (N, N), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    if nombre in ("flor", "semilla"):
        r = 150
        pts = {(0.0, 0.0)}
        anillos = 2 if nombre == "flor" else 1
        for k in range(anillos):
            for (x, y) in list(pts):
                for a in range(6):
                    pts.add((round(x + r * math.cos(a * math.pi / 3), 3), round(y + r * math.sin(a * math.pi / 3), 3)))
        for (x, y) in pts:
            if math.hypot(x, y) <= 2 * r + 1:
                circ(d, C + x, C + y, r)
        circ(d, C, C, 3 * r + 20, 9); circ(d, C, C, 3 * r + 45, 4, ORO2)
    elif nombre == "metatron":
        r = 95; ctr = [(0, 0)]
        for k in range(6):
            a = k * math.pi / 3
            ctr += [(2 * r * math.cos(a), 2 * r * math.sin(a)), (4 * r * math.cos(a), 4 * r * math.sin(a))]
        for (x, y) in ctr: circ(d, C + x, C + y, r, 5)
        for i in range(len(ctr)):
            for j in range(i + 1, len(ctr)):
                d.line([(C + ctr[i][0], C + ctr[i][1]), (C + ctr[j][0], C + ctr[j][1])], fill=ORO2, width=3)
    elif nombre == "merkaba":
        circ(d, C, C, 560, 8); circ(d, C, C, 590, 3, ORO2)
        tri(d, C, C, 540, -math.pi / 2, 9); tri(d, C, C, 540, math.pi / 2, 9)
        tri(d, C, C, 270, -math.pi / 2, 5, ORO2); tri(d, C, C, 270, math.pi / 2, 5, ORO2)
        circ(d, C, C, 270, 4, ORO2)
    elif nombre == "sriyantra":
        for k, s in enumerate([560, 470, 380, 290, 200]):
            tri(d, C, C + (k - 2) * 18, s, math.pi / 2, 6)
        for k, s in enumerate([520, 410, 300, 190]):
            tri(d, C, C - (k - 1.5) * 18, s, -math.pi / 2, 6, ORO2)
        circ(d, C, C, 600, 8); circ(d, C, C, 630, 4, ORO2); circ(d, C, C, 12, 12)
        for a in range(16):
            ang = a * math.pi / 8
            x, y = C + 615 * math.cos(ang), C + 615 * math.sin(ang)
            circ(d, x, y, 40, 4, ORO2)
    glow = img.filter(ImageFilter.GaussianBlur(10))
    out = Image.new("RGBA", (N, N), (0, 0, 0, 0)); out.alpha_composite(glow); out.alpha_composite(glow); out.alpha_composite(img)
    return out

if __name__ == "__main__":
    dibujar(sys.argv[1]).save(sys.argv[2])
