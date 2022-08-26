from cmath import sqrt
import math

t = 2
y = 4
h = 0.5/15
Yn = 10

for i in range(Yn):
  F = (1/10)*sqrt(y) + (2/5)*t*t
  F = y + h*F
  t = t + h
  y = F

error =abs(1-(y/5.09974611536733) )*100
print(str(error) + r"% de error")
#Obtuvimos los valores de la media y la desviación estándar, a partir de la función de densidad de probabilidad de Gauss, 
# la igualamos al pusogausiano. Obtuvimos 0 para la media y para la desv 1-raiz(2pi)
% 

D = readtable('930-data-export.csv',"VariableNamingRule","preserve");

plot(D.(1),D.(2))
title('Demanda de Electricidad en California')
xlabel('Time (Hours)')
ylabel('Total CAL Demand (MWh)')

Y = fft(D.(2));

plot(1/(D.(1)*3600),abs(Y))
title('Transformada de Fourier')
xlabel ('Frecuencia (Segundos^-1)')
ylabel ('Valores (FFT)')

plot(D.(1),abs(Y))
hold on 
ylim ([0 0.25*10^6])
xlim ([0 90])
plot(12,abs(Y(12,1)),"Marker","*","Color",'r',"LineWidth",1);
plot(24,abs(Y(24,1)),"Marker","*","Color",'r',"LineWidth",1);
plot(84,abs(Y(84,1)),"Marker","*","Color",'r',"LineWidth",1);
xlabel('Tiempo (Horas)')
ylabel('Valores (FFT)')
title('Transformada de Fourier / Horas')