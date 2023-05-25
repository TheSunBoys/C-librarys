#include <stdlib.h>

void pause_and_clear() {
    #ifdef WIN32 || WIN64
    system("pause")
    system("cls");
    #else
    system("read -p \"Pressione [ENTER] para sair: \" saindo");
    system("clear");
    #endif
}