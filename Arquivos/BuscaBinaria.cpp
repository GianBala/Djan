#include <stdio.h>
#include <math.h>
int main()
{

int N;
printf("Tamanho do Array: ");scanf("%d",&N);
int n[N];
for(int cont = 0;cont<N;cont++)
{
	printf("Numero %d: ",cont);scanf("%d",&n[cont]);
}
int i;
N -= 1;
printf("Numero a ser achado: ");scanf("%d",&i);
int L = ceil(N/2);
while(1)
{
	if(n[L] == i)
	{
		printf("Posicao %d",L);
		break;
	}
	
	if(n[L] < i)
	{
		if(n[L+1] == i)
		{
		printf("Posicao %d",L+1);
		break;
		}
		L = (L+N)/2;
	}
	
	if(n[L] > i)
	{
		if(n[L-1] == i)
		{
		printf("Posicao %d",L-1);
		break;
		}
		L = (L-1)/2;
	}
	
}

return 0;
}
