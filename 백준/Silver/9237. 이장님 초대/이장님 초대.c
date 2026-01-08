#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b){

    // a, b를 int 포인터로 캐스팅 하고 값 가져오기
    int num1 = *(int*) a;
    int num2 = *(int*) b;

    if (num1 < num2) {
        return 1; 
    }
    if (num2 < num1) {
        return -1;
    }
    return 0;
}

int main() {

    int i;
    // 묘목 수
    int n;
    // 자라는데 걸리는 시간 배열
    int arr[100000];

    // 최댓값
    int max = -1;

    // n입력
    scanf("%d", &n);
    
    // 걸리는 시간 입력과 동시에 제일 오래걸리는 시간, 제일 적게 시간 저장
    for(i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // 내림차순 정렬
    qsort(arr, n, sizeof(int), compare);

    // (묘목 자라는데 걸리는 시간 + 묘목을 심은날 + 묘목을 심는데 걸린시간)으로 배열에 저장
    // 동시에 그 최댓값 구하기
    for(i = 0; i < n; i++){
        arr[i] += i+2;

        if(arr[i] > max){
            max = arr[i];
        }
    }

    // 최댓값 구하기
    printf("%d", max);

    return 0;
}