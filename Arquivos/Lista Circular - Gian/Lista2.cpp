#include <stdio.h>
#include "Lista2.h"
#define N 8

int main()
{

struct Lista L1;
criar_lista(&L1);
int op;
int k = 1;
while(k==1)
{
	printf(" 1 - Inserir Inicio\n 2 - Inserir Fim\n 3 - Remover Inicio\n 4 - Remover Fim\n 5 - Mostrar\n-1 - Encerrar\n\n");
	printf("Operacao: ");scanf("%d",&op);printf("\n");
	switch(op)
	{
		case(1):
			inserir_ini(&L1);
			break;
		case(2):
			inserir_fim(&L1);
			break;
		case(3):
			remover_ini(&L1);
			break;
		case 4:
			remover_fim(&L1);
			break;
		case(5):
			mostrar(&L1);
			break;
		case(-1):
			k = 0;
			break;
	}		
}
return 0;
}





