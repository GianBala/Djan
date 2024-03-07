#include <stdio.h>
#include <stdlib.h>
#include "Lista_Enca.h"

int main()
{

struct no *L;
criar_lista(&L);

int op;
int k = 1;
while(k==1)
{
	printf(" 1 - Inserir Inicio\n 2 - Inserir Fim\n 3 - Inserir Meio\n 4 - Remover Inicio\n 5 - Remover Fim\n 6 - Remover Meio\n 7 - Mostrar\n-1 - Encerrar\n\n");
	printf("Operacao: ");scanf("%d",&op);printf("\n");
	switch(op)
	{
		case(1):
			insere_ini(&L);
			mostrar(&L);
			break;
		case(2):
			insere_fim(&L);
			mostrar(&L);
			break;
		case(3):
			insere_meio(&L);
			mostrar(&L);
			break;
		case 4:
			remove_ini(&L);
			mostrar(&L);
			break;
		case(5):
			remove_fim(&L);
			mostrar(&L);
			break;
		case(6):
			remove_meio(&L);
			mostrar(&L);
			break;
		case(7):
			mostrar(&L);
			break;
		case(-1):
			k = 0;
			break;
	}		
}

return 0;
}
