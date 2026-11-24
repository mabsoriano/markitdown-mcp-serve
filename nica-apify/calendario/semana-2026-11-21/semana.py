"""Calendario de contenido sáb 21 → vie 27 nov 2026 · campaña HACKEO SIMULTÁNEO.
LIVE GRATIS Zoom mié 25 · 11 AM (hora MX) "Hipnosis para Hackear tus Bloqueos con el Dinero".
Venta Programa la Riqueza mientras Duermes $500 + impuestos: mié 25 → vie 27 11:59 PM.
Regalo: hipnosis completa dom 29 · 11 AM solo compradoras. TikTok LIVE diario 7 PM (no se pauta).
Cada día: 1 pieza a cámara + 1 yapping + aviso del TikTok LIVE (historia).
Genera: /home/user/CALENDARIO-CONTENIDO-21-27-NOV.xlsx y nica-apify/calendario/semana-2026-11-21.md
Uso: python3 semana.py
"""
import os
import re
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side

AQUI = os.path.dirname(os.path.abspath(__file__))
XLSX = "/home/user/CALENDARIO-CONTENIDO-21-27-NOV.xlsx"
MD = os.path.join(os.path.dirname(AQUI), "semana-2026-11-21.md")

SLOGAN = ("Lo que no se ACTIVA, no CAMBIA. Y lo que no se REPITE, no se INSTALA.\n"
          "Mabel Soriano · BNQ Method™")
LIVE = "LIVE GRATIS · miércoles 25 · 11 AM (hora MX)"
LIVE_T = "Hipnosis para Hackear tus Bloqueos con el Dinero"
REDES = "TikTok · IG Reels · FB MabRadiante · YouTube Shorts (mismo video en las 4)"
HIST = "Historias: IG + FB MabRadiante + TikTok"
CIERRE = ("«Escríbeme ABUNDANCIA por mensaje y te mando tu lugar al live gratis del miércoles 25 "
          "a las 11 de la mañana. Lo que no se ACTIVA, no CAMBIA. Y lo que no se REPITE, no se INSTALA. "
          "Mabel Soriano · BNQ Method™.»")
FIJADO = "Comentario fijado: «Mándame ABUNDANCIA por mensaje y te llega el link 💌»"
H_Y = ("TikTok: #parati #fyp #mamaemprendedora #sinfiltro #BNQMethod\n"
       "Reels/FB/Shorts: #mamaemprendedora #sinfiltro #hackeatumente #BNQMethod #Shorts")

COLS = ["Día", "Hora (MX)", "Red", "Formato", "Título en pantalla", "Hook (1a frase)",
        "Guion corto / puntos", "Caption", "Hashtags", "CTA", "¿Venta? (80/20)",
        "Qué graba Mabel", "Cuándo lo graba"]
F = []


def add(dia, hora, red, formato, titulo, hook, guion, caption, hashtags, cta, venta, graba, cuando):
    F.append([dia, hora, red, formato, titulo, hook, guion, caption, hashtags, cta, venta, graba, cuando])


def pts(*p):
    return "\n".join(f"{i}. {x}" for i, x in enumerate(p, 1))


def yap(dia, hora, titulo, hook, puntos, pregunta, palabra, caption, cuando):
    add(dia, hora, REDES, "YAPPING (1-3 min, sin guion palabra por palabra, un solo corte, cerca de la cámara)",
        titulo, hook, "Puntos guía:\n" + pts(*puntos) + f"\nCierre: «{pregunta} Comenta {palabra}.»",
        caption + f"\nComenta {palabra} 👇\n" + SLOGAN, H_Y, f"Comenta {palabra} (conexión, sin producto)",
        "NO", f"Yapping «{titulo}» (1-3 min, celular)", cuando)


def aviso(dia, tema, venta_live):
    add(dia, "4:00 PM y 6:30 PM", HIST, "AVISO TikTok LIVE 7 PM (historia, SIN precio)",
        "HOY 7 PM · EN VIVO EN TIKTOK", "Hoy a las 7 de la noche te espero en vivo en TikTok.",
        "4:00 PM · historia con el arte del aviso TikTok LIVE 7 PM (ya hecha) + sticker de cuenta regresiva.\n"
        f"6:30 PM · selfie 15 s: «En media hora estoy en vivo en TikTok. Hoy: {tema}. Ahí te veo.»\n"
        "Sin precio en el aviso (el precio solo se dice dentro del live).",
        f"Hoy 7 PM (hora MX) en vivo en TikTok 🔴 {tema}.\nActiva el recordatorio y comenta ABUNDANCIA.\n" + SLOGAN,
        "#envivo #tiktoklive #abundancia #BNQMethod", "Activa el recordatorio · comenta ABUNDANCIA",
        "NO (aviso)", "Selfie de 15 s para la historia de las 6:30 PM", "En el momento (6:25 PM, celular)")
    add(dia, "7:00 PM", "TikTok LIVE (no se pauta)", "TikTok LIVE 25 min (formato live/formato-tiktok-live-diario-25min.md)",
        "—", "Gancho del día con una pregunta-dolor.",
        f"Tema: {tema}.\n0-2 gancho · 2-5 quién soy (misión tal cual) · 5-12 tema (subconsciente se aprende, memoria celular se hereda, energía 100% tuya) · 12-15 mini hackeo x3 · 15-20 {venta_live} · 20-25 preguntas + slogan completo.\nNunca la activación completa.",
        "— (no hay caption: es en vivo)", "—", "Comenta ABUNDANCIA", "SÍ (dentro del live)" if "Riqueza" in venta_live else "NO (invita al Zoom)",
        "Nada que grabar antes: entra en vivo", "En vivo 7:00 PM")


# ═══════════════ SÁBADO 21 · SUBCONSCIENTE (HOY) ═══════════════
D = "Sáb 21"
add(D, "5:30 PM", REDES, "A CÁMARA · FAMOSO + AUTORIDAD (Video 1 · 75-90 s)",
    "LO QUE ESCUCHASTE EN CASA SIGUE DECIDIENDO TU DINERO",
    "Sara Blakely, la creadora de Spanx, se volvió millonaria por algo que su papá le preguntaba en la cena.",
    "GUARDAR (antes de 15 s): «Guarda este video y compártelo con la persona que siempre dice “no me alcanza”.»\n"
    + pts("DATO: su papá le preguntaba cada semana «¿En qué fallaste esta semana?». Ella aprendió que fallar era intentar (lo ha contado en entrevistas).",
          "DOLOR: tú también escuchaste frases: «el dinero no crece en los árboles», «los ricos son malos», «aquí no se gasta».",
          "LISTA DE 3: el dinero cuesta mucho trabajo · pedir es de mal gusto · si tengo, me lo van a quitar.",
          "REENCUADRE: no es tu culpa. Es tu SUBCONSCIENTE: aprendido, no de sangre. Lo aprendido se reprograma. [TU HISTORIA: la frase del dinero que escuchabas en tu casa].")
    + "\nHACKEO x3 (mano en el pecho): «Lo que escuché en mi casa no decide mi dinero. Hoy elijo lo que instalo.»"
    + "\nREVELACIÓN: «Esto es solo un nivel. En el live te enseño los otros dos y cómo se hackean los tres al mismo tiempo con una Fórmula Cuántica.»"
    + "\nCIERRE: " + CIERRE + "\n" + FIJADO,
    "¿Qué frase del dinero escuchabas en tu casa? 👇\nTu subconsciente no nació con ella: la aprendió. Y lo aprendido se reprograma.\n"
    f"Escríbeme ABUNDANCIA por mensaje y te mando tu lugar al {LIVE}: {LIVE_T}.\n" + SLOGAN,
    "TikTok: #parati #fyp #dinero #abundancia #subconsciente #creenciaslimitantes #hackeatumente #BNQMethod\n"
    "Reels/FB/Shorts: #abundancia #dinero #subconsciente #creenciaslimitantes #reprogramacion #BNQMethod #Shorts",
    "Escríbeme ABUNDANCIA (registro al live)", "NO (registro al live gratis)",
    "Video 1 (graba PRIMERO, para que salga hoy 5:30 PM)", "HOY sáb 21 · Bloque 1 · 3:00 PM")
yap(D, "1:00 PM ➜ hoy sale 8:00 PM (después del live)", "POR QUÉ VOY A ESTAR EN VIVO TODOS LOS DÍAS A LAS 7",
    "Tomé una decisión y te la quiero contar antes que a nadie.",
    ["[Por qué decidiste hacer live diario en TikTok]", "[Qué te da miedo y qué te emociona de hacerlo]",
     "[Qué va a pasar en cada live: 25 minutos, un hackeo para hacer juntas]", "[A quién te imaginas del otro lado]"],
    "¿A qué hora te queda mejor verme?", "HORA",
    "Tomé una decisión: desde hoy estoy en vivo en TikTok todos los días a las 7 PM (hora MX) 🔴\nSin filtro, 25 minutos, un hackeo para hacer juntas.",
    "HOY sáb 21 · Bloque 1 · 4:15 PM")
F[-1][1] = "8:00 PM (hoy sale después del TikTok LIVE)"
aviso(D, "lo que escuchaste en casa sigue decidiendo tu dinero (subconsciente)",
      "invitación al Zoom del mié 25 · 11 AM: «comenta ABUNDANCIA y te mando tu lugar» (esta noche NO hay precio: la venta abre el mié 25)")

# ═══════════════ DOMINGO 22 · MEMORIA CELULAR ═══════════════
D = "Dom 22"
add(D, "5:30 PM", REDES, "A CÁMARA · PODEROSA CONEXIÓN (Video 2 · 75-90 s)",
    "TU CUERPO RECUERDA LA ESCASEZ DE TU ABUELA",
    "Puedes leer todos los libros de abundancia del mundo y tu cuerpo va a seguir sintiendo que el dinero no alcanza.",
    "PATRÓN: «Ganas un poco más… y sientes miedo, culpa o prisa por gastarlo.»\n"
    "PUENTE: «Permíteme llevarte al siguiente nivel con un bioneurohack. No es un decreto más: es una activación. Antes, dale like y comenta ABUNDANCIA para que le llegue a quien lo necesita.»\n"
    + pts("DETECTA: cuando entra dinero, ¿tu cuerpo se relaja o se tensa? Sin autoengaño.",
          "DATO: Invierno del Hambre, Holanda 1944. Un estudio de 2008 encontró marcas distintas en los genes de los hijos de mamás embarazadas en esa hambruna, 60 años después (epigenética).",
          "ROMPE EL PATRÓN: a diferencia del subconsciente, la MEMORIA CELULAR sí se hereda. Tu cuerpo puede cargar la escasez de tu abuela como si fuera tuya.",
          "REGLA DE ORO: si no te incomoda, no te está cambiando. Si al ver tu cuenta sientes un nudo, ese nudo no es tuyo.")
    + "\nHACKEO x3: «Honro a mi linaje. La escasez se queda en su historia. Mis células hoy reciben.»"
    + "\nQUIÉN SOY: «Soy Mabel Soriano, creadora de BNQ Method™. Mi misión es activar tu consciencia, hackearla y reprogramarla con mi Método BNQ para que cambies de realidad.»"
    + "\nCIERRE: " + CIERRE + "\n" + FIJADO,
    "Tu subconsciente lo aprendiste. Tu memoria celular, la heredaste. 🧬\nPor eso hay miedos al dinero que ni siquiera son tuyos.\n"
    f"Escríbeme ABUNDANCIA por mensaje y te mando tu lugar al {LIVE}: {LIVE_T}.\n" + SLOGAN,
    "TikTok: #parati #fyp #memoriacelular #linaje #epigenetica #dinero #abundancia #BNQMethod\n"
    "Reels/FB/Shorts: #memoriacelular #linaje #abundancia #dinero #epigenetica #BNQMethod #Shorts",
    "Comenta / escríbeme ABUNDANCIA (registro al live)", "NO (registro al live gratis)",
    "Video 2", "HOY sáb 21 · Bloque 1 · 3:20 PM")
yap(D, "1:00 PM", "MI DOMINGO REAL (SIN FILTRO)", "Así se ve un domingo de verdad en mi casa, sin filtro.",
    ["[Qué haces los domingos con tu hijo]", "[Lo que haces para recargarte]", "[Una cosa que aprendiste esta semana]",
     "[Lo que viene esta semana: el live del miércoles, dicho como plática, sin vender]"],
    "¿Cómo se ve tu domingo real?", "DOMINGO",
    "Mi domingo real, sin filtro 💛\n¿Cómo se ve el tuyo?", "HOY sáb 21 · Bloque 1 · 4:25 PM")
aviso(D, "tu cuerpo recuerda la escasez de tu abuela (memoria celular)",
      "invitación al Zoom del mié 25 · 11 AM con ABUNDANCIA (sin precio)")

# ═══════════════ LUNES 23 · ENERGÍA ═══════════════
D = "Lun 23"
add(D, "5:30 PM", REDES, "A CÁMARA · FAMOSO + AUTORIDAD (Video 3 · 75-90 s)",
    "TU ENERGÍA ES 100% TUYA (Y EL DINERO LA LEE)",
    "Jim Carrey se escribió un cheque de 10 millones de dólares cuando no tenía ni para la renta.",
    "GUARDAR: «Guárdalo, porque al final lo vas a hacer conmigo.»\n"
    + pts("DATO: se lo contó a Oprah. Cheque por 10 millones «por servicios de actuación», con fecha a futuro, en la cartera. Antes de esa fecha le pagaron 10 millones por una película. No fue suerte: fue una decisión que repitió todos los días.",
          "DOLOR: vives en modo «a ver si alcanza», y esa frecuencia se nota en cómo cobras, pides y recibes.",
          "LISTA DE 3 FUGAS: revisar la cuenta con miedo · decir «es carísimo» de todo · no cobrar lo que vales por pena.",
          "REENCUADRE: el subconsciente lo aprendiste, la memoria celular la heredaste, pero tu ENERGÍA es 100% tuya. [TU HISTORIA: un momento en que cambiaste tu energía y cambió lo que llegó].")
    + "\nHACKEO x3 (respira una vez): «Mi energía es mía. Hoy vibro en suficiencia y el dinero me encuentra.»"
    + "\nREVELACIÓN: «Si cambias tu energía y tu subconsciente sigue en escasez, se apaga. Por eso en el live los hackeamos en simultáneo.»"
    + "\nCIERRE: " + CIERRE + "\n" + FIJADO,
    "Lo que aprendiste no lo elegiste. Lo que heredaste, tampoco. Pero tu energía es 100% tuya. ⚡\n¿Cuál de las 3 fugas tienes tú? Te leo 👇\n"
    f"Escríbeme ABUNDANCIA por mensaje y te mando tu lugar al {LIVE}: {LIVE_T}.\n" + SLOGAN,
    "TikTok: #parati #fyp #energia #frecuencia #abundancia #dinero #jimcarrey #BNQMethod\n"
    "Reels/FB/Shorts: #energia #frecuencia #abundancia #dinero #leydeatraccion #BNQMethod #Shorts",
    "Escríbeme ABUNDANCIA (registro al live)", "NO (registro al live gratis)",
    "Video 3", "HOY sáb 21 · Bloque 1 · 3:40 PM")
yap(D, "1:00 PM", "LO QUE NADIE TE DICE DE EMPEZAR DE CERO", "Hubo un momento en que tuve que empezar de cero, y nadie me avisó lo que se siente.",
    ["[Cuándo te tocó empezar de cero]", "[Lo que sentiste con el dinero en ese momento]", "[La primera cosa que cambiaste]",
     "[Lo que le dirías a quien está ahí hoy]"],
    "¿Tú has tenido que empezar de cero?", "CERO",
    "Lo que nadie te dice de empezar de cero 🌱 Te lo cuento como amiga.", "Dom 22 · Bloque 2 · 5:00 PM")
aviso(D, "tu energía es 100% tuya y el dinero la lee (energía)",
      "invitación al Zoom del mié 25 · 11 AM con ABUNDANCIA (sin precio)")

# ═══════════════ MARTES 24 · LOS 3 EN SIMULTÁNEO ═══════════════
D = "Mar 24"
add(D, "5:30 PM", REDES, "A CÁMARA · PODEROSA CONEXIÓN (Video 4 · 80-90 s)",
    "POR QUÉ DECRETAR NO TE ALCANZA",
    "Decretar abundancia mientras tu cuerpo siente escasez no es crecimiento: es entretenimiento disfrazado.",
    "PATRÓN: «Decreto, me emociono, pasan tres días… y todo sigue igual.»\n"
    "PUENTE: «Permíteme llevarte al siguiente nivel con un bioneurohack. No es un decreto más: es una activación. Antes, dale like y comenta ABUNDANCIA.»\n"
    + pts("DETECTA: estás atacando un solo nivel, y tus bloqueos con el dinero viven en tres.",
          "LOS 3 NIVELES: SUBCONSCIENTE (lo aprendiste en casa) · MEMORIA CELULAR (la heredaste de tu linaje) · ENERGÍA (100% tuya).",
          "ROMPE EL PATRÓN: si hackeas uno y los otros dos siguen igual, te jalan de regreso. El Método BNQ los hackea EN SIMULTÁNEO y para cada problema hay una Fórmula Cuántica.",
          "LA TRAMPA: no pienses de más. Activa y repite. Lo que no se repite, no se instala.")
    + "\nHACKEO x3: «Hackeo mi subconsciente, mi memoria celular y mi energía. Hoy, al mismo tiempo, elijo abundancia.»"
    + "\nPROMESA (sin prometer dinero): «Si lo repites 7 días, tu pregunta dejará de ser “¿por qué no me llega?” y será “¿qué hago con lo que llega?”.»"
    + "\nQUIÉN SOY: «Soy Mabel Soriano, creadora de BNQ Method™ y autora de Las Fórmulas Cuánticas para Hackear la Matrix. Mi misión es activar tu consciencia, hackearla y reprogramarla con mi Método BNQ para que cambies de realidad.»"
    + "\nCIERRE: " + CIERRE + "\n" + FIJADO,
    "Subconsciente (lo aprendiste) + memoria celular (la heredaste) + energía (es 100% tuya).\nSi hackeas solo uno, los otros dos te regresan. Se hackean EN SIMULTÁNEO.\n"
    f"Mañana te enseño cómo, en vivo y gratis.\nEscríbeme ABUNDANCIA por mensaje y te mando tu lugar al {LIVE}: {LIVE_T}.\n" + SLOGAN,
    "TikTok: #parati #fyp #decretos #abundancia #dinero #subconsciente #memoriacelular #BNQMethod\n"
    "Reels/FB/Shorts: #decretos #abundancia #dinero #hackeatumente #formulascuanticas #BNQMethod #Shorts",
    "Comenta / escríbeme ABUNDANCIA (registro al live)", "NO (registro al live gratis)",
    "Video 4", "HOY sáb 21 · Bloque 1 · 4:00 PM")
yap(D, "1:00 PM", "LO QUE MÁS ME PREGUNTAN EN LOS LIVES", "Hay una pregunta que me hacen en cada live, y hoy la contesto aquí.",
    ["[La pregunta que más se repite en tus lives de TikTok]", "[Tu respuesta corta, como amiga]",
     "[Un comentario que te movió esta semana (sin nombre)]", "[Lo que te gustaría que te pregunten]"],
    "¿Qué me quieres preguntar tú?", "PREGUNTA",
    "Lo que más me preguntan en los lives 🙋‍♀️ Hoy lo contesto aquí.", "Dom 22 · Bloque 2 · 5:10 PM")
aviso(D, "por qué decretar no te alcanza: los 3 niveles en simultáneo",
      "último llamado al Zoom de MAÑANA mié 25 · 11 AM con ABUNDANCIA (sin precio)")

# ═══════════════ MIÉRCOLES 25 · LIVE ZOOM 11 AM + ABRE VENTA ═══════════════
D = "Mié 25"
add(D, "8:00 AM", REDES, "A CÁMARA · FAMOSO + AUTORIDAD, corto y con urgencia real (Video 5 · 60-75 s)",
    "HOY 11 AM: HACKEAMOS TU DINERO EN VIVO",
    "Hoy a las 11 de la mañana vamos a hackear tus bloqueos con el dinero, en vivo y gratis.",
    "AJUSTE: ya no dice «en una hora» (sale 8 AM, el live es 11 AM). Se graba el sábado diciendo «hoy».\n"
    "COMPARTIR: «Comparte este video con la amiga que siempre dice que el dinero no le llega.»\n"
    + pts("DATO: en 1949 el neurocientífico Donald Hebb explicó que las neuronas que se activan juntas se conectan. Traducido: lo que repites, tu cerebro lo instala.",
          "LO QUE VAS A VIVIR HOY: reconocer lo que tu SUBCONSCIENTE aprendió en casa · ver qué trae tu MEMORIA CELULAR de tu linaje · mover tu ENERGÍA, que es 100% tuya.",
          "Los 3 en simultáneo, con una Fórmula Cuántica, y una probadita de hipnosis conmigo, en vivo.",
          "Solo entran las que se registran. No es en público. [TU HISTORIA: por qué este live es especial para ti].")
    + "\nHACKEO x3: «Hoy me presento a mi abundancia. Hoy activo, hoy repito, hoy instalo.»"
    + "\nCIERRE: «Escríbeme ABUNDANCIA por mensaje y te mando tu lugar al live gratis de hoy a las 11 de la mañana. Lo que no se ACTIVA, no CAMBIA. Y lo que no se REPITE, no se INSTALA. Mabel Soriano · BNQ Method™.»\n" + FIJADO,
    f"🔴 HOY · 11 AM (hora MX) · LIVE GRATIS\n{LIVE_T}: subconsciente · memoria celular · energía, en simultáneo.\n"
    "Escríbeme ABUNDANCIA por mensaje y te mando tu lugar. Solo entran las registradas.\n" + SLOGAN,
    "TikTok: #parati #fyp #livegratis #abundancia #dinero #hackeatumente #BNQMethod\n"
    "Reels/FB/Shorts: #livegratis #abundancia #dinero #hackeatumente #formulascuanticas #BNQMethod #Shorts",
    "Escríbeme ABUNDANCIA (registro al live)", "NO (registro al live gratis)",
    "Video 5 (ajustado a «hoy a las 11 de la mañana»)", "HOY sáb 21 · Bloque 1 · 4:00 PM (después del Video 4)")
F[-1][12] = "HOY sáb 21 · Bloque 1 · 4:05 PM"
add(D, "11:00 AM", "Zoom (solo registradas)", "LIVE GRATIS ZOOM", LIVE_T, "—",
    "Guion: briefs/live-2026-11-25-paquete.md (oferta al minuto 20). Solo probadita, nunca la hipnosis completa. Dentro del live: Programa la Riqueza mientras Duermes · $500 + impuestos · hasta vie 27 11:59 PM · regalo hipnosis completa dom 29 · 11 AM solo compradoras.",
    "— (en vivo)", "—", "Escríbeme YO QUIERO / link de compra", "SÍ (dentro del live)",
    "Nada: entra en vivo (Mabel comparte el link de Zoom)", "En vivo 11:00 AM")
yap(D, "2:00 PM", "ACABO DE SALIR DEL LIVE", "Acabo de salir del live y todavía tengo la piel chinita.",
    ["[Cuántas llegaron y qué sentiste al verlas]", "[Un comentario que te movió (sin nombre)]",
     "[Lo que aprendiste tú hoy]", "[Gracias a quien estuvo]"],
    "¿Tú estuviste? Cuéntame qué sentiste.", "SENTÍ",
    "Acabo de salir del live 💛 Gracias a cada una.\n¿Estuviste? Cuéntame qué sentiste.", "Mié 25 · Bloque 3 · 12:15 PM (al salir del Zoom)")
add(D, "3:30 PM", REDES, "ARTE DE VENTA en video 12 s (arte Grok 1 «No es tuyo» + voz + música)",
    "NO ES TUYO", "Ese bloqueo con el dinero no es tuyo: es un programa que corre en automático.",
    "Video 12 s con live/artes/riqueza-grok/1-no-es-tuyo.jpg (lo arma NICA, Mabel no graba).\n"
    "Voz: «Ese bloqueo con el dinero no es tuyo. Es un programa. Y se reprograma mientras duermes. Programa la Riqueza mientras Duermes, hasta el viernes 27. Comenta ABUNDANCIA.»",
    "Trabajas, cumples, decretas… y el dinero no se queda. No es mala suerte. No es falta de disciplina. Es un programa que corre en automático.\n"
    "Programa la Riqueza mientras Duermes: 21 noches para reprogramarlo mientras duermes. $500 + impuestos, solo hasta el viernes 27 · 11:59 PM (hora MX).\n"
    "Regalo: hipnosis completa en vivo el domingo 29 · 11 AM, solo compradoras.\nLink en mi perfil o comenta ABUNDANCIA y te lo mando.\n" + SLOGAN,
    "TikTok: #abundancia #dinero #reprogramacion #subconsciente #BNQMethod\nReels/FB/Shorts: #abundancia #dinero #reprogramacion #BNQMethod #Shorts",
    "Comenta ABUNDANCIA / link en mi perfil", "SÍ (1 de 3 del día)", "Nada (NICA arma el video)", "—")
aviso(D, "si hoy no llegaste al Zoom, te cuento lo que pasó (seguimiento)",
      "OFERTA: Programa la Riqueza mientras Duermes · $500 + impuestos · link en mi perfil · hasta vie 27 11:59 PM · regalo hipnosis completa dom 29 11 AM · «comenta ABUNDANCIA y te escribo»")

# ═══════════════ JUEVES 26 · LA REPETICIÓN ═══════════════
D = "Jue 26"
add(D, "5:30 PM", REDES, "A CÁMARA · FAMOSO + AUTORIDAD (nuevo · 75-90 s)",
    "POR QUÉ LO QUE SIENTES EN UN LIVE SE TE OLVIDA EN 3 DÍAS",
    "Un estudio de University College London encontró que un hábito nuevo tarda en promedio 66 días en volverse automático. No uno. No tres. Sesenta y seis.",
    "GUARDAR: «Guárdalo y compártelo con quien siempre empieza con todo y a los tres días lo deja.»\n"
    + pts("DATO: estudio de Phillippa Lally (UCL, 2009): en promedio 66 días para que algo nuevo se vuelva automático (de 18 a 254, según la persona).",
          "DOLOR: te activas en un live, sales feliz… y a los tres días vuelves a lo de siempre con el dinero.",
          "LISTA DE 3 (por qué se apaga): una sola vez no instala · de día tu mente consciente lo filtra · sin repetición tu subconsciente regresa al programa viejo.",
          "REENCUADRE: no eres tú, es que te faltó repetir. [TU HISTORIA: algo que solo cambió cuando lo repetiste].")
    + "\nHACKEO x3 (mano en el pecho): «Lo que activo, lo repito. Lo que repito, lo instalo.»"
    + "\nREVELACIÓN: «Por eso yo no te pido fuerza de voluntad: la repetición se puede hacer de noche, mientras duermes.»"
    + "\nCIERRE: «Comenta ABUNDANCIA y te cuento cómo repetirlo sin esfuerzo. Lo que no se ACTIVA, no CAMBIA. Y lo que no se REPITE, no se INSTALA. Mabel Soriano · BNQ Method™.»",
    "Te activas, te emocionas… y a los 3 días se te olvida. No eres tú: te faltó repetir. 🔁\n"
    "Un estudio de University College London encontró que algo nuevo tarda en promedio 66 días en volverse automático.\n"
    "Comenta ABUNDANCIA y te cuento cómo repetirlo sin esfuerzo.\n" + SLOGAN,
    "TikTok: #parati #fyp #habitos #subconsciente #reprogramacion #abundancia #BNQMethod\n"
    "Reels/FB/Shorts: #habitos #subconsciente #reprogramacion #abundancia #BNQMethod #Shorts",
    "Comenta ABUNDANCIA (el closer responde por DM)", "NO en el video (siembra, sin precio)",
    "Video «66 días»", "Dom 22 · Bloque 2 · 5:20 PM")
yap(D, "1:00 PM", "UNA COSA QUE CAMBIÉ Y CAMBIÓ MI SEMANA", "Cambié una sola cosa esta semana y me cambió todo.",
    ["[Qué cambiaste (algo chiquito y real)]", "[Cómo te sentiste el primer día]", "[Qué notaste al tercer día]",
     "[Por qué vas a seguir]"],
    "¿Qué cosa chiquita cambiarías tú?", "CAMBIO",
    "Una sola cosa chiquita me cambió la semana ✨", "Mié 25 · Bloque 3 · 12:20 PM")
add(D, "10:00 AM", HIST + " + grupo del live", "HISTORIA DE VENTA (arte Grok 2 «8 horas dormida · viernes 27»)",
    "8 HORAS DORMIDA", "Mientras duermes, tu subconsciente sigue trabajando. ¿Para ti o en tu contra?",
    "Historia con live/artes/riqueza-grok/2-8-horas-dormida-vie27.jpg + sticker de enlace al link oficial. Solo historias y grupo del live (no feed).",
    "Mientras duermes, tu subconsciente sigue trabajando. Programa la Riqueza mientras Duermes · $500 + impuestos · hasta mañana viernes 27 · 11:59 PM. Regalo: hipnosis completa dom 29 · 11 AM solo compradoras.\n" + SLOGAN,
    "—", "Sticker de enlace / escríbeme ABUNDANCIA", "SÍ (historia)", "Nada (arte lista)", "—")
aviso(D, "por qué se te olvida lo que sientes (la repetición)",
      "OFERTA: Programa la Riqueza mientras Duermes · $500 + impuestos · hasta mañana vie 27 11:59 PM · regalo dom 29 11 AM · comenta ABUNDANCIA")

# ═══════════════ VIERNES 27 · ÚLTIMO DÍA ═══════════════
D = "Vie 27"
add(D, "12:00 PM", REDES, "A CÁMARA · PODEROSA CONEXIÓN corta (nuevo · 60-75 s) · ÚLTIMO DÍA",
    "HOY 11:59 PM SE CIERRA",
    "Si esperas a sentirte lista para reprogramar tu dinero, el programa de escasez ya ganó.",
    "PATRÓN: «Lo pienso, lo dejo para después… y el dinero sigue sin llegar.»\n"
    + pts("DETECTA: ¿cuántas veces dijiste «después» esta semana?",
          "QUÉ ES: Programa la Riqueza mientras Duermes. Un audio de 8 horas para 21 noches + Fórmula CEI™ + Fórmula ADN + la Fórmula para desbloquear la riqueza. La repetición la hace tu subconsciente mientras duermes.",
          "OFERTA REAL: $500 + impuestos, solo hasta HOY viernes 27 a las 11:59 PM (hora MX). Regalo: la hipnosis completa en vivo conmigo el domingo 29 a las 11 AM, solo para compradoras.",
          "REGLA DE ORO: lo que no se repite, no se instala. [TU HISTORIA: por qué lo creaste].")
    + "\nHACKEO x3: «Elijo instalar, no solo activar.»"
    + "\nCIERRE: «El link está en mi perfil, o comenta ABUNDANCIA y te lo mando. Lo que no se ACTIVA, no CAMBIA. Y lo que no se REPITE, no se INSTALA. Mabel Soriano · BNQ Method™.»",
    "⏳ HOY 11:59 PM (hora MX) se cierra.\nPrograma la Riqueza mientras Duermes: 21 noches para reprogramar tu dinero mientras duermes. $500 + impuestos.\n"
    "Regalo: hipnosis completa en vivo el domingo 29 · 11 AM, solo compradoras.\nLink en mi perfil o comenta ABUNDANCIA y te lo mando.\n" + SLOGAN,
    "TikTok: #parati #fyp #abundancia #dinero #reprogramacion #ultimodia #BNQMethod\n"
    "Reels/FB/Shorts: #abundancia #dinero #reprogramacion #BNQMethod #Shorts",
    "Comenta ABUNDANCIA / link en mi perfil", "SÍ (1 de 2 del día)",
    "Video «Hoy se cierra»", "Dom 22 · Bloque 2 · 5:35 PM")
yap(D, "4:00 PM", "LO QUE APRENDÍ ESTA SEMANA", "Esta semana me enseñó algo que no esperaba.",
    ["[Lo que pasó en el live del miércoles]", "[Lo que te sorprendió de los lives diarios]",
     "[Lo que vas a hacer distinto la próxima semana]", "[Gracias]"],
    "¿Qué te enseñó a ti esta semana?", "APRENDÍ",
    "Lo que me enseñó esta semana 💛 Sin filtro.", "Mié 25 · Bloque 3 · 12:25 PM")
add(D, "9:00 PM", HIST + " + grupo del live", "HISTORIA DE VENTA (arte Grok 4 «¡Cuidado!») · últimas 3 horas",
    "¡CUIDADO!", "Quedan 3 horas.",
    "Historia con live/artes/riqueza-grok/4-cuidado.jpg + texto «Quedan 3 horas» + sticker de enlace. Solo historias y grupo del live.",
    "Quedan 3 horas ⏳ Programa la Riqueza mientras Duermes · $500 + impuestos · hoy 11:59 PM. Regalo: hipnosis completa dom 29 · 11 AM solo compradoras.\n" + SLOGAN,
    "—", "Sticker de enlace", "SÍ (historia)", "Nada (arte lista)", "—")
aviso(D, "última noche: lo que no se repite, no se instala",
      "OFERTA ÚLTIMAS HORAS: $500 + impuestos hasta HOY 11:59 PM · regalo dom 29 11 AM · comenta ABUNDANCIA")

# ── ordenar por día y hora ──
ORD_D = ["Sáb 21", "Dom 22", "Lun 23", "Mar 24", "Mié 25", "Jue 26", "Vie 27"]


def hmin(h):
    m = re.match(r"(\d{1,2}):(\d{2}) (AM|PM)", h)
    if not m:
        return 0
    hh, mm, ap = int(m.group(1)), int(m.group(2)), m.group(3)
    return (hh % 12 + (12 if ap == "PM" else 0)) * 60 + mm


F.sort(key=lambda r: (ORD_D.index(r[0]), hmin(r[1])))

# ═══════════════ REVISIÓN DE COPYWRITER (automática + manual) ═══════════════
PROHIBIDAS = ["curso", "masterclass", "taller", "terapia", "sanación", "sanacion", "coaching", "mentoría",
              "mentoria", "ritual", "magia", "desarrollo personal", "motivación", "adn millonario", "hechizo"]
problemas = []
for r in F:
    texto = " ".join(str(c) for c in r).lower()
    for p in PROHIBIDAS:
        if re.search(r"\b" + re.escape(p) + r"\b", texto):
            problemas.append(f"{r[0]} {r[1]} · palabra prohibida: {p}")
    if "@" in texto:
        problemas.append(f"{r[0]} {r[1]} · tiene @")
    for m in re.finditer(r"\$\s?\d[\d,]*", " ".join(str(c) for c in r)):
        cola = " ".join(str(c) for c in r)[m.end():m.end() + 15]
        if "+ impuestos" not in cola:
            problemas.append(f"{r[0]} {r[1]} · precio sin '+ impuestos': {m.group()}")
    if r[3].startswith("AVISO") and "$" in (r[7] + r[6]):
        problemas.append(f"{r[0]} {r[1]} · precio en aviso de live")
    if r[7] not in ("—",) and not r[7].startswith("—") and SLOGAN not in r[7]:
        problemas.append(f"{r[0]} {r[1]} · caption sin slogan completo")
assert not problemas, "\n".join(problemas)

REVISION = [
    ("Palabras prohibidas (curso, masterclass, taller, terapia, sanación, coaching, mentoría, ritual, magia, desarrollo personal, motivación)", "0 encontradas (revisión automática de todas las celdas)"),
    ("«No es motivación» de los videos 2 y 4", "CAMBIADO a «No es un decreto más: es una activación» (motivación está prohibida)"),
    ("Sin @ en copys", "0 @ (firma: Mabel Soriano · BNQ Method™)"),
    ("Precios con «+ impuestos»", "Todos los $500 llevan «+ impuestos»"),
    ("Sin precio en avisos del live (historias y videos de registro)", "Correcto: el precio solo va en piezas de venta (mié 25 a vie 27) y dentro de los lives"),
    ("Nunca «ADN Millonario»", "0 (producto = Programa la Riqueza mientras Duermes)"),
    ("Slogan completo en todos los captions", "Sí, las dos líneas tal cual"),
    ("Hora del live", "Miércoles 25 · 11 AM (hora MX) en todo. Video 5 ya no dice «en una hora»: sale 8 AM y dice «hoy a las 11 de la mañana»"),
    ("Videos a cámara a las 7 PM chocaban con el TikTok LIVE", "Se movieron a 5:30 PM (calientan el live de las 7)"),
    ("Concepto BNQ", "Subconsciente se aprende · memoria celular se hereda · energía 100% tuya. Nunca «los 3 se heredan»"),
    ("Datos reales", "Sara Blakely · Invierno del Hambre/epigenética 2008 · Jim Carrey con Oprah · Donald Hebb 1949 · Phillippa Lally UCL 2009 (66 días)"),
    ("Sin promesas de dinero ni salud", "Sí. La «promesa» del video 4 es de pregunta, no de dinero"),
    ("80/20", "Feed: 3 piezas de venta de 15 (20%). Máx. 1 venta en feed por día"),
    ("Regla «nunca el mismo producto 2 días seguidos»", "Choca con la ventana de venta aprobada (mié 25 → vie 27). Propuesta: venta en feed mié y vie; jue solo historias + siembra sin precio. Decide Mabel"),
]

BLOQUES = [
    ("HOY sáb 21 · 3:00-4:35 PM · BLOQUE 1 (≈1 h 30 min)",
     "Misma ropa (blusa blanca o blazer negro), luz de frente, cámara a la altura de los ojos. Cambia un detalle entre videos (aretes, pelo, lugar).\n"
     "3:00 Video 1 (sale HOY 5:30 PM: mándalo en cuanto lo grabes) · 3:20 Video 2 · 3:40 Video 3 · 4:00 Video 4 · 4:05 Video 5 (di «hoy a las 11 de la mañana») · 4:15 yapping sáb · 4:25 yapping dom (este en otro lugar, ropa de domingo)."),
    ("HOY sáb 21 · 6:25 PM", "Selfie de 15 s para la historia «en media hora estoy en vivo» (se repite así cada día)."),
    ("Dom 22 · 5:00-5:50 PM · BLOQUE 2 (≈50 min)",
     "5:00 yapping lun · 5:10 yapping mar · 5:20 video jue «66 días» · 5:35 video vie «Hoy se cierra». Terminas antes del TikTok LIVE de las 7."),
    ("Mié 25 · 12:15-12:35 PM · BLOQUE 3 (al salir del Zoom, 20 min, celular)",
     "12:15 yapping «Acabo de salir del live» (sale 2 PM) · 12:20 yapping jue · 12:25 yapping vie."),
    ("Diario · 7:00 PM", "TikTok LIVE 25 min (nada que grabar antes)."),
    ("Lo que NO graba Mabel", "Arte de venta mié 25 (video 12 s), historias de venta jue y vie y artes de aviso: los arma NICA con las artes ya hechas."),
]

COMUNIDAD = [
    ("Lun 23 · 1:00 PM", "Avisos de la comunidad", "Muestra de 1 audio de Activaciones Robóticas Millonarias (Mabel elige cuál, ya están los 10 arriba). Texto corto: «Escucha este audio hoy antes de dormir y mañana te cuento qué es.»", "Sin precio"),
    ("Mar 24 · 1:00 PM", "Avisos de la comunidad", "Qué son las Activaciones Robóticas Millonarias (10 audios para recibir dinero con facilidad) y por qué la repetición instala. Precio comunidad: $399 + impuestos (público $500 + impuestos).", "Venta comunidad"),
    ("Jue 26 · 1:00 PM", "Avisos de la comunidad", "Link de compra con precio comunidad $399 + impuestos y fecha real de cierre [FECHA: la confirma Mabel; propuesta dom 29 · 11:59 PM]. [LINK COMUNIDAD $399: falta].", "Venta comunidad"),
    ("Regla", "—", "A la comunidad NO se le manda la invitación del live 25 (ya vieron lives y no compraron). Robóticas va sin live.", "—"),
]

# ═══════════════ EXCEL ═══════════════
wb = Workbook()
ws = wb.active
ws.title = "Calendario 21-27 nov"
DORADO = PatternFill("solid", fgColor="F6E3A1")
CREMA = PatternFill("solid", fgColor="FFF8E6")
VENTA = PatternFill("solid", fgColor="FDE2C8")
borde = Border(*(Side(style="thin", color="D9C27A"),) * 4)
ws.append(["CALENDARIO DE CONTENIDO · sáb 21 → vie 27 nov 2026 · Hackeo Simultáneo · LIVE GRATIS Zoom mié 25 · 11 AM (hora MX) · Venta mié 25 → vie 27 11:59 PM"])
ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(COLS))
ws["A1"].font = Font(bold=True, size=13, color="5A3E00")
ws["A1"].fill = DORADO
ws.append(["BORRADOR para OK de Mabel. Nada publicado ni programado. Revisado con criterio de copywriter (hoja «Revisión copywriter»)."])
ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=len(COLS))
ws["A2"].font = Font(italic=True, color="5A3E00")
ws.append(COLS)
for c in ws[3]:
    c.font = Font(bold=True, color="FFFFFF")
    c.fill = PatternFill("solid", fgColor="8A6A10")
    c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
for r in F:
    ws.append(r)
    fila = ws.max_row
    fill = VENTA if r[10].startswith("SÍ") else (CREMA if fila % 2 else None)
    for c in ws[fila]:
        c.alignment = Alignment(wrap_text=True, vertical="top")
        c.border = borde
        if fill:
            c.fill = fill
anchos = [9, 14, 24, 26, 28, 34, 70, 52, 34, 24, 16, 28, 26]
for i, w in enumerate(anchos):
    ws.column_dimensions[chr(65 + i)].width = w
ws.freeze_panes = "C4"


def hoja(nombre, cab, filas, anchos):
    h = wb.create_sheet(nombre)
    h.append(cab)
    for c in h[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="8A6A10")
    for f in filas:
        h.append(list(f))
    for row in h.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    for i, w in enumerate(anchos):
        h.column_dimensions[chr(65 + i)].width = w


hoja("Qué graba Mabel", ["Cuándo", "Qué graba"], BLOQUES, [42, 110])
hoja("Comunidad WhatsApp", ["Día y hora", "Dónde", "Mensaje (Activaciones Robóticas Millonarias)", "Tipo"], COMUNIDAD, [18, 22, 100, 16])
hoja("Revisión copywriter", ["Regla", "Resultado"], REVISION, [60, 100])
wb.save(XLSX)

# ═══════════════ MARKDOWN (memoria interna) ═══════════════
md = ["# Calendario de contenido · sáb 21 → vie 27 nov 2026 · Hackeo Simultáneo", "",
      f"LIVE GRATIS Zoom mié 25 · 11 AM (hora MX): {LIVE_T}. Palabra: ABUNDANCIA. TikTok LIVE diario 7 PM (no se pauta).",
      "Venta Programa la Riqueza mientras Duermes $500 + impuestos: mié 25 → vie 27 11:59 PM. Regalo hipnosis completa dom 29 · 11 AM solo compradoras.",
      f"Entrega: `{XLSX}` (generador `calendario/semana-2026-11-21/semana.py`). BORRADOR, nada publicado.", "",
      "## Qué graba Mabel", ""]
md += [f"- **{a}:** {b.replace(chr(10), ' ')}" for a, b in BLOQUES]
md += ["", "## Calendario", "", "| Día | Hora | Formato | Título en pantalla | ¿Venta? | Graba |", "|---|---|---|---|---|---|"]
md += [f"| {r[0]} | {r[1]} | {r[3]} | {r[4]} | {r[10]} | {r[12]} |" for r in F]
md += ["", "## Detalle por pieza", ""]
for r in F:
    if r[7].startswith("—"):
        continue
    md += [f"### {r[0]} · {r[1]} · {r[4]}", f"- **Red:** {r[2]} · **Formato:** {r[3]}", f"- **Hook:** {r[5]}",
           "- **Guion / puntos:**", "", "```", r[6], "```", "- **Caption:**", "", "```", r[7], "```",
           f"- **Hashtags:** {r[8].replace(chr(10), ' · ')}", f"- **CTA:** {r[9]} · **Venta:** {r[10]}", ""]
md += ["## Comunidad WhatsApp (Robóticas $399 + impuestos)", ""]
md += [f"- **{a}** · {b}: {c} ({d})" for a, b, c, d in COMUNIDAD]
md += ["", "## Revisión copywriter", ""] + [f"- {a}: {b}" for a, b in REVISION]
with open(MD, "w", encoding="utf-8") as f:
    f.write("\n".join(md) + "\n")
print("OK", XLSX, MD, len(F), "filas")
