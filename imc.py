peso = float(input("Informe seu peso (kg): "))
altura = float(input("Informe sua altura: "))

imc = peso // (altura*altura)

print (round(imc,2))

if imc >= 16:
    print("Magreza grave")
elif imc >= 16 and imc < 17:
    print("Magreza moderada")
elif imc > 17 and imc <= 18.5:
    print("Magreza leve")
elif imc > 18.6 and imc < 25:
    print("Peso ideal")
elif imc >= 25 and imc <= 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 35:
    print("Obesidade 1")
elif imc >= 35 and imc < 40:
    print("Obesidade 2")
else:
    print("Obesidade 3")
