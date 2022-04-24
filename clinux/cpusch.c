# include <stdio.h>
# include <string.h>

struct process
{
	char id[3];
	int arrival;
	int burst;
	int status;
};

int fcfs_next(struct process p_list[], int processes);

int main()
{
	int ch=0, ch2=0;
	char cont = 'y';
	struct process p_list[100];
	int processes;
	char order[500][5];
	int systime = 0;
	
	while (cont == 'y' || cont == 'Y')
	{
		printf("\tCPU SCHEDULING ALGORITHMS\n");
		printf("1. FCFS\n2. SJF\n3. Exit\n");
		printf("Enter your option:");
		scanf(" %d", &ch);
		if (ch == 3) break;
		else if (ch == 1)
		{
			printf("FCFS CPU SCHEDULER\n");
			printf("Number of Processes:");
			scanf(" %d", &processes);
			for (int i = 0; i < processes; i++)
			{
				printf("Process ID:");
				scanf(" %s", p_list[i].id);
				printf("Arrival Time:");
				scanf(" %d", &(p_list[i].arrival));
				printf("Burst Time:");
				scanf(" %d", &(p_list[i].burst));
				p_list[i].status = 0;
			}
			// exec
			systime = 0;
			int nextpr = fcfs_next(p_list, processes);
			while (nextpr != -1)
			{
				while (systime < p_list[nextpr].arrival) systime++;
				for (int i = 0; i < p_list[nextpr].burst; i++)
				{
					strcpy(order[systime], p_list[nextpr].id);
					printf("-%d-%s--\n", systime, order[systime]);
					systime++;
				}
				p_list[nextpr].status = 1;
				nextpr = fcfs_next(p_list, processes);
			}
			// results
			for (int i = 0; i < systime; i++)
			{
				printf("%d:%s\n", i, order[i]);
			}
		}
		else if (ch == 2)
		{
			printf("SJF CPU SCHEDULER\n");
			printf("1. Non-Preemptive\n2. Preemptive\n3. Exit\n");
			printf("Enter your option:");
			scanf(" %d", &ch2);
			if (ch2 != 1 || ch2 != 2) continue;
			for (int i = 0; i < processes; i++)
			{
				printf("Process ID:");
				scanf(" %s", (p_list[i].id));
				printf("Arrival Time:");
				scanf(" %d", &(p_list[i].arrival));
				printf("Burst Time:");
				scanf(" %d", &(p_list[i].burst));
				p_list[i].status = 0;
			}
		}
		
		printf("Want to continue (y/n)?:");
		scanf(" %c", &cont);
	}
	return 0;
}

int fcfs_next(struct process p_list[], int processes)
{
	int min = -1;
	for (int i = 0; i < processes; i++)
	{
		if (p_list[i].status == 1) continue;
		else if (i == 0 && p_list[i].status == 0)
		{
			min = 0;
		}
		else if (p_list[i].arrival < p_list[min].arrival)
		{
			min = i;
		}
	}
	return min;
}

