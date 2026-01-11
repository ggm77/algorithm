#include <stdio.h>

int n;
int cost[1001][3];

int dp[1001][3];

int min(int a, int b){
    if(a < b){
        return a;
    }
    else {
        return b;
    }
}

int main() {
    int i;

    scanf("%d", &n);

    for(i = 1; i < n+1; i++){
        scanf("%d %d %d", &cost[i][0], &cost[i][1], &cost[i][2]);
    }

    dp[1][0] = cost[1][0];
    dp[1][1] = cost[1][1];
    dp[1][2] = cost[1][2];

    for(i = 2; i < n+1; i++){

        dp[i][0] = min(
            dp[i-1][1]+cost[i][0],
            dp[i-1][2]+cost[i][0]
        );

        dp[i][1] = min(
            dp[i-1][0]+cost[i][1],
            dp[i-1][2]+cost[i][1]
        );

        dp[i][2] = min(
            dp[i-1][0]+cost[i][2],
            dp[i-1][1]+cost[i][2]
        );
    }

    printf("%d", min(dp[n][0], min(dp[n][1], dp[n][2])));

    return 0;
}