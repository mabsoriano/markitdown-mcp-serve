"""Brief semanal 16–22 nov 2026 (Estratega). Genera brief-semana-2026-11-16.docx."""
import os
from docx import Document
from docx.shared import Pt
AQUI = os.path.dirname(os.path.abspath(__file__))
d = Document()
st = d.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(11)
d.add_heading("Brief semanal · 16 al 22 de noviembre de 2026", 0)
d.add_paragraph("De: Estratega · Para: Mabel → NICA · Hecho el sábado 14 de noviembre con tus números del tablero (semana 10–16 nov). "
                "Todo es propuesta: nada se gasta, se publica ni cambia de precio sin tu OK.")
def h(t): d.add_heading(t, 1)
def bl(items):
    for i in items: d.add_paragraph(i, style="List Bullet")
def nl(items):
    for i in items: d.add_paragraph(i, style="List Number")

h("Diagnóstico (tus números)")
nl([
 "Ventas: $0. Tres LIVES sin venta: 6 personas, 28 personas y 55 a 60 personas.",
 "La buena noticia: ya llega gente. De 6 a 60 en tres LIVES: tu convocatoria SÍ está funcionando.",
 "El correo despertó: 1,132 enviados y 233 aperturas (20.6%). Antes abrían 3 a 5. Hoy es tu canal más fuerte.",
 "WhatsApp creció de 100 a 172. Linktree 27 clics, web 44 visitas, NAIA 8 registros.",
 "Dónde se pierde la venta: con 60 personas en vivo y 44 visitas a la web, lo normal sería vender de 1 a 3. Con 0, el problema ya no es cuánta gente llega: es el paso de «me gustó» a «compro».",
])

h("Las 3 razones más probables (y qué hacemos)")
d.add_paragraph("1. La página no dice lo mismo que el LIVE.", style="List Number")
d.add_paragraph("En el LIVE vendes «Hipnosis para hackear tus bloqueos con el dinero», pero el link lleva a una página que se llama «Activación Simultánea / ADN Millonario». "
                "Quien entra duda si es lo mismo, y la duda mata la venta. → Que el título y la primera línea de la página en Hotmart digan EXACTAMENTE «Hipnosis para hackear tus bloqueos con el dinero».")
d.add_paragraph("2. El precio no es claro.", style="List Number")
d.add_paragraph("«$500 + impuestos» obliga a hacer cuentas. → Di en el LIVE el precio final que van a pagar, un solo número, y repítelo. Y la garantía de 7 días de Hotmart, 3 veces.")
d.add_paragraph("3. No hay razón para comprar HOY.", style="List Number")
d.add_paragraph("→ Un bono real solo para quien compre en las 24 horas después del LIVE (por ejemplo, un audio corto de tu voz o una sesión grupal de preguntas), con hora de cierre real. "
                "Y el argumento de tu eslogan: «Lo que no se activa, no cambia. Y lo que no se repite, no se instala»: en el LIVE se activa, en los 21 días se instala.")

h("Plan de la semana")
bl([
 "LIVES: si el de 55–60 personas fue el de TikTok, los LIVES de venta se quedan en TikTok: martes 17 a las 7 PM y sábado 21 a las 5 PM (45 min, probadita de 7–10 min). El miércoles 18 a las 10 AM sigue tu activación gratis de chakras solo para comunidad.",
 "Después de cada LIVE (el mismo día): 1 correo a tu lista con el link de la página y la hora de cierre del bono + 1 mensaje a tus grupos de WhatsApp. El correo es hoy tu mejor canal: úsalo.",
 "Testimonios: en cada LIVE pide «escribe en una palabra qué sentiste» y toma captura (con permiso). Con eso hacemos contenido y le das confianza a la siguiente.",
 "Contenido: la misma mezcla que te gustó (famoso + autoridad, Poderosa Conexión, yapping y NAIA con tu gancho) y CTA al producto en el link de tu perfil.",
 "Competencia (con tu OK): una corrida en Apify de máximo $1 USD para traer los LIVES y videos que más venden de tus competidoras y copiar su estructura (nunca su texto).",
])

h("KPIs y meta de la semana")
bl([
 "Asistentes por LIVE: 60 o más.",
 "Clics en Linktree: de 27 a 60.",
 "Visitas a la página de la hipnosis: de 44 a 80.",
 "Ventas: meta 3 (primera venta de la temporada).",
 "Correo: mantener 20% de apertura o más.",
 "Decisión con el número: si hay clics pero 0 ventas → se corrige la página. Si no hay clics → se corrige el momento y la forma del CTA en el LIVE.",
])

h("Prueba de la semana (una sola)")
d.add_paragraph("En el LIVE del martes: di el precio final en un solo número y el bono de 24 horas. En el del sábado, igual, pero mostrando la página en pantalla con tu celular mientras explicas. Comparamos clics y ventas.")

h("⏳ Pendientes de tu decisión")
nl([
 "¿El LIVE de 55–60 personas fue el de TikTok? Si sí: ¿pasamos el martes 17 de Zoom a TikTok, 7 PM?",
 "¿Qué bono real das a quien compre en 24 horas? (un audio corto, una sesión grupal de preguntas u otro que tú elijas).",
 "¿Cambias el título de la página en Hotmart a «Hipnosis para hackear tus bloqueos con el dinero»? ¿Y cuál es el precio final con impuestos?",
 "¿OK a la corrida de competencia en Apify (máximo $1 USD)?",
])
d.add_paragraph("Lo que no se activa, no cambia. Y lo que no se repite, no se instala. @mabradiante · BNQ Method™")
salida = os.path.join(AQUI, "brief-semana-2026-11-16.docx"); d.save(salida); print(salida)
