n = int(input("dame n:"))
lista = []
for i in range(n-1):
    lista.append(int(input("dame un numero  ")))

auxlist = []

for element in lista:
    if element %2 == 0:
        auxlist.append(element)

lista = auxlist.copy
print(lista)

