"""Reel vertical (1080x1920) de audio robótico: portada de la línea dorada + título hook + audio.

Uso:  python3 reel.py guion.txt "TÍTULO HOOK" "Nombre de la portada" salida.mp4
"""
import subprocess, sys
from pathlib import Path
from PIL import Image, ImageFilter

AQUI = Path(__file__).parent
sys.path.insert(0, str(AQUI.parent / "whatsapp"))
import audio, portada  # noqa: E402


def reel(guion, titulo, nombre_portada, salida):
    mp3 = str(Path(salida).with_suffix(".mp3"))
    audio.main(guion, mp3)
    cuadro = portada.portada(nombre_portada).resize((1080, 1080), Image.LANCZOS)
    fondo = Image.open(portada.BASE).convert("RGB").resize((1920, 1920)).crop((420, 0, 1500, 1920))
    fondo = fondo.filter(ImageFilter.GaussianBlur(30))
    fondo.paste(cuadro, (0, 560))
    lineas = portada.partir(titulo.upper(), portada.ImageFont.truetype(portada.SERIF, 86), 980)
    arriba = fondo.crop((0, 0, 1080, 1080))   # texto_oro trabaja en un lienzo cuadrado
    n_original, portada.N = portada.N, 1080
    portada.texto_oro(arriba, lineas, [86] * len(lineas), 150)
    portada.N = n_original
    fondo.paste(arriba.crop((0, 0, 1080, 560)), (0, 0))
    png = str(Path(salida).with_suffix(".png"))
    fondo.save(png)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-framerate", "2", "-i", png, "-i", mp3,
                    "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
                    "-shortest", "-movflags", "+faststart", salida], check=True)
    print(salida)


if __name__ == "__main__":
    reel(*sys.argv[1:5])
