"""Arma un reel vertical: avatar (gancho) + voz con fondo de foto, tarjetas y subtítulos.
Uso: python3 armar_reel.py config.json
"""
import json, subprocess, sys, re, os

cfg = json.load(open(sys.argv[1]))
W, H, FPS = 1080, 1920, 30
work = cfg["work"]; os.makedirs(work, exist_ok=True)
VERDE, CREMA, ORO = "&H002E3D0F", "&H00E6EFF5", "&H004BA2C9"  # ASS usa BGR


def run(*a):
    subprocess.run(a, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def dur(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", p]).decode())


# 1) gancho: avatar a 1080x1920 (rellenar y recortar)
hook = f"{work}/hook.mp4"
run("ffmpeg", "-y", "-i", cfg["avatar"], "-vf",
    f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},format=yuv420p",
    "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-c:a", "aac", "-ar", "44100", "-ac", "2", hook)
hd = dur(hook)

# 2) cuerpo: fondo = foto difuminada con zoom lento
rest = cfg["voz"]; rd = dur(rest)
frames = int(rd * FPS) + 1
body = f"{work}/body.mp4"
run("ffmpeg", "-y", "-loop", "1", "-i", cfg["foto"], "-i", rest, "-filter_complex",
    f"[0:v]scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
    f"zoompan=z='min(1+0.0004*on,1.25)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={FPS},"
    f"gblur=sigma=10,eq=brightness=-0.28:saturation=0.85,format=yuv420p[v]",
    "-map", "[v]", "-map", "1:a", "-t", f"{rd:.2f}", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
    "-c:a", "aac", "-ar", "44100", "-ac", "2", body)

# 3) tiempos de cada frase: proporcional a letras, ajustado a silencios reales
sil = subprocess.run(["ffmpeg", "-i", rest, "-af", "silencedetect=n=-32dB:d=0.25", "-f", "null", "-"],
                     stderr=subprocess.PIPE).stderr.decode()
pausas = [(float(a) + float(b)) / 2 for a, b in zip(re.findall(r"silence_start: ([\d.]+)", sil),
                                                    re.findall(r"silence_end: ([\d.]+)", sil))]
frases = cfg["frases"]
tot = sum(len(f["t"]) for f in frases); acc = 0; cortes = [0.0]
for f in frases[:-1]:
    acc += len(f["t"]); t = rd * acc / tot
    cerca = [p for p in pausas if abs(p - t) < 1.2 and p > cortes[-1] + 0.6]
    cortes.append(min(cerca, key=lambda p: abs(p - t)) if cerca else t)
cortes.append(rd)


def ts(s):
    s += hd
    return f"{int(s//3600)}:{int(s%3600//60):02d}:{s%60:05.2f}"


def ass_txt(t):
    return t.replace("\n", "\\N")


ev = []
# título en el gancho
ev.append(f"Dialogue: 1,0:00:00.00,0:00:{min(hd,3.5):05.2f},Titulo,,0,0,0,,{ass_txt(cfg['titulo'])}")
# subtítulos del gancho
ev.append(f"Dialogue: 0,0:00:00.00,0:00:{hd:05.2f},Sub,,0,0,0,,{ass_txt(cfg['gancho'])}")
for f, a, b in zip(frases, cortes, cortes[1:]):
    estilo = "Tarjeta" if f.get("tarjeta") else "Sub"
    ev.append(f"Dialogue: 0,{ts(a)},{ts(b)},{estilo},,0,0,0,,{ass_txt(f.get('pantalla', f['t']))}")
ev.append(f"Dialogue: 2,0:00:00.00,{ts(rd)},Marca,,0,0,0,,@mabradiante")

ass = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Titulo,Inter Display ExtraBold,78,{CREMA},{CREMA},{VERDE},&H66000000,1,0,0,0,100,100,0,0,3,24,0,8,70,70,230,1
Style: Sub,Inter ExtraBold,62,{CREMA},{CREMA},&H00000000,&HAA000000,1,0,0,0,100,100,0,0,1,6,3,2,80,80,360,1
Style: Tarjeta,Inter Display ExtraBold,80,{CREMA},{CREMA},{VERDE},&H00000000,1,0,0,0,100,100,0,0,3,34,0,5,90,90,0,1
Style: Marca,Inter SemiBold,40,{CREMA},{CREMA},&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,0,2,0,0,90,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(ev) + "\n"
open(f"{work}/subs.ass", "w").write(ass)

# 4) unir y quemar subtítulos
lista = f"{work}/lista.txt"
open(lista, "w").write(f"file '{hook}'\nfile '{body}'\n")
junto = f"{work}/junto.mp4"
run("ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lista, "-c", "copy", junto)
run("ffmpeg", "-y", "-i", junto, "-vf", f"ass={work}/subs.ass", "-c:v", "libx264", "-preset", "medium",
    "-crf", "20", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", cfg["salida"])
print("listo", cfg["salida"], round(dur(cfg["salida"]), 1), "s; cortes:", [round(c, 1) for c in cortes])
