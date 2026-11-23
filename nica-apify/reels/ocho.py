"""Video de 8 s estilo 'señales' (hook en pantalla, lista en el caption).
Uso: python3 ocho.py "HOOK EN PANTALLA" geometria salida.mp4"""
import subprocess, sys, tempfile
from pathlib import Path
from reel_movimiento import partir, ts, FPS
AQUI = Path(__file__).parent
FONDO = AQUI.parent / "marca" / "fondo-cosmico-limpio.jpg"
T = 8.0

def main(hook, geo, salida):
    tmp = Path(tempfile.mkdtemp())
    ass = tmp / "s.ass"
    cab = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\n\n[V4+ Styles]\n"
           "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, "
           "Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
           "Style: Hook,Liberation Serif,96,&H0060D8F5,&H000000FF,&H00102040,&H80000000,1,0,0,0,100,100,1,0,1,6,4,8,60,60,220,1\n"
           "Style: Firma,Liberation Serif,58,&H0060D8F5,&H000000FF,&H00102040,&H80000000,1,0,0,0,100,100,2,0,1,3,2,2,60,60,210,1\n"
           "Style: Sub,DejaVu Sans,34,&H00FFFFFF,&H000000FF,&H00102040,&H80000000,0,0,0,0,100,100,0,0,1,2,1,2,60,60,120,1\n"
           "Style: Flecha,Liberation Serif,64,&H0060D8F5,&H000000FF,&H00102040,&H80000000,1,0,0,0,100,100,0,0,1,4,2,5,0,0,0,1\n\n"
           "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    pop = r"{\fad(200,0)\fscx70\fscy70\t(0,300,\fscx100\fscy100)}"
    filas = [f"Dialogue: 1,{ts(0)},{ts(T)},Hook,,0,0,0,,{pop}{partir(hook.upper(), 18)}",
             f"Dialogue: 1,{ts(0)},{ts(T)},Firma,,0,0,0,,@mabradiante",
             f"Dialogue: 1,{ts(0)},{ts(T)},Sub,,0,0,0,,Método BNQ™ · Las Fórmulas Cuánticas\\Npara Hackear tu Mente y la Matrix",
             r"Dialogue: 2,%s,%s,Flecha,,0,0,0,,{\pos(540,1480)\t(0,500,\fscx120\fscy120)\t(500,1000,\fscx100\fscy100)}▼ LEE AQUÍ ABAJO ▼" % (ts(2.5), ts(T))]
    ass.write_text(cab + "\n".join(filas) + "\n", encoding="utf-8")
    geo_png = AQUI.parent / "marca" / f"geo-{geo}.png"
    pad = ("aevalsrc='0.06*(sin(2*PI*130.81*t)+0.8*sin(2*PI*196*t)+0.7*sin(2*PI*329.63*t))*(0.7+0.3*sin(2*PI*0.3*t))':s=44100:d=%.1f" % T)
    fr = int(T * FPS)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(FONDO), "-loop", "1", "-framerate", str(FPS), "-i", str(geo_png),
                    "-f", "lavfi", "-i", pad, "-filter_complex",
                    f"[0:v]scale=2160:3840,zoompan=z='1+0.0015*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={fr}:s=1080x1920:fps={FPS},eq=brightness=-0.08[bg];"
                    f"[1:v]format=rgba,scale=900:900,rotate=a='t*0.35':c=none:ow=900:oh=900[g];"
                    f"[bg][g]overlay=x=(W-w)/2:y=(H-h)/2+40:shortest=1,ass={ass}[v];[2:a]afade=t=in:d=1,afade=t=out:st={T-1}:d=1,volume=0.6[a]",
                    "-map", "[v]", "-map", "[a]", "-t", str(T), "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-movflags", "+faststart", salida], check=True)

if __name__ == "__main__":
    main(*sys.argv[1:4])
