#include <stdio.h>

// 컴퓨터의 연결 상태를 저장할 2차원 배열
int computers[100][100] = {0,};

// 방문했는지 저장하는 배열
int visited[100] = {0,};

// 결과 저장용 변수
int result = 0;

void dfs(int here) {
    int i;

    // 방문한적 있으면 바로 종료
    if(visited[here] == 1){
        return ;
    }
    
    // 방문했다고 남기기
    visited[here] = 1;

    // 1번 컴퓨터와 이어져있으니 +1
    result += 1;

    // 연결 된 다음 컴퓨터가 있는지 찾기
    for (i = 0; i < 100; i++){
        // 연결이 되어있다면 함수 호출
        if(computers[here][i] == 1){
            dfs(i);
        }
    }

    return ;
}

int main(){
    
    // 바이러스 걸린 컴퓨터 수, 입력 받을 쌍의 수 저장할 변수
    int total_count, connected_count;
    // 임시 변수
    int i, tmp1, tmp2;

    // 초기 정보 입력
    scanf("%d", &total_count);
    scanf("%d", &connected_count);

    // 연결 정보 입력
    for (i = 0; i < connected_count; i++) {
        scanf("%d %d", &tmp1, &tmp2);
            
        computers[tmp1-1][tmp2-1] = 1;
        computers[tmp2-1][tmp1-1] = 1;
    }

    // 1번 컴퓨터부터 dfs 시작
    dfs(0);

    // 1번 컴퓨터와 연결 된 총 컴퓨터 개수 (문제에서 1번을 제외하라고 해서 -1)
    printf("%d\n", result-1);
    
    return 0;
}