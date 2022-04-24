# include <stdio.h>
# include <string.h>

int allover(int bt[], int pcount);

int main()
{
	char plist[100][3]; int pcount = 0;
	int at[100], bt[100], bt2[100], pr[100];
	//int arct = 0, btct = 0, prct = 0;
	int tq = 2;
	
	int choice;
	printf("\tCPU SCHEDULING ALGORITHMS\n");
	printf("1. Round Robin\n");
	printf("2. Priority-P\n");
	printf("3. Exit\n");
	printf("Enter your option:");
	scanf(" %d", &choice);
	// round robin
	if (choice == 1)
	{
		printf("ROUND ROBIN CPU SCHEDULER\n");
		printf("No. of processes:");
		scanf(" %d", &pcount);
		for (int i = 0; i < pcount; i++)
		{
			printf("Process ID:");
			scanf(" %s", plist[i]);
			printf("Arrival Time:");
			scanf(" %d", &at[i]);
			printf("Burst Time:");
			scanf(" %d", &bt[i]);
			bt2[i] = bt[i];
			printf("\n");
		}
		
		int turn = 0;
		int clk = 0;
		char gantt[1500][3];
		
		// to run clock
		while (allover(bt2, pcount) != 1)
		{
			if (at[turn] <= clk && bt2[turn] > 0)
			{
				for (int j = 0; j < tq; j++)
				{
					strcpy(gantt[clk], plist[turn]);
					if (bt2[turn] > 0)
					{
						bt2[turn]--;
						clk++;
					}
					else
						break;
				}
			}
			else if (at[turn] > clk)
				clk++;
			turn = (turn + 1) % pcount;
		}
		
		// display gantt chart
		for (int i = 0; i < clk; i++)
		{
			printf("%d:%s\t", i, gantt[i]);
		}
		printf("%d:\n", clk);
		
		// display wt, tt, rt
		int wt = 0, tt = 0, rt = 0;
		
		// wt
		for (int i = 0; i < pcount; i++)
		{
			int j;
			for (j = 0; j < clk; j++)
			{
				if (strcmp(gantt[j], plist[i]) == 0)
				{
					wt = j - at[i];
				}
			}
		}
		printf("WT = %d, Avg WT = %f\n", wt, (float)(wt/pcount));
	}
	
	// priority-p
	else if (choice == 2)
	{
	
	}
	
	else
	{
	
	}
	return 0;
}

int allover(int bt[], int pcount)
{
	for (int i = 0; i < pcount; i++)
	{
		if (bt[i] > 0)
			return 0;
	}
	return 1;
}

