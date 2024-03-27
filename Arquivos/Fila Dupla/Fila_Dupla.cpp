#include <stdio.h>
#include <stdlib.h>
#include "Fila_Dupla.h"

//void criar_lista(struct no**);
//void insere_fim(struct no**,struct fila*);
//void remove_ini(struct no**,struct fila*);

int main()
{

struct no* L;
struct fila F;

criar_lista(&L);
insere_fim(&L,&F);
insere_fim(&L,&F);
insere_fim(&L,&F);
insere_fim(&L,&F);
printf("%d %d\n",F.ini->dado,F.fim->dado);
remove_ini(&L,&F);
printf("%d %d\n",F.ini->dado,F.fim->dado);
remove_ini(&L,&F);
remove_ini(&L,&F);
printf("%d %d\n",F.ini->dado,F.fim->dado);

return 0;
}
