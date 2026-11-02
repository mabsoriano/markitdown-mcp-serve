"""Video LARGO de NAIA para YouTube (16:9) con música suave, encabezados y subtítulos.

Uso: python3 video_naia_largo.py guion.txt voz.mp3 clip_naia.mp4 salida.mp4
El guion es el mismo que se le dio a audio.py: las líneas "# TEXTO" son encabezados
que se ven arriba (la primera también es el título de los primeros 3 s).
"""
import re, subprocess, sys, tempfile
from pathlib import Path

INTRO = 2.0   # segundos de música antes de la voz
OUTRO = 4.0


def segmentos(mp3):
    out = subprocess.run(["ffmpeg", "-i", mp3, "-af", "silencedetect=noise=-38dB:d=0.28", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", out)]
    en = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", out)]
    segs, cur = [], 0.0
    for s, e in zip(st, en):
        if s - cur > 0.05:
            segs.append((cur, s))
        cur = e
    return segs


def t(x):
    return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"


def main(guion, voz, clip, salida):
    frases, encabezados, actual = [], [], None
    for l in Path(guion).read_text(encoding="utf-8").splitlines():
        l = l.strip()
        if l.startswith("#"):
            actual = l.lstrip("# ").strip()
            encabezados.append([actual, None])
        elif l and not re.fullmatch(r"[0-9.]+", l):
            frases.append((l, len(encabezados) - 1))
    tsv = Path(voz + ".tiempos.tsv")
    if tsv.exists():   # tiempos exactos que anota audio.py
        segs = [(float(a), float(b)) for a, b, _ in (l.split("\t", 2) for l in tsv.read_text(encoding="utf-8").splitlines())]
    else:
        segs = segmentos(voz)
    assert len(segs) == len(frases), (len(segs), len(frases))
    dur_voz = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", voz],
                                   capture_output=True, text=True).stdout)
    fin = INTRO + dur_voz + OUTRO
    for (texto, h), (a, b) in zip(frases, segs):
        if encabezados[h][1] is None:
            encabezados[h][1] = INTRO + a
    ass = ["[Script Info]", "ScriptType: v4.00+", "WrapStyle: 0", "PlayResX: 1920", "PlayResY: 1080", "",
           "[V4+ Styles]",
           "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
           "Style: Sub,DejaVu Sans,66,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,1,0,0,0,100,100,0,0,1,4,3,5,110,760,0,1",
           "Style: Enc,DejaVu Serif,46,&H0058D7FF,&H00FFFFFF,&H00000000,&H96000000,1,0,0,0,100,100,3,0,1,3,2,8,110,760,80,1",
           "Style: Tit,DejaVu Serif,104,&H0058D7FF,&H00FFFFFF,&H00000000,&H96000000,1,0,0,0,100,100,3,0,1,5,3,5,110,760,0,1",
           "Style: Firma,DejaVu Sans,34,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,1,0,0,0,100,100,2,0,1,2,2,2,110,760,50,1",
           "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    # Columna de texto a la izquierda (NAIA va a la derecha)
    ass.append(f"Dialogue: 2,{t(0)},{t(3.5)},Tit,,0,0,0,,{{\\fad(300,400)}}{encabezados[0][0]}")
    for i, (texto, inicio) in enumerate(encabezados):
        if inicio is None:
            continue
        final = next((e[1] for e in encabezados[i + 1:] if e[1] is not None), fin)
        ass.append(f"Dialogue: 1,{t(max(inicio, 3.5))},{t(final)},Enc,,0,0,0,,{texto}")
    for i, ((texto, _), (a, b)) in enumerate(zip(frases, segs)):
        fin_sub = INTRO + segs[i + 1][0] if i + 1 < len(segs) else fin
        texto = texto.replace("Mabradiante", "@mabradiante")
        ass.append(f"Dialogue: 0,{t(INTRO + a)},{t(fin_sub)},Sub,,0,0,0,,{texto}")
    ass.append(f"Dialogue: 0,{t(0)},{t(fin)},Firma,,0,0,0,,NAIA · @mabradiante · Método BNQ™")
    f = tempfile.NamedTemporaryFile("w", suffix=".ass", delete=False, encoding="utf-8")
    f.write("\n".join(ass))
    f.close()
    # Fondo: el clip ampliado, desenfocado y oscuro; NAIA nítida a la derecha.
    # Música: acorde suave y lento hecho con ondas (gratis), muy por debajo de la voz.
    musica = ("aevalsrc='0.5*sin(2*PI*110*t)*(0.65+0.35*sin(2*PI*0.04*t))"
              "+0.35*sin(2*PI*164.81*t)*(0.65+0.35*sin(2*PI*0.03*t+1))"
              "+0.25*sin(2*PI*220*t)*(0.6+0.4*sin(2*PI*0.05*t+2))"
              f"+0.15*sin(2*PI*329.63*t)*(0.5+0.5*sin(2*PI*0.02*t))':s=44100:d={fin}")
    filtro = (
        "[0:v]split[a][b];"
        "[a]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,boxblur=30:3,eq=brightness=-0.22[bg];"
        "[b]scale=-2:1080[fg];"
        "[bg][fg]overlay=x=1920-w-110:y=0,"
        f"ass={f.name},fade=t=in:st=0:d=1,fade=t=out:st={fin - 1.5}:d=1.5[v];"
        f"[1:a]adelay={int(INTRO * 1000)}|{int(INTRO * 1000)},apad[voz];"
        f"[2:a]lowpass=f=900,aecho=0.8:0.7:120:0.4,volume=0.05,afade=t=in:d=2,afade=t=out:st={fin - 3}:d=3[mus];"
        "[voz][mus]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-15[a]"
    )
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-stream_loop", "-1", "-i", clip, "-i", voz,
                    "-f", "lavfi", "-i", musica, "-filter_complex", filtro,
                    "-map", "[v]", "-map", "[a]", "-t", str(fin), "-r", "30",
                    "-c:v", "libx264", "-crf", "24", "-preset", "fast", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", salida], check=True)
    caps = [(INTRO + segs[[j for j, (_, h) in enumerate(frases) if h == i][0]][0], e[0])
            for i, e in enumerate(encabezados) if any(h == i for _, h in frases)]
    print(salida, round(fin, 1))
    for s, e in caps:
        print(f"{int(s // 60)}:{int(s % 60):02d} {e}")


if __name__ == "__main__":
    main(*sys.argv[1:5])
