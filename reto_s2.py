from ast import And
from random import randint, random
import matplotlib.pyplot as plt
import math
import random
import numpy as np
gobierno = 0
def delta(personas, M, n_personas):
    for i in range(n_personas):
        personas.append(M/n_personas)
    return personas
def interaccion(personas,n_personas):
    global gobierno
    l = randint(0,n_personas-1)
    r = randint(0,n_personas-1)
    pond = 4
    iva = pond/4
    pond = pond - iva
    gobierno += iva
    random = randint(0,1)
    cambio = 0
    if random == 0:
        cambio = -pond
    else:
        cambio = pond
    
    if (personas[l] + cambio) > 0 and (personas[r] - cambio) > 0:
        personas[l] = personas[l] + cambio
        personas[r] = personas[r] - cambio

    return personas
def crear_clases(clases,rango,n_clases):
    for i in range(n_clases):
        n_clase = [0,i*rango,(i+1)*(rango),0]
        clases.append(n_clase)
    return clases
def cuenta_clases(personas,clases,n_clases):
    j = 0
    for i in clases:
        i[0] = 0
        i[3] = 0
    for i in personas:
        #check
        aux = True
        while(aux == True):
            if int(i) > clases[-1][2]:
                clases[-1][0] += 1
                clases[-1][3] += i
                aux = False 
            elif int(i) >= clases[int(j)][1] and int(i) <= clases[int(j)][2]:
                clases[int(j)][0] += 1
                clases[int(j)][3] += i
                aux = False
            else:
                j += 1
                clases[j][0] += 1
                clases[j][3] += i
                aux = False

    return clases
def grafica(personas,bins):
    plt.hist(personas,5)
    plt.show()
def entropia(N,Clases,C):
    S = N*np.log(np.exp(N))
    sum = 0
    for i in Clases:
        sum += i[0]*np.log(np.exp(i[0]))
    
    S = S - sum
    return S
def print_clases(clases,M,n_personas):
    print("% Personas", "  ", "Menor", "  ", "Mayor", "  ", "% Dinero")
    print("")
    for i in clases:
        print(100*i[0]/n_personas,"%", " ",i[1], " ",i[2], " ", 100*i[3]/M,"%")
    print("")
def redestribucion(personas,n_personas):
    global gobierno
    redis = gobierno/n_personas
    for i in personas:
        i += redis
        gobierno -= redis
def bienestara(clases,n_claes,M):
    bienestar = 0
    a = 1
    o1 = M*a
    for i in clases:
        bienestar += i[0]*o1*i[3]
    return bienestar
def bienestarb(clases,n_claes,M):
    bienestar = 0
    a = 1
    o1 = 1 - np.exp(-a*M)
    for i in clases:
        bienestar += i[0]*o1*i[3]
    return bienestar
def main():
    #Declarar Variables
    M = 8000
    personas = []
    n_personas = 1000
    n_clases = 5
    n_momentos = 5
    rango = int((M/n_personas))
    interacciones = 10000
    personas = delta(personas,M,n_personas)

    #Crear las clases
    clases = []
    clases = crear_clases(clases,rango,n_clases)
    tiempo = []
    dista = []
    distb = []
    #Interacciones
    for i in range(interacciones):
        personas = interaccion(personas,n_personas)
        tiempo.append(i+1)
        if i%(interacciones/4) == 0:
            personas.sort()
            clases = cuenta_clases(personas,clases,n_clases)
            print_clases(clases,M,n_personas)
            print(bienestara(clases,n_clases,M))
            print(bienestarb(clases,n_clases,M))
        dista.append(bienestara)
        distb.append(bienestarb)
        
    
    personas.sort()
    #Redistribuir el IVA
    print(gobierno)
    redestribucion(personas,n_personas)
    print(gobierno)
    #Contar las personas
    clases = cuenta_clases(personas,clases,n_clases)
    #imprimir
    grafica(personas,n_clases)
    plt.plot(tiempo,dista)
    plt.plot(tiempo,distb)
    plt.show()

if __name__ == "__main__":
    main()

