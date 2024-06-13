#include <stdio.h>
int conta = 0;
void sort(int v[],int T) // Poderia ser int *v
{
	int back;
	for(int i=0;i<T;i++)
	{
		for(int j=i+1;j<T;j++)
		if(v[j] < v[i])
		{
			back = v[j];
			v[j] = v[i];
			v[i] = back;
			conta+=1;
		}
	}
	
}

int main()
{
int T = 10;
int V[] = {2,7,10,3,1,5,9,8,4,6};

sort(V,T);
for(int cont=0;cont<10;cont++)
{
	printf("%d ",V[cont]);
}
return 0;
}

