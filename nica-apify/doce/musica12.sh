#!/usr/bin/env bash
# Música gratis para los videos de 12 s: 0-6 s suave y tensa (dolor) → 6-12 s luminosa (solución).
# Uso: ./musica12.sh video_sin_audio.mp4 salida_con_musica.mp4
set -e
M1="0.22*sin(2*PI*110*t)+0.16*sin(2*PI*130.81*t)+0.14*sin(2*PI*164.81*t)"      # La menor, grave
M2="0.18*sin(2*PI*130.81*t)+0.16*sin(2*PI*164.81*t)+0.15*sin(2*PI*196*t)+0.10*sin(2*PI*261.63*t)"  # Do mayor
ARP="0.07*sin(2*PI*(523.25+262*floor(mod(t*4,3)))*t)*(0.5+0.5*sin(2*PI*4*t))"   # destellos
ffmpeg -y -loglevel error -i "$1" \
  -f lavfi -i "aevalsrc='($M1)*(0.7+0.3*sin(2*PI*0.5*t))':s=44100:d=6" \
  -f lavfi -i "aevalsrc='($M2)*(0.8+0.2*sin(2*PI*0.7*t))+$ARP':s=44100:d=6" \
  -filter_complex "[1:a]afade=t=in:d=1,lowpass=f=1200[a];[2:a]lowpass=f=4000,afade=t=out:st=4.8:d=1.2[b];\
[a][b]acrossfade=d=0.3,aecho=0.8:0.7:180:0.3,volume=1.6,loudnorm=I=-16[m]" \
  -map 0:v -map "[m]" -c:v copy -c:a aac -b:a 160k -shortest -movflags +faststart "$2"
