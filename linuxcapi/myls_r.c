# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <unistd.h>
# include <sys/wait.h>
# include <dirent.h>
# include <fcntl.h>
# include <limits.h>
void ls_r(char *path, int tabs);

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
	
	if (closedir(dirptr) == -1)
	{
		printf("ERROR: Directory cannot be closed\n");
		return 0;
	}
	
	ls_r(argv[1], 0);
	
	return 0;
}

void ls_r(char *path, int tabs)
{
	DIR *dir = opendir(path);
	if (dir == NULL)
		return;
	
	struct dirent *entry = readdir(dir);
	while (entry != NULL)
	{
		for (int i = 0; i < tabs; i++)
			printf("\t");
		printf("%s\n", entry->d_name);
		if (entry->d_type == DT_DIR && strcmp(entry->d_name, "..") != 0 && strcmp(entry->d_name, ".") != 0)
		{
			char *newpath = (char *)malloc(( strlen(entry->d_name) + strlen(path) + 10 ) * sizeof(char));
			int i;
			for (i = 0; i < strlen(path); i++)
				newpath[i] = path[i];
			newpath[i++] = '/';
			for (int j = 0; j < strlen(entry->d_name); j++)
				newpath[i++] = entry->d_name[j];
			newpath[i++] = '/';
			newpath[i] = '\0';
			ls_r(newpath, tabs+1);
		}
		entry = readdir(dir);
	}
	
	if (closedir(dir) == -1)
		return;

	return;
}

