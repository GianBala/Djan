#include <stdio.h>
#include "Fila.h"

int main()
{
struct fila F;

criar_fila(&F);
insere_fim(&F,5);
insere_fim(&F,6);
insere_fim(&F,7);
insere_fim(&F,8);
remove_ini(&F);
mostrar_pontas(&F);

return 0;
}
