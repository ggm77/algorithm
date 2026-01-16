#include <stdio.h>

// 마지막
// 점화식 = max(마지막 값 미사용, 마지막 값 사용)
// dp[수열길이][최대값]
// dp[i][j] = max(dp[i-1][j], dp[i-1][마지막 값-1]+1)

int max(int a, int b){
    if(a > b){
        return a;
    }
    else {
        return b;
    }
}

int main() {
    int i, j;
    int n;
    int arr[1001];
    int dp[1001][1001];
    int max_val;

    scanf("%d", &n);

    max_val = -1;
    for(i = 0; i < n; i++){
        scanf("%d", &arr[i]);
        if(max_val < arr[i]){
            max_val = arr[i];
        }
    }

    for(i = 1; i < n+1; i++){
        for(j = 1; j < max_val+1; j++){
            if(arr[i-1] <= j){
                dp[i][j] = max(dp[i-1][j], dp[i-1][arr[i-1]-1]+1);
            }
            else {
                dp[i][j] = dp[i-1][j];
            }
            
        }
    }

    printf("%d", dp[n][max_val]);

    return 0;
}