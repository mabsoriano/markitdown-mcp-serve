"""Semana 12–18 nov 2026 · 2 piezas diarias con Mabel (1 yapping + 1 con CTA) + 1 NAIA.
Genera semana-2026-11-12.xlsx. Uso: python3 semana.py"""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
AQUI = os.path.dirname(os.path.abspath(__file__))
FIRMA = "Lo que no se activa, no cambia. @mabradiante · BNQ Method™"
REG = "Regístrate gratis: el link está en mi perfil."
PAGINA = "https://hotmart.com/es/marketplace/productos/activacionadnmillonario/U104269730G"
H_LIVE = "#hipnosis #hackeatumente #bloqueosconeldinero #abundancia #livegratis #mabradiante #BNQMethod"
H_Y = "#mabradiante #BNQMethod #tdah #emprendedora #mamaemprendedora #fyp"
H_NAIA = "#NAIA #activacion #hackeatumente #abundancia #mabradiante #BNQMethod"

def g(*partes):
    t, out = 0.0, []
    for et, tx in partes:
        d = max(4, round(len(tx.split()) / 2.6)); a, b = int(t), int(t + d)
        out.append(f"{a//60}:{a%60:02d}–{b//60}:{b%60:02d} {et + ': ' if et else ''}{tx}"); t += d
    return "\n".join(out)

def live_cta(cuando):  # cuando: "Hoy a las 6:30 de la tarde", "El domingo 15 a las 11 de la mañana"...
    return f"{cuando}, hora CDMX, te guío gratis por Zoom en una hipnosis para hackear tus bloqueos con el dinero. {REG}"

def naia(tema, hackeos, orden, frase):
    return ("Soy NAIA. Hoy activamos tu " + tema + ".\nPon tu mano en el pecho. Repite conmigo.\n"
            + "\n".join(hackeos) + f"\nHoy instalo una nueva orden: {orden}\n{frase} {frase} {frase}\n"
            "Lo que no se activa, no cambia y se transforma. Yo soy NAIA. Y esto es @mabradiante.")

# Cada fila: fecha, día, hora, quién, tipo, título, primera frase, guion/puntos, texto en pantalla, copy, hashtags, CTA
F = []
def add(fecha, dia, hora, quien, tipo, titulo, hook, guion, pantalla, copy, hashtags, cta):
    F.append([fecha, dia, hora, quien, tipo, titulo, hook, guion, pantalla, copy, hashtags, cta])

# ─────────── JUEVES 12 · LIVE 6:30 PM (urgente) ───────────
add("2026-11-12", "Jueves 12", "1:00 PM", "Mabel a cámara (30–45 s)", "Aviso del LIVE de hoy",
    "HOY 6:30 PM: HIPNOSIS EN VIVO (GRATIS)", "Si el martes no alcanzaste a entrar, hoy repito la hipnosis en vivo.",
    g(("GANCHO", "Si el martes no alcanzaste a entrar, hoy repito la hipnosis en vivo."),
      ("QUÉ ES", "Es una hipnosis guiada para ver qué bloqueo está frenando el dinero, y darle a tu mente una nueva instrucción. Estás despierta y decides todo el tiempo."),
      ("PREPÁRATE", "Audífonos, un lugar cómodo y nunca manejando."),
      ("CTA", live_cta("Hoy a las 6:30 de la tarde"))),
    "0–3 s: HOY 6:30 PM · HIPNOSIS EN VIVO · GRATIS. Final: «REGÍSTRATE · LINK EN MI PERFIL · BNQ Method™».",
    f"¿No alcanzaste a entrar el martes? 🌀 Hoy, 6:30 PM (hora CDMX), repito la hipnosis para hackear tus bloqueos con el dinero. Gratis, por Zoom.\n{REG}\n{FIRMA}", H_LIVE, "LIVE hoy 6:30 PM")
add("2026-11-12", "Jueves 12", "8:30 PM", "Mabel a cámara (1–2 min)", "Yapping (conexión, sin venta)",
    "LO QUE PASÓ HOY EN LA HIPNOSIS", "Acabo de terminar el LIVE y te cuento cómo me sentí.",
    "Puntos guía (platicando, sin guion):\n1. [Cuántas llegaron y qué sentiste al verlas]\n2. [Una palabra que escribieron en el chat (sin nombres)]\n3. [Qué te pasa a ti cuando guías una hipnosis]\nCierre: «Si estuviste, ¿qué sentiste? Y si no, el domingo 15 la repito.»",
    "0–3 s: LO QUE PASÓ HOY EN LA HIPNOSIS", f"Así me sentí hoy 💛 Gracias a cada una que llegó.\nSi estuviste, cuéntame qué sentiste 👇\n{FIRMA}", H_Y, "Sin CTA")
add("2026-11-12", "Jueves 12", "9:30 PM", "NAIA (automático, Mabel no graba)", "NAIA · Audio robótico",
    "NAIA · ACTIVACIÓN DE MERECIMIENTO", "Soy NAIA. Hoy activamos tu merecimiento.",
    naia("merecimiento", ["Hoy hackeo mi «no merezco».", "Hackeo las memorias de esfuerzo sin recompensa.", "Hackeo los pactos de lealtad con la carencia de mi linaje.", "Hackeo mi memoria celular y mi subconsciente."], "merezco recibir.", "Merezco recibir."),
    "Clip fijo de NAIA + subtítulos grandes. Frase clave en pantalla: «MEREZCO RECIBIR». Fijo: «NAIA · @mabradiante · BNQ Method™».",
    f"¿Te cuesta recibir aunque des todo? 🔓 Pon tu mano en el pecho y repite con NAIA. Guárdalo y escúchalo cuando lo necesites.\n{FIRMA}", H_NAIA, "Guardar")

# ─────────── VIERNES 13 ───────────
add("2026-11-13", "Viernes 13", "1:00 PM", "Mabel a cámara (1–2 min)", "Yapping (conexión, sin venta)",
    "UN DÍA NORMAL DE UNA NEUROHACKER CON TDAH", "Te voy a enseñar cómo es de verdad un día mío, sin filtro.",
    "Puntos guía:\n1. [A qué hora empiezas y qué haces primero]\n2. [Tu activación de la mañana: 1 minuto]\n3. [Lo que más te cuesta del día]\n4. [Cómo te organizas con 4 horas]\nCierre: «¿Y tú cómo arrancas tu día?»",
    "0–3 s: UN DÍA NORMAL DE UNA NEUROHACKER CON TDAH", f"Un día mío, sin filtro 🧠☕\n¿Y tú cómo arrancas el tuyo? Cuéntame 👇\n{FIRMA}", H_Y, "Sin CTA")
add("2026-11-13", "Viernes 13", "6:00 PM", "Mabel a cámara (1:30 min)", "Rompe una creencia + lista de 3",
    "NO ES QUE TRABAJES POCO: TU CUERPO FRENA EL DINERO", "No es que trabajes poco. Es que tu cuerpo vive el dinero como un peligro, y lo frena antes de que llegue.",
    g(("GANCHO", "No es que trabajes poco. Es que tu cuerpo vive el dinero como un peligro, y lo frena antes de que llegue."),
      ("GUARDAR", "Guárdalo y compártelo con la amiga que dice «trabajo y trabajo, y el dinero no se mueve»."),
      ("LISTA DE 3", "Tres señales: uno, te da pena cobrar. Dos, evitas ver tu cuenta. Tres, dejas pasar oportunidades."),
      ("DATO", "Kahneman y Tversky mostraron que perder nos duele más o menos el doble de lo que nos alegra ganar."),
      ("", "[TU HISTORIA: cuándo notaste que tu cuerpo se tensaba con el dinero]"),
      ("HACKEO", "Mano en el pecho, exhala y repite 3 veces: el dinero es seguro conmigo, me permito recibirlo."),
      ("CTA", live_cta("El domingo 15 a las 11 de la mañana")) ),
    "0–3 s: NO ES QUE TRABAJES POCO. Lista: 1 PENA DE COBRAR · 2 NO VES TU CUENTA · 3 DEJAS PASAR OPORTUNIDADES. Final: «LIVE GRATIS · DOMINGO 15 · 11 AM · BNQ Method™».",
    f"No es que trabajes poco 💸 Tu cuerpo frena el dinero antes de que llegue.\nDomingo 15, 11 AM (CDMX): hipnosis gratis para hackear ese bloqueo. {REG}\n{FIRMA}", H_LIVE, "LIVE dom 15")
add("2026-11-13", "Viernes 13", "9:30 PM", "NAIA (automático)", "NAIA · Audio robótico",
    "NAIA · ACTIVACIÓN DE RECIBIR", "Soy NAIA. Hoy activamos tu capacidad de recibir.",
    naia("capacidad de recibir", ["Hoy hackeo mi culpa de recibir.", "Hackeo las memorias de «el dinero cuesta mucho trabajo».", "Hackeo los pactos de lealtad que me mantenían en carencia.", "Hackeo mi memoria celular y mi subconsciente."], "recibo con calma y lo sostengo.", "Recibo con calma."),
    "Clip fijo de NAIA + subtítulos. Frase clave: «RECIBO CON CALMA». Fijo: «NAIA · @mabradiante · BNQ Method™».",
    f"Si recibir te da culpa, esto es para ti 🔓 Repite con NAIA.\nGuárdalo para antes de cobrar.\n{FIRMA}", H_NAIA, "Guardar")

# ─────────── SÁBADO 14 ───────────
add("2026-11-14", "Sábado 14", "1:00 PM", "Mabel a cámara (1–2 min)", "Yapping (conexión, sin venta)",
    "RESPONDO LO QUE MÁS ME PREGUNTAN", "Esta es la pregunta que más me hacen, y hoy te la contesto.",
    "Puntos guía:\n1. [Lee una pregunta real de tus comentarios o DMs]\n2. [Tu respuesta en 3 frases]\n3. [Qué te gustaría que te pregunten]\nCierre: «Déjame tu pregunta y la contesto en otro video.»",
    "0–3 s: RESPONDO LO QUE MÁS ME PREGUNTAN", f"Respondo tu pregunta 💬\nDéjame la tuya aquí abajo 👇\n{FIRMA}", H_Y, "Sin CTA")
add("2026-11-14", "Sábado 14", "6:00 PM", "Mabel a cámara (1:30 min)", "Decreto para hacer ya",
    "DI ESTO SI TE DA PENA COBRAR", "Si te tiembla la voz cuando dices tu precio, repite esto conmigo.",
    g(("GANCHO", "Si te tiembla la voz cuando dices tu precio, repite esto conmigo."),
      ("GUARDAR", "Guárdalo para tu próxima venta."),
      ("LISTA DE 3", "Tres señales: bajas el precio antes de que te lo pidan, regalas tu trabajo, te disculpas al cobrar."),
      ("DATO", "Ethan Kross, de la Universidad de Michigan, encontró que hablarte por tu nombre te ayuda a manejar mejor tus emociones."),
      ("", "[TU HISTORIA: la vez que te bajaste el precio]"),
      ("HACKEO", "Di tu nombre y repite 3 veces: [tu nombre], tu trabajo vale y lo sostienes con calma."),
      ("CTA", live_cta("Mañana domingo a las 11 de la mañana")) ),
    "0–3 s: DI ESTO SI TE DA PENA COBRAR. Final: «MAÑANA · 11 AM · LIVE GRATIS · BNQ Method™».",
    f"¿Te da pena cobrar? 💬 Haz este decreto conmigo 3 veces.\nMañana domingo, 11 AM (CDMX): hipnosis gratis para hackear tus bloqueos con el dinero. {REG}\n{FIRMA}", H_LIVE, "LIVE dom 15")
add("2026-11-14", "Sábado 14", "9:30 PM", "NAIA (automático)", "NAIA · Audio robótico",
    "NAIA · ACTIVACIÓN DE VALOR", "Soy NAIA. Hoy activamos tu valor.",
    naia("valor", ["Hoy hackeo mi miedo a cobrar.", "Hackeo las memorias que me dijeron que no era suficiente.", "Hackeo los pactos de lealtad que me mantenían pequeña.", "Hackeo mi memoria celular y mi subconsciente."], "cobro lo que vale mi trabajo.", "Cobro lo que vale mi trabajo."),
    "Clip fijo de NAIA + subtítulos. Frase clave: «COBRO LO QUE VALE MI TRABAJO».",
    f"Tu trabajo vale ✨ Repite con NAIA y guárdalo para antes de cobrar.\n{FIRMA}", H_NAIA, "Guardar")

# ─────────── DOMINGO 15 · LIVE 11 AM ───────────
add("2026-11-15", "Domingo 15", "8:00 AM", "Mabel a cámara (30 s)", "Aviso del LIVE de hoy",
    "HOY 11 AM: HIPNOSIS EN VIVO", "Hoy a las 11 de la mañana te guío en una hipnosis en vivo, y es gratis.",
    g(("GANCHO", "Hoy a las 11 de la mañana te guío en una hipnosis en vivo, y es gratis."),
      ("PREPÁRATE", "Audífonos, lugar cómodo, nunca manejando. Y una intención: ¿qué quieres soltar con el dinero?"),
      ("CTA", "Si no te registraste, todavía estás a tiempo: el link está en mi perfil.")),
    "0–3 s: HOY 11 AM · HIPNOSIS EN VIVO · GRATIS. Final: «REGÍSTRATE · LINK EN MI PERFIL · BNQ Method™».",
    f"Hoy, 11 AM (hora CDMX) 🌀 Hipnosis en vivo y gratis para hackear tus bloqueos con el dinero.\n{REG}\n{FIRMA}", H_LIVE, "LIVE hoy 11 AM")
add("2026-11-15", "Domingo 15", "7:00 PM", "Mabel a cámara (1–2 min)", "Yapping (conexión, sin venta)",
    "LO QUE ME ENSEÑÓ EL LIVE DE HOY", "Hoy en el LIVE alguien escribió algo que no me puedo sacar de la cabeza.",
    "Puntos guía:\n1. [Una frase o reacción del chat (sin nombre, con permiso)]\n2. [Por qué te movió]\n3. [Qué te recuerda de tu propia historia]\nCierre: «El martes repito: 11 AM y 7 PM.»",
    "0–3 s: LO QUE ME ENSEÑÓ EL LIVE DE HOY", f"Lo que me llevo de hoy 💛\nEl martes 17 repito la hipnosis: 11 AM y 7 PM (CDMX).\n{FIRMA}", H_Y, "Sin CTA")
add("2026-11-15", "Domingo 15", "9:30 PM", "NAIA (automático)", "NAIA · Audio robótico",
    "NAIA · ACTIVACIÓN PARA EMPEZAR LA SEMANA", "Soy NAIA. Hoy activamos tu nueva semana.",
    naia("nueva semana", ["Hoy hackeo la angustia del lunes.", "Hackeo las memorias de semanas en modo supervivencia.", "Hackeo los pactos de lealtad con el cansancio.", "Hackeo mi memoria celular y mi subconsciente."], "empiezo esta semana en abundancia.", "Empiezo en abundancia."),
    "Clip fijo de NAIA + subtítulos. Frase clave: «EMPIEZO EN ABUNDANCIA».",
    f"Antes de dormir, activa tu semana 🌙 Repite con NAIA.\n{FIRMA}", H_NAIA, "Guardar")

# ─────────── LUNES 16 ───────────
add("2026-11-16", "Lunes 16", "1:00 PM", "Mabel a cámara (1–2 min)", "Yapping (conexión, sin venta)",
    "MI ACTIVACIÓN DE LUNES (1 MINUTO)", "Esto es lo primero que hago los lunes, y me toma un minuto.",
    "Puntos guía:\n1. [Dónde estás: coche, cocina, caminando]\n2. [Haces tu activación de 1 minuto frente a cámara]\n3. [Cómo te cambia el día]\nCierre: «¿Tú qué haces los lunes para no arrancar en automático?»",
    "0–3 s: MI ACTIVACIÓN DE LUNES (1 MINUTO)", f"Mi minuto de lunes ☀️ Hazlo conmigo.\n¿Tú qué haces para no arrancar en automático? 👇\n{FIRMA}", H_Y, "Sin CTA")
add("2026-11-16", "Lunes 16", "6:00 PM", "Mabel a cámara (1:30 min)", "Rompe una creencia + lista de 3",
    "¿POR QUÉ TRABAJAS TANTO Y EL DINERO NO SE MUEVE?", "¿Por qué trabajas tanto y el dinero no se mueve?",
    g(("GANCHO", "¿Por qué trabajas tanto y el dinero no se mueve?"),
      ("GUARDAR", "Guárdalo y mándaselo a quien trabaja el doble y sigue igual."),
      ("LISTA DE 3", "Uno: te da culpa cobrar y regalas tu trabajo. Dos: no miras tu cuenta para no sentir miedo. Tres: repites lo que oíste en casa."),
      ("DATO", "Karlsson, Loewenstein y Seppi lo llamaron «efecto avestruz»: evitamos mirar el dinero cuando esperamos malas noticias."),
      ("", "[TU HISTORIA: cuál de las 3 te pasaba]"),
      ("HACKEO", "Repite 3 veces: merezco recibir por lo que doy."),
      ("CTA", live_cta("Mañana martes a las 11 de la mañana y a las 7 de la noche")) ),
    "0–3 s: ¿POR QUÉ TRABAJAS TANTO Y EL DINERO NO SE MUEVE? Final: «MAÑANA · 11 AM y 7 PM · LIVE GRATIS · BNQ Method™».",
    f"¿Trabajas tanto y el dinero no se mueve? 🫠 Son 3 programas que lo frenan.\nMañana martes, 11 AM y 7 PM (CDMX): hipnosis gratis para hackearlos. {REG}\n{FIRMA}", H_LIVE, "LIVE mar 17")
add("2026-11-16", "Lunes 16", "9:30 PM", "NAIA (automático)", "NAIA · Audio robótico",
    "NAIA · ACTIVACIÓN DE ABUNDANCIA", "Soy NAIA. Hoy activamos tu abundancia.",
    naia("abundancia", ["Hoy hackeo mi escasez.", "Hackeo mis memorias de carencia.", "Hackeo mis pactos de lealtad con la pobreza de mi linaje.", "Hackeo mi memoria celular y mi subconsciente."], "soy segura para recibir.", "Soy segura para recibir."),
    "Clip fijo de NAIA + subtítulos. Frase clave: «SOY SEGURA PARA RECIBIR». (Si ya publicaste el video de Abundancia, reutilízalo.)",
    f"¿Sientes que el dinero se frena antes de llegar? 🔓 Repite con NAIA.\n{FIRMA}", H_NAIA, "Guardar")

# ─────────── MARTES 17 · LIVES 11 AM y 7 PM ───────────
add("2026-11-17", "Martes 17", "8:00 AM", "Mabel a cámara (30 s)", "Aviso del LIVE de hoy",
    "HOY 11 AM Y 7 PM: HIPNOSIS EN VIVO", "Hoy te hipnotizo en vivo dos veces: a las 11 de la mañana y a las 7 de la noche.",
    g(("GANCHO", "Hoy te hipnotizo en vivo dos veces: a las 11 de la mañana y a las 7 de la noche."),
      ("PREPÁRATE", "Elige tu horario. Audífonos, lugar cómodo, nunca manejando."),
      ("CTA", "Regístrate gratis: el link está en mi perfil.")),
    "0–3 s: HOY · 11 AM y 7 PM · HIPNOSIS EN VIVO. Final: «REGÍSTRATE · LINK EN MI PERFIL · BNQ Method™».",
    f"Hoy, 11 AM y 7 PM (hora CDMX) 🌀 Hipnosis en vivo y gratis para hackear tus bloqueos con el dinero.\n{REG}\n{FIRMA}", H_LIVE, "LIVE hoy 11 y 7")
add("2026-11-17", "Martes 17", "9:00 PM", "Mabel a cámara (1–2 min)", "Yapping (conexión, sin venta)",
    "DOS LIVES EN UN DÍA: ASÍ TERMINÉ", "Hoy hice dos LIVES y te cuento cómo terminé.",
    "Puntos guía:\n1. [Cómo te sentiste en cada uno]\n2. [Lo más bonito que pasó]\n3. [Qué aprendiste de ti]\nCierre: «Gracias por estar. ¿Qué te llevas tú?»",
    "0–3 s: DOS LIVES EN UN DÍA", f"Dos LIVES en un día 💛 Gracias.\n¿Qué te llevas tú? 👇\n{FIRMA}", H_Y, "Sin CTA")
add("2026-11-17", "Martes 17", "10:00 PM", "NAIA (automático)", "NAIA · Audio robótico",
    "NAIA · ACTIVACIÓN DEL ÉXITO", "Soy NAIA. Hoy activamos tu éxito.",
    naia("éxito", ["Hoy hackeo mi miedo al éxito.", "Hackeo las memorias que me dijeron que no era suficiente.", "Hackeo los pactos de lealtad que me mantenían pequeña.", "Hackeo mi memoria celular y mi subconsciente."], "el éxito es seguro para mí.", "El éxito es seguro para mí."),
    "Clip fijo de NAIA + subtítulos. Frase clave: «EL ÉXITO ES SEGURO PARA MÍ». (Puedes reutilizar el video de Éxito.)",
    f"¿Y si no te da miedo fracasar… sino brillar? ✨ Repite con NAIA.\n{FIRMA}", H_NAIA, "Guardar")

# ─────────── MIÉRCOLES 18 · LIVE COMUNIDAD 10 AM (no se pauta) ───────────
add("2026-11-18", "Miércoles 18", "1:00 PM", "Mabel a cámara (1–2 min)", "Yapping (conexión, sin venta)",
    "HOY ACTIVAMOS LOS 7 CHAKRAS CON MI COMUNIDAD", "Hoy en la mañana hice algo distinto con mi comunidad, y te lo cuento.",
    "Puntos guía:\n1. [Qué hicieron en la activación en vivo de las 10 AM]\n2. [Qué sentiste tú]\n3. [Por qué la hiciste solo para tu comunidad]\nCierre: «Si quieres estar en la próxima, únete a mi comunidad Neurohackers: link en mi perfil.»",
    "0–3 s: HOY ACTIVAMOS LOS 7 CHAKRAS", f"Hoy activamos los 7 chakras con mi comunidad 🌈\n¿Quieres estar en la próxima? Únete a Neurohackers: link en mi perfil.\n{FIRMA}", H_Y, "Comunidad")
add("2026-11-18", "Miércoles 18", "6:00 PM", "Mabel a cámara (1:30 min)", "Rompe una creencia + lista de 3",
    "NO ESTÁS CANSADA: TIENES FUGAS DE ENERGÍA", "No estás cansada. Estás dejando tu energía en lugares que no te la regresan.",
    g(("GANCHO", "No estás cansada. Estás dejando tu energía en lugares que no te la regresan."),
      ("GUARDAR", "Guárdalo y compártelo con quien está cansada de estar cansada."),
      ("LISTA DE 3", "Tres fugas: uno, pensar todo el día en lo que no puedes controlar. Dos, decir que sí cuando quieres decir que no. Tres, cargar problemas que no son tuyos."),
      ("DATO", "En 2019 la OMS incluyó el «burnout» como un fenómeno ligado al estrés crónico del trabajo."),
      ("", "[TU HISTORIA: tu fuga de energía más grande]"),
      ("HACKEO", "Mano en el pecho y repite 3 veces: mi energía regresa a mí."),
      ("CTA", "Guárdalo y únete a mi comunidad Neurohackers: el link está en mi perfil.")),
    "0–3 s: NO ESTÁS CANSADA: TIENES FUGAS DE ENERGÍA. Lista: 1 LO QUE NO CONTROLAS · 2 SÍ CUANDO ES NO · 3 PROBLEMAS AJENOS. Aviso: práctica de bienestar, no es diagnóstico. «BNQ Method™».",
    f"No es cansancio: son fugas de energía ⚡ Haz el hackeo conmigo.\nÚnete a mi comunidad Neurohackers: link en mi perfil.\n{FIRMA}", "#energia #burnout #hackeatumente #chakras #mabradiante #BNQMethod", "Comunidad")
add("2026-11-18", "Miércoles 18", "9:30 PM", "NAIA (automático)", "NAIA · Audio robótico",
    "NAIA · ACTIVACIÓN DE TU ENERGÍA", "Soy NAIA. Hoy activamos tu energía.",
    naia("energía", ["Hoy hackeo mis fugas de energía.", "Hackeo las memorias de cargar lo que no es mío.", "Hackeo los pactos de lealtad con el cansancio.", "Hackeo mi memoria celular y mi subconsciente."], "mi energía regresa a mí.", "Mi energía regresa a mí."),
    "Clip fijo de NAIA + subtítulos. Frase clave: «MI ENERGÍA REGRESA A MÍ».",
    f"Recupera tu energía 🌈 Repite con NAIA y guárdalo para cuando te sientas drenada.\n{FIRMA}", H_NAIA, "Guardar")

# ─────────── 13-nov · Mabel pidió volver a sus 2 formatos ganadores ───────────
# FAMOSO (Sara Blakely, Steve Jobs, Beyoncé) y su estructura «PODEROSA CONEXIÓN» (le funcionó cañón en TikTok):
# verdad incómoda → patrón → like + comenta → 1 Detecta → 2 Rompe el patrón invisible → 3 Reprograma con acción
# → 4 Repetición 7 días → regla de oro → cuidado con la trampa → promesa → quién soy → CTA.
H_FAMA = "#mabradiante #BNQMethod #hackeatumente #mentalidad #mty"
def pc(patron, verdad, detecta, rompe, reprograma, palabra, cta):
    return g(("VERDAD INCÓMODA", verdad),
             ("PATRÓN", f"Si te repites «{patron}», esto es para ti. Permíteme llevarte al siguiente nivel con un bioneurohack + acción para que lo hackees de raíz en tiempo real. No es motivación, no es bla bla: es una activación."),
             ("ANTES", f"Dale like y escribe {palabra} en comentarios."),
             ("1 · DETECTA", detecta),
             ("2 · ROMPE EL PATRÓN INVISIBLE", rompe),
             ("3 · REPROGRAMA CON ACCIÓN", reprograma),
             ("4 · REPETICIÓN", "Haz esto 7 días: cada noche escribe qué acción incómoda hiciste hoy que sí genera resultados. Sé honesta: qué, cómo y para qué."),
             ("REGLA DE ORO", "Si no te incomoda, no te está cambiando."),
             ("CUIDADO CON LA TRAMPA", "No pienses de más, no te paralices. Crea, ejecuta, claridad, repetición. Vuelve el ciclo."),
             ("PROMESA", f"Si haces esto 7 días, tu pregunta va a dejar de ser «{patron}» y va a empezar a ser «¿cómo escalo esto?»."),
             ("QUIÉN SOY", "[Quién soy en 1 frase: Mabel, neurohacker, creadora del BNQ Method™]"),
             ("CTA", cta))
NUEVAS = {
 ("2026-11-13", "6:00 PM"): ["2026-11-13", "Viernes 13", "6:00 PM", "Mabel a cámara (2 min)", "FAMOSO + autoridad",
    "12 EDITORIALES LE DIJERON QUE NO A J.K. ROWLING",
    "Doce editoriales le dijeron que no a Harry Potter. Y tú dejaste de intentarlo con el primer no.",
    g(("GANCHO", "Doce editoriales le dijeron que no a Harry Potter. Y tú dejaste de intentarlo con el primer no."),
      ("GUARDAR Y COMPARTIR", "Guárdalo y compártelo con alguien que dejó un sueño por un «no»."),
      ("DOLOR", "Ofreces lo que haces, alguien te dice que no, y tu mente lo traduce como «no sirvo» o «el dinero no es para mí»."),
      ("LISTA DE 3", "3 creencias que J.K. Rowling no se permitió: 1. Un «no» es un veredicto. 2. Si no me compran, no valgo. 3. Hay que esperar a que alguien te elija."),
      ("DATO / AUTORIDAD", "Ella ha contado que el manuscrito fue rechazado por una docena de editoriales antes de que una pequeña dijera que sí. Harry Potter es hoy una de las sagas más vendidas de la historia. Tu subconsciente también guardó qué significa un «no»."),
      ("TU HISTORIA", "[15–20 s: un «no» que te frenó y qué hiciste después]"),
      ("HACKEO (hazlo conmigo)", "Escribe el último «no» que recibiste y a un lado: «¿qué aprendí?». Repite conmigo: un no es información, no es mi valor. Un no es información, no es mi valor. Un no es información, no es mi valor."),
      ("REVELACIÓN", "El dinero no se frena por los «no» que recibes. Se frena por los intentos que dejas de hacer."),
      ("CTA", "El domingo 15 a las 11 de la mañana, hora CDMX, te guío gratis en una hipnosis para hackear tus bloqueos con el dinero. Regístrate: el link está en mi perfil.")),
    "0–3 s: 12 EDITORIALES LE DIJERON QUE NO A J.K. ROWLING. Lista: 1 UN NO NO ES VEREDICTO · 2 TU VALOR NO DEPENDE DE UNA VENTA · 3 NO ESPERES QUE TE ELIJAN. Final: «LIVE GRATIS · DOMINGO 15 · 11 AM · BNQ Method™».",
    f"12 editoriales le dijeron que no a J.K. Rowling 📚 y las 3 creencias que ella no se permitió.\nDomingo 15, 11 AM (CDMX): hipnosis gratis para hackear tus bloqueos con el dinero. {REG}\n{FIRMA}", H_FAMA, "LIVE dom 15"],
 ("2026-11-14", "6:00 PM"): ["2026-11-14", "Sábado 14", "6:00 PM", "Mabel a cámara (2–3 min)", "PODEROSA CONEXIÓN (tu formato ganador)",
    "«ME ESFUERZO Y NO ME VA BIEN»: ROMPE ESTE PATRÓN",
    "Mucha gente cree que está creciendo porque escucha podcasts, lee libros y guarda frases. Pero sigue actuando igual.",
    pc("me esfuerzo y no me va bien",
       "Mucha gente cree que está creciendo porque escucha podcasts, lee libros y guarda frases. Pero sigue actuando igual. Eso no es crecimiento: es entretenimiento disfrazado. El crecimiento real se ve así: te das cuenta de un patrón, lo cuestionas aunque duela, cambias tu comportamiento y lo sostienes en el tiempo.",
       "Sé metaconsciente, sin autoengaño: ¿estoy ocupada o avanzo de verdad? ¿Hago cosas que se ven productivas pero no generan resultados? ¿O estoy evitando lo incómodo? Si te dolió alguna, ahí está el punto.",
       "El problema casi siempre es uno de estos 3: perfeccionismo (hasta que esté perfecto, avanzo), dispersión (haces mil cosas y ninguna escala) y evasión (evitas lo que sí mueve la aguja).",
       "Aquí se separa la gente que de verdad quiere hackearse de la que hace scroll. Hoy elige UNA acción incómoda que sí mueva la aguja (cobrar, ofrecer, publicar, pedir) y hazla antes de dormir.",
       "HACKEO",
       "Y si quieres hackearlo de raíz, el domingo 15 a las 11 de la mañana, hora CDMX, te guío gratis en una hipnosis para hackear tus bloqueos con el dinero. El link está en mi perfil."),
    "0–3 s: «ME ESFUERZO Y NO ME VA BIEN». Pasos en pantalla: 1 DETECTA · 2 ROMPE EL PATRÓN · 3 REPROGRAMA CON ACCIÓN · 4 REPETICIÓN. «Si no te incomoda, no te está cambiando». «BNQ Method™».",
    f"«Me esfuerzo y no me va bien» 🔓 No es motivación: es un bioneurohack + acción para romper el patrón de raíz.\nComenta HACKEO 👇 y el domingo 15, 11 AM (CDMX), hipnosis gratis para hackear tus bloqueos con el dinero. Link en mi perfil.\n{FIRMA}", H_FAMA, "LIVE dom 15"],
 ("2026-11-16", "6:00 PM"): ["2026-11-16", "Lunes 16", "6:00 PM", "Mabel a cámara (2–3 min)", "PODEROSA CONEXIÓN (tu formato ganador)",
    "«ESTOY OCUPADA TODO EL DÍA Y NO AVANZO»",
    "Estar ocupada no es lo mismo que avanzar. Y tu mente lo sabe, aunque no te lo diga.",
    pc("estoy ocupada todo el día y no avanzo",
       "Estar ocupada no es lo mismo que avanzar. Llenas el día de pendientes para sentir que haces algo, pero lo que de verdad te daría dinero sigue en la lista de «luego».",
       "Pregúntate con honestidad: de todo lo que hice hoy, ¿qué me acercó a cobrar? Si la respuesta es «nada», no es falta de tiempo: es un patrón.",
       "Revisa cuál es el tuyo: perfeccionismo (lo preparo de más), dispersión (empiezo diez cosas) o evasión (hago lo fácil para no hacer lo que da miedo).",
       "Mañana, antes de abrir tus redes, haz durante 20 minutos la UNA tarea que más te acerca a cobrar. Solo una.",
       "AVANZO",
       "Y mañana martes, a las 11 de la mañana y a las 7 de la noche, hora CDMX, te guío gratis en una hipnosis para hackear tus bloqueos con el dinero. El link está en mi perfil."),
    "0–3 s: «ESTOY OCUPADA TODO EL DÍA Y NO AVANZO». Pasos: 1 DETECTA · 2 ROMPE EL PATRÓN · 3 REPROGRAMA CON ACCIÓN · 4 REPETICIÓN. Final: «MAÑANA · 11 AM y 7 PM · LIVE GRATIS · BNQ Method™».",
    f"Estar ocupada no es avanzar ⏳ Rompe el patrón con este bioneurohack + acción.\nComenta AVANZO 👇 y mañana martes, 11 AM y 7 PM (CDMX): hipnosis gratis para hackear tus bloqueos con el dinero. Link en mi perfil.\n{FIRMA}", H_FAMA, "LIVE mar 17"],
 ("2026-11-18", "6:00 PM"): ["2026-11-18", "Miércoles 18", "6:00 PM", "Mabel a cámara (2 min)", "FAMOSO + autoridad",
    "ARIANNA HUFFINGTON SE DESMAYÓ DE CANSANCIO",
    "En 2007, Arianna Huffington, fundadora del HuffPost, se desmayó de agotamiento en su oficina. Y eso explica por qué tú vives cansada.",
    g(("GANCHO", "En 2007, Arianna Huffington, fundadora del HuffPost, se desmayó de agotamiento en su oficina. Y eso explica por qué tú vives cansada."),
      ("GUARDAR Y COMPARTIR", "Guárdalo y compártelo con quien está cansada de estar cansada."),
      ("DOLOR", "Duermes y despiertas igual. Haces todo por todos y a ti no te queda energía para lo que de verdad quieres."),
      ("LISTA DE 3", "3 fugas de energía que ella reconoció y tú quizá tienes: 1. Creer que descansar es de flojas. 2. Decir que sí cuando quieres decir que no. 3. Cargar lo que no puedes controlar."),
      ("DATO / AUTORIDAD", "Ella misma contó que se golpeó la cara al caer y que eso la llevó a cambiar su forma de vivir; después escribió el libro «Thrive». Lo espiritual lo llama fuga de energía; la ciencia, agotamiento."),
      ("TU HISTORIA", "[15–20 s: el momento en que tu cuerpo te dijo «ya basta»]"),
      ("HACKEO (hazlo conmigo)", "Divide una hoja en dos: «en mi control» y «fuera de mi control». Suelta hoy una cosa de la segunda columna. Repite conmigo: mi energía regresa a mí. Mi energía regresa a mí. Mi energía regresa a mí."),
      ("REVELACIÓN", "No te falta fuerza. Te sobran fugas."),
      ("CIERRE", "Guárdalo y únete a mi comunidad Neurohackers: el link está en mi perfil.")),
    "0–3 s: ARIANNA HUFFINGTON SE DESMAYÓ DE CANSANCIO. Lista: 1 DESCANSAR NO ES DE FLOJAS · 2 SÍ CUANDO ES NO · 3 LO QUE NO CONTROLAS. Aviso: práctica de bienestar, no es diagnóstico. «BNQ Method™».",
    f"Arianna Huffington se desmayó de cansancio en 2007 ⚡ y las 3 fugas de energía que tú quizá tienes.\nÚnete a mi comunidad Neurohackers: link en mi perfil.\n{FIRMA}", "#energia #burnout #hackeatumente #mabradiante #BNQMethod", "Comunidad"],
}
F = [NUEVAS.get((r[0], r[2]), r) for r in F]
# 13-nov · Mabel: todas las piezas con CTA llevan el CTA del PRODUCTO de la semana (no solo el LIVE).
import re as _re
PROD = "Hipnosis para hackear tus bloqueos con el dinero"
CTA_PROD = f"Si quieres hackearlo de raíz, la {PROD} está en el link de mi perfil."
def _prod(r):
    if r[11] not in ("LIVE dom 15", "LIVE mar 17") or r[4] == "Aviso del LIVE de hoy":
        return r
    r = list(r)
    r[7] = _re.sub(r"(CTA: ).*", lambda m: m.group(1) + CTA_PROD, r[7])
    r[8] = _re.sub(r"Final: «[^»]*»", "Final: «HIPNOSIS PARA HACKEAR TUS BLOQUEOS CON EL DINERO · LINK EN MI PERFIL · BNQ Method™»", r[8])
    primera = r[9].split("\n")[0]
    r[9] = f"{primera}\n{PROD}: el link está en mi perfil 👆\n{FIRMA}"
    r[11] = "Producto · link en perfil"
    return r
F = [_prod(r) for r in F]

URG_NUEVO = [
 ["1", "Hoy viernes · ya", "Revisa cuántas personas se registraron para el domingo", "Administrador de anuncios (pauta del domingo 15) + chats de WhatsApp. Mándame captura.", "5 min"],
 ["2", "Hoy viernes · 1 PM", "Yapping «Un día normal de una neurohacker con TDAH»", "Pestaña «Calendario». Sin guion.", "10 min"],
 ["3", "Hoy viernes · 6 PM", "Video FAMOSO: J.K. Rowling (12 editoriales)", "Pestaña «Calendario». Invita al LIVE del domingo.", "20 min"],
 ["4", "Sábado · 10 AM", "Acercamiento 1 a tus grupos", "Pestaña «Comunidad».", "5 min"],
 ["5", "Sábado · 7 PM", "Correo de Brevo «Mañana, 11 AM»", "Pestaña «Correos Brevo».", "10 min"],
 ["—", "Esta semana", "Hootsuite NO se toca", "Tus piezas van a otras horas que los videos sin rostro ya programados.", "—"],
]
URGENTE = URG_NUEVO

# ─────────── COMUNIDAD (grupos de WhatsApp) ───────────
COM = [
 ["Jueves 12 · 4:30 PM (HOY)", "Recordatorio", "Grupos de WhatsApp (Fórmulas Cuánticas + inscripciones)",
  "Hola, mis neurohackers 💛 Hoy a las 6:30 PM (hora CDMX) repito la hipnosis para hackear tus bloqueos con el dinero, para quien no alcanzó a entrar el martes.\nAquí está el link de Zoom: [LINK ZOOM 6:30 PM]\nAudífonos, lugar cómodo y nunca manejando. Nos vemos ahí ✨\nLo que no se activa, no cambia. @mabradiante · BNQ Method™"],
 ["Sábado 14 · 10:00 AM", "ACERCAMIENTO 1 · valor", "Grupos de WhatsApp",
  "Buenos días, mis neurohackers ☀️ Les dejo un regalo para el fin de semana: la activación de NAIA para recibir (va el video aquí abajo). Pónganla con audífonos y repitan con ella.\n💬 Cuéntenme con una sola palabra: ¿qué sintieron?\nY una noticia: el miércoles 18 a las 10 AM tengo una ACTIVACIÓN GRATIS EN VIVO solo para ustedes, mi comunidad: corte de fugas energéticas y activación de tus 7 chakras. Les mando el link el martes 💛\nBNQ Method™ · @mabradiante"],
 ["Domingo 15 · 9:00 AM", "Recordatorio", "Grupos de WhatsApp",
  "Hoy a las 11 AM (hora CDMX) es la hipnosis para hackear tus bloqueos con el dinero 🌀 Si alguien de tu familia o una amiga la necesita, compártele este mensaje.\nLink de Zoom: [LINK ZOOM 11 AM]\nBNQ Method™ · @mabradiante"],
 ["Martes 17 · 8:00 PM", "ACERCAMIENTO 2 · invitación exclusiva", "Grupos de WhatsApp",
  "Mis neurohackers 💛 Mañana miércoles 18 a las 10 AM (hora CDMX) es nuestra ACTIVACIÓN GRATIS EN VIVO, solo para la comunidad:\n⚡ Corte de fugas energéticas y activación de tus 7 chakras.\nHaremos una meditación corta de coherencia y una activación guiada, juntas.\nLink de Zoom: [LINK ZOOM MIÉRCOLES 10 AM]\n¿Quién se apunta? Escriban un 🌈 para saber que vienen.\nBNQ Method™ · @mabradiante"],
 ["Miércoles 18 · 9:30 AM", "Recordatorio", "Grupos de WhatsApp",
  "En 30 minutos empezamos 🌈 Activación gratis en vivo: corte de fugas energéticas y activación de tus 7 chakras.\nLink: [LINK ZOOM MIÉRCOLES 10 AM]\nBNQ Method™ · @mabradiante"],
]

GUIA = [
 ["Por qué el yapping es tu forma de hacer comunidad", "No tienes que contar tu vida privada. La conexión no viene de exponerte: viene de que te vean siendo tú, haciendo lo que haces, y de que les preguntes algo. 1 a 2 minutos, platicando, un solo corte."],
 ["5 formatos que conectan SIN exponerte", "1) Detrás de cámaras: preparando tu LIVE o tu activación. 2) Respondo una pregunta de comentarios. 3) Lo que aprendí hoy (de un LIVE, de un libro, de una alumna sin nombre). 4) Mi minuto de activación: lo haces frente a cámara. 5) Una frase que me cambió el día."],
 ["La regla de oro", "Cada yapping termina con UNA pregunta fácil de contestar («¿y tú?», «cuéntame con una palabra»). Las respuestas son tu comunidad empezando."],
 ["Responder = hacer comunidad", "10 minutos al día: contesta los comentarios con su nombre y una pregunta. En el grupo, reacciona a lo que escriben. Eso vale más que publicar más."],
 ["Lo que NO tienes que hacer", "No tienes que mostrar a tu hijo, tu casa ni tus problemas. No tienes que estar arreglada. No tienes que tener un guion: los puntos guía de cada yapping bastan."],
 ["Tu meta de esta semana", "7 yappings (1 diario) + contestar comentarios 10 min al día + 2 acercamientos al grupo. Nada más."],
]

CORREOS = [
 ["Jueves 12 · AHORA (antes de las 2 PM)", "Hoy a las 6:30 PM te guío en vivo", "Hoy repito la hipnosis (por si no entraste el martes)",
  "Hola, [NOMBRE] 💛\n\nSi el martes no alcanzaste a entrar, hoy repito la hipnosis para hackear tus bloqueos con el dinero.\n\n📅 Hoy, jueves 12 de noviembre · 6:30 PM (hora CDMX) · por Zoom · gratis.\n\nEs una práctica guiada en vivo: estás despierta y decides todo el tiempo. Solo necesitas audífonos y un lugar cómodo (nunca manejando).\n\n👉 Entra aquí: [LINK ZOOM 6:30 PM]\n\nNos vemos ahí.\nMabel"],
 ["Sábado 14 · 7:00 PM", "Mañana, 11 AM: hipnosis en vivo", "¿Por qué el dinero no llega aunque trabajes?",
  "Hola, [NOMBRE] 💛\n\nMuchas veces el dinero no llega por falta de esfuerzo. Llega un bloqueo aprendido que lo frena antes de empezar.\n\nMañana lo trabajamos juntas:\n📅 Domingo 15 de noviembre · 11 AM (hora CDMX) · por Zoom · gratis.\n\n👉 Regístrate aquí: [LINK DE REGISTRO]\n\nMabel"],
 ["Domingo 15 · 8:00 AM", "Es hoy 🌀 11 AM", "Hoy a las 11 te espero",
  "Hola, [NOMBRE]\n\nHoy a las 11 AM (hora CDMX) es la hipnosis para hackear tus bloqueos con el dinero.\n👉 Link de Zoom: [LINK ZOOM 11 AM]\n\nAudífonos, lugar cómodo y una intención: ¿qué quieres soltar con el dinero?\n\nMabel"],
 ["Domingo 15 · 3:00 PM", "Si no alcanzaste a entrar", "La oferta de hoy y la siguiente fecha",
  "Hola, [NOMBRE]\n\nGracias a todas las que llegaron hoy 💛 Si te lo perdiste, el martes 17 la repito: 11 AM y 7 PM (hora CDMX).\n\nY si ya quieres empezar, aquí está la Activación Simultánea · Hipnosis para hackear tus bloqueos con el dinero, a $500 + impuestos:\n👉 " + PAGINA + "\n\nMabel"],
 ["Lunes 16 · 7:00 PM", "Mañana: 11 AM o 7 PM", "Elige tu horario para mañana",
  "Hola, [NOMBRE] 💛\n\nMañana martes 17 repito la hipnosis para hackear tus bloqueos con el dinero, en 2 horarios: 11 AM y 7 PM (hora CDMX). Por Zoom y gratis.\n\n👉 Regístrate aquí: [LINK DE REGISTRO]\n\nMabel"],
 ["Martes 17 · 8:00 AM", "Hoy: 11 AM y 7 PM", "Hoy te hipnotizo dos veces",
  "Hola, [NOMBRE]\n\nHoy es el día: hipnosis para hackear tus bloqueos con el dinero.\n🕚 11 AM: [LINK ZOOM 11 AM]\n🕖 7 PM: [LINK ZOOM 7 PM]\n(hora CDMX)\n\nMabel"],
 ["Martes 17 · 6:00 PM (solo lista de comunidad)", "Mañana 10 AM, solo para ti", "Activación gratis en vivo para mi comunidad",
  "Hola, [NOMBRE] 💛\n\nMañana miércoles 18 a las 10 AM (hora CDMX) tengo una ACTIVACIÓN GRATIS EN VIVO solo para mi comunidad:\n⚡ Corte de fugas energéticas y activación de tus 7 chakras.\n\nHaremos una meditación corta de coherencia y una activación guiada.\n👉 Link: [LINK ZOOM MIÉRCOLES 10 AM]\n\nMabel"],
]
CIERRE_CORREO = ("\n\n—\nSígueme en redes: @mabradiante (TikTok, Instagram, YouTube).\nÚnete a mi comunidad Neurohackers y recibe links de activaciones, material, hackeos y reprogramación antes que nadie: [LINK COMUNIDAD]\n\n"
                 "La fórmula definitiva no es un decreto, es la BIO-NEUROABUNDANCIA: la reprogramación simultánea de tu ADN, tu energía y tu subconsciente. Porque lo que no se ACTIVA, NO CAMBIA.\n@mabradiante · BNQ Method™")

URGENTE = [
 ["1", "Ahora (antes de las 2 PM)", "Mandar el correo de hoy en Brevo", "Pestaña «Correos Brevo», fila 1. Pega el link de Zoom de las 6:30 PM.", "15 min"],
 ["2", "1:00 PM", "Grabar y publicar el aviso «HOY 6:30 PM»", "Pestaña «Calendario», jueves 12, 1:00 PM. 30 a 45 segundos, a cámara.", "15 min"],
 ["3", "4:30 PM", "Mensaje a tus grupos de WhatsApp", "Pestaña «Comunidad», fila 1. Pega el link de Zoom.", "5 min"],
 ["4", "6:15 PM", "Abrir Zoom 15 min antes", "Guion: live/guion-live-2026-11-10.md (mismo guion). Sin pantallas si te traba.", "—"],
 ["5", "6:30 PM", "LIVE", "Oferta: Activación Simultánea $500 + impuestos. Link de pago en el chat.", "1 h"],
 ["6", "8:30 PM", "Yapping «Lo que pasó hoy en la hipnosis»", "Pestaña «Calendario». 1 a 2 min, sin guion.", "10 min"],
 ["7", "9:30 PM", "Publicar NAIA · Merecimiento", "Lo genera NAIA; tú solo publicas.", "5 min"],
 ["—", "Esta semana", "Hootsuite NO se toca", "Ya están programados los 5 videos sin rostro del 11 al 15 (TikTok 8 PM; IG/YouTube 11 AM). Por eso tus piezas van a otras horas.", "—"],
]

wb = Workbook()
ORO = PatternFill("solid", fgColor="F3E6C6"); AZUL = PatternFill("solid", fgColor="E3E8F7"); VERDE = PatternFill("solid", fgColor="DCF0E8")
def hoja(ws, enc, filas, anchos, relleno=None):
    ws.append(enc)
    for c in ws[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="3B2A6B"); c.alignment = Alignment(wrap_text=True, vertical="center")
    for f in filas: ws.append(f)
    for i, w in enumerate(anchos): ws.column_dimensions[chr(65 + i)].width = w
    for r in ws.iter_rows(min_row=2):
        for c in r: c.alignment = Alignment(wrap_text=True, vertical="top")
        if relleno: relleno(r)
    ws.freeze_panes = "A2"
ws = wb.active; ws.title = "1 · HOY viernes 13"
hoja(ws, ["#", "Hora", "Qué haces", "Dónde está / cómo", "Tiempo"], URGENTE, [5, 22, 38, 70, 10])
ws2 = wb.create_sheet("2 · Calendario 12–18")
def pinta(r):
    q = r[3].value or ""
    fill = AZUL if q.startswith("NAIA") else (VERDE if "Yapping" in (r[4].value or "") else ORO)
    for c in r[:6]: c.fill = fill
hoja(ws2, ["Fecha", "Día", "Hora", "Quién", "Tipo", "TÍTULO (pantalla y portada)", "Primera frase", "Guion por tiempos / puntos guía", "Texto en pantalla", "Copy (con BNQ Method™)", "Hashtags", "CTA"], F,
     [11, 12, 9, 22, 22, 34, 36, 70, 40, 46, 30, 14], pinta)
ws3 = wb.create_sheet("3 · Comunidad")
hoja(ws3, ["Cuándo", "Tipo", "Dónde", "Mensaje (copia y pega)"], COM, [24, 26, 26, 90])
ws3.append([]); ws3.append(["CÓMO HACER COMUNIDAD SIN EXPONERTE"]); ws3[ws3.max_row][0].font = Font(bold=True, size=13)
for a, b in GUIA:
    ws3.append([a, "", "", b])
    for c in ws3[ws3.max_row]: c.alignment = Alignment(wrap_text=True, vertical="top")
    ws3[ws3.max_row][0].font = Font(bold=True)
ws4 = wb.create_sheet("4 · Correos Brevo")
hoja(ws4, ["Cuándo", "Asunto", "Vista previa", "Cuerpo (el cierre fijo ya va incluido)"], [c[:3] + [c[3] + CIERRE_CORREO] for c in CORREOS], [26, 32, 38, 90])
ws5 = wb.create_sheet("5 · Reglas de la semana")
for t in ["2 piezas diarias con tu cara: 1 yapping (conexión, sin venta) + 1 pieza con CTA en tus 2 formatos ganadores: FAMOSO + autoridad, o PODEROSA CONEXIÓN. Más 1 de NAIA (automática): las activaciones solo van en NAIA.",
          "Hootsuite: no se toca. Tus piezas van a otras horas que los 5 videos sin rostro ya programados.",
          "Palabras prohibidas: curso, masterclass, taller, terapia, sanación, coaching, ritual. Sin promesas de dinero ni de salud.",
          "Todo lleva «BNQ Method™» junto a @mabradiante. Precio siempre «+ impuestos». En correos: link a la PÁGINA del producto, no al de pago.",
          "El LIVE del miércoles 18 (chakras) es SOLO para la comunidad: no se pauta y el precio ($499 + impuestos) se dice dentro del LIVE.",
          "Lo que va entre [corchetes] lo llenas tú. Nunca se inventa tu historia."]:
    ws5.append([t]); ws5[ws5.max_row][0].alignment = Alignment(wrap_text=True)
ws5.column_dimensions["A"].width = 120
salida = os.path.join(AQUI, "semana-2026-11-12.xlsx"); wb.save(salida); print(salida, len(F), "piezas")
