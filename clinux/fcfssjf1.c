# include <stdio.h>
# include <string.h>

int min(int a[], int size);
int allover(int bt[], int pcount);
int nextappear(char pname[3], char gantt[1500][3], int tstart, int tend);

int main()
{
	char plist[100][3]; int pcount = 0;
	int at[100], bt[100], bt2[100];

	int choice;
	printf("\tCPU SCHEDULING ALGORITHMS\n");
	printf("1. FCFS\n");
	printf("2. SJF\n");
	printf("3. Exit\n");
	printf("Enter your option:");
	scanf(" %d", &choice);
	// fcfs
	if (choice == 1)
	{
		printf("FCFS CPU SCHEDULER\n");
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
		
		int clk = 0;
		char gantt[1500][3];
		int firstarr = 0;

		// to run clock
		while (allover(bt2, pcount) != 1)
		{
            firstarr = -1;
			for (int i = 0; i < pcount; i++)
            {
                if (firstarr == -1)
                {
                    if (at[i] <= clk && bt2[i] > 0)
						firstarr = i;
                }
                else if (at[i] <= clk && bt2[i] > 0 && at[i] < at[firstarr])
                {
                    firstarr = i;
                }
            }
            if (firstarr > -1)
			{
                for (int j = 0; j < bt[firstarr]; j++)
                {
                    strcpy(gantt[clk], plist[firstarr]);
                    bt2[firstarr]--;
                    clk++;
                }
			}
			else
			{
				strcpy(gantt[clk], "Nil");
                clk++;
			}
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
					//printf("%d--%d--\n", i+1, wt2);
				}
				else if (next == -1) break;
				else
				{
					if (next - curr != 1)
						wt2 += (next - curr - 1);
					curr = next;
					//printf("%d--%d--\n", i+1, wt2);
				}
			}
			wt2 -= at[i];
			wt[i] = wt2;
		}
		float wsum = 0;
		for (int k = 0; k < pcount; k++)
			wsum += wt[k];
		printf("WT = %f, Avg WT = %f\n", wsum, (float)(wsum/pcount));

		// tt
		float tsum = 0;
		for (int i = 0; i < pcount; i++)
		{
			tt[i] = wt[i] + bt[i];
			tsum += tt[i];
		}
		printf("TT = %f, Avg TT = %f\n", tsum, (float)(tsum/pcount));

		// rt
		int firstfound = 0;
		float rsum = 0;
		for (int i = 0; i < pcount; i++)
		{
			firstfound = nextappear(plist[i], gantt, 0, clk);
			rt[i] = firstfound - at[i];
			rsum += rt[i];
		}
		printf("RT = %f, Avg RT = %f\n", rsum, (float)(rsum/pcount));
	}
	
	// sjf
	else if (choice == 2)
	{
		printf("SJF CPU SCHEDULER\n");
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

		int minp;
		int clk = 0;
		char gantt[1500][3];
		
		// to run clock
		while (allover(bt2, pcount) != 1)
		{
			// decide shortest of all arrived processes
			minp = -1;
			for (int i = 0; i < pcount; i++)
			{
				if (minp == -1)
				{
					if (at[i] <= clk && bt2[i] > 0)
						minp = i;
				}
				else if (at[i] <= clk && bt2[i] > 0 && bt2[i] < bt2[minp])
				{
					minp = i;
				}
			}
			//printf("((%d))\n", minp);
			if (minp > -1)
			{
				strcpy(gantt[clk], plist[minp]);
				bt2[minp]--;
			}
			else
			{
				strcpy(gantt[clk], "Nil");
			}
			clk++;
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
					//printf("%d--%d--\n", i+1, wt2);
				}
				else if (next == -1) break;
				else
				{
					if (next - curr != 1)
						wt2 += (next - curr - 1);
					curr = next;
					//printf("%d--%d--\n", i+1, wt2);
				}
			}
			wt2 -= at[i];
			wt[i] = wt2;
		}
		float wsum = 0;
		for (int k = 0; k < pcount; k++)
			wsum += wt[k];
		printf("WT = %f, Avg WT = %f\n", wsum, (float)(wsum/pcount));

		// tt
		float tsum = 0;
		for (int i = 0; i < pcount; i++)
		{
			tt[i] = wt[i] + bt[i];
			tsum += tt[i];
		}
		printf("TT = %f, Avg TT = %f\n", tsum, (float)(tsum/pcount));

		// rt
		int firstfound = 0;
		float rsum = 0;
		for (int i = 0; i < pcount; i++)
		{
			firstfound = nextappear(plist[i], gantt, 0, clk);
			rt[i] = firstfound - at[i];
			rsum += rt[i];
		}
		printf("RT = %f, Avg RT = %f\n", rsum, (float)(rsum/pcount));
	}
	
	else
	{
	
	}
	return 0;
}

int min(int a[], int size)
{
	int m = 0;
	for (int i = 0; i < size; i++)
	{
		if (a[i] < a[m])
			m = i;
	}
	return m;
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