#include <stdio.h>
#include "Arvore.h"

int main()
{

struct Arvore* A = 0;
A = insere_bala(A,4);
A = insere_bala(A,3);
A = insere_bala(A,2);
A = insere_bala(A,5);
A = insere_bala(A,6);
A = insere_bala(A,7);
//A = insere_bala(A,8);
//A = insere_bala(A,9);
//A = insere_bala(A,10);
//A = insere_bala(A,11);
//A = insere_bala(A,12);
//A = insere_bala(A,13);
//A = insere_bala(A,14);
//A = insere_bala(A,15);
//A = insere_ord2(A,1);
//A = remove_folha(A,5);
//A = insere_ord2(A,5);

int y = fator_bala(A->dir);

printf("Dado %d\n",A->dado);

mostra_arvore(A);
printf("\n");

int x = altura(A);
printf("Altura %d\n",x);

A = limpa_arvore(A);
A = insere_ord2(A,4);

mostra_arvore(A);


return 0;
}
