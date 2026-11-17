"""Video de 12 s: clip 1 (dolor, 6 s) + clip 2 (solución + CTA, 6 s) con textos y firma. Sin audio
(Mabel pone canción de moda). Uso: python3 armar12.py clip1.mp4 clip2.mp4 textos.txt salida.mp4
textos.txt: línea 1 = texto del dolor; línea 2 = título de la solución; línea 3 = frase de la fórmula; línea 4 = CTA.
"""
import subprocess, sys, tempfile
from pathlib import Path

c1, c2, textos, salida = sys.argv[1:5]
dolor, solucion, formula, cta = [l.strip() for l in Path(textos).read_text(encoding="utf-8").splitlines()[:4]]
ass = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Dolor,Montserrat ExtraBold,78,&H00FFFFFF,&H00FFFFFF,&H00000000,&H78000000,0,0,0,0,100,100,0,0,1,5,4,5,90,90,0,1
Style: Sol,Montserrat ExtraBold,76,&H0058D7FF,&H00FFFFFF,&H00000000,&H78000000,0,0,0,0,100,100,0,0,1,5,4,5,90,90,0,1
Style: Formula,Montserrat SemiBold,40,&H00FFFFFF,&H00FFFFFF,&H00000000,&H78000000,0,0,0,0,100,100,0,0,1,3,3,5,110,110,0,1
Style: Cta,Montserrat ExtraBold,54,&H00101820,&H00FFFFFF,&H0058D7FF,&H0058D7FF,0,0,0,0,100,100,1,0,3,14,0,5,90,90,0,1
Style: Firma,Great Vibes,92,&H007AC7E8,&H00FFFFFF,&H00102030,&H64000000,0,0,0,0,100,100,0,0,1,1.5,3,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.20,0:00:06.00,Dolor,,0,0,0,,{{\\pos(540,620)\\fad(250,150)}}{dolor}
Dialogue: 0,0:00:06.10,0:00:12.00,Sol,,0,0,0,,{{\\pos(540,520)\\fad(200,0)}}{solucion}
Dialogue: 0,0:00:07.00,0:00:12.00,Formula,,0,0,0,,{{\\pos(540,820)\\fad(250,0)}}{formula}
Dialogue: 0,0:00:08.50,0:00:12.00,Cta,,0,0,0,,{{\\pos(540,1080)\\fad(200,0)}}{cta}
Dialogue: 0,0:00:00.00,0:00:12.00,Firma,,0,0,0,,{{\\pos(540,1290)}}@mabradiante
"""
f = tempfile.NamedTemporaryFile("w", suffix=".ass", delete=False, encoding="utf-8"); f.write(ass); f.close()
norm = "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30,trim=0:6,setpts=PTS-STARTPTS"
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", c1, "-i", c2, "-filter_complex",
    f"[0:v]{norm},eq=brightness=-0.08[a];[1:v]{norm}[b];[a][b]xfade=transition=fade:duration=0.3:offset=5.85,"
    f"ass={f.name}[v]", "-map", "[v]", "-an", "-t", "12", "-c:v", "libx264", "-crf", "19", "-pix_fmt", "yuv420p",
    "-movflags", "+faststart", salida], check=True)
print(salida)
