"""NICA · Espía de competencia con Apify.

Lee competidores.txt, saca las últimas publicaciones de cada cuenta
(TikTok o Instagram) y guarda en resultados/ un CSV con todo y un
resumen con las 10 publicaciones que más pegaron.

Uso:
    export APIFY_TOKEN="tu_token"
    python nica_apify.py            # 20 publicaciones por cuenta
    python nica_apify.py 50         # 50 publicaciones por cuenta
"""
import csv
import json
import os
import sys
import urllib.request
from datetime import date
from pathlib import Path

BASE = Path(__file__).parent
API = "https://api.apify.com/v2/acts/{actor}/run-sync-get-dataset-items"


def correr_actor(actor, entrada, token):
    req = urllib.request.Request(
        API.format(actor=actor),
        data=json.dumps(entrada).encode(),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"},
    )
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.load(r)


def tiktok(usuario, limite, token):
    items = correr_actor("clockworks~tiktok-scraper", {
        "profiles": [usuario],
        "resultsPerPage": limite,
        "shouldDownloadVideos": False,
        "shouldDownloadCovers": False,
    }, token)
    return [{
        "red": "tiktok",
        "cuenta": usuario,
        "fecha": i.get("createTimeISO", ""),
        "vistas": i.get("playCount", 0),
        "likes": i.get("diggCount", 0),
        "comentarios": i.get("commentCount", 0),
        "compartidos": i.get("shareCount", 0),
        "texto": (i.get("text") or "").replace("\n", " "),
        "link": i.get("webVideoUrl", ""),
    } for i in items if "error" not in i]


def instagram(usuario, limite, token):
    items = correr_actor("apify~instagram-scraper", {
        "directUrls": [f"https://www.instagram.com/{usuario}/"],
        "resultsType": "posts",
        "resultsLimit": limite,
    }, token)
    return [{
        "red": "instagram",
        "cuenta": usuario,
        "fecha": i.get("timestamp", ""),
        "vistas": i.get("videoViewCount") or i.get("videoPlayCount") or 0,
        "likes": i.get("likesCount", 0),
        "comentarios": i.get("commentsCount", 0),
        "compartidos": 0,
        "texto": (i.get("caption") or "").replace("\n", " "),
        "link": i.get("url", ""),
    } for i in items if "error" not in i]


REDES = {"tiktok": tiktok, "instagram": instagram}


def leer_competidores():
    cuentas = []
    for linea in (BASE / "competidores.txt").read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#"):
            continue
        red, usuario = linea.split()[:2]
        red = red.lower()
        if red not in REDES:
            print(f"⚠️  Red no reconocida '{red}' — usa tiktok o instagram")
            continue
        cuentas.append((red, usuario.lstrip("@")))
    return cuentas


def interaccion(p):
    return p["likes"] + p["comentarios"] * 3 + p["compartidos"] * 5


def main():
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("❌ Falta tu llave de Apify. Corre: export APIFY_TOKEN=\"tu_token\"")
    limite = int(sys.argv[1]) if len(sys.argv) > 1 else 20

    cuentas = leer_competidores()
    if not cuentas:
        sys.exit("❌ competidores.txt está vacío. Agrega al menos una cuenta.")

    publicaciones = []
    for red, usuario in cuentas:
        print(f"🔎 {red} @{usuario}...")
        try:
            nuevas = REDES[red](usuario, limite, token)
        except Exception as e:
            print(f"   ⚠️  No se pudo: {e}")
            continue
        print(f"   ✅ {len(nuevas)} publicaciones")
        publicaciones += nuevas

    if not publicaciones:
        sys.exit("❌ No se obtuvo ninguna publicación.")

    salida = BASE / "resultados"
    salida.mkdir(exist_ok=True)
    hoy = date.today().isoformat()

    archivo_csv = salida / f"competencia_{hoy}.csv"
    with open(archivo_csv, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(publicaciones[0]))
        w.writeheader()
        w.writerows(publicaciones)

    top = sorted(publicaciones, key=interaccion, reverse=True)[:10]
    lineas = [f"# Top 10 de la competencia · {hoy}", ""]
    for n, p in enumerate(top, 1):
        lineas += [
            f"## {n}. @{p['cuenta']} ({p['red']})",
            f"👁 {p['vistas']:,} · ❤️ {p['likes']:,} · 💬 {p['comentarios']:,} · 🔁 {p['compartidos']:,}",
            f"> {p['texto'][:280]}",
            p["link"],
            "",
        ]
    archivo_md = salida / f"top10_{hoy}.md"
    archivo_md.write_text("\n".join(lineas), encoding="utf-8")

    print(f"\n🎉 Listo:\n   {archivo_csv}\n   {archivo_md}")


if __name__ == "__main__":
    main()
