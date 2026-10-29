"""Video NAIA: python3 video.py guion.txt audio.mp3 loop.mp4 "TITULO" salida.mp4"""
import re, subprocess, sys, tempfile
txt, mp3, loop, titulo, salida = sys.argv[1:6]
lines = [l.strip() for l in open(txt, encoding="utf-8") if l.strip() and not re.fullmatch(r"[0-9.]+", l.strip())]
parts = [p for l in lines for p in re.split(r"(?<=\.)\s+", l)]
out = subprocess.run(["ffmpeg","-i",mp3,"-af","silencedetect=noise=-38dB:d=0.28","-f","null","-"],capture_output=True,text=True).stderr
st = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", out)]
en = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", out)]
dur = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",mp3],capture_output=True,text=True).stdout)
segs, cur = [], 0.0
for s, e in zip(st, en):
    if s - cur > 0.05: segs.append((cur, s))
    cur = e
assert len(segs) == len(parts), (len(segs), len(parts))
fin = dur + 1.0
def t(x): return f"{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}"
ass = ["[Script Info]","ScriptType: v4.00+","PlayResX: 1080","PlayResY: 1920","",
"[V4+ Styles]","Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
"Style: Sub,DejaVu Sans,72,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,1,0,0,0,100,100,0,0,1,5,3,2,110,140,620,1",
"Style: Tit,DejaVu Serif,84,&H0058D7FF,&H00FFFFFF,&H00000000,&H96000000,1,0,0,0,100,100,2,0,1,5,3,5,90,90,0,1",
"Style: Firma,DejaVu Sans,46,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,1,0,0,0,100,100,2,0,1,3,2,8,90,90,1560,1",
"","[Events]","Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text",
f"Dialogue: 1,{t(0)},{t(3)},Tit,,0,0,0,,{{\\pos(540,1060)\\fad(0,300)}}{titulo}"]
for i, (p, (a, b)) in enumerate(zip(parts, segs)):
    end = segs[i+1][0] if i+1 < len(segs) else fin
    p = p.replace("Mabradiante", "@mabradiante")
    ass.append(f"Dialogue: 0,{t(a)},{t(end)},Sub,,0,0,0,,{p}")
ass.append(f"Dialogue: 0,{t(0)},{t(fin)},Firma,,0,0,0,,NAIA · @mabradiante")
f = tempfile.NamedTemporaryFile("w", suffix=".ass", delete=False, encoding="utf-8"); f.write("\n".join(ass)); f.close()
subprocess.run(["ffmpeg","-y","-loglevel","error","-stream_loop","-1","-i",loop,"-i",mp3,
  "-filter_complex",f"[0:v]ass={f.name},fade=t=out:st={fin-0.6}:d=0.6[v];[1:a]apad=pad_dur=1[a]",
  "-map","[v]","-map","[a]","-t",str(fin),"-c:v","libx264","-crf","20","-preset","medium","-pix_fmt","yuv420p",
  "-c:a","aac","-b:a","160k","-movflags","+faststart",salida], check=True)
print(salida, round(fin,1))
