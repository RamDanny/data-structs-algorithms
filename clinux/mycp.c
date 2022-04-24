# include <stdio.h>
# include <string.h>
# include <unistd.h>
# include <sys/wait.h>
# include <dirent.h>
# include <fcntl.h>
# include <limits.h>

int main(int argc, char *argv[])
{
	if (argc != 3)
	{
		printf("ERROR: Enter only 2 arguments\n");
		return 0;
	}
	
	int sourcefd = open(argv[1], O_RDONLY);
	if (sourcefd == -1)
	{
		printf("ERROR: Failed to open source file\n");
		return 0;
	}
	
	char fildata[100];
	if (read(sourcefd, fildata, 100) == -1)
	{
		printf("ERROR: Failed to read source file\n");
		return 0;
	}
	
	int targetfd = open(argv[2], O_WRONLY | O_CREAT, S_IRWXU);
	if (targetfd == -1)
	{
		printf("ERROR: Failed to open target file\n");
		return 0;
	}
	
	if (write(targetfd, fildata, strlen(fildata)) == -1)
	{
		printf("ERROR: Failed to write into target file\n");
		return 0;
	}
	printf("Copied!\n");
	
	if (close(targetfd) == -1)
	{
		printf("ERROR: Failed to close target file\n");
		return 0;
	}
	
	if (close(sourcefd) == -1)
	{
		printf("ERROR: Failed to close source file\n");
		return 0;
	}
	return 0;
}

/*for (int i = 0; i < 100; i++)
	{
		printf("%c", fildata[i]);
		printf("\n");
	}*/
	
