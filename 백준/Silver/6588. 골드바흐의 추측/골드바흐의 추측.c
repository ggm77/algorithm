#include <stdio.h>

int main() {
    int i ,j;
    int input[100000];
    int temp, max, input_len;
    int prime[1000001] = {0,};

    input_len = 0;
    max = 0;
    while(1){
        scanf("%d", &temp);
        if(temp == 0){
            break;
        }

        input[input_len++] = temp;
        if(max < temp){
            max = temp;
        }
    }

    for(i = 2; i < max; i++){
        if(prime[i] != 1){
            for(j = 2; j < max/i+1; j++){
                if(i*j < max){
                    prime[i*j] = 1;
                }
            }
        }
    }

    for(i = 0; i < input_len; i++){
        for(j = input[i]; j >= 2; j--){
            if(prime[j] == 0 && input[i]-j > 1 && prime[input[i]-j] == 0){
                printf("%d = %d + %d\n", input[i], input[i]-j, j);
                break;
            }
        }
        if(j == 1){
            printf("Goldbach's conjecture is wrong.\n");
        }
    }

    return 0;
}