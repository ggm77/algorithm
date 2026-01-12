#include <stdio.h>

// r = h1 - h2
void subtraction(
    int h1, int m1, int s1,
    int h2, int m2, int s2,
    int *r_h, int *r_m, int *r_s
) {
    *r_s = s1 - s2;
    if(*r_s < 0){
        *r_s += 60;
        m2 += 1;
    }

    *r_m = m1 - m2;
    if(*r_m < 0){
        *r_m += 60;
        h2 += 1;
    }

    *r_h = h1 - h2;
    if(*r_h < 0){
        *r_h += 24;
    }
}

int main() {
    int cur_h,cur_m,cur_s;
    int target_h,target_m,target_s;
    int h,m,s;

    scanf("%d:%d:%d", &cur_h, &cur_m, &cur_s);
    scanf("%d:%d:%d", &target_h, &target_m, &target_s);

    if(
        cur_h < target_h
        || (cur_h == target_h && cur_m < target_m)
        || (cur_h == target_h && cur_m == target_m && cur_s < target_m)
    ) {
        // 목표 - 현재
        subtraction(
            target_h, target_m, target_s,
            cur_h, cur_m, cur_s,
            &h, &m, &s
        );
    }
    else {
        // 24 - (현재 - 목표)
        subtraction(
            cur_h, cur_m, cur_s,
            target_h, target_m, target_s,
            &h, &m, &s
        );

        subtraction(
            24, 0, 0,
            h, m, s,
            &h, &m, &s
        );
    }

    if(h < 10){
        printf("0%d:", h);
    }
    else {
        printf("%d:", h);
    }

    if(m < 10){
        printf("0%d:", m);
    }
    else {
        printf("%d:", m);
    }

    if(s < 10){
        printf("0%d", s);
    }
    else {
        printf("%d", s);
    }

    return 0;
}