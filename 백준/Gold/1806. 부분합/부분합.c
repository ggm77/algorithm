#include <stdio.h>

int main() {
    int i, j;

    int arr[100000];
    int n, s;
    int start, sum;
    int min = 100001;

    scanf("%d %d", &n, &s);

    for(i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }

    start = 0;
    sum = 0;
    for(i = 0; i < n; i++){
        sum += arr[i];
        if(s <= sum){
            for(j = start; j <= i; j++){
                if(sum < s){
                    break;
                }
                if(i-start+1 < min){
                    min = i-start+1;
                }
                sum -= arr[j];
                start += 1;
            }
            
        }
    }

    if(min == 100001){
        printf("0");
        return 0;
    }

    printf("%d", min);

    return 0;
}