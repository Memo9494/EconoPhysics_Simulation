#include <winbgim.h>

 int main()

{

 initwindow(400,300);            // Abre una ventana gráfica de  400x300 pixeles

moveto(0,0);                         // Pone el cursor en 0,0

lineto(50,50);                        // Dibuja una línea desde 0,0 hasta 50,50

while(!kbhit());                     // Espera a que el usuario presione una tecla

closegraph();                      // Cierra la ventana gráfica

return 0;

}
