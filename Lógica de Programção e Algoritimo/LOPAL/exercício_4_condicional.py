lado1= int(input("Digite o primeiro lado:"))
lado2= int(input("Digite o segundo lado:"))
lado3= int(input("Digite o terceiro lado:"))

if((lado1+lado2) > lado3 and (lado1+lado3) > lado2 and (lado2+lado3) > lado1):
    if(lado1 == lado2 and lado2 == lado3 and lado3 == lado1):
     print ("EQUILÁTERO")

    elif(lado1 != lado2 and lado2 != lado3 and lado3 != lado1):
        print ("ESCALENO")

    else:
     print("ISÓSCELES")

else:
     print("O triâgulo não existe!")
