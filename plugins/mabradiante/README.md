# Paquete de agentes de @mabradiante

Trae: **NICA**, **estratega**, **productor** y las herramientas de anuncios **/ads** (basadas en
github.com/Hainrixz/claude-ads, licencia MIT).

## Usarlo en cualquier proyecto (una vez por computadora o proyecto)
En Claude Code escribe:

    /plugin marketplace add https://github.com/mabsoriano/markitdown-mcp-serve.git#claude/quirky-hawking-0lt1ol
    /plugin install mabradiante@mabradiante

## Para editar un agente
La copia oficial vive aquí, en `plugins/mabradiante/agents/`. `.claude/agents/` y
`.claude/skills/` de este repo apuntan a esta carpeta. Para que el cambio llegue a los otros
proyectos: sube la versión en `.claude-plugin/plugin.json` y en el otro proyecto corre
`/plugin marketplace update mabradiante`.
