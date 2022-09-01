from ast import And
from random import randint, random
import matplotlib.pyplot as plt
import math
import random as rnd
import numpy as np
#Definimos 3 clases
    #Employers
    #Employed
    #Unemployed
class Agent:
    def __init__ (self,_money,_employer,_employee_set,_id):
        self.money = _money
        self.employer = _employer
        self.employee_set = _employee_set
        self.id = _id
    def sumar (self):
        self.money = self.money + 1
        return self.money        
def delta(A, M,N,Unemployed_Number):
    Initial_money = M/N
    Employee_set = []
    for i in range(N):
        id = i
        Nuevo = Agent(M/N,Unemployed_Number,Employee_set,id)
        A.append(Nuevo)
    return A
def interaccion(A,N,Unemployed_Number,Wage_average,V,Wage_a,Wage_b):
    a = rnd.choices(A)[0]
    U = []
    C = []
    W = []
    #If a is unemployed
    if a.employer == Unemployed_Number:
        #U_union_C
        H = []
        H_money = []
        M_H = 0
        for i in A:
            if((i.employer == Unemployed_Number or len(i.employee_set) != 0) and i != a ):
                H.append(i)
                H_money.append(i.money)
        rnd_c = rnd.choices(H,H_money,k=1)[0]
        if(rnd_c.money > Wage_average):
            a.employer = rnd_c.id
            rnd_c.employee_set.append(a.id)
    #Select B
    b = rnd.choices(A)[0] 
    while a == b:
        b = rnd.choices(A)[0]
    exp = rnd.uniform(0,b.money)
    b.money -= exp
    V+= exp
    #Exchange with the V with C and W and firing
    u = 0
    if (a.employer != Unemployed_Number) or (len(a.employee_set) != 0):
        
        revenue = rnd.uniform(0,V)
        V -= revenue
        if a.employer != Unemployed_Number:
            A[a.employer].money += revenue
        else:
            a.money += revenue
            u = max(len(a.employee_set)-(a.money/Wage_average),0)
            for i in range(u):
                a.employee_set[i].pop()
            for i in a.employee_set:
                w_coins = rnd.uniform(Wage_a,Wage_b)
                if(a.money > w_coins):
                    a.money -= w_coins
                    i.money += w_coins
                else:
                    broke_money = rnd.uniform(0,a.money)
                    a.money -= w_coins
                    i.money += w_coins
    return A

def main():
    #Declare Variables
    N = 1000
    M = 100000
    T = 2000
    V = 0
    Unemployed_Number = M+1
    A = []
    Wage_a = 2
    Wage_b = 9
    Wage_average = int((Wage_a+Wage_b)/2)
    A = delta(A,M,N,Unemployed_Number)
    A = interaccion(A,N,Unemployed_Number,Wage_average,V,Wage_a,Wage_b)
    for i in range(T):
        A = interaccion(A,N,Unemployed_Number,Wage_average,V,Wage_a,Wage_b)
    m_final = []
    for i in A:
        m_final.append(i.money)
    personas = []
    for i in A:
        personas.append(i.id)
    for i in A:
        print(i.money)
        print(i.id)
    m_final.sort()
    plt.plot(personas,m_final)
    plt.show()
if __name__ == "__main__":
    main()
