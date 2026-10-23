"""Audio de activación con voz gratuita (Google, español latino, mujer).

Uso:  python3 audio.py guion.txt salida.mp3
El guion lleva una frase por línea. Una línea con solo un número = pausa en
segundos (ej. "2.5"). Línea vacía = pausa corta.
"""
import subprocess, sys, tempfile, urllib.parse, urllib.request
from pathlib import Path

URL = "https://translate.googleapis.com/translate_tts?ie=UTF-8&client=gtx&tl=es-419&q="
RITMO = 1.0         # 0.9 si se quiere más lento


def voz(frase, destino):
    req = urllib.request.Request(URL + urllib.parse.quote(frase), headers={"User-Agent": "Mozilla/5.0"})
    destino.write_bytes(urllib.request.urlopen(req, timeout=20).read())


def silencio(seg, destino):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i",
                    "anullsrc=r=24000:cl=mono", "-t", str(seg), destino], check=True)


def main(guion, salida):
    tmp = Path(tempfile.mkdtemp())
    partes = []
    for i, linea in enumerate(Path(guion).read_text(encoding="utf-8").splitlines()):
        linea = linea.strip()
        p = tmp / f"{i:03d}.wav"
        try:
            silencio(float(linea), p) if linea else silencio(0.5, p)
        except ValueError:
            mp3 = tmp / f"{i:03d}.mp3"
            voz(linea, mp3)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mp3, "-ar", "24000",
                            "-ac", "1", "-filter:a", f"atempo={RITMO}", p], check=True)
            partes.append(p)
            p = tmp / f"{i:03d}b.wav"
            silencio(0.35, p)
        partes.append(p)
    lista = tmp / "lista.txt"
    lista.write_text("".join(f"file '{p}'\n" for p in partes))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lista,
                    "-af", "loudnorm", "-ar", "44100", "-b:a", "128k", salida], check=True)
    print(salida)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
