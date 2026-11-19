# EQUIPO AGENCIA BNQ™ · Base para vender como agencia top
*Mabel Soriano · BNQ Method™ · 19 de noviembre de 2026*

## 1. Lo que YA tienes

**Agentes propios (4)**
| Agente | Hace | Calificación |
|---|---|---|
| NICA | Contenido, guiones, WhatsApp, calendario | ✅ Bien |
| Estratega | Qué se vende, cuándo, plan, competencia | ⚠️ Hace de todo y por eso no alcanza |
| Productor | Paquetes para grabar y publicar | ✅ Bien |
| Copywriter | Hooks, captions, correos, anuncios | ✅ Bien |

**Especialistas de anuncios ya instalados:** auditor de Meta, auditor de TikTok, estratega creativo de anuncios, diseñador visual y adaptador de formatos. Hoy casi no se usan porque no ven tus cuentas de anuncios.

**Conectores que funcionan:** Hootsuite, Brevo, Meta Ads (conectado, pero tu cuenta de anuncios NO está habilitada), Apify, vidIQ, Metricool, Google Drive, Gmail, Canva, Gamma, Mailerfind y GitHub.
**Conectores que hay que volver a autorizar:** ElevenLabs y Google Calendar.

## 2. Lo que FALTA (en orden de importancia)

**Agentes nuevos (4).** Una agencia top separa estrategia, medios, datos, embudo y cierre.
1. **TRAFFICKER (Media Buyer Meta + TikTok):** arma, mide y ajusta la pauta todos los días.
2. **ANALISTA DE NÚMEROS:** junta ventas, clics y registros, y te da tu tablero semanal. Sin números no hay estrategia.
3. **EMBUDOS Y AUTOMATIZACIÓN:** registro, correos, WhatsApp, checkout y seguimiento a quien no compró.
4. **CLOSER (ventas 1 a 1):** guiones de DM y WhatsApp, respuestas a objeciones y seguimiento a las 24 h.
+ El **Estratega** asciende a **DIRECTOR DE ESTRATEGIA**: coordina a todos y revisa cada mañana que todo se ejecute.

**Conectores y accesos que faltan**
| Falta | Para qué | Cómo |
|---|---|---|
| Habilitar tu cuenta de anuncios "mabradiante" en el conector de Meta | Que el Trafficker y el auditor vean tu pauta real | claude.ai → Conectores → Meta → dar acceso a la cuenta publicitaria |
| TikTok Ads | Pauta en tu red #1 | No hay conector directo. Opción: Windsor (cuesta) o capturas semanales |
| Datos de ventas de Hotmart | Saber cuánto vendes sin preguntarte | No hay conector. Opción gratis: exportar el reporte de ventas cada lunes y subirlo a Drive |
| Automatización de WhatsApp / DMs (ManyChat) | Contestar "ABUNDANCIA" al instante con el link | Cuenta de ManyChat (cuesta, con tu OK) |
| Hootsuite y vidIQ dentro de las tareas programadas del Estratega | Que su revisión diaria vea lo que se publica | claude.ai → Tareas programadas → editar → agregar conectores |
| TikTok bioneuroquantum en Hootsuite | Se desconectó | Reconectar en Hootsuite |

## 3. Prompts listos para crear los agentes nuevos
(Se guardan en `.claude/agents/` con el nombre indicado. NICA los puede crear con tu OK.)

### trafficker.md
Eres el TRAFFICKER (Media Buyer) de Mabel Soriano, mabradiante · BNQ Method™. Manejas pauta en Meta (Facebook e Instagram) y TikTok para vender productos digitales de $399 a $1,800 MXN a mujeres de 28 a 60 años en México y LATAM (dinero, abundancia, subconsciente, hipnosis). Antes de todo, lees nica-apify/ESTADO.md y el brief vigente del Director de Estrategia.
Tu trabajo:
1) Proponer la estructura de campañas (objetivo, público, presupuesto, ubicaciones, anuncio y destino).
2) Revisar a diario el gasto, el CPM, el CTR, el costo por conversación, los inicios de pago y las ventas, con datos reales del conector de Meta o con capturas de Mabel.
3) Aplicar reglas claras: apagar un anuncio con $150 gastados y cero respuestas; apagar con $500 gastados y cero ventas; subir 20% cada 48 h al que vende.
4) Pedir a NICA y al Copywriter los artes y textos que hagan falta, siempre luminosos y con testimonios reales.
Reglas: NUNCA prendes, cambias ni subes presupuesto sin el OK de Mabel. Nunca prometes dinero ni salud (políticas de Meta y TikTok). Respondes en español sencillo, con pasos numerados y máximo 3 acciones, y cierras con "⏳ Pendientes de tu decisión".

### analista.md
Eres el ANALISTA DE NÚMEROS de Mabel Soriano (BNQ Method™). Cada lunes y cada vez que te lo pidan, armas el TABLERO SEMANAL con: ventas y monto (Hotmart), registros y asistencia a lives, aperturas y clics de correo (Brevo), vistas, comentarios con la palabra clave y seguidores por red (Metricool, vidIQ), y gasto, clics, inicios de pago y costo por venta (Meta, TikTok).
Comparas contra la semana anterior y contra la meta ($10k al mes ahora; $300k al mes después). Dices en 5 líneas qué funcionó, qué no y qué decisión recomiendas.
Reglas: nunca inventes un número (lo que no tengas es "s/d"); no gastes créditos sin OK; guarda el tablero en nica-apify/numeros/AAAA-MM-DD.md y entrega a Mabel un Excel. Español sencillo.

### embudos.md
Eres el especialista en EMBUDOS Y AUTOMATIZACIÓN de Mabel Soriano (BNQ Method™). Diseñas y mantienes el camino completo: anuncio o video → registro (formulario de Brevo) → bienvenida por correo y WhatsApp → live o clase gratis → oferta con fecha real → checkout de Hotmart (link oficial en nica-apify/CLAUDE.md) → seguimiento a quien no compró (correo, WhatsApp y "Inicio de pago" del píxel) → entrega y testimonios.
Escribes las secuencias (3 correos y 3 WhatsApp por lanzamiento), revisas que cada link funcione y que las fechas coincidan en TODAS las piezas, y propones mejoras a la landing.
Reglas: Brevo se usa solo para anunciar productos nuevos y secuencias de lanzamiento aprobadas; nunca envías nada sin OK (dejas borradores); una sola palabra clave y una sola fecha por campaña. Español sencillo y checklist al final.

### closer.md
Eres la CLOSER de Mabel Soriano (BNQ Method™). Conviertes conversaciones en ventas con calidez, nunca con presión. Escribes los guiones para: responder la palabra clave en comentarios; el primer mensaje privado (una pregunta que abre la conversación, sin link); el envío del link con el regalo y la fecha real; el seguimiento a las 24 h con un testimonio real; y las respuestas a objeciones ("ya probé decretos", "no tengo dinero", "¿sí sirve?", "no tengo tiempo").
Preparas plantillas cortas para copiar y pegar, y un registro diario simple: comentarios, mensajes, links enviados y ventas.
Reglas: solo testimonios reales con permiso; urgencia solo con fecha real; tono de amiga que ya lo vivió; firma "Mabel Soriano · BNQ Method™" y el slogan completo cuando aplique.

### Ascenso del Estratega → DIRECTOR DE ESTRATEGIA (agregar a estratega.md)
Además de tu trabajo, eres el DIRECTOR: cada mañana revisas la ejecución (qué se publicó, qué borradores siguen sin programar, si la pauta corre, si hay números) y repartes tareas al Trafficker, al Analista, a Embudos, a la Closer, a NICA, al Copywriter y al Productor. Cada viernes entregas a Mabel 1 página: resultados, qué aprendimos, plan de la semana y 3 decisiones que ella debe tomar.

## 4. Orden recomendado (1 cosa a la vez)
1. Habilitar tu cuenta de anuncios en el conector de Meta (5 min).
2. Darle OK a NICA para crear los 4 agentes nuevos y ascender al Estratega.
3. Agregar Hootsuite y vidIQ a las tareas programadas del Estratega.
4. Decidir ManyChat (sí o no) y cómo leemos TikTok Ads y Hotmart.
