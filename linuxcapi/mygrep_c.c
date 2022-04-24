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
	char line[100];
	int lines = 0, k = 0;
	int matchct = 0;
	for (int i = 0; i < strlen(fildata); i++)
	{
		if (fildata[i] == '\n')
		{
			lines++;
			line[k++] = '\0';
			char *pos = strstr(line, pattern);
			if (pos != NULL)
			{
				matchct++;
			}
			k = 0;
			continue;
		}
		line[k++] = fildata[i];
	}
	printf("%d\n", matchct);
	
	if (close(sourcefd) == -1)
	{
		printf("ERROR: Failed to close source file\n");
		return 0;
	}
	return 0;
}


