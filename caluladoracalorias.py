#calculadora IMC
#Guillermo Romeo Cepeda Medina
#No se necesita un array para hacer el código, la estructura del código en
#canvas tampoco sugiere el uso de uno por como lo plantea.


nombre = str(input("¡Hola!, Nombre completo "))
peso = float(input("peso "))
estatura = float(input("estatura"))
IMC = peso/(estatura * estatura)

if(IMC < 18.5):
    print("De acuerdo con estos datos tú IMC es de ", IMC ," LO QUE INDICA ", "Peso bajo")
elif(IMC >= 18.5 and IMC <= 24.9 ):
    print("De acuerdo con estos datos tú IMC es de ", IMC ," LO QUE INDICA ", "Peso normal")
elif(IMC >= 25 and IMC <= 29.9 ):
    print("De acuerdo con estos datos tú IMC es de ", IMC ," LO QUE INDICA ", "Sobrepeso")
else:
    print("De acuerdo con estos datos tú IMC es de ", IMC ," LO QUE INDICA ", "Obesidad")
