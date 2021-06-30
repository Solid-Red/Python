import time
import os

luz=time.daylight
año=time.strftime("%Y")
mes=time.strftime("%m")
dia=time.strftime("%d")
hora=time.strftime("%H")
minuto=time.strftime("%M")
segundo=time.strftime("%S")
zona=time.strftime("%z")
dia_semana=time.strftime("%A")
dia_noche=time.strftime("%p")
mes_long=time.strftime("%B")
hora_12=time.strftime("%I")

os.system("title ASCII_CLOCK_V1.0")
##print("año:",año)
##print("mes:",mes)
##print("dia:",dia)
##print("hora:",hora)
##print("minuto:",minuto)
##print("segundo:",segundo)
###print(zona)
##print("dia de semana :",dia_semana)
##print("Am/Pm:",dia_noche)
##print("Nombre mes :",mes_long)
##print("hora 12:",hora_12)

cero="░█████╗░\n██╔══██╗\n██║░░██║\n██║░░██║\n╚█████╔╝\n░╚════╝░"
uno="██╗\n██║\n██║\n██║\n██║\n╚═╝"
dos="██████╗░\n╚════██╗\n░░███╔═╝\n██╔══╝░░\n███████╗\n╚══════╝"
tres="██████╗░\n╚════██╗\n░█████╔╝\n░╚═══██╗\n██████╔╝\n╚═════╝░"
cuatro="░░██╗██╗\n░██╔╝██║\n██╔╝░██║\n███████║\n╚════██║\n░░░░░╚═╝"
cinco="███████╗\n██╔════╝\n██████╗░\n╚════██╗\n██████╔╝\n╚═════╝░"
seis="░█████╗░\n██╔═══╝░\n██████╗░\n██╔══██╗\n╚█████╔╝\n░╚════╝░"
siete="███████╗\n╚════██║\n░░░░██╔╝\n░░░██╔╝░\n░░██╔╝░░\n░░╚═╝░░░"
ocho="░█████╗░\n██╔══██╗\n╚█████╔╝\n██╔══██╗\n╚█████╔╝\n░╚════╝░"
nueve="░█████╗░\n██╔══██╗\n╚██████║\n░╚═══██║\n░█████╔╝\n░╚════╝░"

cero_n=["░█████╗░","██╔══██╗","██║░░██║","██║░░██║","╚█████╔╝","░╚════╝░"]
uno_n=["██╗","██║","██║","██║","██║","╚═╝"]
dos_n=["██████╗░","╚════██╗","░░███╔═╝","██╔══╝░░","███████╗","╚══════╝"]
tres_n=["██████╗░","╚════██╗","░█████╔╝","░╚═══██╗","██████╔╝","╚═════╝░"]
cuatro_n=["░░██╗██╗","░██╔╝██║","██╔╝░██║","███████║","╚════██║","░░░░░╚═╝"]
cinco_n=["███████╗","██╔════╝","██████╗░","╚════██╗","██████╔╝","╚═════╝░"]
seis_n=["░█████╗░","██╔═══╝░","██████╗░","██╔══██╗","╚█████╔╝","░╚════╝░"]
siete_n=["███████╗","╚════██║","░░░░██╔╝","░░░██╔╝░","░░██╔╝░░","░░╚═╝░░░"]
ocho_n=["░█████╗░","██╔══██╗","╚█████╔╝","██╔══██╗","╚█████╔╝","░╚════╝░"]
nueve_n=["░█████╗░","██╔══██╗","╚██████║","░╚═══██║","░█████╔╝","░╚════╝░"]

pm=[" █▀█ █▀▄▀█","█▀▀ █░▀░█"]
am=[" ▄▀█ █▀▄▀█","█▀█ █░▀░█"]

Day="█▀▄ ▄▀█ █▄█\n█▄▀ █▀█ ░█░"
Night="█▄░█ █ █▀▀ █░█ ▀█▀\n█░▀█ █ █▄█ █▀█ ░█░"

def printer(h,m,s):
    m1=list(str(h))
    m2=list(str(m))
    m3=list(str(s))

    print("Year:",time.strftime("%Y"),"/ Month:",time.strftime("%m"),"/ Day:",time.strftime("%d"),"---Weekday:",time.strftime("%A"),"\n")
    lista=[cero_n,uno_n,dos_n,tres_n,cuatro_n,cinco_n,seis_n,siete_n,ocho_n,nueve_n]
    punto=["██╗","╚═╝","░░░","░░░","██╗","╚═╝"]
    if time.strftime("%p")=="AM":
        print(am[0],"\n",am[1],"\n")
    elif time.strftime("%p")=="PM":
        print(pm[0],"\n",pm[1],"\n")
    for i in range(6):
        print(lista[int(m1[0])][i],lista[int(m1[1])][i],punto[i],lista[int(m2[0])][i],lista[int(m2[1])][i],punto[i],lista[int(m3[0])][i],lista[int(m3[1])][i])
    if int(time.strftime("%H"))>5 and int(time.strftime("%H"))<18 :
        os.system("color c")
        print(Day)
        
    else:
        os.system("color a")
        print(Night)
        

##print(cero)
##print(uno)
##print(dos)
##print(tres)
##print(cuatro)
##print(cinco)
##print(seis)
##print(siete)
##print(ocho)
##print(nueve)

a=time.strftime("%S")
b=time.strftime("%S")
while True:
    if a!=b:
        os.system("cls")
        printer((time.strftime("%I")),(time.strftime("%M")),(time.strftime("%S")))
        print("-----By Blue_Savarin 26/06/2021------")
        #para un formato de hora tipo 24 
        #printer((time.strftime("%H")),(time.strftime("%M")),(time.strftime("%S")))
        #print(time.strftime("%H"),time.strftime("%M"),time.strftime("%S"))
        a=time.strftime("%S")
        
    b=time.strftime("%S")
