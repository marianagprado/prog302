#include <math.h>
#include <stdio.h>

int main()
{
    int a, b, c, delta, raiz1, raiz2;
    printf("Valor de a:");
    scanf("%d", &a);
    printf("Valor de b:");
    scanf("%d", &b);
    printf("Valor de c:");
    scanf("%d", &c);
    delta = pow(b,2) - ((4)*(a)*(c));
    
    if (delta < 0){
        printf("não possui raizes reais");
    }
    else if (delta == 0){
        printf("possui apenas uma raiz real \n");
        raiz1 = (-1)*(b) +  (sqrt(delta) / (2*a));
        printf("raiz: %d", raiz1);
    }
    else{
        printf("possui duas raizes reais \n");
        raiz1 = ((-1)*(b) +  sqrt(delta)) / (2*a);
        raiz2 = ((-1)*(b) -  sqrt(delta)) / (2*a);
        printf("raiz positiva: %d, raiz negativa: %d", raiz1, raiz2);
    }

    return 0;
}