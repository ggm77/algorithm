#include <stdio.h>
#include <string.h>

int max(int a, int b){
    if(a > b){
        return a;
    }
    else {
        return b;
    }
}

int main() {

    // i: 이용 가능한 첫 번째 문자열 최대 번호 (1~) j: 두 번째 문자열(1~)
    // max(마지막에 들어온 문자 안쓰기, 마지막에 들어온 문자 쓰기)
    // dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+1)

    int i, j;
    char str1[1001];
    char str2[1001];
    int str1_len, str2_len;
    int dp[1001][1001] = {0,};

    scanf("%s", str1);
    scanf("%s", str2);
    str1_len = strlen(str1);
    str2_len = strlen(str2);
    
    for(i = 1; i < str1_len+1; i++){
        for(j = 1; j < str2_len+1; j++){
            if(str2[j-1] == str1[i-1]){
                dp[i][j] = dp[i-1][j-1]+1;
            }
            else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }

    printf("%d", dp[str1_len][str2_len]);

    return 0;
}