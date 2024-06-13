#include <stdio.h>
#include "Pilha.h"
int main()
{
struct Pilha* P;
push(&P,1);
mostrar_topo(&P);
push(&P,2);
push(&P,3);
mostrar_topo(&P);
pop(&P);
mostrar_topo(&P);
pop(&P);
mostrar_topo(&P);
return 0;	
}
