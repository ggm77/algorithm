#include <stdio.h>

// dp[최대 코스트][최대 앱 개수] = 메모리
// 점화식 = max(마지막 앱 안 지움, (코스트 보다 작을 때)마지막 앱 지움)
// dp[i][j] = max(dp[i][j-1], dp[i-cost[j]][j-1]+memory[j])

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
    int n, m;
    int memory[100];
    int cost[100];
    int cost_sum = 0;

    int dp[10001][101] = {0,};

    scanf("%d %d", &n, &m);
    for(i = 0; i < n; i++){
        scanf("%d", &memory[i]);
    }
    for(i = 0; i < n; i++){
        scanf("%d", &cost[i]);
        cost_sum += cost[i];
    }

    for(i = 0; i < cost_sum+1; i++){
        for(j = 1; j < n+1; j++){
            if(cost[j-1] <= i){
                dp[i][j] = max(dp[i][j-1], dp[i-cost[j-1]][j-1]+memory[j-1]);
            }
            else{
                dp[i][j] = dp[i][j-1];
            }
        }
    }

    for(i = 0; i < cost_sum+1; i++){
        if(m <= dp[i][n]){
            printf("%d", i);
            return 0;
        }
    }

    return 0;
}