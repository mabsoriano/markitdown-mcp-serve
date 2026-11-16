"""Semana 16–22 nov 2026 · campaña PROGRAMA LA RIQUEZA MIENTRAS DUERMES (sin pauta, LIVES en TikTok).
2 piezas diarias con Mabel (yapping + famoso/Poderosa Conexión o aviso de LIVE) + 1 NAIA (abre con gancho).
Reglas: sin @ en copys · sin precio en avisos de LIVE · sin probadita larga · eslogan nuevo. Uso: python3 semana.py"""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
AQUI = os.path.dirname(os.path.abspath(__file__))
FIRMA = "Lo que no se activa, no cambia. Y lo que no se repite, no se instala.\nMabel Soriano · mabradiante · BNQ Method™"
PROD = "Programa la Riqueza mientras Duermes"
CTA_PROD = f"Si el dinero no te llega o no se te queda, {PROD} está en el link de mi perfil: 21 noches para reprogramarlo."
H_D = "#dinero #abundancia #hackeatumente #reprogramacion #BNQMethod #mabradiante"
H_Y = "#mabradiante #BNQMethod #tdah #emprendedora #mamaemprendedora"
H_N = "#NAIA #activacion #abundancia #hackeatumente #BNQMethod"
def g(*partes):
    t, out = 0.0, []
    for et, tx in partes:
        d = max(4, round(len(tx.split()) / 2.6)); a, b = int(t), int(t + d)
        out.append(f"{a//60}:{a%60:02d}–{b//60}:{b%60:02d} {et + ': ' if et else ''}{tx}"); t += d
    return "\n".join(out)
F = []
def add(*r): F.append(list(r))
def Y(f, dia, hora, titulo, hook, puntos, pregunta, copy):
    add(f, dia, hora, "Mabel a cámara (1–2 min, sin guion)", "Yapping (conexión, sin venta)", titulo, hook,
        "Puntos guía:\n" + "\n".join(f"{i}. {p}" for i, p in enumerate(puntos, 1)) + f"\nCierre: «{pregunta}»",
        f"0–3 s: {titulo}", copy + "\n" + FIRMA, H_Y, "Sin CTA")
def NAIA(f, dia, hora, gancho, tema, hackeos, orden, frase, copy):
    guion = (f"[TÚ, 0–2 s] {gancho}\n[NAIA] Hoy activamos tu {tema}. Pon tu mano en el pecho. Repite conmigo.\n" + " ".join(hackeos) +
             f"\nHoy instalo una nueva orden: {orden}\n{frase} {frase} {frase}\nLo que no se activa, no cambia y se transforma. Yo soy NAIA. Y esto es mabradiante.")
    add(f, dia, hora, "NAIA · tus 2 primeros segundos a cámara + NAIA con movimiento", "NAIA · Audio robótico",
        f"NAIA · {tema.upper()}", gancho, guion,
        f"0–2 s: tú + «{gancho.upper()[:42]}». Luego NAIA con acercamiento lento, partículas doradas y subtítulos palabra por palabra. Frase clave en grande.",
        copy + "\n" + FIRMA, H_N, "Guardar")
def AVISO(f, dia, hora):
    add(f, dia, hora, "Mabel a cámara (15–30 s) + historia + WhatsApp", "Aviso del LIVE (3 h antes, SIN precio)",
        "HOY 8:30 PM EN VIVO EN TIKTOK", "Hoy a las 8:30 de la noche estoy en vivo aquí en TikTok.",
        g(("GANCHO", "Hoy a las 8:30 de la noche estoy en vivo aquí en TikTok."),
          ("QUÉ HAREMOS", "Te explico por qué el dinero no se queda y cómo reprogramarlo mientras duermes."),
          ("CTA", "Actívale la campanita para que te avise.")),
        "0–3 s: HOY 8:30 PM · EN VIVO EN TIKTOK · ACTIVA LA CAMPANITA (sin precio).",
        "Hoy a las 8:30 PM (hora CDMX) estoy en vivo en TikTok 🔴 Por qué el dinero no se queda y cómo reprogramarlo mientras duermes. Actívale la campanita.\n" + FIRMA, H_D, "LIVE TikTok hoy")
def LIVE(f, dia):
    add(f, dia, "8:30 PM", "Mabel EN VIVO en TikTok (30–45 min)", "LIVE EN TIKTOK", "LIVE: POR QUÉ EL DINERO NO SE QUEDA", "Si el dinero no te llega o no se te queda, quédate 5 minutos.",
        "Guion: briefs/campana-riqueza-2026-11-15-al-21.md (sección 2). Probadita de 2 minutos MÁXIMO. Oferta: Programa la Riqueza mientras Duermes, link en perfil, regalo hipnosis COMPLETA en vivo el domingo 22 · 11 AM solo compradoras (precio y regalo hasta el sábado 21). Pide «escríbeme YO». Repite la oferta cada vez que entre gente.",
        "—", "—", "—", "Producto · link en perfil")

# ── LUNES 16 · último día del Buen Fin ──
Y("2026-11-16", "Lunes 16", "1:00 PM", "LO QUE APRENDÍ DE MI LIVE DEL DOMINGO", "El domingo hice un LIVE y quiero contarte lo que aprendí.",
  ["[Cuántas se inscribieron y cuántas llegaron (62 y 25)]", "[Lo que sentiste al ver quién se quedó hasta el final]", "[Lo que vas a hacer distinto]", "[Gracias a quien estuvo]"],
  "¿Tú qué haces cuando algo no sale como esperabas?", "Lo que aprendí de mi LIVE 💛 Sin filtro.\n¿Tú qué haces cuando algo no sale como esperabas? 👇")
add("2026-11-16", "Lunes 16", "6:00 PM", "Mabel a cámara (2–3 min)", "PODEROSA CONEXIÓN", "«ESTOY OCUPADA TODO EL DÍA Y NO AVANZO»",
    "Estar ocupada no es lo mismo que avanzar. Y tu mente lo sabe, aunque no te lo diga.",
    g(("VERDAD INCÓMODA", "Estar ocupada no es lo mismo que avanzar. Llenas el día de pendientes para sentir que haces algo, pero lo que de verdad te daría dinero sigue en la lista de «luego»."),
      ("PATRÓN", "Si te repites «estoy ocupada todo el día y no avanzo», permíteme llevarte al siguiente nivel con un bioneurohack + acción. No es motivación: es una activación."),
      ("ANTES", "Dale like y escribe AVANZO en comentarios."),
      ("1 · DETECTA", "De todo lo que hiciste hoy, ¿qué te acercó a cobrar? Si la respuesta es «nada», no es falta de tiempo: es un patrón."),
      ("2 · ROMPE EL PATRÓN INVISIBLE", "Perfeccionismo (lo preparo de más), dispersión (empiezo diez cosas) o evasión (hago lo fácil para no hacer lo que da miedo)."),
      ("3 · REPROGRAMA CON ACCIÓN", "Mañana, antes de abrir tus redes, haz 20 minutos la UNA tarea que más te acerca a cobrar."),
      ("4 · REPETICIÓN", "7 días: cada noche escribe qué acción incómoda hiciste que sí genera resultados."),
      ("REGLA DE ORO", "Si no te incomoda, no te está cambiando."),
      ("CUIDADO CON LA TRAMPA", "No pienses de más: crea, ejecuta, claridad, repetición."),
      ("PROMESA", "Si haces esto 7 días, tu pregunta va a dejar de ser «¿por qué no avanzo?» y va a ser «¿cómo escalo esto?»."),
      ("QUIÉN SOY", "[Soy Mabel Soriano, tu bioneurohacker de cabecera y creadora de BNQ Method™]"),
      ("CTA", "Y hoy es el último día del Buen Fin: la Hipnosis para hackear tus bloqueos con el dinero está en el link de mi perfil, solo hasta las 11:59 de la noche.")),
    "0–3 s: «ESTOY OCUPADA TODO EL DÍA Y NO AVANZO». Pasos: 1 DETECTA · 2 ROMPE EL PATRÓN · 3 REPROGRAMA · 4 REPETICIÓN. Final: «ÚLTIMO DÍA BUEN FIN · LINK EN MI PERFIL».",
    "Estar ocupada no es avanzar ⏳ Comenta AVANZO y haz este bioneurohack conmigo.\nÚltimo día del Buen Fin: la Hipnosis para hackear tus bloqueos con el dinero, hasta hoy 11:59 PM. Link en mi perfil.\n" + FIRMA, H_D, "Buen Fin · hoy")
NAIA("2026-11-16", "Lunes 16", "9:30 PM", "Trabajas, cumples, decretas… y el dinero no se queda.", "abundancia",
     ["Hoy hackeo mi escasez.", "Hackeo mis memorias de carencia.", "Hackeo los pactos de lealtad con la pobreza de mi linaje.", "Hackeo mi memoria celular y mi subconsciente."],
     "soy segura para recibir.", "Soy segura para recibir.", "¿Trabajas y el dinero no se queda? 🔓 Repite con NAIA y guárdalo.")

# ── MARTES 17 · LIVE TikTok 8:30 PM ──
Y("2026-11-17", "Martes 17", "1:00 PM", "MI ACTIVACIÓN DE 1 MINUTO ANTES DE TRABAJAR", "Esto es lo primero que hago antes de trabajar, y me toma un minuto.",
  ["[Dónde estás: coche, cocina, caminando]", "[Haces tu minuto de activación frente a cámara]", "[Cómo te cambia el día]"],
  "¿Tú qué haces para no arrancar en automático?", "Mi minuto antes de trabajar ☀️ Hazlo conmigo.\n¿Tú qué haces para no arrancar en automático? 👇")
AVISO("2026-11-17", "Martes 17", "5:30 PM")
LIVE("2026-11-17", "Martes 17")
NAIA("2026-11-17", "Martes 17", "10:00 PM", "No te da miedo fracasar. Te da miedo brillar.", "éxito",
     ["Hoy hackeo mi miedo al éxito.", "Hackeo las memorias que me dijeron que no era suficiente.", "Hackeo los pactos de lealtad que me mantenían pequeña.", "Hackeo mi memoria celular y mi subconsciente."],
     "el éxito es seguro para mí.", "El éxito es seguro para mí.", "¿Y si no te da miedo fracasar, sino brillar? ✨ Repite con NAIA.")

# ── MIÉRCOLES 18 · chakras 10 AM (Zoom, solo comunidad) ──
Y("2026-11-18", "Miércoles 18", "1:00 PM", "HOY ACTIVAMOS LOS 7 CHAKRAS CON MI COMUNIDAD", "Hoy en la mañana hice algo distinto con mi comunidad, y te lo cuento.",
  ["[Qué hicieron en la activación de las 10 AM]", "[Qué sentiste tú]", "[Por qué la hiciste solo para tu comunidad]"],
  "¿Quieres estar en la próxima? Únete a mi comunidad Neurohackers: link en mi perfil.", "Hoy activamos los 7 chakras con mi comunidad 🌈\n¿Quieres estar en la próxima? Link en mi perfil.")
add("2026-11-18", "Miércoles 18", "6:00 PM", "Mabel a cámara (2 min)", "FAMOSO + AUTORIDAD", "ARIANNA HUFFINGTON SE DESMAYÓ DE CANSANCIO",
    "En 2007, Arianna Huffington, fundadora del HuffPost, se desmayó de agotamiento en su oficina. Y eso explica por qué tú vives cansada.",
    g(("GANCHO", "En 2007, Arianna Huffington, fundadora del HuffPost, se desmayó de agotamiento en su oficina. Y eso explica por qué tú vives cansada."),
      ("GUARDAR Y COMPARTIR", "Guárdalo y compártelo con quien está cansada de estar cansada."),
      ("DOLOR", "Duermes y despiertas igual. Haces todo por todos y a ti no te queda energía para lo que de verdad quieres."),
      ("LISTA DE 3", "3 fugas de energía: 1. Creer que descansar es de flojas. 2. Decir que sí cuando quieres decir que no. 3. Cargar lo que no puedes controlar."),
      ("DATO / AUTORIDAD", "Ella contó que se golpeó la cara al caer y que eso la llevó a cambiar su forma de vivir; después escribió el libro «Thrive»."),
      ("TU HISTORIA", "[15–20 s: el momento en que tu cuerpo te dijo «ya basta»]"),
      ("HACKEO", "Divide una hoja en «en mi control» y «fuera de mi control». Suelta una cosa de la segunda. Repite 3 veces: mi energía regresa a mí."),
      ("REVELACIÓN", "No te falta fuerza. Te sobran fugas."),
      ("CIERRE", "Guárdalo y únete a mi comunidad Neurohackers: el link está en mi perfil.")),
    "0–3 s: ARIANNA HUFFINGTON SE DESMAYÓ DE CANSANCIO. Lista: 1 DESCANSAR NO ES DE FLOJAS · 2 SÍ CUANDO ES NO · 3 LO QUE NO CONTROLAS. Aviso: práctica de bienestar.",
    "Arianna Huffington se desmayó de cansancio ⚡ y las 3 fugas de energía que tú quizá tienes.\nÚnete a mi comunidad Neurohackers: link en mi perfil.\n" + FIRMA, "#energia #burnout #hackeatumente #BNQMethod", "Comunidad")
NAIA("2026-11-18", "Miércoles 18", "9:30 PM", "No estás cansada: tienes fugas de energía.", "energía",
     ["Hoy hackeo mis fugas de energía.", "Hackeo las memorias de cargar lo que no es mío.", "Hackeo los pactos de lealtad con el cansancio.", "Hackeo mi memoria celular y mi subconsciente."],
     "mi energía regresa a mí.", "Mi energía regresa a mí.", "Recupera tu energía 🌈 Repite con NAIA.")

# ── JUEVES 19 · LIVE TikTok 8:30 PM ──
Y("2026-11-19", "Jueves 19", "1:00 PM", "RESPONDO LO QUE MÁS ME PREGUNTAN DEL DINERO", "Esta es la pregunta que más me hacen del dinero, y hoy te la contesto.",
  ["[Lee una pregunta real de comentarios o DMs]", "[Tu respuesta en 3 frases]", "[Invita: hoy 8:30 PM en vivo respondo más]"],
  "Déjame tu pregunta y la contesto en el LIVE de hoy.", "Respondo tu pregunta del dinero 💬\nDéjamela aquí y hoy a las 8:30 PM la contesto en vivo 👇")
AVISO("2026-11-19", "Jueves 19", "5:30 PM")
LIVE("2026-11-19", "Jueves 19")
NAIA("2026-11-19", "Jueves 19", "10:00 PM", "Si te da culpa cobrar, este audio es para ti.", "valor",
     ["Hoy hackeo mi culpa de cobrar.", "Hackeo las memorias de «el dinero cuesta mucho trabajo».", "Hackeo los pactos de lealtad que me mantenían en carencia.", "Hackeo mi memoria celular y mi subconsciente."],
     "cobro lo que vale mi trabajo.", "Cobro lo que vale mi trabajo.", "Tu trabajo vale ✨ Repite con NAIA antes de cobrar.")

# ── VIERNES 20 ──
Y("2026-11-20", "Viernes 20", "1:00 PM", "UN DÍA NORMAL DE UNA NEUROHACKER CON TDAH", "Te voy a enseñar cómo es de verdad un día mío, sin filtro.",
  ["[A qué hora empiezas y qué haces primero]", "[Tu activación de 1 minuto]", "[Lo que más te cuesta del día]", "[Cómo te organizas con 4 horas]"],
  "¿Y tú cómo arrancas tu día?", "Un día mío, sin filtro 🧠☕\n¿Y tú cómo arrancas el tuyo? 👇")
add("2026-11-20", "Viernes 20", "6:00 PM", "Mabel a cámara (2 min)", "FAMOSO + AUTORIDAD", "A OPRAH LA QUITARON DE LAS NOTICIAS",
    "A Oprah Winfrey la quitaron de su puesto como presentadora de noticias en Baltimore. Y eso no la detuvo.",
    g(("GANCHO", "A Oprah Winfrey la quitaron de su puesto como presentadora de noticias en Baltimore. Y eso no la detuvo."),
      ("GUARDAR Y COMPARTIR", "Guárdalo y compártelo con quien siente que la vida le cerró una puerta."),
      ("DOLOR", "Te dijeron que no, te quitaron algo o te fue mal, y desde ahí decidiste que el dinero no es para ti."),
      ("LISTA DE 3", "3 creencias que ella no se permitió: 1. Si me quitaron algo, es porque no valgo. 2. Una puerta cerrada es el final. 3. Tengo que encajar donde no encajo."),
      ("DATO / AUTORIDAD", "Ella ha contado que la movieron de las noticias a un programa de la mañana; ahí encontró su voz y años después tuvo uno de los programas más vistos de la televisión."),
      ("TU HISTORIA", "[15–20 s: una puerta que se cerró y lo que se abrió después]"),
      ("HACKEO", "Mano en el pecho y repite 3 veces: lo que se cierra me lleva a lo que es para mí."),
      ("REVELACIÓN", "No te quitaron tu valor. Te movieron al lugar donde lo vas a cobrar."),
      ("CTA", CTA_PROD + " Solo hasta mañana sábado.")),
    "0–3 s: A OPRAH LA QUITARON DE LAS NOTICIAS. Lista: 1 NO ES TU VALOR · 2 NO ES EL FINAL · 3 NO TIENES QUE ENCAJAR. Final: «PROGRAMA LA RIQUEZA · LINK EN MI PERFIL».",
    "A Oprah la quitaron de las noticias 📺 y las 3 creencias que ella no se permitió.\n" + PROD + ": link en mi perfil, solo hasta mañana sábado.\n" + FIRMA, H_D, "Producto · link en perfil")
NAIA("2026-11-20", "Viernes 20", "9:30 PM", "Doce editoriales le dijeron que no a J.K. Rowling. Y tú dejaste de intentarlo con el primer no.", "persistencia",
     ["Hoy hackeo mi miedo al rechazo.", "Hackeo las memorias de cada «no» que me hizo pequeña.", "Hackeo los pactos de lealtad con rendirme.", "Hackeo mi memoria celular y mi subconsciente."],
     "un no es información, no es mi valor.", "Un no es información, no es mi valor.", "12 editoriales le dijeron que no a J.K. Rowling 📚 ¿Y tú? Repite con NAIA.")

# ── SÁBADO 21 · último día del precio · LIVE TikTok 8:30 PM ──
Y("2026-11-21", "Sábado 21", "1:00 PM", "POR QUÉ HAGO LO QUE HAGO", "Mucha gente me pregunta por qué hago esto, y hoy te lo cuento.",
  ["[Qué buscabas cuando empezaste]", "[El momento que lo cambió todo]", "[A quién quieres ayudar]", "[Hoy a las 8:30 PM estás en vivo]"],
  "¿Tú por qué me sigues? Cuéntame.", "Por qué hago lo que hago 💛\n¿Tú por qué me sigues? 👇")
AVISO("2026-11-21", "Sábado 21", "5:30 PM")
LIVE("2026-11-21", "Sábado 21")
NAIA("2026-11-21", "Sábado 21", "10:00 PM", "Si bajas tu precio antes de que te lo pidan, esto es para ti.", "merecimiento",
     ["Hoy hackeo mi «no merezco».", "Hackeo las memorias de esfuerzo sin recompensa.", "Hackeo los pactos de lealtad con la carencia.", "Hackeo mi memoria celular y mi subconsciente."],
     "merezco recibir.", "Merezco recibir.", "Merezco recibir 🔓 Repite con NAIA y guárdalo.")

# ── DOMINGO 22 · hipnosis completa 11 AM, SOLO compradoras (Zoom privado) ──
Y("2026-11-22", "Domingo 22", "1:00 PM", "LO QUE VIVÍ HOY CON MIS COMPRADORAS", "Hoy hice una hipnosis completa en vivo solo para quienes confiaron en mí.",
  ["[Cómo te sentiste]", "[Una palabra que escribieron (sin nombres, con permiso)]", "[Por qué solo para quienes compraron]"],
  "¿Te gustaría estar en la próxima? Escríbeme YO.", "Lo que viví hoy 💛 Gracias a quienes confiaron.\n¿Te gustaría estar en la próxima? Escríbeme YO 👇")
add("2026-11-22", "Domingo 22", "6:00 PM", "Mabel a cámara (2 min)", "FAMOSO + AUTORIDAD", "A MICHAEL JORDAN NO LO ELIGIERON",
    "A Michael Jordan no lo eligieron para el equipo principal de su escuela. Y eso cambió todo.",
    g(("GANCHO", "A Michael Jordan no lo eligieron para el equipo principal de su escuela. Y eso cambió todo."),
      ("GUARDAR Y COMPARTIR", "Guárdalo y compártelo con quien siente que nunca la eligen."),
      ("DOLOR", "Ves que a otras sí les llega, sí las eligen, sí les va bien. Y tú te quedas esperando tu turno."),
      ("LISTA DE 3", "3 creencias que lo pudieron frenar: 1. Si no me eligen, no sirvo. 2. Otros tienen más suerte. 3. Para qué intento si ya me dijeron que no."),
      ("DATO / AUTORIDAD", "Él ha contado que en segundo año lo dejaron en el equipo de nivel menor; entrenó todo ese año y después se convirtió en uno de los mejores jugadores de la historia."),
      ("TU HISTORIA", "[15–20 s: una vez que no te eligieron]"),
      ("HACKEO", "Repite 3 veces: yo me elijo primero."),
      ("REVELACIÓN", "Lo que no se repite, no se instala. Él no tuvo suerte: tuvo repetición."),
      ("CIERRE", "Guárdalo y sígueme: esta semana viene algo nuevo.")),
    "0–3 s: A MICHAEL JORDAN NO LO ELIGIERON. Lista: 1 NO ES TU VALOR · 2 NO ES SUERTE · 3 INTENTA OTRA VEZ.",
    "A Michael Jordan no lo eligieron 🏀 y las 3 creencias que lo pudieron frenar.\nGuárdalo y sígueme.\n" + FIRMA, H_D, "Guardar")
NAIA("2026-11-22", "Domingo 22", "9:30 PM", "Si el domingo en la noche te llega la angustia del lunes, haz esto antes de dormir.", "nueva semana",
     ["Hoy hackeo la angustia del lunes.", "Hackeo las memorias de semanas en modo supervivencia.", "Hackeo los pactos de lealtad con el cansancio.", "Hackeo mi memoria celular y mi subconsciente."],
     "empiezo esta semana en abundancia.", "Empiezo en abundancia.", "Activa tu semana antes de dormir 🌙 Repite con NAIA.")

import datetime as _dt
F.sort(key=lambda r: (r[0], _dt.datetime.strptime(r[2], "%I:%M %p")))
HOY = [
 ["1", "Lunes 16 · ya", "Subir la historia «Último día del Buen Fin»", "Ya la tienes (te la mandé). Repítela a las 6 PM y a las 10 PM.", "5 min"],
 ["2", "Lunes 16 · 1:00 PM", "Yapping «Lo que aprendí de mi LIVE del domingo»", "Pestaña «Calendario».", "10 min"],
 ["3", "Lunes 16 · 6:00 PM", "PODEROSA CONEXIÓN «Estoy ocupada todo el día y no avanzo»", "Pestaña «Calendario». Cierra con el último día del Buen Fin.", "20 min"],
 ["4", "Lunes 16 · 9:30 PM", "NAIA · Abundancia (tus 2 primeros segundos a cámara)", "Pestaña «Calendario».", "10 min"],
 ["5", "Martes 17 · 11:00 AM", "Live privado con tu(s) compradora(s)", "Lo prometido del Buen Fin, por Zoom privado.", "—"],
]
NUM = [
 ["Ventas de la semana 10–16", "$0 (al domingo); 0 «YO» en el live del 15"],
 ["LIVES", "6 → 28 → 55–60 personas; live del dom 15: 62 inscritas, 25 entraron, 9 al final"],
 ["Correo", "1,132 enviados · 233 aperturas (20.6%)"],
 ["Linktree / web / NAIA", "27 clics · 44 visitas · 8 registros"],
 ["WhatsApp", "172 (antes 100)"],
 ["Diagnóstico", "Ya llega gente; se pierde en el paso a comprar. Por eso: sin probaditas largas, oferta clara con regalo para compradoras, precio y regalo con fecha real (sábado 21)."],
 ["Meta de la semana", "3 ventas de Programa la Riqueza · LIVES de TikTok con 30+ personas · 60 clics en Linktree"],
]
COM = [
 ["Martes 17 · 1:00 PM", "Acercamiento 1 · valor + LIVE", "Mis neurohackers 💛 Les dejo la activación de NAIA de abundancia (video aquí abajo): pónganla con audífonos.\nY hoy a las 8:30 PM estoy en vivo en TikTok: por qué el dinero no se queda y cómo reprogramarlo mientras duermes. Búscame en TikTok como mabradiante\n" + FIRMA],
 ["Martes 17 · 8:00 PM", "Recordatorio chakras (solo comunidad)", "Mañana miércoles 18 a las 10 AM (hora CDMX): ACTIVACIÓN GRATIS EN VIVO solo para ustedes, mi comunidad · Corte de fugas energéticas y activación de tus 7 chakras. Link: [LINK ZOOM MIÉRCOLES]\n" + FIRMA],
 ["Viernes 20 · 7:00 PM", "Acercamiento 2 · último aviso", "Mis neurohackers 💛 Mañana sábado es el último día de Programa la Riqueza mientras Duermes con su regalo: la hipnosis COMPLETA en vivo conmigo el domingo 22 a las 11 AM, solo para quienes lo tomen. Link: [LINK DE LA PÁGINA]\nY mañana a las 8:30 PM estoy en vivo en TikTok.\n" + FIRMA],
]
wb = Workbook()
def hoja(ws, enc, filas, anchos):
    ws.append(enc)
    for c in ws[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="3B2A6B")
    for f in filas: ws.append(f)
    for i, w in enumerate(anchos): ws.column_dimensions[chr(65 + i)].width = w
    for r in ws.iter_rows(min_row=2):
        for c in r: c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "A2"
ws = wb.active; ws.title = "1 · HOY lunes 16"; hoja(ws, ["#", "Cuándo", "Qué haces", "Dónde / cómo", "Tiempo"], HOY, [5, 22, 50, 60, 10])
ws2 = wb.create_sheet("2 · Calendario 16–22")
hoja(ws2, ["Fecha", "Día", "Hora", "Quién", "Tipo", "TÍTULO", "Primera frase", "Guion / puntos", "Texto en pantalla", "Copy (sin @)", "Hashtags", "CTA"], F, [11, 12, 9, 26, 24, 34, 36, 70, 40, 46, 30, 16])
FILL = {"Yapping": "DCF0E8", "NAIA": "E3E8F7", "LIVE": "FDE2E4", "Aviso": "FFF3C4"}
for r in ws2.iter_rows(min_row=2):
    t = r[4].value or ""
    col = next((v for k, v in FILL.items() if k in t), "F3E6C6")
    for c in r[:6]: c.fill = PatternFill("solid", fgColor=col)
hoja(wb.create_sheet("3 · Comunidad"), ["Cuándo", "Tipo", "Mensaje (copia y pega en tus grupos)"], COM, [22, 30, 100])
hoja(wb.create_sheet("4 · Tus números"), ["Dato", "Valor"], NUM, [30, 110])
salida = os.path.join(AQUI, "semana-2026-11-16.xlsx"); wb.save(salida); print(salida, len(F), "piezas")
