"""Hoja de trabajo 'Mi Mapa de Bloqueos con el Dinero' (línea galaxia + dorado). Salida PDF y JPG."""
import sys; sys.argv=[sys.argv[0],"/tmp/x"]
exec(open("landing/checkout_roboticas_galaxia.py").read().split("# 1 HERO")[0])
W2,H2=1240,1754
bg=galaxia(W2,H2,31); d=ImageDraw.Draw(bg)
def c(t,f,y,col=BLANCO): d.text(((W2-d.textlength(t,font=f))/2,y),t,font=f,fill=col)
oro_txt(bg,((W2-ImageDraw.Draw(bg).textlength("Mi Mapa de Bloqueos",font=F(SER,76)))/2,70),"Mi Mapa de Bloqueos",F(SER,76))
oro_txt(bg,((W2-ImageDraw.Draw(bg).textlength("con el Dinero",font=F(SER,76)))/2,160),"con el Dinero",F(SER,76))
d=ImageDraw.Draw(bg)
c("LIVE GRATIS · Miércoles 25 nov · 11 AM · BNQ Method™",F(SB,30),270,ORO)
c("Imprímela o tenla en tu celular. La llenamos juntas en el live.",F(SB,28),320)
secs=[("1 · SUBCONSCIENTE (lo aprendiste de niña)","¿Qué frase de dinero escuchabas en tu casa?"),
      ("2 · MEMORIA CELULAR (lo heredaste)","¿Qué le pasaba con el dinero a tu mamá, papá o abuelos?"),
      ("3 · ENERGÍA (es 100% tuya)","¿Qué sientes en el cuerpo cuando cobras, pagas o abres el banco?"),
      ("4 · MI DECISIÓN","¿Qué quiero que cambie con mi dinero en las próximas 21 noches?")]
y=400
for t,q in secs:
    d.rounded_rectangle((70,y,W2-70,y+265),26,fill=(40,22,80),outline=ORO,width=3)
    d.text((100,y+22),t,font=F(B,36),fill=ORO); d.text((100,y+78),q,font=F(SB,28),fill=BLANCO)
    for k in range(3): d.line((100,y+140+k*42,W2-100,y+160+k*45),fill=(255,205,90),width=2)
    y+=295
c("Lo que no se ACTIVA, no CAMBIA. Y lo que no se REPITE, no se INSTALA.",F(SB,28),y+10,ORO)
c("Mabel Soriano · BNQ Method™",F(B,30),y+55)
bg.save("/home/user/MAPA-DE-BLOQUEOS-LIVE-25.jpg",quality=92); bg.save("/home/user/MAPA-DE-BLOQUEOS-LIVE-25.pdf")
print("ok")
