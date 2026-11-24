"""Audio de activación con voz gratuita (Google, español latino, mujer).

Uso:  python3 audio.py guion.txt salida.mp3 [naia]
Con "naia" al final suena con la voz de NAIA (ver naia/NAIA.md): ágil, apenas
más grave y con un eco suave de androide (opción A, aprobada por Mabel 29-oct-2026).
Sin "naia", voz normal.
El guion lleva una frase por línea. Una línea con solo un número = pausa en
segundos (ej. "2.5"). Línea vacía = pausa corta. Línea que empieza con "#" =
encabezado que solo se ve en pantalla (video largo), no se dice.
"""
import subprocess, sys, tempfile, urllib.parse, urllib.request
from pathlib import Path

URL = "https://translate.googleapis.com/translate_tts?ie=UTF-8&client=gtx&tl=es-419&q="
RITMO = 1.0         # 0.9 si se quiere más lento
# NAIA: tono 4 % más grave y ágil (asetrate baja tono; atempo acelera).
# aecho le da el toque de androide. En NAIA las pausas se acortan (retención).
NAIA = "asetrate=24000*0.96,aresample=24000,atempo=1.22,aecho=0.8:0.5:30:0.12"
PAUSA_NAIA = 0.55
ESCALA_NAIA = 1 / (0.96 * 1.22)   # cuánto cambia la duración con el filtro NAIA


def voz(frase, destino):
    req = urllib.request.Request(URL + urllib.parse.quote(frase), headers={"User-Agent": "Mozilla/5.0"})
    destino.write_bytes(urllib.request.urlopen(req, timeout=20).read())


def silencio(seg, destino):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i",
                    "anullsrc=r=24000:cl=mono", "-t", str(seg), destino], check=True)


def duracion(archivo):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                 "-of", "csv=p=0", archivo], capture_output=True, text=True).stdout)


def main(guion, salida, naia=False):
    pausa = PAUSA_NAIA if naia else 1.0
    tmp = Path(tempfile.mkdtemp())
    partes, tiempos, reloj = [], [], 0.0
    for i, linea in enumerate(Path(guion).read_text(encoding="utf-8").splitlines()):
        linea = linea.strip()
        if linea.startswith("#"):   # encabezado en pantalla, no se dice
            continue
        p = tmp / f"{i:03d}.wav"
        try:
            silencio(float(linea) * pausa, p) if linea else silencio(0.5, p)
        except ValueError:
            mp3 = tmp / f"{i:03d}.mp3"
            voz(linea, mp3)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mp3, "-ar", "24000",
                            "-ac", "1", "-filter:a", f"atempo={RITMO}", p], check=True)
            partes.append(p)
            dur = duracion(p)
            tiempos.append((reloj, reloj + dur, linea))
            reloj += dur
            p = tmp / f"{i:03d}b.wav"
            silencio(0.15 if naia else 0.35, p)
        partes.append(p)
        reloj += duracion(p)
    lista = tmp / "lista.txt"
    lista.write_text("".join(f"file '{p}'\n" for p in partes))
    filtro = (NAIA + ",loudnorm") if naia else "loudnorm"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lista,
                    "-af", filtro, "-ar", "44100", "-b:a", "128k", salida], check=True)
    # Momento exacto de cada frase (para los subtítulos de los videos)
    k = ESCALA_NAIA if naia else 1.0
    Path(salida + ".tiempos.tsv").write_text(
        "".join(f"{a * k:.3f}\t{b * k:.3f}\t{t}\n" for a, b, t in tiempos), encoding="utf-8")
    print(salida)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], len(sys.argv) > 3 and sys.argv[3].lower() == "naia")
