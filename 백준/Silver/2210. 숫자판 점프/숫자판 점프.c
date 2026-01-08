#include <stdio.h>
#include <string.h>

// 입력 저장용
int arr[5][5];

// 방문한 5단계를 문자열로 저장
char visited[1000000][7];
int visited_len = 0;

// 현재 방문한 기록 저장용
char current[7];

// 결과 저장용
int result = 0;

void dfs(int x, int y, int current_len) {
    int i;

    // 5단계 이상일 때
    if(current_len >= 6){
        // 문자열 마지막에 \0 추가
        current[6] = '\0';
        visited[visited_len][6] = '\0';

        // 저장된 문자열 중에서 겹치는게 있는지 검사
        for(i = 0; i < visited_len; i++){
            // 두 문자열이 같다면 == 만든적이 있으면 즉시 종료
            if(strcmp(visited[i], current) == 0){
                return;
            }
        }
        // 만든적 없으면
        if(i == visited_len){
            // 결과 저장
            result += 1;

            // 방문기록 남기기
            strcpy(visited[visited_len++], current);
        }
        return ;
    }

    // 현재 값 저장
    current[current_len++] = arr[x][y]  + 48;

    // 네 방향 방문
    if(x-1 >= 0){
        dfs(x-1, y, current_len);
    }
    if(x+1 < 5){
        dfs(x+1, y, current_len);
    }
    if(y-1 >= 0){
        dfs(x, y-1, current_len);
    }
    if(y+1 < 5){
        dfs(x, y+1, current_len);
    }
}

int main() {
    int i, j;

    // 입력
    for(i = 0; i < 5; i++){
        for(j = 0; j < 5; j++){
            scanf("%d",&arr[i][j]);
        }
    }

    // 각 위치에서 dfs
    for(i = 0; i < 5; i++){
        for(j = 0; j < 5; j++){
            dfs(i, j, 0);
        }
    }

    printf("%d\n",result);

    return 0;
}