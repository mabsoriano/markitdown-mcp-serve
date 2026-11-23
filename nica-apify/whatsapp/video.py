"""Une la portada y el audio en un solo video MP4 para WhatsApp.

Uso:  python3 video.py portada.png audio.mp3 [salida.mp4]
Sale junto al audio con el mismo nombre y extensión .mp4.
"""
import subprocess, sys
from pathlib import Path


def video(portada, audio, salida=None):
    salida = salida or str(Path(audio).with_suffix(".mp4"))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-framerate", "2", "-i", portada,
                    "-i", audio, "-vf", "scale=1080:1080,format=yuv420p", "-c:v", "libx264",
                    "-tune", "stillimage", "-c:a", "aac", "-b:a", "128k", "-shortest",
                    "-movflags", "+faststart", salida], check=True)
    print(salida)


if __name__ == "__main__":
    video(*sys.argv[1:4])
