#calculadora de calorias
#Guillermo Romeo Cepeda Medina
nombre = str(input("Nombre del alimento "))
carbs = int(input("Gramos Calorias "))
lipidos = int(input("Gramos Lipidos "))
proteina = int(input("Gramos Proteina "))

calorias = (carbs * 4) + (lipidos * 9) + (proteina * 4)
print(" Las calorias proporcionadas por" , nombre , "son " , calorias)
