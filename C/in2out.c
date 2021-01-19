/*getchar() : is a library function that reads the next input character and returns that as its value.

c = getchar();  The variable c contains the next character of the input


putchar() : is a library function that prints a character each time that is called. */

#include <stdio.h>

void main(){
    int c;
    c = getchar();     
    while(c!=EOF){
        putchar(c);
        c = getchar();
    }
}


//The below is another method where we give the character input directly at the while loop

/*
#include <stdio.h>

void main(void){
    int c;
    while((c = getchar()!=EOF){
        putchar(c);
    }
}

/*
