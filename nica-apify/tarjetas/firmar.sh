#!/usr/bin/env bash
# Pone la firma de Mabel grande y legible sobre una tarjeta de Grok (6 s, 9:16).
# Uso: ./firmar.sh entrada.mp4 salida.mp4 [y_arroba]   (y_arroba: altura de @mabradiante, por defecto 1225)
set -e
ENTRADA="$1"; SALIDA="$2"; Y="${3:-1225}"; Y2=$((Y + 145))
DIR="$(cd "$(dirname "$0")" && pwd)"
ASS="$(mktemp --suffix=.ass)"
sed "s/\\\\pos(540,1225)/\\\\pos(540,$Y)/; s/\\\\pos(540,1370)/\\\\pos(540,$Y2)/" "$DIR/firma.ass" > "$ASS"
# 1080x1920; la firma diminuta de Grok (abajo, zona de botones de TikTok) se difumina y se funde en oscuro.
ffmpeg -y -loglevel error -i "$ENTRADA" -an -filter_complex \
"[0:v]scale=1080:-2:flags=lanczos,crop=1080:1920,setsar=1,split[a][b];\
[b]crop=1080:300:0:1620,boxblur=30:5[blur];[a][blur]overlay=0:1620[c];\
color=c=0x140d06:s=1080x480:d=7,format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='255*min(1,pow(Y/300,1.6))'[grad];\
[c][grad]overlay=0:1440:shortest=1,ass=$ASS,fps=30[v]" \
-map "[v]" -c:v libx264 -crf 18 -pix_fmt yuv420p -movflags +faststart "$SALIDA"
rm -f "$ASS"
