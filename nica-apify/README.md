# NICA · Espía de competencia (Apify)

Saca las últimas publicaciones de tu competencia en **TikTok** e **Instagram**
y te dice cuáles pegaron más, para que veas qué ganchos y temas funcionan.

## Cómo se usa (3 pasos)

1. **Pon a tu competencia** en `competidores.txt`, una por línea:
   ```
   tiktok    nombredelacuenta
   instagram nombredelacuenta
   ```
2. **Pon tu llave de Apify** (la sacas en apify.com → Settings → API & Integrations):
   ```
   export APIFY_TOKEN="tu_token"
   ```
3. **Córrelo:**
   ```
   python nica_apify.py
   ```

## Qué te entrega

En la carpeta `resultados/`:
- `competencia_FECHA.csv` → todas las publicaciones (se abre en Excel o Google Sheets).
- `top10_FECHA.md` → las 10 que más interacción tuvieron, con su texto y link.

## Costo

Usa créditos de tu cuenta de Apify. Con 20 publicaciones por cuenta
y 5 competidores, el plan gratis alcanza de sobra.
Para sacar más: `python nica_apify.py 50`
