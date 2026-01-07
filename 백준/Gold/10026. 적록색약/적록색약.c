#include <stdio.h>

int n;
int arr[100][100] = {0,};

int visited[100][100] = {0,};

void dfs(int x, int y) {

    // 방문한적 있으면 종료
    if(visited[x][y] == 1){
        return ;
    }

    // 방문 저장
    visited[x][y] = 1;

    // 상하 좌우 방문
    if(x-1 >= 0){
        if(arr[x-1][y] == arr[x][y]){
            dfs(x-1, y);
        }
    }
    if(x+1 < n){
        if(arr[x+1][y] == arr[x][y]){
            dfs(x+1, y);
        }
    }
    if(y-1 >= 0){
        if(arr[x][y-1] == arr[x][y]){
            dfs(x, y-1);
        }
    }
    if(y+1 < n){
        if(arr[x][y+1] == arr[x][y]){
            dfs(x, y+1);
        }
    }
}

int main() {
    int i, j, result, previous;
    char temp;

    scanf("%d", &n);

    for(i = 0; i < n; i++){
        for(j = 0; j < n; j++){
            scanf(" %c", &temp);

            if(temp == 'R'){
                arr[i][j] = -1;
            }
            if(temp == 'G'){
                arr[i][j] = 0;
            }
            if(temp == 'B'){
                arr[i][j] = 1;
            }
        }
    }

    // 적록색약 x
    result = 0;
    for(i = 0; i < n; i++){
        for(j = 0; j < n; j++){
            if(visited[i][j] == 0){
                result += 1;
                dfs(i, j);
            }
        }
    }
    printf("%d ", result);

    // 방문한 기록 초기화 & 빨간색을 초록색으로 합치기
    for(i = 0; i < n; i++){
        for(j = 0; j < n; j++){
            if(arr[i][j] == -1){
                arr[i][j] = 0;
            }
            visited[i][j] = 0;
        }
    }

    // 적록색약 o
    result = 0;
    for(i = 0; i < n; i++){
        for(j = 0; j < n; j++){
            if(visited[i][j] == 0){
                result += 1;
                dfs(i, j);
            }
        }
    }
    printf("%d", result);

    return 0;
}