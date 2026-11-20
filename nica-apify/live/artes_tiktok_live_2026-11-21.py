"""Arte AVISO TikTok LIVE (sáb 21 y mar 24 · 8:30 PM), 9:16, sin precio, sin @.
Reutiliza el generador del live del 25 (live/artes_live_2026-11-25.py): mismas funciones de fondo, foto y textos."""
import pathlib
from PIL import ImageDraw

BASE = pathlib.Path(__file__).with_name("artes_live_2026-11-25.py").read_text(encoding="utf-8")
exec(BASE.split("# ---------- 4:5 ----------")[0])  # solo funciones y colores, no genera las artes del 25

W, H = 1080, 1920
bg = fondo(W, H, seed=23); bg = foto_arco(bg, 290, 650, 500, 640); d = ImageDraw.Draw(bg)
pill(d, "● EN VIVO EN TIKTOK", F(SAN, 40), W/2, 190, ROJO, (255, 255, 255), padx=46)
y = centro(d, "Hackea tus bloqueos", F(SER, 94), 290, CAFE, 40, W-80)
y = centro(d, "con el dinero", F(SER, 94), y, CAFE, 40, W-80)
y = centro(d, "en simultáneo", F(SER, 116), y+4, ORO, 40, W-80, stroke=CREMA)
print("title_end", y)
f = F(SAN, 34); items = ["Subconsciente", "Memoria celular", "Energía"]
tot = sum(d.textlength(t, font=f) + 60 for t in items) + 2*20; x = (W - tot)/2; yr = 1330
for t in items:
    tw = d.textlength(t, font=f)
    d.rounded_rectangle((x, yr, x+tw+60, yr+76), 38, fill=(255, 246, 214), outline=ORO, width=3)
    d.text((x+30, yr+18), t, font=f, fill=CAFE); x += tw + 60 + 20
d.rounded_rectangle((150, 1430, 930, 1592), 30, fill=ORO)
centro(d, "HOY · 8:30 PM", F(SER, 72), 1440, (255, 238, 180), 150, 780)
centro(d, "hora Monterrey / CDMX", F(SAN, 36), 1530, CREMA, 150, 780)
pill(d, "Comenta ABUNDANCIA", F(SAN, 54), W/2, 1618, CAFE, ORO2, padx=60, pady=24, outline=ORO2)
centro(d, "Mabel Soriano · BNQ Method™", F(SAN, 34), 1748, CAFE, 0, W)
bg.save("/home/user/TIKTOK-LIVE-AVISO-9x16.jpg", quality=93)
print("ok")
