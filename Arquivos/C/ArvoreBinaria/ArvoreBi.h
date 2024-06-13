#include <stdio.h>
#include <stdlib.h>

struct no{
	int dado;
	struct no* esq;
	struct no* dir;
};

// Inicialização de Funções
struct no* add_galho(int,struct no*,struct no*);
void mostra_arvore(struct no*);


struct no* add_galho(int n,struct no* ESQ,struct no* DIR){
	struct no* novo = (struct no*) malloc(sizeof(struct no));
	if(novo)
	{
		novo->dado = n;
		novo->esq = ESQ;
		novo->dir = DIR;
		return novo;
	}
	else
	{
		printf("Erro na Alocacao de Memoria");
		return 0;
	}
}

void mostra_arvore(struct no* A){
	if(A)
	{
		printf("%d\n",A->dado);
		mostra_arvore(A->dir);
		mostra_arvore(A->esq);
	}	
}

int pertence(struct no* A, int n){

	if(A)
	{
		return A->dado==n || pertence(A->esq ,n) || pertence(A->dir,n);
	}
	else
	{
		return 0;
	}

}






