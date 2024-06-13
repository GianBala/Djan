#include <stdio.h>

int buscaBinaria(int arr[], int inicio, int fim, int alvo) {
    while (inicio <= fim) {
        int meio = (inicio + fim)/2;

        if (arr[meio] == alvo)
            return meio;

        if (arr[meio] > alvo)
            fim = meio - 1;
            
        else
            inicio = meio + 1;
    }

    return -1;
}

int main() {
    int lista[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int tamanho = sizeof(lista) / sizeof(lista[0]);
    int alvo = 7;

    int resultado = buscaBinaria(lista, 0, tamanho - 1, alvo);

    if (resultado != -1)
        printf("%d", resultado);
    else
        printf("Elemento nao encontrado na lista");

    return 0;
}

