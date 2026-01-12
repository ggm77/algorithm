#include <stdio.h>

int main() {
    int i;
    int t, n;
    int index;

    scanf("%d", &t);

    for(i = 0; i < t; i++){
        index = 0;
        scanf("%d", &n);

        while(n != 0){
            if(n%2 != 0){
                printf("%d ", index);
            }
            n = n >> 1;
            index += 1;
        }
    }

    return 0;
}