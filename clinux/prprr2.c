# include <stdio.h>
# include <string.h>

int allover(int bt[], int pcount);
int nextappear(char pname[3], char gantt[1500][3], int tstart, int tend);

int main()
{
	char plist[100][3]; int pcount = 0;
	int at[100], bt[100], bt2[100];
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
		int wt[100], tt[100], rt[100];
		for (int k = 0; k < pcount; k++)
		{
			wt[k] = 0;
			tt[k] = 0;
			rt[k] = 0;
		}
		
		// wt
		int wt2 = 0, curr = -1, next = 1;
		for (int i = 0; i < pcount; i++)
		{
			wt2 = 0;
			curr = -1;
			next = 1;
			while (next != -1)
			{
				next = nextappear(plist[i], gantt, curr+1, clk);
				if (curr == -1)
				{
					curr = next;
					wt2 = curr;
					printf("%d--%d--\n", i+1, wt2);
				}
				else if (next == -1) break;
				else
				{
					if (next - curr != 1)
						wt2 += (next - curr - 1);
					curr = next;
					printf("%d--%d--\n", i+1, wt2);
				}
			}
			wt2 -= at[i];
			wt[i] = wt2;
		}
		float sum = 0;
		for (int k = 0; k < pcount; k++)
			sum += wt[k];
		printf("WT = %f, Avg WT = %f\n", sum, (float)(sum/pcount));
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

int nextappear(char pname[3], char gantt[1500][3], int tstart, int tend)
{
	int i;
	for (i = tstart; i < tend; i++)
	{
		if (strcmp(gantt[i], pname) == 0)
			return i;
	}
	return -1;
}