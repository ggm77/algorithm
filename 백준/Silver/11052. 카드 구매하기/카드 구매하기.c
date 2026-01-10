#include <stdio.h>

int max(int a, int b){
    if(a < b){
        return b;
    }
    else {
        return a;
    }
}

int main() {
    int i, j;
    int n;
    int pack[1001];
    int dp[1001] = {0,};

    scanf("%d", &n);

    for(i = 0; i < n; i++){
        scanf("%d", &pack[i+1]);
    }

    //만들어야하는 카드 개수
    for(i = 1; i <= n; i++){
        // 선택할 수 있는 카드들 중에서 모두 시도
        for(j = 1; j <= i; j++){
            dp[i] = max(dp[i], dp[i-j] + pack[j]);
        }
    }

    printf("%d", dp[n]);

    return 0;
}