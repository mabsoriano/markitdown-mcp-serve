"""Faceless PROBLEMA -> SOLUCIÓN con clips reales del banco, voz + música + firmas.
Uso: python3 problema_solucion.py guion.txt "TÍTULO" salida.mp4 N "p1.mp4,p2.mp4" "s1.mp4,s2.mp4,s3.mp4"
N = número de frase (0,1,2...) donde arranca la SOLUCIÓN (destello)."""
import subprocess, sys, tempfile
from pathlib import Path
from reel_movimiento import partir, ts, dur, ass_escape
sys.path.insert(0, str(Path(__file__).parent.parent / "whatsapp"))
import audio
X = 0.5  # duración del cruce entre clips

def run(*a): subprocess.run(["ffmpeg","-y","-loglevel","error",*map(str,a)], check=True)

def tramo(clips, D, tmp, tag):
    per = (D + X*(len(clips)-1)) / len(clips); outs = []
    for k, c in enumerate(clips):
        o = tmp/f"{tag}{k}.mp4"; d0 = dur(c); f = max(per/d0, 1.0)
        run("-i", c, "-vf", f"setpts={f:.4f}*PTS,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,"
            f"zoompan=z='1+0.0006*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30",
            "-t", f"{per:.2f}", "-an", "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", o)
        outs.append((o, per))
    return outs

def main(guion, titulo, salida, n, prob, sol):
    tmp = Path(tempfile.mkdtemp()); partes, ev, t = [], [], 0.0
    for i, l in enumerate(Path(guion).read_text(encoding="utf-8").splitlines()):
        l = l.strip()
        if not l: continue
        p = tmp/f"{i}.wav"
        try: audio.silencio(float(l), p); partes.append(p); t += dur(p); continue
        except ValueError: pass
        m = tmp/f"{i}.mp3"; audio.voz(l, m); run("-i", m, "-ar", "24000", "-ac", "1", p)
        d = dur(p); ev.append((t, t+d+0.3, l)); partes.append(p); t += d
        q = tmp/f"{i}b.wav"; audio.silencio(0.35, q); partes.append(q); t += dur(q)
    (tmp/"l.txt").write_text("".join(f"file '{p}'\n" for p in partes))
    voz = tmp/"voz.m4a"; run("-f","concat","-safe","0","-i",tmp/"l.txt","-af","loudnorm","-ar","44100","-c:a","aac",voz)
    total = dur(voz) + 0.5; T = ev[int(n)][0]
    segs = tramo(prob.split(","), T + X/2, tmp, "p") + tramo(sol.split(","), total - T + X/2, tmp, "s")
    # cadena de cruces; el de problema->solución es destello blanco
    np_ = len(prob.split(",")); ins, fc, off, prev = [], [], 0.0, "0:v"
    for k, (o, d) in enumerate(segs): ins += ["-i", o]
    for k in range(1, len(segs)):
        off += segs[k-1][1] - X
        tr = "fadewhite" if k == np_ else "fade"
        fc.append(f"[{prev}][{k}:v]xfade=transition={tr}:duration={X}:offset={off:.2f}[x{k}]"); prev = f"x{k}"
    base = tmp/"base.mp4"
    run(*ins, "-filter_complex", ";".join(fc), "-map", f"[{prev}]", "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", base)
    cab = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\n\n[V4+ Styles]\n"
           "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
           "Style: Titulo,Liberation Serif,74,&H0060D8F5,&H000000FF,&H00102040,&H80000000,1,0,0,0,100,100,1,0,1,6,3,8,60,60,130,1\n"
           "Style: Frase,DejaVu Sans,76,&H00FFFFFF,&H000000FF,&H00000000,&H90000000,1,0,0,0,100,100,0,0,1,7,4,5,70,70,0,1\n"
           "Style: Firma,Liberation Serif,58,&H0060D8F5,&H000000FF,&H00102040,&H80000000,1,0,0,0,100,100,2,0,1,4,2,2,60,60,210,1\n"
           "Style: Sub,DejaVu Sans,34,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,3,1,2,60,60,120,1\n\n"
           "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    f = [f"Dialogue: 1,{ts(0)},{ts(total)},Titulo,,0,0,0,,{ass_escape(partir(titulo.upper(),20))}",
         f"Dialogue: 1,{ts(0)},{ts(total)},Firma,,0,0,0,,@mabradiante",
         f"Dialogue: 1,{ts(0)},{ts(total)},Sub,,0,0,0,,Método BNQ™ · Las Fórmulas Cuánticas\\Npara Hackear tu Mente y la Matrix",
         r"Dialogue: 3,%s,%s,Frase,,0,0,0,,{\pos(540,1480)\c&H60D8F5&\fad(300,0)}👉 LINK EN MI PERFIL" % (ts(max(total-6,0)), ts(total))]
    for a, b, x in ev:
        f.append(f"Dialogue: 2,{ts(a)},{ts(min(b,total))},Frase,,0,0,0,,{{\\fad(120,120)\\fscx70\\fscy70\\t(0,180,\\fscx100\\fscy100)}}{ass_escape(partir(x))}")
    ass = tmp/"s.ass"; ass.write_text(cab+"\n".join(f)+"\n", encoding="utf-8")
    pad = ("aevalsrc='0.06*(sin(2*PI*130.81*t)+0.8*sin(2*PI*196*t)+0.7*sin(2*PI*329.63*t)+0.5*sin(2*PI*587.33*t))*(0.7+0.3*sin(2*PI*0.08*t))"
           "+0.03*(sin(2*PI*174.61*t)+sin(2*PI*261.63*t)+sin(2*PI*440*t))*(0.5+0.5*sin(2*PI*0.05*t+1))"
           "+0.015*sin(2*PI*1046.5*t)*(0.5+0.5*sin(2*PI*0.5*t))':s=44100:d=%.2f" % (total+1))
    mus = tmp/"m.m4a"
    run("-f","lavfi","-i",pad,"-af","aecho=0.8:0.85:600|1200:0.35|0.25,lowpass=f=2500,afade=t=in:d=3,afade=t=out:st=%.2f:d=3,volume=0.55"%max(total-3,0),"-ac","2","-c:a","aac",mus)
    run("-i", base, "-i", voz, "-i", mus, "-filter_complex",
        f"[0:v]eq=saturation=0.35:brightness=-0.04:enable='lt(t,{T:.2f})',ass={ass}[v];[2:a]volume=0.35[m];[1:a][m]amix=inputs=2:duration=first:normalize=0[a]",
        "-map","[v]","-map","[a]","-t",f"{total:.2f}","-c:v","libx264","-preset","veryfast","-pix_fmt","yuv420p","-c:a","aac","-b:a","160k","-movflags","+faststart",salida)
    print(salida, round(total,1))

if __name__ == "__main__":
    main(*sys.argv[1:7])
