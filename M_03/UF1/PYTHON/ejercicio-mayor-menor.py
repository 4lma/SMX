num_1=int(input("Inserte un dividente: "))
num_2=int(input("Inserte un divisoir: "))
if(num_2==0):
    print("No se puede dividir entre 0")
else:
    res=num_1%num_2
    cociente=num_1//num_2
    if (res==0):
        print("Es exacto. El cociente és:",cociente)
    else:
        print("No es exacto. El cociente és:",cociente,"y el residuo és:",res)
