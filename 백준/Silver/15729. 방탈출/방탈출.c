#include <stdio.h>

// 버튼 토글하는 함수
void change(int *num){
    if(*num == 1){
        *num = 0;
    }
    else {
        *num = 1;
    }
}

int main() {
    int i;
    int n; //버튼 개수
    int target[1000000] = {0,}; //정답
    int current[1000000] = {0,}; //현재 상태
    int result = 0; //결과

    // n입력
    scanf("%d", &n);

    // 정답 입력
    for (i = 0; i < n; i++){
        scanf("%d", &target[i]);
    }

    // 그리디로 순차적으로 확인
    for(i = 0; i < n; i++){
        if(target[i] != current[i]){
            result += 1;
            change(&current[i]);
            if(i+1 < n){
                change(&current[i+1]);
            }
            if(i+2 < n){
                change(&current[i+2]);
            }
        }
    }

    printf("%d", result);

    return 0;
}