#include <stdio.h>
#include <stdlib.h>

struct lista
{
	int dado; // Conteudo do n� 
	struct lista* prox; // Ponteiro para proximo item da fila
};

struct fila
{
	struct lista* ini; // Ponteiro para o inicio da fila
	struct lista* fim; // Ponteiro para o fim da fila
};


// Inicializa��o das fun��es // 
void criar_fila(struct fila*);
void insere_fim(struct fila*,int);
void remove_ini(struct fila*);
void mostrar_pontas(struct fila*);


void criar_fila(struct fila*F){ // Inicio e Fim da fila inicialmente nulos
	F->ini = NULL; 
	F->fim = NULL;
}

void insere_fim(struct fila*F,int n){ // Inserir um elemento no final da fila
	
	struct lista* novo = (struct lista*) malloc(sizeof(struct lista)); // Aloca um n� a ser adicionado na fila
	novo->dado = n; // Preenche o conteudo do n�
	if(F->fim) // Se houver algum elemento na fila
	{
		F->fim->prox = novo; // O atual �ltimo elemento aponta para o novo �ltimo elemento
	}
	else
	{
		F->ini = novo; // Caso a fila esteja vazia, o n� � considerado como in�cio
	}
	F->fim = novo; // Final da fila aponta para o n� criado
}

void remove_ini(struct fila*F){ // Remove o primeiro elemento da fila
	if(F->ini) // Se houver algum elemento na fila
	{
		struct lista* aux = F->ini; // Um ponteiro auxiliar aponta para o primeiro n� da fila
		F->ini = F->ini->prox; // O inicio se torna o n� que o n� anterior estava apontando, no caso o segundo na fila
		free(aux); // Libera o espa�o do n� removido
	}
	else
	printf("Fila Vazia\n");
}

void mostrar_pontas(struct fila* F){ // Mostra o inicio e fim da fila
	printf("Inicio = %d / Fim = %d",F->ini->dado,F->fim->dado);
}
