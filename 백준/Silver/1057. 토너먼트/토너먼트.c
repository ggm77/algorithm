#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    int i, j, temp;
    int n, num1, num2;
    int team_count;

    scanf("%d %d %d", &n, &num1, &num2);

    if(num1 > num2){
        temp = num1;
        num1 = num2;
        num2 = temp;
    }
   
    for(i = 1; i < (n/2.0)+1; i++){
        team_count = (int) pow(2, i);
        if(abs(num2-num1) <= team_count){
            for(j = 1; j <= n; j += team_count){
                if(j <= num1 && num2 <= j+team_count-1){
                    printf("%d", i);
                    return 0;
                }
            }
        }
    }

    printf("-1");

    return 0;
}
