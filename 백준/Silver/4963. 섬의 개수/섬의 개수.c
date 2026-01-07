#include <stdio.h>

// 지도
int w, h;
int map[50][50];

// 방문 내역
int visited[50][50];

// 섬 개수 저장용
int result;

void dfs(int x, int y){
    // 방문한적 있으면 종료
    if(visited[x][y] == 1){
        return ;
    }

    // 방문 했다고 저장
    visited[x][y] = 1;

    // 방문한 장소가 바다면 종료
    if(map[x][y] == 0){
        return ;
    }

    // 가로, 세로, 대각선 방문
    if(x-1 >= 0){
        dfs(x-1, y);
        if(y+1 < w){
            dfs(x-1, y+1);
        }
    }
    if(x+1 < h){
        dfs(x+1, y);
        if(y-1 >= 0){
            dfs(x+1, y-1);
        }
    }
    if(y-1 >= 0){
        dfs(x, y-1);
        if(x-1 >= 0){
            dfs(x-1, y-1);
        }
    }
    if(y+1 < w){
        dfs(x, y+1);
        if(x+1 < h){
            dfs(x+1, y+1);
        }
    }

}

// dfs로 섬 개수 세는 함수
int count_islands(){
    int i, j;

    // 지도를 쭉 돌면서 섬을 만나면 dfs
    result = 0;
    for(i = 0; i < h; i++){
        for(j = 0; j < w; j++){
            if(map[i][j] == 1 && visited[i][j] == 0){
                result += 1;
                dfs(i, j);
            }
        }
    }

    return result;
}

int main() {
    int i, j;

    while(1) {
        scanf("%d %d", &w, &h);

        if(w == 0 && h == 0){
            break;
        }

        // 지도 입력
        for(i = 0; i < h; i++){
            for(j = 0; j < w; j++){
                // 이전에 방문 했던 내용 초기화
                visited[i][j] = 0;

                scanf("%d", &map[i][j]);
            }
        }

        printf("%d\n", count_islands());

    }

    return 0;
}