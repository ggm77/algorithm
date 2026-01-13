#include <stdio.h>
#include <string.h>

int main() {
    int i, j, k;
    int n;
    char in[1000][9];
    char out[1000][9];
    int result = 0;
    int index = 0;
    int count = 0;

    scanf("%d", &n);

    for(i = 0; i < n; i++){
        scanf("%s", in[i]);
    }

    for(i = 0; i < n; i++){
        scanf("%s", out[i]);
    }

    // 출구로 나온 차들 목록 조사
    for(i = 0; i < n; i++){
        if(strcmp(in[index], out[i]) == 0){
            result = i - count;

            // 그 다음으로 들어온 추월하지 않은 자동차 찾기
            for(j = index+1; j < n; j++){
                if(i+1 < n){
                    for(k = i+1; k < n; k++){
                        if(strcmp(out[k], in[j]) == 0){
                            index = j;
                            count += 1;
                            break;
                        }
                    }
                    if(k != n){
                        break;
                    }
                }
            }
        }
    }

    printf("%d", result);

    return 0;
}