#include <stdio.h>
#include <stdlib.h>

struct Pilha
{
	int dado; // Dado do nó da pilha
	struct Pilha* prox; // Ponteiro para o próximo nó da pilha
};


// Inicialização das Funções //
void criar_pilha(struct Pilha**);
void push(struct Pilha**);
void pop(struct Pilha**);  

void criar_pilha(struct Pilha** P){ // Inicializa com a pilha sendo nula
	P = NULL;
}

void push(struct Pilha** P, int n){ // Adiciona um nó ao topo da pilha
	struct Pilha* novo = (struct Pilha*) malloc(sizeof(struct Pilha)); // Aloca um nó para ser adicionado ao topo da pilha
	novo->dado = n; // Modifica o valor do nó
	novo->prox = *P; // O novo nó aponta para o topo da pilha
	*P = novo; // O novo nó se torna o topo da pilha
}

void pop(struct Pilha** P){
	struct Pilha* aux = *P; // Pilha auxiliar aponta para o topo da pilha
	*P = (*P)->prox; // Nó abaixo do topo da pilha se torna o topo da pilha
	free(aux); // Antigo topo da pilha tem seu espaço desalocado
}

mostrar_topo(struct Pilha** P){ // Mostra o topo da pilha
	printf("%d\n",(*P)->dado);
}


