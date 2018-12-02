gasolina=int(input("¿Que tipo de gasolina quiere?"(Super-Normal=1,Super-Turbo=2.SinPlomo-Normal=3,SinPlomo-Aditivos=4,Diesel-Normal=5,DieselFast$Furius=6)))
litros=int(input("¿Cuantos litros quieres?"))
if gasolina==1:
    gasolina=1.5
    print("El importe es de", gasolina*litros,"€.")
if gasolina==2:
   gasolina=1.55
    print("El importe es de",gasolina*litros,"€.")
if gasolina==3:
    gasolina=1.6
    print("El importe es de",gasolina*litros,"€.")
if gasolina==4:
    gasolina=1.65
    print("El importe es de",gasolina*litros,"€.")
if gasolina==5:
    gasolina=1.7
    print("El importe es de",gasolina*litros,"€.")
if gasolina==6:
    gasolina=1.75
    print("El importe es de",gasolina*litros,"€.")
