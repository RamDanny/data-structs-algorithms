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
	int shmid = shmget(111, 100, IPC_CREAT | 00666);
	char *mem = shmat(shmid, NULL, 0);
	char text[100];
	
	// Server only code
	// Control comes after client starts convo
	do
	{
		strcpy(text, mem);
		text[strlen(mem)-1] = '\0';
		printf("Client] %s\n", text);
		printf("Server] ");
		gets(text);
		strcpy(mem, text);
		strcat(mem, "c");
		// control goes to client
		while (mem[strlen(mem)-1] == 'c');
	} while (mem[strlen(mem)-1] == 's' || mem[strlen(mem)-1] == 'c');
	
	shmdt(mem);
	shmctl(shmid, IPC_RMID, NULL);
	// Control goes back to client
}

