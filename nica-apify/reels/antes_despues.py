"""Video 12-15 s ANTES/DESPUÉS con voz + música + firmas.
Uso: python3 antes_despues.py guion.txt "TÍTULO" clip_antes.mp4 clip_despues.mp4 salida.mp4
Si clip_antes == clip_despues, el ANTES se hace en gris y apagado (transformación)."""
import subprocess, sys, tempfile
from pathlib import Path
from reel_movimiento import partir, ts, dur, ass_escape, FPS
sys.path.insert(0, str(Path(__file__).parent.parent / "whatsapp"))
import audio

def main(guion, titulo, antes, despues, salida):
    tmp = Path(tempfile.mkdtemp()); partes, eventos, t = [], [], 0.0
    for i, l in enumerate(Path(guion).read_text(encoding="utf-8").splitlines()):
        l = l.strip()
        if not l: continue
        p = tmp / f"{i}.wav"
        try:
            audio.silencio(float(l), p); partes.append(p); t += dur(p); continue
        except ValueError: pass
        mp3 = tmp / f"{i}.mp3"; audio.voz(l, mp3)
        subprocess.run(["ffmpeg","-y","-loglevel","error","-i",mp3,"-ar","24000","-ac","1","-af","atempo=1.12",p],check=True)
        d = dur(p); eventos.append((t, t+d+0.15, l)); partes.append(p); t += d
        q = tmp/f"{i}b.wav"; audio.silencio(0.2, q); partes.append(q); t += dur(q)
    (tmp/"l.txt").write_text("".join(f"file '{p}'\n" for p in partes))
    voz = tmp/"voz.m4a"
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",tmp/"l.txt","-af","loudnorm","-ar","44100","-c:a","aac",voz],check=True)
    total = max(dur(voz) + 0.6, 12.0); mitad = total / 2
    cab = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\n\n[V4+ Styles]\n"
           "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
           "Style: Titulo,Liberation Serif,74,&H0060D8F5,&H000000FF,&H00102040,&H80000000,1,0,0,0,100,100,1,0,1,5,3,8,60,60,130,1\n"
           "Style: Frase,DejaVu Sans,66,&H00FFFFFF,&H000000FF,&H00143C78,&H90000000,1,0,0,0,100,100,0,0,1,6,4,2,70,70,560,1\n"
           "Style: Firma,Liberation Serif,58,&H0060D8F5,&H000000FF,&H00102040,&H80000000,1,0,0,0,100,100,2,0,1,3,2,2,60,60,210,1\n"
           "Style: Sub,DejaVu Sans,34,&H00FFFFFF,&H000000FF,&H00102040,&H80000000,0,0,0,0,100,100,0,0,1,2,1,2,60,60,120,1\n\n"
           "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    f = [f"Dialogue: 1,{ts(0)},{ts(total)},Titulo,,0,0,0,,{ass_escape(partir(titulo.upper(),20))}",
         f"Dialogue: 1,{ts(0)},{ts(total)},Firma,,0,0,0,,@mabradiante",
         f"Dialogue: 1,{ts(0)},{ts(total)},Sub,,0,0,0,,Método BNQ™ · Las Fórmulas Cuánticas\\Npara Hackear tu Mente y la Matrix"]
    for a, b, x in eventos:
        f.append(f"Dialogue: 2,{ts(a)},{ts(min(b,total))},Frase,,0,0,0,,{{\\fad(100,100)}}{ass_escape(partir(x,24))}")
    ass = tmp/"s.ass"; ass.write_text(cab+"\n".join(f)+"\n", encoding="utf-8")
    pad = ("aevalsrc='0.06*(sin(2*PI*130.81*t)+0.8*sin(2*PI*196*t)+0.7*sin(2*PI*329.63*t)+0.5*sin(2*PI*587.33*t))*(0.7+0.3*sin(2*PI*0.08*t))"
           "+0.03*(sin(2*PI*174.61*t)+sin(2*PI*261.63*t)+sin(2*PI*440*t))*(0.5+0.5*sin(2*PI*0.05*t+1))':s=44100:d=%.2f" % (total+1))
    musica = tmp/"m.m4a"
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","lavfi","-i",pad,"-af","aecho=0.8:0.85:600|1200:0.35|0.25,lowpass=f=2500,afade=t=in:d=1,afade=t=out:st=%.2f:d=1.5,volume=0.55"%(total-1.5),"-ac","2","-c:a","aac",musica],check=True)
    base = "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30"
    gris = ",eq=saturation=0.05:brightness=-0.12:contrast=0.9" if antes == despues else ""
    def tramo(src, d, extra):
        return ["-stream_loop","-1","-i",src], f"{base},trim=0:{d:.2f},setpts=PTS-STARTPTS{extra}"
    i1, f1 = tramo(antes, mitad, gris); i2, f2 = tramo(despues, total-mitad, "")
    subprocess.run(["ffmpeg","-y","-loglevel","error",*i1,*i2,"-i",voz,"-i",musica,"-filter_complex",
        f"[0:v]{f1}[a];[1:v]{f2}[b];[a][b]xfade=transition=fadewhite:duration=0.6:offset={mitad-0.3:.2f},ass={ass}[v];"
        f"[3:a]volume=0.35[m];[2:a][m]amix=inputs=2:duration=longest:normalize=0[au]",
        "-map","[v]","-map","[au]","-t",f"{total:.2f}","-c:v","libx264","-preset","veryfast","-pix_fmt","yuv420p",
        "-c:a","aac","-b:a","160k","-movflags","+faststart",salida],check=True)
    print(salida, round(total,1))

if __name__ == "__main__":
    main(*sys.argv[1:6])
