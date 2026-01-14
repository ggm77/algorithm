#include <stdio.h>

int main() {
    char s[101];
    int i;

    i = 0;
    while(scanf("%c", &s[i]) != EOF){
        i++;
    }

    s[i] = '\0';

    for(i = 0; i < 101; i++){
        if(s[i] == '\0'){
            break;
        }

        if(64 < s[i] && s[i] < 78){
            printf("%c", s[i]+13);
        }
        else if(77 < s[i] && s[i] < 91){
            printf("%c", 64+(s[i]+13-90));
        }
        else if(96 < s[i] && s[i] < 110){
            printf("%c", s[i]+13);
        }
        else if(109 < s[i] && s[i] < 123){
            printf("%c", 96+(s[i]+13-122));
        }
        else {
            printf("%c", s[i]);
        }
    }

    return 0;
}