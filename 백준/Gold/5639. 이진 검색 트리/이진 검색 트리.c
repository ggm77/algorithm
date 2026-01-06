#include <stdio.h>

int arr[10000] = {0,};
int arr_len = 0;

void print_by_postorder(int start_index, int end_index) {
    int i;

    if(start_index > end_index) {
        return;
    }

    for (i = start_index; i <= end_index; i++) {
        if(arr[start_index] < arr[i]){
            break;
        }
    }

    print_by_postorder(start_index+1, i-1);
    print_by_postorder(i, end_index);

    printf("%d\n", arr[start_index]);

    return ;
}

int main() {
    int i, inp, reverse_index;

    // 입력 받기
    while (scanf("%d", &inp) != EOF) {
        arr[arr_len++] = inp;
    }
    
    print_by_postorder(0, arr_len-1);

    return 0;
}