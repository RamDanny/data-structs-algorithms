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
	int i;
	for (i = 0; i < strlen(mem)-1; i++)
	{
		fname[i] = mem[i];
	}
	fname[i] = '\0';
	
	// Server only code
	// Control comes after client gives filename
	int f = open(fname, O_RDWR | O_CREAT, S_IRWXU);
	printf("Server] Enter data to write: ");
	gets(fildata);
	write(f, fildata, strlen(fildata)+1);
	printf("Server] File data written: %s\n", fildata);
	mem[strlen(mem)-1] = 'c';
	close(f);
	
	shmdt(mem);
	shmctl(shmid, IPC_RMID, NULL);
	// Control goes back to client
}

