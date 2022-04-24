# include <stdio.h>
# include <string.h>
# include <unistd.h>
# include <sys/wait.h>
# include <dirent.h>
# include <fcntl.h>
# include <limits.h>

int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		printf("ERROR: Enter only 1 argument\n");
		return 0;
	}
	
	DIR *dirptr = opendir(argv[1]);
	if (dirptr == NULL)
	{
		printf("ERROR: Directory cannot be accessed\n");
		return 0;
	}
	
	struct dirent *direntry = readdir(dirptr);
	while (direntry != NULL)
	{
		printf("%s\n", direntry->d_name);
		direntry = readdir(dirptr);
	}
	
	if (closedir(dirptr) == -1)
	{
		printf("ERROR: Directory cannot be closed\n");
		return 0;
	}
	
	return 0;
}

