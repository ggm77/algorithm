#include <stdio.h>
#include <stdbool.h>
int main(){
    int arr[8];
    bool ascending = true;
    bool descending = true;
    
    for (int i = 0; i < 8; i++){
        scanf("%d",&arr[i]);
    }
    
    for (int i = 0; i < 8; i++){
        if (arr[i] != i+1){
            ascending = false;
        }
        if (arr[i] != 8-i){
            descending = false;
        }
    }
    if (ascending){
        printf("ascending\n");
    }
    else if (descending){
        printf("descending\n");
    }
    else{
        printf("mixed\n");
    }
    return 0;
}