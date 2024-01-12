from random import *
#1 Juku läheb kinno
nimi=input("Mis on sinu nimi?").capitalize() #"anna"->"Anna"
print("Tere",nimi) #"Tere, Anan"
if nimi=="Juku":
    print("Lahme kinno")
    vanus=int(input("Kui vana sa oled?"))
    if vanus<0 or vanus>100:
        pilet="vale vanus"
    elif vanus<6:
        pilet="tasuta pilet"
    elif vanus<=14:
        pilet="latepilet"
    elif vanus<=65:
        pilet="täispilet"
    elif vanus<=100:
        pilet="sooduspilet"
    print(pilet)  #Ilus vastus ja õige
else:
    print("Ma ootan Jukut")






















#protsent=randint(-100,500) #0-100 0-60-"2", 61-75-"3", 76-89-"4", 90-10-"5"
#print(protsent,"% on testi tulemus")
#if protsent<0 or protsent>100:
#    tulemus="valed andmed"
#elif 0<protsent<60:    #protsent>0 and protsent<60, protsent<60
#    tulemus="hinne 2"
#elif 60<=protsent<75:
#    tulemus="hinne 3"
#elif 75<=protsent<90:
#    tulemus="hinne 4"
#else:                 #elif 90<=protsent<=100: 
#    tulemus="hinne 5"
#print(tulemus)







#arv=randint(0,100) #случайное целое число от 0...100
#print(arv)
#if arv%2==0:
#    print(arv,"on paaris arv")
#else:
#    print(arv,"on paaritu arv")
#print()






#print("Tund on alanud")
#hilinemine=input("Kas õpilane on hilinenud?")   #"JAH"-a.upper(),"jah"-a.lower(),"Jah"-a.capitalize(),jAH
#if hilinemine.upper()=="JAH":
#    print("Õpilane ootab 30 min")
#print("Õpilane astub klassi")
   
