#include <stdio.h>

// 돌다리 개수
int n;
// 돌다리
int arr[100000] = {0,};

// 방문 저장용
int visited[100000] = {0,};

// 결과
int result = 0;

void dfs(int here) {

    // 방문한적 있으면 종료
    if(visited[here]){
        return ;
    }

    // 방문 했다고 저장
    result += 1;
    visited[here] = 1;

    // 앞으로 이동
    if(here + arr[here] < n) {
        dfs(here+arr[here]);
    }

    // 뒤로 이동
    if(here - arr[here] >= 0) {
        dfs(here-arr[here]);
    }
}

int main() {

    int s, i;

    scanf("%d", &n);
    for(i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    scanf("%d", &s);

    dfs(s-1);

    printf("%d", result);

    return 0;
}