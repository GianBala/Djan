#include <stdio.h>
#include <stdlib.h>

struct lista
{
	int dado; // Conteudo do nó 
	struct lista* prox; // Ponteiro para proximo item da fila
};

struct fila
{
	struct lista* ini; // Ponteiro para o inicio da fila
	struct lista* fim; // Ponteiro para o fim da fila
};


// Inicialização das funções // 
void criar_fila(struct fila*);
void insere_fim(struct fila*,int);
void remove_ini(struct fila*);
void mostrar_pontas(struct fila*);


void criar_fila(struct fila*F){ // Inicio e Fim da fila inicialmente nulos
	F->ini = NULL; 
	F->fim = NULL;
}

void insere_fim(struct fila*F,int n){ // Inserir um elemento no final da fila
	
	struct lista* novo = (struct lista*) malloc(sizeof(struct lista)); // Aloca um nó a ser adicionado na fila
	novo->dado = n; // Preenche o conteudo do nó
	if(F->fim) // Se houver algum elemento na fila
	{
		F->fim->prox = novo; // O atual último elemento aponta para o novo último elemento
	}
	else
	{
		F->ini = novo; // Caso a fila esteja vazia, o nó é considerado como início
	}
	F->fim = novo; // Final da fila aponta para o nó criado
}

void remove_ini(struct fila*F){ // Remove o primeiro elemento da fila
	if(F->ini) // Se houver algum elemento na fila
	{
		struct lista* aux = F->ini; // Um ponteiro auxiliar aponta para o primeiro nó da fila
		F->ini = F->ini->prox; // O inicio se torna o nó que o nó anterior estava apontando, no caso o segundo na fila
		free(aux); // Libera o espaço do nó removido
	}
	else
	printf("Fila Vazia\n");
}

void mostrar_pontas(struct fila* F){ // Mostra o inicio e fim da fila
	printf("Inicio = %d / Fim = %d",F->ini->dado,F->fim->dado);
}
