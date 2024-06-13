import java.util.Scanner;

//Deivison da Silva Costa (20220006152)
//Giancarlo Silveira Cavalcante (20220055086)

public class CalculadoraMatrizes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n;
        do {
            System.out.print("Digite a dimensão da matriz quadrada: ");
            n = scanner.nextInt();
            if(n<1){
                System.out.println("A dimensão é inválida. Digite uma dimensão válida.");
            }
        }while(n<=0);
        System.out.println();
        int[][] matriz1 = new int[n][n];
        int[][] matriz2 = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print("Digite o termo na posição "+ i+" "+ j+" da primeira matriz:");
                matriz1[i][j] = scanner.nextInt();
            }
        }
        System.out.println("\n----------------------------------------------------\n");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print("Digite o termo na posição "+ i+" "+ j+" da segunda matriz:");
                matriz2[i][j] = scanner.nextInt();
            }
        }

        do{
            System.out.println("BEM-VINDO A CALCULADORA DE MATRIZES!");
            System.out.println("1 - SOMA DE MATRIZES");
            System.out.println("3 - MULTIPLICAÇÃO  POR UM ESCALAR");
            System.out.println("6 - DETERMINANTE DE AMBAS AS MATRIZES(apenas com uma, duas ou 3 dimensões)");
            System.out.println("7 - SOMA DOS ELEMENTOS DE CADA MATRIZ INDICANDO QUAL É MAIOR");
            System.out.println("8 - SAIR");
            System.out.println("9 - PRINTAR MATRIZES");

            int num = scanner.nextInt();

            switch (num){
                case 1:
                    somaDeMatrizes(matriz1, matriz2, n);
                    break;
                case 3:
                    System.out.print("Digite um escalar: ");
                    int escalar = scanner.nextInt();
                    multiPorEscalar(matriz1, matriz2, n, escalar);
                    break;
                case 6:
                    determinante(n,matriz1,matriz2);
                    break;
                case 7:
                    somaMaior(n, matriz1, matriz2);
                    break;
                case 8:
                    scanner.close();
                    System.out.println("FINALIZANDO.....");
                    System.exit(0);
                case 9:
                    printarMatrizes(n,matriz1,matriz2);
                    break;
                default:
                    System.out.println("\nVocê digitou uma opção inválida, digite uma opção válida.\n");
            }
        }while(true);

    }

    public static void somaDeMatrizes(int[][] m1, int[][] m2, int n){
        int[][] mAux = new int[n][n];
        System.out.println("\nResultado da soma:\n");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                mAux[i][j] = m1[i][j] + m2[i][j];
                System.out.print(mAux[i][j]+ " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void multiPorEscalar(int[][] m1, int[][] m2, int n, int escalar){
        int[][] mAux1 = new int[n][n];
        int[][] mAux2 = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                mAux1[i][j] = m1[i][j] * escalar;
                mAux2[i][j] = m2[i][j] * escalar;
            }
        }
        System.out.printf("\nResultado da multiplicação da matriz 1 por %d: \n\n", escalar);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(mAux1[i][j]+" ");
            }
            System.out.println();
        }

        System.out.printf("\n\nResultado da multiplicação da matriz 2 por %d: \n\n", escalar);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(mAux2[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println();
        System.out.println();
    }

    public static void determinante(int n,int[][] m1,int[][] m2){
        int det1, det2;
        if(n>3){
            System.out.println("A ser implementado acima de 3 dimensões.");
            System.out.println();
        }
        if(n == 1){
            System.out.println("Determinante da matriz 1: "+ m1[0][0]);
            System.out.println("Determinante da matriz 2: "+ m2[0][0]);
            System.out.println();
        } else if (n == 2) {
            det1 = (m1[0][0] * m1[1][1]) - (m1[0][1] * m1[1][0]);
            det2 = (m2[0][0] * m2[1][1]) - (m2[0][1] * m2[1][0]);
            System.out.println("Determinante da matriz 1: "+ det1);
            System.out.println("Determinante da matriz 2: "+ det2);
            System.out.println();
        } else if (n == 3) {
            det1 = m1[0][0]*m1[1][1]*m1[2][2];
            det1 += m1[0][1]*m1[1][2]*m1[2][0];
            det1 += m1[0][2]*m1[1][0]*m1[2][1];
            det1 -= m1[0][2]*m1[1][1]*m1[2][0];
            det1 -= m1[1][2]*m1[2][1]*m1[0][0];
            det1 -= m1[2][2]*m1[0][1]*m1[1][0];
            System.out.println("Determinante da matriz 1: "+ det1);
            System.out.println();
            det2 = m2[0][0]*m2[1][1]*m2[2][2];
            det2 += m2[0][1]*m2[1][2]*m2[2][0];
            det2 += m2[0][2]*m2[1][0]*m2[2][1];
            det2 -= m2[0][2]*m2[1][1]*m2[2][0];
            det2 -= m2[1][2]*m2[2][1]*m2[0][0];
            det2 -= m2[2][2]*m2[0][1]*m2[1][0];
            System.out.println();
            System.out.println("\nDeterminante da matriz 2: "+ det2);
            System.out.println();
        }
    }


    public static void somaMaior(int n,int[][] m1,int[][] m2){
        //Soma de Matrizes
        int aux1 = 0 , aux2 = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                aux1 += m1[i][j];
                aux2 += m2[i][j];
            }
        }

        if(aux1 == aux2){
            System.out.println("a soma das matrizes é igual.");
            System.out.println();
        }else {
            String s = aux1 > aux2 ? "A matriz um é maior\nSoma da matriz 1: "+ aux1+"\nSoma da matriz 2: " + aux2 :
                    "A matriz dois é maior\nSoma da matriz 2: "+ aux2+"\nSoma da matriz 1: " + aux1;
            System.out.println(s);
            System.out.println();
        }
    }

    public static void printarMatrizes(int n,int[][] m1,int[][] m2){
        System.out.println("Escolha uma opção: ");
        System.out.println("1 - printar matriz 1");
        System.out.println("2 - printar matriz 2");
        System.out.println("3 - printar as duas matrizes");
        Scanner scanner = new Scanner(System.in);
        int aux = scanner.nextInt();
        switch (aux){
            case 1:
                System.out.println("Matriz 1: ");
                printar(n, m1);
                break;
            case 2:
                System.out.println("Matriz 2: ");
                printar(n, m2);
                break;
            case 3:
                System.out.println("Matriz 1:");
                printar(n, m1);
                System.out.println("\nMatriz 2:");
                printar(n, m2);
                break;
            default:
                System.out.println("Opção inválida.");
        }
    }

    public static void printar(int n, int[][] matriz){
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }

}
