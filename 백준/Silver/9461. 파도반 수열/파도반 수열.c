#include <stdio.h>

long long dp[101] = {0,};


long long check(int n){
    int i;

    if(dp[n] != 0){
        return dp[n];
    }

    for(i = 6; i < n+1; i++){
        if(dp[i] == 0){
            dp[i] = dp[i-1] + dp[i-5];
        }
    }

    return dp[n];
}

int main() {
    int i;
    int t, n;

    dp[1] = 1;
    dp[2] = 1;
    dp[3] = 1;
    dp[4] = 2;
    dp[5] = 2;

    scanf("%d", &t);
    for(i = 0; i < t; i++){
        scanf("%d", &n);
        printf("%lld\n", check(n));
    }

    return 0;
}