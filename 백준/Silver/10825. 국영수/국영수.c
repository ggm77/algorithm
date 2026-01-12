#include <stdio.h>
#include <stdlib.h>

typedef struct Data {
    char name[11];
    int voca;
    int english;
    int math;
} Data;

struct Data data[100000];
int n;

int compare(const void *a, const void *b){
    int i;

    Data* data1 = (Data*) a;
    Data* data2 = (Data*) b;

    if(data1->voca > data2->voca){
        return -1;
    }
    else if(data1->voca < data2->voca){
        return 1;
    }


    if(data1->english < data2->english){
        return -1;
    }
    else if(data1->english > data2->english){
        return 1;
    }

    if(data1->math > data2->math){
        return -1;
    }
    else if(data1->math < data2->math){
        return 1;
    }

    // 이름 비교
    for(i = 0; i < 10; i++){
        if(data1->name[i] < data2->name[i]){
            return -1;
        }
        if(data1->name[i] > data2->name[i]){
            return 1;
        }
    }

    return 0;
}

int main() {
    int i;
    
    scanf("%d", &n);

    for(i = 0; i < n; i++){
        scanf("%s %d %d %d", data[i].name, &data[i].voca, &data[i].english, &data[i].math);
    }

    qsort(data, n, sizeof(Data), compare);

    for(i = 0; i < n; i++){
        printf("%s\n", data[i].name);
    }

    return 0;
}