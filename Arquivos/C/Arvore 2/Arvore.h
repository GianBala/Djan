#include <stdio.h>
#include <stdlib.h>

struct Arvore{
	int dado;
	struct Arvore* esq;
	struct Arvore* dir;
};
// Inicialização de Funções
void insere_ord(struct Arvore**,int);
struct Arvore* insere_ord2(struct Arvore*,int);
struct Arvore* remove_folha(struct Arvore*,int);
struct Arvore* limpa_arvore(struct Arvore*);
struct Arvore* bala_esq(struct Arvore*);
struct Arvore* bala_dir(struct Arvore*);
struct Arvore* insere_bala(struct Arvore*,int);
int fator_bala(struct Arvore*);
void mostra_arvore(struct Arvore*);
int max(int,int);
int altura(struct Arvore*);
int quant_no(struct Arvore*);


void insere_ord(struct Arvore** A,int n){
	
	if(*A)
	{	
		if(n > (*A)->dado)
		{
			insere_ord(&((*A)->dir),n);
		}
		else if(n < (*A)->dado)
		{
			insere_ord(&((*A)->esq),n);		
		}
		else
		{
			printf("Numero Invalido");	
		}
	}
	else
	{
		struct Arvore* novo = (struct Arvore*) malloc(sizeof(struct Arvore));
		novo->dado = n;
		novo->esq = NULL;
		novo->dir = NULL;
		*A = novo;
		
	}
	
}

struct Arvore* insere_ord2(struct Arvore* A,int n){
	
	if(!A)
	{
		A = (struct Arvore*) malloc(sizeof(struct Arvore));
		A->dado = n;
		A->esq = NULL;
		A->dir = NULL;
	}
	
	else if(n < A->dado)
	{
		A->esq = insere_ord2(A->esq ,n);	
	}
	
	else
	{
		A->dir = insere_ord2(A->dir,n);	
	}

return A;
}

struct Arvore* remove_folha(struct Arvore* A,int n){
	if(A)
	{
		 if(n == A->dado)
		 {
		 	free(A);
		 	A = NULL;
		 }
		 else if(n > A->dado)
		 {
		 	A->dir = remove_folha(A->dir,n);
		 }
		 else if(n < A->dado)
		 {
		 	A->esq = remove_folha(A->esq,n);
		 }
	}
	return A;
}

struct Arvore* limpa_arvore(struct Arvore* A){
	if(A)
	{
		limpa_arvore(A->esq);
		limpa_arvore(A->dir);
		free(A);
		A = NULL;	
	}
	return A;
}

void mostra_arvore(struct Arvore* A){
	if(A)
	{
		//printf("%d ",A->dado);
		mostra_arvore(A->esq);
		//printf("%d ",A->dado);
		mostra_arvore(A->dir);
		printf("%d ",A->dado);	
	}
}

int max(int a, int b){
	if(a>b)
	{
		return a;
	}
	else
	{
		return b;
	}
}

int altura(struct Arvore* A){
	if(!A)
	{
		return -1;
	}
	else
	{
		return 1 + max(altura(A->esq), altura(A->dir));
	}

}

int quant_no(struct Arvore* A){
	if(A)
	{
		return 1 + quant_no(A->esq) + quant_no(A->dir);
	}
	else
	{
		return 0;
	}
}

int fator_bala(struct Arvore* A){
	if(A)
	{
		return(altura(A->esq) - altura(A->dir));
	}
}

struct Arvore* bala_esq(struct Arvore* A){
	struct Arvore* aux = A->dir;
	A->dir = aux->esq;
	aux->esq = A;
	A = aux;
	
	return A;
}

struct Arvore* bala_dir(struct Arvore* A){
	struct Arvore* aux = A->esq;
	A->esq = aux->dir;
	aux->dir = A;
	A = aux;
	
	return A;
}

struct Arvore* insere_bala(struct Arvore*A,int n){
	if(!A)
	{
		A = (struct Arvore*) malloc(sizeof(struct Arvore));
		A->dado = n;
		A->esq = NULL;
		A->dir = NULL;
	}
	
	else if(n < A->dado)
	{
		A->esq = insere_bala(A->esq ,n);	
	}
	
	else
	{
		A->dir = insere_bala(A->dir,n);	
	}

	
	int bal = fator_bala(A);

    if(bal > 1 && n < A->esq->dado)
	{ 
		return bala_dir(A); //Rotação Simples para a Direita.
	}
    
	else if (bal < -1 && n > A->dir->dado)
	{
		return bala_esq(A);//Rotação Simples para a Esquerda.
	}
    
	else if(bal > 1 && n > A->esq->dado)
	{ 
        A->esq = bala_esq(A->esq);//Rotação Dupla para a Direita.
        return bala_dir(A);
    }
    
	else if(bal < -1 && n < A->dir->dado)
	{ 
        A->dir = bala_dir(A->dir);//Rotação Dupla para a Esquerda.
        return bala_esq(A); 
    }
    
return A;
}





