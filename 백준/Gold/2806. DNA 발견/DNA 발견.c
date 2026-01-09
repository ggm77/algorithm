#include <stdio.h>

// 입력 저장용 변수
int arr[1000000];
int n;

//DP 저장용 dp[type][N]
int dp[2][1000000];

// 최솟값 구하는 함수
int min(int a, int b){
    if(a < b){
        return a;
    }
    else {
        return b;
    }
}

//DP 이용해서 최솟값 구하기
void find(int here) {

    if(here == 0){
        if(arr[0] == 0){
            dp[0][0] = 0;
            dp[1][0] = 1;
            return ;
        }
        if(arr[0] == 1){
            dp[0][0] = 1;
            dp[1][0] = 0;

            return ;
        }
    }

    // here가 A일 때
    if(arr[here] == 0) {
        // 그대로 / 전체 반전
        dp[0][here] = min(dp[0][here-1], dp[1][here-1]+1);
        // N-1까지 반전+마지막 요소 바꾸기 / 마지막 요소 바꾸기
        dp[1][here] = min(dp[0][here-1]+2, dp[1][here-1]+1);
    }
    // here가 B일 때
    else {
        // 마지막 요소 반전 / 전체 반전
        dp[0][here] = min(dp[0][here-1]+1, dp[1][here-1]+1);
        // N-1반전 / 그대로
        dp[1][here] = min(dp[0][here-1]+1, dp[1][here-1]);
    }

    return ;
}

int main() {

    int i;
    char temp;

    // n입력
    scanf("%d", &n);
    
    // DNA를 정수로 배열에 저장
    for(i = 0; i < n; i++){
        scanf(" %c", &temp);
        if(temp == 'A'){
            arr[i] = 0;
        }
        if(temp == 'B'){
            arr[i] = 1;
        }

        //DP 진행
        find(i);
    }

    // DP 결과 읽어서 (전부 A인 경우)와 (전부 B인 경우+전체 반전) 중에 최솟값 출력
    printf("%d", min(dp[0][n-1], dp[1][n-1]+1));

    return 0;
}