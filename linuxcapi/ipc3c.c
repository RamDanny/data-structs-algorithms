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
	int first = 1;
	
	// Client only code
	// control starts at client
	do
	{
		if (first == 0)
		{
			strcpy(text, mem);
			text[strlen(mem)-1] = '\0';
			printf("Server] %s\n", text);
		}
		else
		{
			first = 0;
		}
		printf("Client] ");
		gets(text);
		strcpy(mem, text);
		strcat(mem, "s");
		// control goes to server
		while (mem[strlen(mem)-1] == 's');
	} while (mem[strlen(mem)-1] == 's' || mem[strlen(mem)-1] == 'c');
	
	shmdt(mem);
	shmctl(shmid, IPC_RMID, NULL);
}

