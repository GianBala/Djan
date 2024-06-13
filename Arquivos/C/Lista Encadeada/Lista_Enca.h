#include <stdio.h>
#include <stdlib.h>

struct no{
int dado;
struct no* prox;
};

void criar_lista(struct no**);
void mostrar(struct no**);
int tam(struct no**);
void insere_ini(struct no**);
void insere_fim(struct no**);
void insere_meio(struct no**);
void remove_ini(struct no**);
void remove_fim(struct no**);
void remove_meio(struct no**);
int eh_vazia(struct no**);

void criar_lista(struct no** L){
	
	*L = 0; // Lista inicia vazia
}

void mostrar(struct no** L){
	
	if(eh_vazia(L) == 0)
	{	
		for(struct no*aux = *L;aux;aux=aux->prox){
			printf("%d ",aux->dado);
		}
		printf("\n\n");
	}
	else
	{
		printf("Lista Vazia");
	}
}

int tam(struct no** L){
	
	struct no* aux = *L;
	if(aux==0)
	{
		return 0;
	}
	int t=1;
	for(aux = *L;aux->prox;aux=aux->prox)
	{
		t++;
	}
	return t;
}

void insere_ini(struct no** L){
	
	struct no* novo = (struct no*)malloc(sizeof(struct no)); // Aloca o espa�o na memoria para o novo n�
	if(novo) // Se o espa�o for alocado
	{
		printf("Valor a ser adicionado no inicio: ");scanf("%d",&novo->dado);printf("\n"); // Dado do n� � preenchido
		novo->prox = *L; // Novo n� aponta para o primeiro n�
		*L = novo; // Novo n� � adicionado ao inicio
	}
	else{printf("Erro, memoria nao alocada\n");}
}

void insere_fim(struct no** L){
	
	struct no*aux = *L;
	struct no* novo = (struct no*)malloc(sizeof(struct no)); // Aloca o espa�o na memoria para o novo n�
	if(novo) // Se o espa�o for alocado
	{
		printf("Valor a ser adicionado no fim: ");scanf("%d",&novo->dado);printf("\n"); // Dado do n� � preenchido
		novo->prox = 0; // Como vai ser adicionado ao fim, aponta para nada
		
		if(aux==0) // Se a Lista for Vazia, adiciona o no ao inicio
		{
			*L = novo;
		}
		
		else
		{
		for(aux = *L;aux->prox;aux=aux->prox); // Percorre toda a lista at� que n�o tenha mais nada para apontar 
		aux->prox = novo; // Ultimo n� aponta para o novo n� no fim
		}
	}
	else{printf("Erro, memoria nao alocada\n");}
}

void insere_meio(struct no** L){
	
	struct no* novo = (struct no*)malloc(sizeof(struct no)); // Aloca espa�o na memoria par novo n�
	struct no*aux = *L;
	if(novo){ // Se o espa�o for alocado
		int p,i=1;
		printf("Valor a ser adicionado no meio: ");scanf("%d",&novo->dado); // Dado do n� � preenchido
		printf("Posicao do novo no: ");scanf("%d",&p);printf("\n");
		while(p>tam(L))
		{
			printf("\nPosicao fora do alcance\n\n");
			printf("Posicao do novo no: ");scanf("%d",&p);
		}
		if(p==0)
		{
			novo->prox = *L; // Novo n� aponta para o primeiro n�
			*L = novo; // Novo n� � adicionado ao inicio	
		}
		else
		{
			if(aux==0) // Se a Lista for Vazia, adiciona o no ao inicio
			{
				*L = novo;
			}
			else
			{
				while(i<p)
				{	
					aux=aux->prox;
					i += 1;
				}
				novo->prox = aux->prox;
				aux->prox = novo;
			}
		}
		
			
	}
	else{printf("Erro, memoria nao alocada\n");}
}

void remove_ini(struct no** L){
	
	if(eh_vazia(L) == 0)
	{
		struct no* aux = *L;
		*L = aux->prox;
		free(aux);	
	}
	else
	{
		printf("Lista Vazia\n");
	}
}

void remove_fim(struct no** L){
	
	if(eh_vazia(L) == 0)
	{
		struct no* aux = *L;
		for(;aux->prox->prox;aux=aux->prox);
		free(aux->prox);
		aux->prox = 0;
	}
	else
	{
		printf("Lista Vazia\n");
	}
}

void remove_meio(struct no** L){
	
	if(eh_vazia(L) == 0)
	{
	
		int p,i=1;
		struct no*aux = *L;
		struct no* sai;
		
		printf("Posicao do no: ");scanf("%d",&p);
		while(p>tam(L)-1)
		{
			printf("\nPosicao fora do alcance\n\n");
			printf("Posicao do novo no: ");scanf("%d",&p);
		}
		printf("\n");
		if(p==0)
		{
			remove_ini(L);
		}
		
		else if(p==(tam(L)-1))
		{
			remove_fim(L);
		}
		
		else
		{
			while(i<p)
			{
				aux=aux->prox;
				i += 1;
			}
			sai = aux->prox;
			aux->prox = aux->prox->prox;
			free(sai);
		}
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


