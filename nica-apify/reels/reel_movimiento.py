"""Reel faceless EN MOVIMIENTO (1080x1920): fondo con zoom lento + frases que aparecen al ritmo de la voz.

Uso:  python3 reel_movimiento.py guion.txt "TÍTULO HOOK" salida.mp4 [fondo.jpg]
Guion: una frase por línea; una línea con solo un número = pausa en segundos.
"""
import subprocess, sys, tempfile
from pathlib import Path

AQUI = Path(__file__).parent
sys.path.insert(0, str(AQUI.parent / "whatsapp"))
import audio  # noqa: E402

FONDO = AQUI.parent / "marca" / "fondo-cosmico-faceless.jpg"
FPS = 30


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                capture_output=True, text=True).stdout)


def ts(s):
    h, s = divmod(s, 3600); m, s = divmod(s, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def ass_escape(t):
    return t.replace("{", "(").replace("}", ")")


def partir(t, n=22):
    pal, lineas, act = t.split(), [], ""
    for w in pal:
        if len(act) + len(w) + 1 > n and act:
            lineas.append(act); act = w
        else:
            act = (act + " " + w).strip()
    lineas.append(act)
    return r"\N".join(lineas)


def main(guion, titulo, salida, fondo=FONDO):
    tmp = Path(tempfile.mkdtemp())
    partes, eventos, t = [], [], 0.0
    for i, linea in enumerate(Path(guion).read_text(encoding="utf-8").splitlines()):
        linea = linea.strip()
        p = tmp / f"{i:03d}.wav"
        try:
            audio.silencio(float(linea) if linea else 0.5, p)
            partes.append(p); t += dur(p)
        except ValueError:
            mp3 = tmp / f"{i:03d}.mp3"
            audio.voz(linea, mp3)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mp3, "-ar", "24000", "-ac", "1", p], check=True)
            d = dur(p)
            eventos.append((t, t + d + 0.3, linea))
            partes.append(p); t += d
            q = tmp / f"{i:03d}b.wav"; audio.silencio(0.35, q); partes.append(q); t += dur(q)
    lista = tmp / "lista.txt"
    lista.write_text("".join(f"file '{p}'\n" for p in partes))
    wav = tmp / "voz.m4a"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lista,
                    "-af", "loudnorm", "-ar", "44100", "-c:a", "aac", "-b:a", "128k", wav], check=True)
    total = dur(wav)

    # Subtítulos ASS: título fijo arriba + frase grande que aparece con efecto "pop".
    ass = tmp / "subs.ass"
    cab = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\n\n[V4+ Styles]\n"
           "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, "
           "Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, "
           "MarginR, MarginV, Encoding\n"
           "Style: Titulo,Liberation Serif,74,&H0060D8F5,&H000000FF,&H00102040,&H80000000,1,0,0,0,100,100,1,0,1,5,3,8,60,60,130,1\n"
           "Style: Frase,DejaVu Sans,82,&H00FFFFFF,&H000000FF,&H00143C78,&H90000000,1,0,0,0,100,100,0,0,1,6,4,5,70,70,0,1\n\n"
           "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    filas = [f"Dialogue: 1,{ts(0)},{ts(total)},Titulo,,0,0,0,,{ass_escape(partir(titulo.upper(), 20))}"]
    for a, b, txt in eventos:
        anim = r"{\fad(120,120)\fscx70\fscy70\t(0,180,\fscx100\fscy100)}"
        filas.append(f"Dialogue: 2,{ts(a)},{ts(min(b, total))},Frase,,0,0,0,,{anim}{ass_escape(partir(txt))}")
    ass.write_text(cab + "\n".join(filas) + "\n", encoding="utf-8")

    frames = int(total * FPS) + FPS
    vf = (f"scale=2160:3840,"
          f"zoompan=z='min(1+0.0004*on,1.25)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)+sin(on/90)*40':"
          f"d={frames}:s=1080x1920:fps={FPS},"
          f"eq=brightness=-0.12:saturation=1.1,"
          f""
          f"ass={ass}")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(fondo), "-i", wav,
                    "-vf", vf, "-t", f"{total:.2f}", "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p",
                    "-r", str(FPS), "-c:a", "copy", "-shortest", "-movflags", "+faststart", salida], check=True)
    print(salida, round(total, 1), "s")


if __name__ == "__main__":
    main(*sys.argv[1:5])
