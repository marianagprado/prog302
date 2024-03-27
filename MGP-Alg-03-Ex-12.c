#include <stdio.h>

int main()
{
    int ano;
    printf("Digite um ano:");
    scanf("%d", &ano);
    if (ano%400==0){
        printf("Bissexto");
    }
    else if (ano%100==0){
        printf("Não é bissexto");
    }
    else if (ano%4==0){
        printf("Bissexto");
    }
    else{
        printf("Não é bissexto");
    }

    return 0;
}
