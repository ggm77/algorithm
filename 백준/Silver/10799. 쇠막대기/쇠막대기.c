#include <stdio.h>
#include <string.h>

int main() {

    int i;
    char s[100000];
    int len, open, result;

    scanf("%s", s);
    len = strlen(s);

    open = 0;
    result = 0;

    for(i = 0; i < len; i++){

        if(s[i] == '('){
            if(i+1 < len && s[i+1] == ')'){
                result += open;
                i++;
            }
            else {
                open += 1;
            }
        }
        else {
            open -= 1;
            result += 1;
        }


    }

    printf("%d", result);

    return 0;
}