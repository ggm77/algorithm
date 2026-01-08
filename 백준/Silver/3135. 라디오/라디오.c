#include <stdio.h>
#include <stdlib.h>

int main() {

    int i;
    // 즐겨찾기 저장용
    int arr[5];
    // 문제에서 정한 변수
    int a, b, n;

    // 목표에 제일 근접한 주파수가 저장된 인덱스
    int close_index;

    // 즐겨찾기와 b의 최소 거리를 저장하는 변수
    int distance;

    // a, b, n 입력
    scanf("%d %d", &a, &b);
    scanf("%d", &n);

    // a와 b의 거리를 미리 저장
    distance = abs(b - a);
    close_index = -1;

    // 즐겨찾기 리스트 입력과 동시에 b와 제일 가까운 값 찾기
    for(i = 0; i < n; i++){
        scanf("%d", &arr[i]);
        
        if(abs(b - arr[i]) < distance){
            close_index = i;
            distance = abs(b - arr[i]);
        }
    }

    // a와 제일 가까우면 두 지점 거리 출력
    if(close_index == -1){
        printf("%d", abs(a-b));
    }
    // 즐겨찾기한 요소가 더 가까우면 그 지점부터 거리+(즐겨찾기 버튼 누르는 1번) 출력
    else {
        printf("%d", abs(arr[close_index] - b)+1);
    }

    return 0;
}