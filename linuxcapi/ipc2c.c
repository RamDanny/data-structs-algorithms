# include <sys/ipc.h>
//# define NULL 0
# include <sys/shm.h>
# include <sys/types.h>
# include <unistd.h>
# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <ctype.h>
# include <sys/wait.h>
# include <stdio_ext.h>
# include <dirent.h>
# include <fcntl.h>
# include <limits.h>

int main() 
{
	int shmid = shmget(111, 50, IPC_CREAT | 00666);
	char *mem = shmat(shmid, NULL, 0);
	char fname[20], fildata[100];
	
	// client only code
	// control starts at client
	printf("Client] Enter file name:");
	gets(fname);
	strcpy(mem, fname);
	strcat(mem, "s");
	// control goes to server
	while (mem[strlen(mem)-1] == 's');
	// control comes back to client
	int f = open(fname, O_RDWR);
	read(f, fildata, 100);
	printf("Client] File data read: %s\n", fildata);
	close(f);
	
	shmdt(mem);
	shmctl(shmid, IPC_RMID, NULL);
}

