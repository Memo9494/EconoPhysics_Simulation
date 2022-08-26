n = int(input())
a = 0
b = 1
suma = 0
arreglo = [0]
for i in range(0,n-1):

    suma = a + b
    a = b
    b = suma
    arreglo.append(suma)
    
print(arreglo)
