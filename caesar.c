#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage; ./caesar key\n");
        return 1;
    }

    for (int i = 0;i<strlen(argv[1]);i++)
    {
        if(!isdigit(argv[1][i]))
        {
            printf("Usaga: ./caesar key\n");
            return 1;
        }
    }
        int k = atoi(argv[1]);

    string plaintext = get_string("Plaintext: ");
    printf("Ciphertext: ");

    for (int x = 0; x<strlen(plaintext);x++)
    {
        if (isupper(plaintext[x]))
        {
            printf("%c",(plaintext[x]-65 + k)%26+65);
        }
        else if(islower(plaintext[x]))
        {
            printf("%c",(plaintext[x]-97 + k)%26+97);
        }
        else
        {
            printf("%c",plaintext[x]);
        }

    }
    printf("\n");

    }



