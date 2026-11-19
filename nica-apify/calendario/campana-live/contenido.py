# Campaña LIVE "Hipnosis para hackear tus bloqueos con el dinero" · 29 oct – 10 nov 2026
# Mezcla aprobada por Mabel (28-oct): A = Mabel a cámara con decreto/ritual · B = rompe creencia o pregunta-dolor + lista de 3 ·
# Y = yapping diario (sin CTA) · R = audio robótico automático (solo días de venta de Robóticas).
LIVE1 = "martes 3 de noviembre"
LIVE2 = "martes 10 de noviembre"   # PROPUESTA: cambiar aquí si Mabel elige otra fecha

def cta_live(fecha, manana=False):
    cuando = "Mañana" if manana else f"El {fecha}"
    return (f"{cuando} a las 11 de la mañana, hora CDMX, te guío gratis por Zoom en una hipnosis "
            f"para hackear tus bloqueos con el dinero. Regístrate: el link está en mi perfil.")

CTA_ROBO = ("Si quieres los 10 audios, uno para cada momento del día: Activaciones Robóticas Millonarias, "
            "500 pesos, con la garantía de 7 días de Hotmart. Está en el link de mi perfil.")

H_LIVE = "#hipnosis #autohipnosis #hackeatumente #reprogramacionmental #bloqueosconeldinero #abundancia #mabradiante #metodoBNQ #livegratis"
H_DIN = "#dinero #abundancia #hackeatumente #reprogramacionmental #decretos #mabradiante #metodoBNQ #fyp"
H_REL = "#relaciones #amorpropio #hackeatumente #reprogramacionmental #mabradiante #metodoBNQ #fyp"
H_Y = "#mabradiante #tdah #emprendedora #mamaemprendedora #hackeatumente #fyp"
H_ROBO = "#audiosroboticos #afirmacionesroboticas #decretos #abundancia #hackeatumente #mabradiante #metodoBNQ"

def guion(partes):
    """partes: lista de (etiqueta, texto). Calcula tiempos a ~2.6 palabras por segundo."""
    t, out = 0.0, []
    for et, tx in partes:
        d = max(4, round(len(tx.split()) / 2.6))
        a, b = int(t), int(t + d)
        out.append((f"{a//60}:{a%60:02d}–{b//60}:{b%60:02d}", f"{et}: {tx}" if et else tx))
        t += d
    return out

def pieza(n, tipo, quien, titulo, hook, partes, pantalla, copy, hashtags, hora, cta):
    return dict(n=n, tipo=tipo, quien=quien, titulo=titulo, hook=hook, guion=guion(partes),
                pantalla=pantalla, copy=copy, hashtags=hashtags, hora=hora, cta=cta)

def A(titulo, hook, guardar, dolor, lista, dato, historia, hackeo, revel, cta, pantalla, copy, hashtags=H_DIN, hora="19:30", etiqueta_cta="LIVE"):
    return pieza("A", "Decreto o ritual para hacer ya", "Tú a cámara", titulo, hook,
                 [("GANCHO", hook), ("GUARDAR", guardar), ("DOLOR", dolor), ("LISTA DE 3", lista), ("DATO", dato),
                  ("", f"[TU HISTORIA: {historia}]"), ("HACKEO (hazlo conmigo 3 veces)", hackeo), ("REVELACIÓN", revel), ("CTA", cta)],
                 pantalla, copy, hashtags, hora, etiqueta_cta)

def B(titulo, hook, guardar, dolor, lista, dato, historia, hackeo, revel, cta, pantalla, copy, hashtags=H_DIN, hora="21:00", etiqueta_cta="LIVE"):
    p = A(titulo, hook, guardar, dolor, lista, dato, historia, hackeo, revel, cta, pantalla, copy, hashtags, hora, etiqueta_cta)
    p.update(n="B", tipo="Rompe una creencia o pregunta-dolor + lista de 3")
    return p

def Y(titulo, hook, puntos, pregunta, copy, hora="18:00"):
    return dict(n="Y", tipo="Yapping (platicando, sin guion)", quien="Tú a cámara, natural, 1 a 3 min, un solo corte",
                titulo=titulo, hook=hook, puntos=puntos, pregunta=pregunta, copy=copy, hashtags=H_Y, hora=hora, cta="Sin CTA")

def R(titulo, hook, hackeos, instalo, frase, hora="18:00"):
    lineas = [("[VOZ ROBÓTICA]", hook), ("", "Guarda este audio y escúchalo 3 veces hoy. Mano en el pecho. Repite conmigo, en voz alta o en tu mente."),
              ("", " ".join(f"Hoy hackeo {h}." for h in hackeos)), ("", f"Hoy instalo: {instalo}"),
              ("FRASE CLAVE, 3 veces", f"{frase} {frase} {frase}"), ("CTA", CTA_ROBO),
              ("", "Lo que no se activa, no cambia. Mabel, arroba mabradiante, Método BNQ™.")]
    return pieza("R", "Audio robótico (venta de Robóticas)", "Automático: lo genero yo con voz y tu portada. Tú no grabas.",
                 titulo, hook, lineas,
                 f"0–3 s: {titulo} (letras grandes, línea dorada). Cada decreto como subtítulo grande. Final: «ACTIVACIONES ROBÓTICAS MILLONARIAS · $500 · LINK EN MI PERFIL».",
                 f"{hook} 🤖✨ Escúchalo 3 veces y repite conmigo.\nLos 10 audios completos: Activaciones Robóticas Millonarias · $500 · garantía de 7 días de Hotmart. Link en mi perfil 👆",
                 H_ROBO, hora, "Robóticas $500")

def LIVEDAY(fecha_txt):
    return pieza("A", "Aviso del día del LIVE", "Tú a cámara, 30 a 45 s", "HOY A LAS 11 AM: HIPNOSIS EN VIVO",
                 "Hoy a las 11 de la mañana te hipnotizo en vivo, y es gratis.",
                 [("GANCHO", "Hoy a las 11 de la mañana te hipnotizo en vivo, y es gratis."),
                  ("LISTA DE 3 para estar lista", "Uno: audífonos. Dos: un lugar cómodo donde nadie te interrumpa, y nunca manejando. Tres: una intención. ¿Qué quieres soltar hoy con el dinero?"),
                  ("", "Es una práctica de bienestar, no sustituye atención médica ni psicológica."),
                  ("CTA", "Si no te registraste, todavía estás a tiempo: el link está en mi perfil y te llega el acceso a Zoom.")],
                 "0–3 s: HOY A LAS 11 AM · HIPNOSIS EN VIVO. Lista: 1 AUDÍFONOS · 2 LUGAR CÓMODO · 3 TU INTENCIÓN. Final: «REGÍSTRATE · LINK EN MI PERFIL · 11 AM CDMX».",
                 f"Hoy, {fecha_txt}, 11 AM (hora CDMX) 🌀 Hipnosis en vivo y gratis para hackear tus bloqueos con el dinero. Por Zoom.\nRegístrate: link en mi perfil 👆",
                 H_LIVE, "08:00", "LIVE (hoy)")

# ───────────────────────── SEMANA 1 · CTA: LIVE martes 3 de noviembre ─────────────────────────
S1 = [
("2026-10-29", "Jueves 29 oct", "Vacío y despertar", [
  R("EL INTERRUPTOR: 1 MINUTO PARA SALIR DE LA ESCASEZ", "Cuando sientas que la escasez te gana, prende el interruptor.",
    ["el pánico de fin de mes", "el pensamiento en loop de «no va a alcanzar»", "la alarma en mi cuerpo", "mi memoria celular y mi subconsciente"],
    "en un minuto cambio de estado. Apago la escasez. Prendo la calma y la acción.", "Interruptor activado."),
  B("NO ES QUE TRABAJES POCO: TU CUERPO FRENA EL DINERO",
    "No es que trabajes poco. Es que tu cuerpo vive el dinero como un peligro, y lo frena antes de que llegue.",
    "Guarda este video y compártelo con la amiga que siempre dice «trabajo y trabajo, y el dinero no se mueve».",
    "Te esfuerzas, haces todo, y el dinero no se mueve. Llega una oportunidad y algo en ti se tensa. No eres tú: es un programa de alarma.",
    "Tres señales: uno, te da pena cobrar o decir tu precio. Dos, evitas ver tu cuenta del banco. Tres, cuando aparece una oportunidad, encuentras la razón para no tomarla.",
    "Los psicólogos Daniel Kahneman y Amos Tversky mostraron que perder nos duele más o menos el doble de lo que nos alegra ganar. Por eso tu cuerpo se pone en alerta cuando toca cobrar, pedir o arriesgar.",
    "cuándo te diste cuenta de que tu cuerpo se tensaba con el dinero",
    "Mano en el pecho. Exhala largo. Repite conmigo: el dinero es seguro conmigo, me permito recibirlo. El dinero es seguro conmigo, me permito recibirlo. El dinero es seguro conmigo, me permito recibirlo.",
    "No es que el dinero no quiera llegar. Es que tu cuerpo le cierra la puerta para dejar de sentir peligro.",
    cta_live(LIVE1),
    "0–3 s: NO ES QUE TRABAJES POCO. Lista: 1 PENA DE COBRAR · 2 NO VES TU CUENTA · 3 DEJAS PASAR OPORTUNIDADES. Dato: Kahneman y Tversky. Final: «LIVE GRATIS · MARTES 3 NOV · 11 AM · LINK EN MI PERFIL».",
    "No es que trabajes poco 💸 Tu cuerpo vive el dinero como peligro y lo frena antes de que llegue.\nEl martes 3 de noviembre, 11 AM (CDMX), te guío gratis en una hipnosis para hackear ese bloqueo. Regístrate: link en mi perfil 👆", H_LIVE),
  Y("LO QUE NADIE VIO DE MI PRIMER LIVE", "Te voy a contar lo que de verdad pasó en mi primer LIVE.",
    ["[Cómo te preparaste y qué esperabas]", "[Que te trabaste cambiando de pantallas y cómo te sentiste]",
     "[Que llegaron 5 personas y lo que sentiste al guiarlas]", "[Qué vas a cambiar: sin pantallas, solo tú y tu voz]"],
    "¿Tú qué haces cuando algo no te sale como lo planeaste?",
    "Lo que no se ve detrás de un LIVE 🎥 Te lo cuento sin filtro.\n¿Tú qué haces cuando algo no sale como planeaste? Te leo 👇"),
]),
("2026-10-30", "Viernes 30 oct · quincena", "Energía y dinero", [
  Y("LO QUE ME FRENABA CON EL DINERO (TENGO TDAH)", "Tengo TDAH y te voy a contar qué me frenaba con el dinero, y qué hago hoy.",
    ["[Cómo era tu relación con el dinero antes]", "[Algo que te frenaba con el dinero: cobrar, pedir, decir tu precio… lo que tú hayas vivido]",
     "[Qué hackeo usas hoy]", "[Qué le dirías a otra mujer con TDAH]"],
    "¿Qué sientes que te frena a ti con el dinero? Sin juicio, cuéntame.",
    "Dinero + TDAH 🧠 Lo que me frenaba y lo que me funciona hoy, sin fórmulas mágicas.\n¿Qué te frena a ti? Cuéntame 👇"),

  A("DÍA DE QUINCENA: DI ESTO PARA ABRIRTE A RECIBIR", "Hoy es quincena. Te haya llegado poco, mucho o nada, di esto.",
    "Guárdalo para cada quincena y compártelo con quien trabaja mucho y siente que el dinero no se mueve.",
    "Ves que a otras les llega y a ti algo te frena: no pides, no cobras, no te atreves. No eres tú: es el programa de «el dinero no es para mí».",
    "Tres pasos: uno, pies en el piso y mano en el pecho. Dos, di en voz alta la cantidad que te gustaría recibir, sin voltear la cara. Tres, di el decreto.",
    "Una revisión de estudios de 2018, de Andrea Zaccaro, asoció la respiración lenta con más sensación de calma. Es una práctica de bienestar, no un tratamiento.",
    "cómo vivías tú la quincena antes",
    "Exhala largo y repite conmigo: me abro a recibir y lo sostengo con calma. Me abro a recibir y lo sostengo con calma. Me abro a recibir y lo sostengo con calma.",
    "El dinero no se frena por falta de trabajo. Se frena cuando no te sientes segura de recibir.",
    cta_live(LIVE1),
    "0–3 s: DÍA DE QUINCENA: DI ESTO. Pasos: 1 MANO EN EL PECHO · 2 DI LA CANTIDAD · 3 DECRETO. Final: «LIVE GRATIS · MARTES 3 NOV · 11 AM».",
    "Llegue poco, mucho o nada esta quincena, di esto conmigo 💰 Ábrete a recibir.\nY el martes 3 de noviembre, 11 AM (CDMX): hipnosis gratis para hackear tus bloqueos con el dinero. Link en mi perfil 👆", H_LIVE),
  B("¿POR QUÉ TRABAJAS TANTO Y EL DINERO NO SE MUEVE?", "¿Por qué trabajas tanto y el dinero no se mueve?",
    "Guarda este video y mándaselo a quien trabaja el doble y sigue igual.",
    "No es flojera ni que no sepas hacerlo. Hay tres programas trabajando en automático que frenan el dinero antes de que llegue.",
    "Uno: te da culpa cobrar, y cobras de menos o regalas tu trabajo. Dos: no miras tu cuenta para no sentir miedo. Tres: repites lo que oíste en casa, como «el dinero cuesta mucho trabajo».",
    "Los economistas Karlsson, Loewenstein y Seppi lo llamaron «efecto avestruz»: evitamos mirar nuestra información de dinero cuando creemos que va a ser mala noticia.",
    "cuál de las 3 te pasaba a ti",
    "Repite conmigo: merezco recibir por lo que doy. Merezco recibir por lo que doy. Merezco recibir por lo que doy.",
    "Lo que no miras, lo maneja tu programa.",
    cta_live(LIVE1),
    "0–3 s: ¿POR QUÉ TRABAJAS TANTO Y EL DINERO NO SE MUEVE? Lista: 1 CULPA AL COBRAR · 2 NO MIRAS TU CUENTA · 3 REPITES LO DE CASA. Dato: efecto avestruz. Final: «LIVE GRATIS · MARTES 3 NOV · 11 AM».",
    "¿Trabajas tanto y el dinero no se mueve? 🫠 No es mala suerte: son 3 programas que lo frenan.\nMartes 3 de noviembre, 11 AM (CDMX): hipnosis gratis para hackearlos. Link en mi perfil 👆", H_LIVE),
]),
("2026-10-31", "Sábado 31 oct", "Metas y comunidad", [
  R("ACTIVACIÓN DE CONFIANZA CON EL DINERO", "Si el dinero te da miedo, este audio es para hacer las paces con él.",
    ["mi desconfianza con el dinero", "el «seguro algo va a salir mal»", "el miedo a equivocarme", "mi memoria celular y mi subconsciente"],
    "confío en mí para recibir, decidir y cuidar mi dinero.", "Confío en mí con el dinero."),
  B("NO TE FALTA DISCIPLINA: TU CEREBRO PROTEGE TU IDENTIDAD DE SIEMPRE",
    "No te falta disciplina. Tu cerebro está protegiendo a la persona que siempre has sido.",
    "Guárdalo para el día en que vuelvas a dejar algo a medias.",
    "Empiezas con todo el lunes y el jueves ya lo dejaste. No es flojera: es identidad.",
    "Tres señales: uno, dices «yo no soy de las que…». Dos, saboteas justo cuando vas bien. Tres, te cuesta imaginarte con más dinero.",
    "La psicóloga Daphna Oyserman, de la Universidad del Sur de California, estudia cómo actuamos según la identidad que sentimos posible para nosotras.",
    "una meta que dejaste y por qué",
    "Repite conmigo: soy una mujer que termina lo que empieza. Soy una mujer que termina lo que empieza. Soy una mujer que termina lo que empieza.",
    "Primero cambia quién eres. Después cambian tus resultados.",
    cta_live(LIVE1),
    "0–3 s: NO TE FALTA DISCIPLINA. Lista: 1 «YO NO SOY DE LAS QUE…» · 2 SABOTEAS CUANDO VAS BIEN · 3 NO TE IMAGINAS CON MÁS. Dato: Oyserman, USC. Final: «LIVE GRATIS · MARTES 3 NOV · 11 AM».",
    "No es disciplina, es identidad 🧠 Tu cerebro protege a la de siempre.\nMartes 3 de noviembre, 11 AM (CDMX): hipnosis gratis para hackear tus bloqueos con el dinero. Link en mi perfil 👆", H_LIVE),
  Y("LO QUE MÁS ME PREGUNTAN EN COMENTARIOS", "Esto es lo que más me preguntan en comentarios, y hoy te contesto.",
    ["[Pregunta real 1 de tus comentarios]", "[Pregunta real 2]", "[Pregunta real 3]", "[Qué te gustaría que te pregunten]"],
    "¿Qué pregunta me harías tú?", "Respondo lo que más me preguntan 💬\nDéjame tu pregunta aquí abajo y la contesto en otro video 👇"),
]),
("2026-11-01", "Domingo 1 nov · Día de Muertos", "Valor puro", [
  A("LOS PROGRAMAS DE DINERO QUE HEREDASTE DE TU FAMILIA", "Hoy pones la ofrenda a tus ancestros. ¿Y si también les devuelves lo que no te toca cargar?",
    "Guarda este ritual para hoy en la noche y compártelo con tu familia.",
    "Tu abuela trabajó sin descanso, tu mamá se privó de todo. Y tú sientes que si te va bien, los traicionas. No eres tú: es lealtad.",
    "Tres programas heredados: uno, sufrir para merecer. Dos, ahorrar con miedo y nunca disfrutar. Tres, ayudar a todos menos a ti.",
    "En 2003, los psicólogos Robert Emmons y Michael McCullough pidieron a un grupo anotar cada semana cosas por las que agradecían; reportaron sentirse más optimistas que quienes anotaban molestias.",
    "a quién honras hoy y qué programa le devuelves",
    "Ritual espiritual: enciende una vela junto a tu ofrenda o una foto, escribe el programa heredado y di: gracias por la vida; lo que es tuyo te lo devuelvo con amor, y yo elijo prosperar. (3 veces)",
    "Prosperar no es traicionar a tu familia. Es sanar lo que ellos no pudieron.",
    cta_live(LIVE1),
    "0–3 s: LOS PROGRAMAS DE DINERO QUE HEREDASTE. Lista: 1 SUFRIR PARA MERECER · 2 AHORRAR CON MIEDO · 3 AYUDAR A TODOS MENOS A TI. Aviso: ritual espiritual, de tradición. Final: «LIVE GRATIS · MARTES 3 NOV · 11 AM».",
    "Día de Muertos 🕯️🌼 Honra a tus ancestros y devuélveles con amor lo que no te toca cargar.\nEl martes 3, 11 AM (CDMX), hipnosis gratis para soltar los bloqueos con el dinero que heredaste. Link en mi perfil 👆", H_LIVE),
  B("LA HIPNOSIS NO TE DUERME: TE ENFOCA", "La hipnosis no te duerme ni te controla. Te enfoca.",
    "Guarda este video y compártelo con quien le tiene miedo a la hipnosis.",
    "Seguro te imaginas un péndulo y a alguien haciendo cosas raras en un escenario. Eso es show, no hipnosis.",
    "Tres verdades: uno, estás despierta todo el tiempo. Dos, tú decides; nadie te hace hacer nada. Tres, es atención enfocada, como cuando una película te atrapa.",
    "En 2016, un equipo de la Universidad de Stanford dirigido por David Spiegel observó con resonancia magnética cambios en la actividad de zonas del cerebro relacionadas con la atención durante la hipnosis.",
    "la primera vez que hiciste una hipnosis y qué sentiste",
    "Cierra los ojos un momento y repite conmigo: yo decido, yo me enfoco, yo me activo. Yo decido, yo me enfoco, yo me activo. Yo decido, yo me enfoco, yo me activo.",
    "La hipnosis no te quita el control. Te lo regresa.",
    cta_live(LIVE1),
    "0–3 s: LA HIPNOSIS NO TE DUERME: TE ENFOCA. Lista: 1 ESTÁS DESPIERTA · 2 TÚ DECIDES · 3 ATENCIÓN ENFOCADA. Dato: Stanford, David Spiegel, 2016. Final: «LIVE GRATIS · MARTES 3 NOV · 11 AM».",
    "La hipnosis no es lo que te contaron 🌀 Estás despierta y tú decides.\nPruébala conmigo el martes 3 de noviembre, 11 AM (CDMX), gratis. Link en mi perfil 👆", H_LIVE),
  Y("A QUIÉN HONRO HOY", "Hoy es Día de Muertos y quiero contarte a quién honro.",
    ["[A quién recuerdas hoy]", "[Qué te enseñó, también con el dinero]", "[Qué decidiste no repetir]", "[Qué le agradeces]"],
    "¿A quién honras tú hoy?", "Día de Muertos 🕯️ Hoy honro a quien me enseñó tanto.\n¿A quién honras tú? Escríbelo aquí 👇"),
]),
("2026-11-02", "Lunes 2 nov", "Dinero", [
  Y("MAÑANA ME VUELVO A PARAR FRENTE A LA CÁMARA", "Mañana hago mi segundo LIVE y te voy a ser honesta con lo que siento.",
    ["[Los nervios de hacer un LIVE]", "[Qué aprendiste del primero]", "[Por qué lo haces gratis]", "[Qué esperas que se lleve quien llegue]"],
    "¿Qué te da miedo intentar otra vez?", "Mañana lo vuelvo a intentar 🎥\n¿Qué te da miedo intentar otra vez? Te leo 👇"),
  A("DI ESTO ANTES DE ABRIR TU APP DEL BANCO", "Antes de abrir tu app del banco, di esto.",
    "Guárdalo y úsalo cada vez que te dé miedo ver tu saldo.",
    "Se te aprieta el estómago antes de ver la cuenta, y mejor no la abres. No eres tú: tu cerebro está en modo escasez.",
    "Tres pasos: uno, exhala largo antes de abrir la app. Dos, mira el número completo. Tres, di el decreto en voz baja.",
    "Los investigadores Sendhil Mullainathan y Eldar Shafir, en su libro «Escasez», explican que la preocupación por el dinero ocupa espacio mental y nos hace decidir peor.",
    "cómo era para ti abrir la app del banco",
    "Repite conmigo: miro mi dinero con calma y decido desde la abundancia. Miro mi dinero con calma y decido desde la abundancia. Miro mi dinero con calma y decido desde la abundancia.",
    "El miedo no cuida tu dinero. Lo cuida tu calma.",
    cta_live(LIVE1, manana=True),
    "0–3 s: DI ESTO ANTES DE ABRIR TU APP DEL BANCO. Pasos: 1 EXHALA · 2 MIRA EL NÚMERO · 3 DECRETO. Dato: Mullainathan y Shafir, «Escasez». Final: «MAÑANA · 11 AM · LIVE GRATIS».",
    "Antes de ver tu saldo, haz esto 📱💸\nY mañana martes 3, 11 AM (CDMX): hipnosis gratis para hackear tus bloqueos con el dinero. Link en mi perfil 👆", H_LIVE),
  B("MAÑANA TE HIPNOTIZO EN VIVO: ESTO ES LO QUE VAMOS A HACER", "Mañana te hipnotizo en vivo y te cuento exactamente qué vamos a hacer.",
    "Guarda este video como recordatorio y compártelo con quien quieras que vaya contigo.",
    "Si sientes que lo has intentado todo con el dinero y sigues igual, no es falta de ganas. Es un programa que vive debajo de lo que piensas.",
    "Vamos a hacer tres cosas: uno, Bio, soltar la alarma del cuerpo. Dos, Neuro, ver el programa de dinero que aprendiste. Tres, Quantum, instalar una nueva instrucción con tu decreto.",
    "La Asociación Americana de Psicología describe la hipnosis como un estado de atención enfocada. Estás despierta y decides todo el tiempo.",
    "por qué hiciste este LIVE gratis",
    "Repite conmigo: mañana me doy una hora para mí. Mañana me doy una hora para mí. Mañana me doy una hora para mí.",
    "No necesitas estar lista. Necesitas estar presente.",
    cta_live(LIVE1, manana=True),
    "0–3 s: MAÑANA TE HIPNOTIZO EN VIVO. Lista: 1 BIO · 2 NEURO · 3 QUANTUM. Ficha: «LIVE GRATIS · MARTES 3 NOV · 11 AM (CDMX) · POR ZOOM». Final: «REGÍSTRATE · LINK EN MI PERFIL».",
    "Mañana, 11 AM (CDMX) 🌀 Hipnosis en vivo y gratis para hackear tus bloqueos con el dinero.\nBio · Neuro · Quantum. Regístrate: link en mi perfil 👆", H_LIVE),
]),
("2026-11-03", "Martes 3 nov · LIVE 1", "LIVE 11 AM", [
  LIVEDAY(LIVE1),
  Y("ASÍ ME SENTÍ EN EL LIVE DE HOY", "Acabo de terminar el LIVE y quiero contarte cómo me sentí.",
    ["[Cuántas llegaron y qué sentiste]", "[Un momento que te movió (sin nombres)]", "[Qué hiciste distinto esta vez]", "[Que habrá otro LIVE el martes 10]"],
    "Si estuviste, ¿qué sentiste? Y si no, ¿qué te detuvo?", "Así me sentí hoy 💛 Gracias a cada una que llegó.\nSi estuviste, cuéntame qué sentiste 👇", hora="20:00"),
]),
]

# ───────────────────────── SEMANA 2 · CTA: LIVE martes 10 de noviembre ─────────────────────────
S2 = [
("2026-11-04", "Miércoles 4 nov", "Relaciones", [
  A("ESCRIBE ESTO SI SIEMPRE ATRAES LO MISMO", "Si siempre terminas en el mismo tipo de relación, escribe esto hoy.",
    "Guárdalo para hacerlo en la noche y compártelo con tu amiga que siempre se enamora del mismo.",
    "Cambia la persona, pero la historia se repite: das de más y recibes de menos. No eres tú: es un programa de merecimiento.",
    "Tres líneas: uno, «lo que siempre me pasa es…». Dos, «lo aprendí cuando…». Tres, «hoy elijo…».",
    "El psicólogo James Pennebaker estudió la escritura expresiva: escribir sobre lo que sientes durante unos minutos, varios días, ayuda a ordenar las emociones.",
    "el patrón que tú repetías en el amor",
    "Repite conmigo: merezco recibir lo mismo que doy. Merezco recibir lo mismo que doy. Merezco recibir lo mismo que doy.",
    "El mismo «no merezco» que te engancha en el amor es el que te bloquea con el dinero.",
    cta_live(LIVE2),
    "0–3 s: ESCRIBE ESTO SI SIEMPRE ATRAES LO MISMO. Lista: 1 «SIEMPRE ME PASA…» · 2 «LO APRENDÍ CUANDO…» · 3 «HOY ELIJO…». Dato: Pennebaker. Final: «LIVE GRATIS · MARTES 10 NOV · 11 AM».",
    "¿Siempre el mismo tipo de relación? ✍️ Escribe estas 3 líneas hoy.\nEl martes 10 de noviembre, 11 AM (CDMX): hipnosis gratis para hackear el «no merezco» con el dinero. Link en mi perfil 👆", H_REL),
  B("NO TE ENGANCHAS POR AMOR: TE ENGANCHA LA INCERTIDUMBRE", "No te enganchas por amor. Te engancha la incertidumbre.",
    "Guarda este video y mándaselo a quien está esperando un mensaje que no llega.",
    "Te escribe, desaparece, regresa. Y tú más enganchada. No eres tú: es tu cerebro buscando la recompensa.",
    "Tres señales: uno, revisas el celular a cada rato. Dos, un mensaje suyo te cambia el día. Tres, te conformas con migajas.",
    "La antropóloga Helen Fisher estudió con resonancia magnética a personas recién rechazadas y vio activas zonas del cerebro ligadas a la recompensa y al deseo intenso.",
    "una relación en la que te enganchaste",
    "Mano en el pecho y repite conmigo: mi paz no depende de un mensaje. Mi paz no depende de un mensaje. Mi paz no depende de un mensaje.",
    "No extrañas a la persona. Extrañas la descarga.",
    cta_live(LIVE2),
    "0–3 s: NO TE ENGANCHAS POR AMOR. Lista: 1 REVISAS EL CELULAR · 2 UN MENSAJE TE CAMBIA EL DÍA · 3 MIGAJAS. Dato: Helen Fisher. Final: «LIVE GRATIS · MARTES 10 NOV · 11 AM».",
    "No es amor, es enganche 💔 Tu cerebro busca la recompensa.\nMartes 10 de noviembre, 11 AM (CDMX): hipnosis gratis. Link en mi perfil 👆", H_REL),
  Y("LO QUE APRENDÍ DEL LIVE", "Esto aprendí en el LIVE del martes y no me lo esperaba.",
    ["[Lo que más te sorprendió]", "[Una reacción real del chat, solo con permiso]", "[Qué vas a mejorar]", "[Por qué vas a repetirlo]"],
    "¿Qué te gustaría que hiciéramos en el próximo?", "Lo que aprendí del LIVE 🌀\n¿Qué quieres que hagamos en el próximo? 👇"),
]),
("2026-11-05", "Jueves 5 nov", "Vacío y despertar", [
  R("ACTIVACIÓN PARA COBRAR LO QUE VALES", "Si te tiembla la voz cuando dices tu precio, repite esto conmigo.",
    ["la vergüenza de cobrar", "el «es que me da pena»", "el descuento que doy antes de que me lo pidan", "mi memoria celular y mi subconsciente"],
    "digo mi precio con calma, lo sostengo y lo recibo.", "Cobro lo que vale mi trabajo."),
  B("NO ESTÁS PERDIDA: ESTÁS DESPERTANDO", "No estás perdida. Estás despertando, y por eso nada te llena como antes.",
    "Guárdalo y compártelo con quien siente que ya no encaja en su vida.",
    "Lo que antes te emocionaba ya no te mueve, y te sientes rara. No eres tú: es tu consciencia pidiendo otra cosa.",
    "Tres señales: uno, ya no toleras conversaciones vacías. Dos, buscas sentido, no solo dinero. Tres, sientes que hay algo más y no sabes qué.",
    "El neurólogo Marcus Raichle describió en 2001 la «red neuronal por defecto»: la que se activa cuando la mente divaga, y que se estudia en la meditación.",
    "cuándo sentiste que estabas despertando",
    "Repite conmigo: no estoy perdida, estoy despertando. No estoy perdida, estoy despertando. No estoy perdida, estoy despertando.",
    "Lo que se cae no es tu vida. Es el programa que ya no te queda.",
    cta_live(LIVE2),
    "0–3 s: NO ESTÁS PERDIDA: ESTÁS DESPERTANDO. Lista: 1 NO TOLERAS LO VACÍO · 2 BUSCAS SENTIDO · 3 HAY ALGO MÁS. Dato: Raichle, 2001. Final: «LIVE GRATIS · MARTES 10 NOV · 11 AM».",
    "No estás perdida, estás despertando 🌀\nMartes 10 de noviembre, 11 AM (CDMX): hipnosis gratis para hackear tus bloqueos con el dinero. Link en mi perfil 👆", H_LIVE),
  Y("CÓMO ERA YO ANTES DE DESPERTAR", "Si me hubieras conocido hace unos años, no me reconocerías.",
    ["[Cómo eras antes]", "[El momento que lo cambió todo]", "[Qué fue lo más difícil de soltar]", "[Cómo eres hoy]"],
    "¿Tú en qué momento sentiste que algo cambió?", "Antes y después 🌱 Sin filtro.\n¿Cuándo sentiste tú que algo cambió? 👇"),
]),
("2026-11-06", "Viernes 6 nov", "Energía", [
  Y("MI TDAH NO ES MI ENEMIGO", "Durante años pensé que mi TDAH era mi problema. Hoy lo veo distinto.",
    ["[Cómo te enteraste de tu TDAH]", "[Lo que más te costaba]", "[Lo que hoy ves como tu fuerza]", "[Un hackeo que te funciona]"],
    "¿Tienes TDAH o conoces a alguien? Cuéntame.", "Mi TDAH no es mi enemigo 🧠⚡\n¿Tú también? Cuéntame 👇"),
  A("HAZ ESTO 1 MINUTO ANTES DE PAGAR O COBRAR", "Antes de pagar o cobrar, haz esto un minuto y nota la diferencia en tu cuerpo.",
    "Guárdalo para tu próximo pago y compártelo con quien cobra con pena.",
    "Pagas con nudo en la garganta y cobras pidiendo perdón. No eres tú: es tu sistema nervioso en modo alarma.",
    "Tres pasos: uno, pies en el piso y mano en el pecho. Dos, inhala en 4 y exhala largo en 6, una vez. Tres, mira la cantidad y di el decreto.",
    "Investigadores de Stanford, con Melis Balban en 2023, compararon ejercicios de respiración y el «suspiro» con exhalación larga se asoció con mejor estado de ánimo. Es bienestar, no un tratamiento.",
    "el pago o cobro que más te costaba",
    "Pies en el piso, exhala largo y repite: doy y recibo con calma. Doy y recibo con calma. Doy y recibo con calma.",
    "No es la cantidad la que te asusta. Es el estado en el que la ves.",
    cta_live(LIVE2),
    "0–3 s: HAZ ESTO 1 MINUTO ANTES DE PAGAR O COBRAR. Pasos: 1 PIES EN EL PISO · 2 INHALA 4 · EXHALA 6 · 3 DECRETO. Dato: Stanford, 2023. Final: «LIVE GRATIS · MARTES 10 NOV · 11 AM».",
    "Tu hackeo de 1 minuto antes de pagar o cobrar ⏱️\nMartes 10 de noviembre, 11 AM (CDMX): hipnosis gratis para hackear tus bloqueos con el dinero. Link en mi perfil 👆", H_LIVE),
  B("NO ERES FLOJA: TU CUERPO ESTÁ EN MODO ALARMA", "No eres floja. Tu cuerpo lleva meses en modo alarma.",
    "Guárdalo y compártelo con quien está cansada de estar cansada.",
    "Duermes y despiertas igual de cansada, y encima te culpas. No eres tú: es un cuerpo que no se ha sentido a salvo.",
    "Tres señales: uno, todo te parece urgente. Dos, no puedes descansar sin culpa. Tres, el dinero te preocupa hasta en la noche.",
    "En 2019 la Organización Mundial de la Salud incluyó el «burnout» en su clasificación como un fenómeno ligado al estrés crónico del trabajo que no se ha manejado bien.",
    "cuándo te diste cuenta de que vivías en alarma",
    "Mano en el pecho y repite conmigo: estoy a salvo, puedo bajar la guardia. Estoy a salvo, puedo bajar la guardia. Estoy a salvo, puedo bajar la guardia.",
    "Un cuerpo en alarma no recibe. Primero se calma, después recibe.",
    cta_live(LIVE2),
    "0–3 s: NO ERES FLOJA: TU CUERPO ESTÁ EN MODO ALARMA. Lista: 1 TODO ES URGENTE · 2 DESCANSAR CON CULPA · 3 EL DINERO EN LA NOCHE. Dato: OMS, 2019. Aviso: no es diagnóstico. Final: «LIVE GRATIS · MARTES 10 NOV · 11 AM».",
    "No es flojera, es modo alarma 🚨\nMartes 10 de noviembre, 11 AM (CDMX): hipnosis gratis. Link en mi perfil 👆", H_LIVE),
]),
("2026-11-07", "Sábado 7 nov", "Metas", [
  R("ACTIVACIÓN DE PROSPERIDAD", "Hoy recibes. Este audio es tu activación de prosperidad.",
    ["el dinero que llega y se va", "el «pago y me quedo en cero»", "el miedo a disfrutar lo que gané", "mi memoria celular y mi subconsciente"],
    "lo que llega se queda, crece y regresa multiplicado.", "Vivo en prosperidad."),
  B("3 SEÑALES DE QUE TE AUTOSABOTEAS JUSTO CUANDO VAS BIEN", "Justo cuando por fin vas bien, algo pasa y todo se cae. No es casualidad.",
    "Guárdalo para la próxima vez que estés a punto de lograrlo.",
    "Te enfermas antes del lanzamiento, te peleas cuando todo va bien, gastas lo que ibas a invertir. No eres tú: es un techo aprendido.",
    "Tres señales: uno, dejas todo para el último minuto. Dos, te da miedo que te vaya demasiado bien. Tres, buscas una excusa antes de empezar.",
    "En 1978 los psicólogos Steven Berglas y Edward Jones describieron el «autoboicot» o self-handicapping: ponernos obstáculos para tener una excusa si algo sale mal.",
    "una vez que te autosaboteaste justo antes de lograrlo",
    "Repite conmigo: me permito que me vaya bien. Me permito que me vaya bien. Me permito que me vaya bien.",
    "No le tienes miedo al fracaso. Le tienes miedo a quién serías si te va bien.",
    cta_live(LIVE2),
    "0–3 s: 3 SEÑALES DE QUE TE AUTOSABOTEAS. Lista: 1 TODO AL ÚLTIMO MINUTO · 2 MIEDO A QUE TE VAYA BIEN · 3 LA EXCUSA. Dato: Berglas y Jones, 1978. Final: «LIVE GRATIS · MARTES 10 NOV · 11 AM».",
    "¿Te autosaboteas justo cuando vas bien? 🧱\nMartes 10 de noviembre, 11 AM (CDMX): hipnosis gratis para hackear ese techo. Link en mi perfil 👆", H_LIVE),
  Y("POR QUÉ CREÉ EL MÉTODO BNQ™", "Te voy a contar por qué creé mi propio método.",
    ["[Qué buscabas y no encontrabas]", "[Qué juntaste: espiritualidad, ciencia y práctica]", "[Qué significa Bio, Neuro y Quantum para ti]", "[A quién quieres ayudar]"],
    "¿Qué te gustaría que te enseñara del método?", "Por qué creé el Método BNQ™ 🧬🧠⚛️\n¿Qué quieres que te enseñe? 👇"),
]),
("2026-11-08", "Domingo 8 nov", "Valor puro", [
  A("RITUAL DE DOMINGO PARA EMPEZAR LA SEMANA SIN ESCASEZ", "Haz este ritual hoy y empieza la semana sin escasez.",
    "Guárdalo para cada domingo y compártelo con tu familia.",
    "El domingo en la noche llega la angustia del lunes y de las cuentas. No eres tú: es el programa de siempre arrancando la semana.",
    "Tres pasos: uno, escribe 3 cosas que el dinero te dio esta semana. Dos, elige una sola acción de dinero para el lunes. Tres, di el decreto.",
    "En 2003 Robert Emmons y Michael McCullough encontraron que anotar cada semana motivos de gratitud se asoció con sentirse más optimista.",
    "cómo eran tus domingos en la noche",
    "Repite conmigo: empiezo esta semana en abundancia. Empiezo esta semana en abundancia. Empiezo esta semana en abundancia.",
    "La semana no empieza el lunes. Empieza en el estado en que te duermes el domingo.",
    cta_live(LIVE2),
    "0–3 s: RITUAL DE DOMINGO SIN ESCASEZ. Pasos: 1 3 GRACIAS · 2 1 ACCIÓN · 3 DECRETO. Dato: Emmons y McCullough, 2003. Final: «LIVE GRATIS · MARTES 10 NOV · 11 AM».",
    "Ritual de domingo ✨ Empieza la semana sin escasez.\nY el martes 10, 11 AM (CDMX): hipnosis gratis para hackear tus bloqueos con el dinero. Link en mi perfil 👆", H_LIVE),
  B("NO NECESITAS CREER PARA QUE FUNCIONE: NECESITAS REPETIR", "No necesitas creerlo para que funcione. Necesitas repetirlo.",
    "Guárdalo para el día en que sientas que los decretos no te sirven.",
    "Dices «soy abundante» y por dentro algo se ríe. No eres tú: tu cerebro todavía no tiene ese camino.",
    "Tres claves: uno, corto. Dos, diario y a la misma hora. Tres, con el cuerpo: mano en el pecho y voz.",
    "Un estudio de Phillippa Lally, del University College London, en 2009, encontró que un hábito tarda en promedio 66 días en volverse automático.",
    "el decreto que repetiste hasta que se volvió tuyo",
    "Repite conmigo: cada día mi cerebro aprende a vivir en abundancia. Cada día mi cerebro aprende a vivir en abundancia. Cada día mi cerebro aprende a vivir en abundancia.",
    "La fe ayuda. Pero la repetición instala.",
    cta_live(LIVE2),
    "0–3 s: NO NECESITAS CREER: NECESITAS REPETIR. Lista: 1 CORTO · 2 DIARIO · 3 CON EL CUERPO. Dato: Lally, UCL 2009 · 66 días. Final: «LIVE GRATIS · MARTES 10 NOV · 11 AM».",
    "¿Los decretos no te funcionan? 🔁 No es fe: es repetición.\nMartes 10 de noviembre, 11 AM (CDMX): hipnosis gratis. Link en mi perfil 👆", H_LIVE),
  Y("MI SEMANA, SIN FILTRO", "Así fue mi semana, sin filtro.",
    ["[Lo mejor de la semana]", "[Lo más difícil]", "[Algo que aprendiste de ti]", "[Qué viene la próxima semana]"],
    "¿Cómo estuvo tu semana?", "Mi semana sin filtro 🤍\n¿Y la tuya? Cuéntame 👇"),
]),
("2026-11-09", "Lunes 9 nov", "Dinero", [
  Y("POR QUÉ HAGO ESTE LIVE GRATIS", "Mucha gente me pregunta por qué hago este LIVE gratis.",
    ["[Por qué lo haces]", "[Qué pasó en el primero]", "[Qué quieres que pase mañana]", "[Qué le dirías a quien duda en entrar]"],
    "¿Qué te detiene de probar algo nuevo?", "¿Por qué gratis? Te lo cuento 💛\n¿Qué te detiene de probar algo nuevo? 👇"),
  A("DI ESTO ANTES DE DECIR TU PRECIO", "Antes de decir tu precio, di esto en tu mente.",
    "Guárdalo para tu próxima venta y compártelo con quien siempre se baja el precio.",
    "Dices tu precio y en el mismo segundo ofreces descuento. No eres tú: es el programa de «no valgo tanto».",
    "Tres pasos: uno, di tu nombre en tu mente. Dos, exhala largo. Tres, di tu precio y quédate en silencio.",
    "El psicólogo Ethan Kross, de la Universidad de Michigan, encontró que hablarte por tu nombre te da distancia y te ayuda a manejar mejor tus emociones.",
    "la vez que te bajaste el precio y te arrepentiste",
    "Pon tu nombre y repite: [tu nombre], tu trabajo vale y lo sostienes con calma. [Tu nombre], tu trabajo vale y lo sostienes con calma. [Tu nombre], tu trabajo vale y lo sostienes con calma.",
    "El precio no lo sostiene tu voz. Lo sostiene tu identidad.",
    cta_live(LIVE2, manana=True),
    "0–3 s: DI ESTO ANTES DE DECIR TU PRECIO. Pasos: 1 TU NOMBRE · 2 EXHALA · 3 PRECIO Y SILENCIO. Dato: Ethan Kross, U. de Michigan. Final: «MAÑANA · 11 AM · LIVE GRATIS».",
    "Antes de decir tu precio, haz esto 💬💰\nMañana martes 10, 11 AM (CDMX): hipnosis gratis para hackear tus bloqueos con el dinero. Link en mi perfil 👆", H_LIVE),
  B("MAÑANA TE HIPNOTIZO EN VIVO (Y ES GRATIS)", "Mañana te hipnotizo en vivo, y esta vez no te lo pierdes.",
    "Guarda este video como recordatorio y compártelo con quien quieras que vaya contigo.",
    "Esta semana hablamos de dinero, de amor, de cansancio y de autosabotaje. Todo viene del mismo lugar: un programa que se puede hackear.",
    "Para estar lista: uno, regístrate hoy, el link está en mi perfil. Dos, aparta 11 de la mañana, hora CDMX. Tres, audífonos, lugar cómodo y nunca manejando.",
    "La Clínica Mayo describe la hipnosis como un estado de atención y concentración elevadas. Es una práctica de bienestar: no sustituye atención médica ni psicológica.",
    "una frase de lo que más te movió del LIVE pasado",
    "Repite conmigo: mañana me elijo. Mañana me elijo. Mañana me elijo.",
    "No necesitas otra señal. Esta es.",
    cta_live(LIVE2, manana=True),
    "0–3 s: MAÑANA TE HIPNOTIZO EN VIVO (Y ES GRATIS). Checklist: ☐ REGÍSTRATE · ☐ 11 AM (CDMX) · ☐ AUDÍFONOS. Final: «REGÍSTRATE · LINK EN MI PERFIL».",
    "Mañana martes 10, 11 AM (CDMX) 🌀 Hipnosis en vivo y gratis.\nRegístrate: link en mi perfil 👆", H_LIVE),
]),
("2026-11-10", "Martes 10 nov · LIVE 2", "LIVE 11 AM", [
  LIVEDAY(LIVE2),
  Y("ASÍ ME SENTÍ EN EL SEGUNDO LIVE", "Terminé mi segundo LIVE y esto es lo que siento.",
    ["[Cómo te fue]", "[Qué cambió del primero al segundo]", "[Un momento que te movió (sin nombres)]", "[Qué sigue]"],
    "Si estuviste, ¿qué sentiste?", "Segundo LIVE ✅ Gracias 💛\nSi estuviste, cuéntame qué sentiste 👇", hora="20:00"),
]),
]

# ───────────────────────── ANUNCIOS · Meta (Facebook + Instagram) ─────────────────────────
ANUNCIOS = dict(
  reglas=[
    "Meta no permite que el anuncio diga o insinúe cosas personales de quien lo ve (dinero, deudas, salud). No: «¿Tienes deudas?» ni «Tu dinero se te va». Sí: «Cuando el dinero llega y se va, no siempre es mala suerte».",
    "Sin promesas de dinero ni de salud. La hipnosis se dice como práctica de bienestar.",
    "El formulario necesita el link de tu aviso de privacidad (en www.mabradiante.com).",
  ],
  fases=[
    dict(nombre="Fase 1 · LIVE del martes 3 de noviembre", fechas="Jueves 29 oct a martes 3 nov, 10:00 AM", fecha_live="Martes 3 nov · 11 AM (CDMX)"),
    dict(nombre="Fase 2 · LIVE del martes 10 de noviembre", fechas="Martes 3 nov, 14:00 a martes 10 nov, 10:00 AM", fecha_live="Martes 10 nov · 11 AM (CDMX)"),
  ],
  videos=[
    dict(id="V1", nombre="Es un programa", duracion="20 a 25 s · vertical 9:16 · tú a cámara",
         guion=[("0–3 s", "Cuando el dinero llega y se va, no siempre es mala suerte. Muchas veces es un programa."),
                ("3–12 s", "Un programa que aprendiste de niña, que vive en tu cuerpo y que se repite solo."),
                ("12–20 s", "El [FECHA DEL LIVE] a las 11 de la mañana te guío gratis, por Zoom, en una hipnosis para hackear ese programa."),
                ("20–25 s", "Regístrate aquí abajo y te llega el acceso.")],
         pantalla="0–3 s: «¿EL DINERO LLEGA Y SE VA?» · al final: «LIVE GRATIS · [FECHA] · 11 AM CDMX · REGÍSTRATE»"),
    dict(id="V2", nombre="La hipnosis no te duerme", duracion="15 a 20 s · vertical 9:16 · tú a cámara",
         guion=[("0–3 s", "La hipnosis no te duerme ni te controla. Te enfoca."),
                ("3–10 s", "Estás despierta, tú decides, y por eso puedes ver lo que te frena con el dinero."),
                ("10–20 s", "Pruébala conmigo, gratis, el [FECHA DEL LIVE] a las 11 de la mañana por Zoom. Regístrate aquí abajo.")],
         pantalla="0–3 s: «LA HIPNOSIS NO TE DUERME» · final: «LIVE GRATIS · [FECHA] · 11 AM CDMX»"),
    dict(id="V3", nombre="Haz esto conmigo (10 segundos)", duracion="25 a 30 s · vertical 9:16 · tú a cámara",
         guion=[("0–3 s", "Haz esto conmigo, son 10 segundos."),
                ("3–15 s", "Mano en el pecho. Exhala largo. Repite: el dinero es seguro conmigo."),
                ("15–22 s", "¿Sentiste algo? Eso fue una probadita."),
                ("22–30 s", "El [FECHA DEL LIVE] a las 11 de la mañana hacemos la hipnosis completa, gratis, por Zoom. Regístrate aquí abajo.")],
         pantalla="0–3 s: «HAZ ESTO CONMIGO · 10 SEGUNDOS» · decreto en pantalla · final: «LIVE GRATIS · [FECHA] · 11 AM CDMX»"),
  ],
  imagenes=[
    dict(id="I1", nombre="Arte «Dolor» (ya aprobado)", detalle="Mismo diseño de live/artes/, solo cambia la fecha a la del LIVE. Medidas: 1080×1350 (feed) y 1080×1920 (historias)."),
    dict(id="I2", nombre="Arte «Foto» (ya aprobado)", detalle="Tu foto real con la línea dorada, solo cambia la fecha. Mismas medidas."),
  ],
  textos=[
    "LIVE GRATIS · Hipnosis para hackear tus bloqueos con el dinero 🌀\n[FECHA DEL LIVE], 11 AM (hora CDMX), por Zoom.\nTe guío en una autohipnosis en vivo con mi Método BNQ™: Bio, Neuro y Quantum.\nRegístrate y te llega el acceso.",
    "Cuando el dinero llega y se va, no siempre es mala suerte: muchas veces es un programa aprendido.\nEl [FECHA DEL LIVE] a las 11 AM (CDMX) lo trabajamos juntas en una hipnosis en vivo y gratis.\nCupo de la sala de Zoom limitado. Regístrate aquí.",
    "La hipnosis no te duerme: te enfoca. Estás despierta y tú decides.\nPruébala gratis conmigo el [FECHA DEL LIVE], 11 AM (CDMX), por Zoom.\nPráctica de bienestar, no sustituye atención médica ni psicológica.",
  ],
  titulos=["LIVE gratis: hipnosis y dinero", "Hackea tus bloqueos con el dinero", "Hipnosis en vivo · 11 AM"],
  formulario=dict(
    nombre="Registro LIVE Hipnosis Dinero",
    intro="LIVE GRATIS · Hipnosis para hackear tus bloqueos con el dinero. [FECHA DEL LIVE], 11 AM (hora CDMX), por Zoom.",
    preguntas=["Nombre", "Correo", "País", "¿Qué te gustaría soltar con el dinero? (opcional, respuesta corta)"],
    final="¡Listo! Guarda este link: [FECHA DEL LIVE], 11 AM (hora CDMX). Botón: «Entrar a Zoom» → [LINK DE ZOOM]. También te lo mandamos por correo.",
  ),
  publico="Mujeres de 25 a 55 años · todo México · público Advantage+ con sugerencias: espiritualidad, meditación, hipnosis, ley de atracción, Joe Dispenza, abundancia.",
  regla="A las 48 horas: el anuncio con costo por registro de más del doble que el mejor se apaga, y su presupuesto pasa al ganador.",
)
