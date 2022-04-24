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
	
	int sourcefd = open(argv[2], O_RDONLY);
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
	
	char *pattern = argv[1];
	int linelist[100];
	int lines = 1;
	linelist[0] = -1;
	for (int i = 0; i < strlen(fildata); i++)
	{
		if (fildata[i] == '\n')
		{
			linelist[lines++] = i;
		}
		printf("%c", fildata[i]);
	}
	printf("\n");
	printf("lines = %d\n", lines);
	
	if (close(sourcefd) == -1)
	{
		printf("ERROR: Failed to close source file\n");
		return 0;
	}
	return 0;
}


