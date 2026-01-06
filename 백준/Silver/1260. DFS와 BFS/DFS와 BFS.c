#include <stdio.h>

// 결과 저장용 배열
int dfs_result[1000] = {0,};
int bfs_result[1000] = {0,};
int dfs_count = 0;
int bfs_count = 0;

// 그래프 저장용 배열
int arr[1000][1000] = {0,};

// dfs 방문 저장용 배열
int dfs_visited[1000] = {0,};

// bfs 방문 저장용 배열
int bfs_visited[1000] = {0,};

// bfs 큐
int queue[10000] = {0,};
int queue_count = 0;
int queue_cursor = 0;
int queue_len = 0;

// dfs
void dfs(int here){
    int i;

    // 방문한적 있으면 종료
    if(dfs_visited[here] == 1) {
        return ;
    }

    // 방문했다고 저장
    dfs_visited[here] = 1;

    // 결과에 추가
    dfs_result[dfs_count++] = here+1;

    // 연결 된게 있는지 찾기
    for (i = 0; i < 1000; i++) {
        // 연결 된게 있으면 함수 호출
        if(arr[here][i] == 1) {
            dfs(i);
        }
    }

    return ;
}

// bfs
void bfs(int here){
    int i;
    int val;

    // 방문 했다고 저장
    bfs_visited[here] = 1;

    // 큐에 추가
    queue[queue_count++] = here;
    queue_len += 1;

    while (queue_len > 0) {
        // 큐에서 요소 하나 추출
        val = queue[queue_cursor++];
        queue_len -= 1;

        bfs_result[bfs_count++] = val+1;

        for (i = 0; i < 1000; i++) {
            // 현재 노드와 연결 되어있고, 방문한적이 없을 때
            if(arr[val][i] == 1 && bfs_visited[i] == 0) {
                // 방문 했다고 표시
                bfs_visited[i] = 1;

                // 큐에 추가
                queue[queue_count++] = i;
                queue_len += 1;
            }
        }
    }

    
}

int main(){
    // 문제의 변수
    int n, m, v;

    // 임시 변수
    int i, tmp1, tmp2;

    // n, m, v 입력
    scanf("%d %d %d", &n, &m, &v);

    // 그래프 입력
    for (i = 0; i < m; i++) {
        scanf("%d %d", &tmp1, &tmp2);

        arr[tmp1-1][tmp2-1] = 1;
        arr[tmp2-1][tmp1-1] = 1;
    }

    // dfs 실행
    dfs(v-1);

    // bfs 실행
    bfs(v-1);

    // dfs 결과 출력
    for (i = 0; i < 1000; i++) {
        if(dfs_result[i] != 0) {
            printf("%d ", dfs_result[i]);
        }
    }
    printf("\n");

    // bfs 결과 출력
    for (i = 0; i < 1000; i++) {
        if(bfs_result[i] != 0) {
            printf("%d ", bfs_result[i]);
        }
    }
    printf("\n");
}