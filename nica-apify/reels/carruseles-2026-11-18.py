import sys; sys.path.insert(0, "/home/user/markitdown-mcp-serve/nica-apify/reels")
from carrusel import portada, lamina, cierre
from pathlib import Path
O = Path("/home/user/CARRUSELES"); O.mkdir(exist_ok=True)
# 1 · Miércoles 18
p = "1-MIE18-FAMILIA"; f = "mabel-brazos.png"
portada(f, "Ayudar a tu familia con dinero", "TE PUEDE ESTAR BLOQUEANDO", "Lee hasta el final →", O/f"{p}-01.jpg")
lamina("No porque ayudar esté mal… sino por DESDE DÓNDE lo haces.", O/f"{p}-02.jpg", f)
lamina("Si das por culpa, por miedo a que te juzguen o para “pagar” algo… tu cuerpo aprende que el dinero SE VA.", O/f"{p}-03.jpg", f)
lamina("Dar desde la abundancia es: “Doy porque tengo, y sigo teniendo.”", O/f"{p}-04.jpg", f)
lamina("“Honro a mi familia y elijo un camino nuevo con el dinero.”", O/f"{p}-05.jpg", f, sub="Repítelo 3 veces, mano en el pecho")
cierre("Lo que no se repite, no se instala.", O/f"{p}-06.jpg", f)
# 2 · Jueves 19
p = "2-JUE19-7-DECRETOS"; f = "mabel-sonrisa.jpg"
portada(f, "Reprograma tu dinero esta noche con", "ESTOS 7 DECRETOS", "Guárdalo →", O/f"{p}-01.jpg")
dec = ["El dinero es seguro conmigo.", "Merezco recibir sin culpa.", "Lo que mi familia no pudo recibir, yo lo recibo.",
       "Cobro lo que valgo con amor.", "El dinero llega, se queda y lo disfruto.", "Soy la primera de mi linaje en vivir en abundancia.",
       "Hoy instalo un programa nuevo."]
for i, t in enumerate(dec, 1): lamina(t, O/f"{p}-{i+1:02d}.jpg", f, num=str(i))
cierre("Una vez no basta. Lo que no se repite, no se instala.", O/f"{p}-09.jpg", f)
# 3 · Sábado 21
p = "3-SAB21-MENSAJES-ALMA"; f = "mabel-brazos.png"
portada(f, "Mensajes que me dio mi alma", "SOBRE EL DINERO", "Desliza →", O/f"{p}-01.jpg")
for i, t in enumerate(["“No tienes que ganártelo. Tienes que permitírtelo.”",
                       "“El dinero no te juzga. Tú te juzgas cuando lo tienes.”",
                       "“Lo que heredaste no es tu destino. Es tu punto de partida.”",
                       "“Lo que repites cada noche, eso eres cada mañana.”"], 2):
    lamina(t, O/f"{p}-{i:02d}.jpg", f)
cierre("Guarda esto para cuando lo necesites", O/f"{p}-06.jpg", f)
print("ok")
