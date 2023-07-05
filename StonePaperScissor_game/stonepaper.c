#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>

void br(int len){ // DECOREATION
    printf("\n");
    for (int i = 0; i< len; i++) printf("- ");
    printf("\n");
}

int randomNogenerator(int a)
{
    srand(time(NULL));
    return rand() % a;
}

int playerSelect(){
    int tries = 0;
    int selected = -1;

    while(tries < 3){
        printf("\t Select 0 for Rock\n\t\t1 for Paper\n\t\t2 for Scissors");
        printf("\n >>> ");
        scanf("%d", &selected);
        if ((selected == 0) || (selected == 1) || (selected == 2)) break;
        tries++;
        selected = -1;
        printf("\nINCORRECT CHOICE, TRY AGAIN\n");
    }
    return selected;
}

int computerSelect(){
    int c = randomNogenerator(3);
    switch (c)
        {
        case 0:
            printf("Computer selected: Rock\n\n");
            break;
        case 1:
            printf("Computer selected: Paper\n\n");
            break;
        case 2:
            printf("Computer selected: Scissors\n\n");
            break;
        }
    return c;
}

int decide(int player, int computer){
    // 0 - ROCK
    // 1 - PAPER
    // 2 - SCISSORS

    // WINNING CONDITIONS
    // 0 > 2
    // 1 > 0
    // 2 > 1

    // RETURNING  0 - IF DRAW
    //           -1 - IF PLAYER WIN 
    //            1 - IF COMPUTER WIN

    if (player == computer) return 0;
    if (player-computer > 0) return -1;
    else return 1;
}

int main()
{
    int playerscore = 0, compscore = 0;
    int tries, playerChoice, computerChoice;

    for (int i = 1; i < 4; i++)
    {
        br(50);
        br(50);
        printf("Round %d :\n", i);
        tries = 0;
        playerChoice = -1;
        computerChoice = -1;
        
        while(tries < 3){
            printf("Player turn:\n");
            playerChoice = playerSelect();

            if (playerChoice == -1){
                char choices = 'y';

                if(tries == 2) {
                    printf("Exiting ... ");
                    return 0;
                }
                printf("Incorrect choice, Want to exit ? (Y/N) : ");
                fflush(stdin);                                        // char - int ya int char jaisa input lene ke baad 
                                                                      // kuch gadbad hota h C me ... So fflush() se input saaf karte h 
                scanf("%c", &choices);
                if (tolower(choices) == 'y') return 0;
                tries++;
                
            }
            else break;
        }

        printf("Player selected : %d", playerChoice); // 0 - ROCK
                                                      // 1 - PAPER
                                                      // 2 - SCISSORS

        printf("\nComputer turn:\n");
        computerChoice = computerSelect();

        int decidd = decide(playerChoice, computerChoice);
        if (!(decidd)) printf("****Match is draw****\n\n");
        else if (decidd < 0){
            printf("****Player won this round****\n\n");
            playerscore = playerscore + 1;
        }
        else{
            printf("****Computer won this round****\n\n");
            compscore = compscore + 1;
        }

        printf("\nPlayer's score: %d and Computer's score: %d\n", playerscore, compscore);
    }
    br(0);
    br(50);
    printf("\n\t====== RESULT =======\n");
    if (playerscore > compscore)
    {
        printf("***** The Winner is 'PLAYER' with %d points while Computer's points is %d *****\n", playerscore, compscore);
    }
    else if (playerscore == compscore)
    {
        printf(" There is DRAW between player and Computer as:\n Players's points is %d\n Computer's points is %d\n", playerscore, compscore);
    }
    else
    {
        printf("***** The Winner is 'COMPUTER' with %d points while Players's points is %d *****\n", compscore, playerscore);
    }

    return 0;
}