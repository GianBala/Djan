#include <stdio.h>
#define N 8
struct Lista
{
	int V[N];
	int ini;
	int fim;
	int quant;
};

void criar_lista(struct Lista*);
int cheia(struct Lista*);
int vazia(struct Lista*);
void inserir_fim(struct Lista*);
void inserir_ini(struct Lista*);
void remover_fim(struct Lista*);
void remover_ini(struct Lista*);
void mostrar(struct Lista*);


void criar_lista(struct Lista* L)
{
	L->	quant = 0;
	L->ini = 0;
	L->fim = -1;
}

void mostrar(struct Lista* L)
{
	if(vazia(L) == 0)
	{
	int pos = L->ini;
	printf(" ");
	for(int cont=0;cont<L->quant;cont++)
	{
		printf("%d ",L->V[pos]);
		if(pos == N-1)
		{
			pos = 0;
		}
		else
		{
		pos += 1;
		}
	}
	}
	else
	{
		printf("Lista Vazia");
	}
	printf("\n\n");
}

int cheia(struct Lista* L)
{
	if(L->quant == N)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

int vazia(struct Lista* L)
{
	if(L->quant == 0)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

void inserir_fim(struct Lista* L)
{
	if(cheia(L) == 0)
	{
		L->fim += 1;
		if(L->fim > N-1)
		{
			L->fim = 0;
		}
		int n;
		printf("Numero: ");scanf("%d",&n);
		L->V[L->fim] = n;
		L->quant += 1;
		
	}
	else
	{
		printf("Lista Cheia\n\n");
	}
}

void inserir_ini(struct Lista* L)
{
	if(cheia(L) == 0)
	{
		int n;
		if(vazia(L) == 1)
		{
			printf("Numero: ");scanf("%d",&n);
			L->V[L->ini] = n;
			L->quant += 1;
			L->fim += 1;
		}
		else
		{
		L->ini -= 1;
		if(L->ini < 0)
		{
			L->ini = N-1;
		}
		printf("Numero: ");scanf("%d",&n);
		L->V[L->ini] = n;
		L->quant += 1;
		}
	}
	else
	{
		printf("Lista Cheia\n\n");
	}
}

void remover_fim(struct Lista* L)
{
	if(vazia(L) == 0)
	{
		L->fim -= 1;
		L->quant -= 1;
		if(L->fim < 0)
		{
			L->fim = N-1;
		}
	}
	else
	{
		printf("Lista Vazia\n\n");
	}
}

void remover_ini(struct Lista* L)
{
	if(vazia(L) == 0)
	{
		L->ini += 1;
		L->quant -= 1;
		if(L->ini > N-1)
		{
			L->ini = 0;
		}
	}
	else
	{
		printf("Lista Vazia\n\n");
	}
}

