#include <stdio.h>

// a, b, c에 들어갈 수 있는 최대 용량 변수
int max_a, max_b, max_c;

// 방문 했는지 저장용
int visited[201][201]= {0,};

// 결과 저장용
int result[200] = {0,};
int result_count = 0;

void dfs(int a, int b, int c) {
    
    int i;

    // 방문한적 있으면 종료
    if(visited[a][b] == 1){
        return ;
    }

    // 방문했다고 저장
    visited[a][b] = 1;

    // a 물병 비어있으면 결과에 저장
    if (a == 0) {
        result[result_count++] = c;
    }

    if(a != 0){
        // a를 b로
        if(max_b-b < a) {
            dfs(a-(max_b-b), max_b, c);
        } else {
            dfs(0, b+a, c);
        }
        // a를 c로
        if(max_c-c < a) {
            dfs(a-(max_c-c), b, max_c);
        } else {
            dfs(0, b, c+a);
        }
    }

    if(b != 0){
        // b를 a로
        if(max_a-a < b) {
            dfs(max_a, b-(max_a-a), c);
        } else {
            dfs(a+b, 0, c);
        }
        // b를 c로
        if(max_c-c < b) {
            dfs(a, b-(max_c-c), max_c);
        } else {
            dfs(a, 0, c+b);
        }
    }

    if(c != 0){
        // c를 a로
        if(max_a-a < c) {
            dfs(max_a, b, c-(max_a-a));
        } else {
            dfs(a+c, b, 0);
        }
        // c를 b로
        if(max_b-b < c) {
            dfs(a, max_b, c-(max_b-b));
        } else {
            dfs(a, b+c, 0);
        }
    }
}

int main() {
    int temp, i, j;

    scanf("%d %d %d", &max_a, &max_b, &max_c);

    dfs(0, 0, max_c);

    // 오름차순 정렬 및 출력
    for(i = 0; i < result_count; i++){
        for(j = result_count-1; j > i; j--){
            if(result[i] > result[j]){
                temp = result[j];
                result[j] = result[i];
                result[i] = temp;
            }
        }
        printf("%d ", result[i]);
    }

    return 0;
}