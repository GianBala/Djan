#include <stdio.h>
#include "ArvoreBi.h"

int main()
{
	struct no* A;
	A = add_galho(1,0,0);
	A->esq = add_galho(2,0,0);
	A->esq->esq = add_galho(3,0,0);
	A->dir = add_galho(4,0,0);
	mostra_arvore(A);
	printf("Result = %d",pertence(A,3));
}
