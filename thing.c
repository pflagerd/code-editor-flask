#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char** argv) {

    int fd = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd < 0) {
        return 1;
    }

    // Save original stdout
    int saved_stdout = dup(STDOUT_FILENO);

    dup2(fd, STDOUT_FILENO);

    system("ls");

    dup2(saved_stdout, STDOUT_FILENO);

    close(fd);
    close(saved_stdout);

}
