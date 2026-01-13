#include <stdio.h>

int main() {
    int i;
    char ans[3][17] = {"advertise", "does not matter", "do not advertise"};
    int n, r, e, c;

    scanf("%d", &n);

    for(i = 0; i < n; i++){
        scanf("%d %d %d", &r, &e, &c);

        if(r < e-c){
            printf("%s\n", ans[0]);
        }
        else if(r == e-c){
            printf("%s\n", ans[1]);
        }
        else {
            printf("%s\n", ans[2]);
        }
    }


    return 0;
}