lec = 1
cuantosVan = 0
suma = 0
while(lec != 0):
    lec = int(input('Ingresa un numero'))
    suma = suma + lec
    cuantosVan = cuantosVan + 1

print("suma",suma)
print("cuantosVan",cuantosVan-1)
print("promedio",suma/(cuantosVan-1))