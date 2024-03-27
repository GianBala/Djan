#include <stdio.h>
#include <stdlib.h>

struct no{
int dado;
struct no* prox;
struct no* ant;
};

struct fila{
struct no* ini;
struct no* fim;
};

void criar_lista(struct no**);
void insere_fim(struct no**,struct fila*);
void remove_ini(struct no**,struct fila*);
int eh_vazia(struct no**);

void criar_lista(struct no** L){
	
	*L = 0; // Lista inicia vazia
}


void insere_fim(struct no** L,struct fila* F){
	
	struct no*aux = *L;
	struct no* novo = (struct no*)malloc(sizeof(struct no)); // Aloca o espaço na memoria para o novo nó
	if(novo) // Se o espaço for alocado
	{
		printf("Valor a ser adicionado no fim: ");scanf("%d",&novo->dado);printf("\n"); // Dado do nó é preenchido
		novo->prox = 0; // Como vai ser adicionado ao fim, aponta para nada
		
		if(aux==0) // Se a Lista for Vazia, adiciona o no ao inicio
		{
			*L = novo;
			F->ini = novo;
			F->fim = novo;
		}
		
		else
		{
		for(;aux->prox;aux=aux->prox); // Percorre toda a lista até que não tenha mais nada para apontar 
		novo->ant = F->fim;
		aux->prox = novo; // Ultimo nó aponta para o novo nó no fim
		F->fim = novo;
		}
	}
	else{printf("Erro, memoria nao alocada\n");}
}

void remove_ini(struct no** L,struct fila* F){
	
	if(eh_vazia(L) == 0)
	{
		struct no* aux = *L;
		*L = aux->prox;
		(*L)->ant = 0;
		F->ini = *L;
		free(aux);
	}
	else
	{
		printf("Lista Vazia\n");
	}
}

int eh_vazia(struct no** L){
	
	if(L==0)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}


