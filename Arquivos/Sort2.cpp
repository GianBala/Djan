#include <stdio.h>
int conta = 0;
void sort(int v[],int T) // Poderia ser int *v
{
	int back = 0;
	for(int cont=0;cont<T;cont++)
	{
		for(int cont2=0;cont2<T-1;cont2++)
		if(v[cont2] > v[cont2+1])
		{
			back = v[cont2];
			v[cont2] = v[cont2+1];
			v[cont2+1] = back;
			conta+=1;
		}
	}
	
}

int main()
{
int T = 10;
int V[] = {2,7,6,3,1,5,9,8,4,10};

sort(V,T);
for(int cont=0;cont<10;cont++)
{
	printf("%d ",V[cont]);
}
printf("\n");
printf("Busca 2 = %d",conta);
return 0;
}
