#include <stdio.h>
#include <stdlib.h>

struct Pilha
{
	int dado; // Dado do n� da pilha
	struct Pilha* prox; // Ponteiro para o pr�ximo n� da pilha
};


// Inicializa��o das Fun��es //
void criar_pilha(struct Pilha**);
void push(struct Pilha**);
void pop(struct Pilha**);  

void criar_pilha(struct Pilha** P){ // Inicializa com a pilha sendo nula
	P = NULL;
}

void push(struct Pilha** P, int n){ // Adiciona um n� ao topo da pilha
	struct Pilha* novo = (struct Pilha*) malloc(sizeof(struct Pilha)); // Aloca um n� para ser adicionado ao topo da pilha
	novo->dado = n; // Modifica o valor do n�
	novo->prox = *P; // O novo n� aponta para o topo da pilha
	*P = novo; // O novo n� se torna o topo da pilha
}

void pop(struct Pilha** P){
	struct Pilha* aux = *P; // Pilha auxiliar aponta para o topo da pilha
	*P = (*P)->prox; // N� abaixo do topo da pilha se torna o topo da pilha
	free(aux); // Antigo topo da pilha tem seu espa�o desalocado
}

mostrar_topo(struct Pilha** P){ // Mostra o topo da pilha
	printf("%d\n",(*P)->dado);
}


