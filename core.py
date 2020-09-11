import random
from prettytable import PrettyTable


def fcfs():
	process_queue = []
	total_wtime = 0
	n = int(input('Enter the total no of processes: '))

	print("Do you want automated process?(y/n): ",end="")
	choice=input()
	if choice=="y" or choice=="Y":
		for i in range(n):
		    process_queue.append([])
		    process_queue[i].append("pro_"+str(i))
		    process_queue[i].append(random.randint(0,20))
		    total_wtime += process_queue[i][1]
		    process_queue[i].append(random.randint(1,20))

	elif choice=="n" or choice =="N":
		for i in range(n):
		    process_queue.append([])
		    process_queue[i].append(input('Enter p_name: '))
		    process_queue[i].append(int(input('Enter p_arrival: ')))
		    total_wtime += process_queue[i][1]
		    process_queue[i].append(int(input('Enter p_burst: ')))
		    print()
		
	
	print()

	process_queue.sort(key = lambda process_queue:process_queue[1])

	print('ProcessName\tArrivalTime\tBurstTime')
	for i in range(n):
	    print(process_queue[i][0],'\t\t',process_queue[i][1],'\t\t',process_queue[i][2])
	    
	print('Total waiting time: ',total_wtime)
	print('Average waiting time: ',(total_wtime/n),"\n\n")

def sjf():
	process_queue = []
	total_wtime = 0
	n = int(input('Enter the total no of processes: '))

	print("Do you want automated process?(y/n): ",end="")
	choice=input()
	if choice=="y" or choice=="Y":
		for i in range(n):
		    process_queue.append([])
		    process_queue[i].append("pro_"+str(i))
		    process_queue[i].append(random.randint(1,20))

	elif choice=="n" or choice =="N":
		for i in range(n):
		    process_queue.append([])
		    process_queue[i].append(input('Enter p_name: '))
		    process_queue[i].append(int(input('Enter p_burst: ')))
		    print()
		
	print()
	process_queue.sort(key = lambda process_queue:process_queue[1])

	for i in process_queue[:n-1]:
		total_wtime+=total_wtime+i[1]
	print('ProcessName\tBurstTime')
	for i in range(n):
	    print(process_queue[i][0],'\t\t',process_queue[i][1])
	    
	print('Total waiting time: ',total_wtime)
	print('Average waiting time: ',(total_wtime/n),"\n")

def roundRobin():
	numb = int(input("Enter the total no of processes: "))
	quant = int(input("Enter the Quantum range: "))
	a=[]
		
	print("Do you want automated process?(y/n): ",end="")
	choice=input()
	if choice=="y" or choice=="Y":
		for i in range(numb):
			b=[]
			name = "pro_"+str(i)
			burst = int(random.randint(0,20))
			b.append(name)
			b.append(burst)
			a.append(b)

	elif choice=="n" or choice =="N":
		for i in range(numb):
			b=[]
			name = str(input("Enter process name: "))
			burst = int(input("Enter the burst time: "))
			b.append(name)
			b.append(burst)
			a.append(b)
			print()
		
	print()

	bt=[]
	prc=[]
	fbt=[]
	for i in range(len(a)):
		bt.append(a[i][1])
		fbt.append(a[i][1])
		prc.append(a[i][0])
	# print("burst time: ",bt)
	# print("The processes: ", prc)
	# print("\n")

	#to print the time line of the process    
	line=[]
	add=0
	while any(bt[i]!=0 for i in range(len(bt))):
		for j in range(len(bt)):
			if (bt[j]<quant and bt[j]!=0):
				evry=[]
				add+=bt[j]
				evry.append(prc[j])
				evry.append(add)
				line.append(evry)
				bt[j]-=bt[j]
			elif bt[j]>=quant:
				evry=[]
				add+=quant
				bt[j]-=quant
				evry.append(prc[j])
				evry.append(add)
				line.append(evry)
	# print(line)


	#to associate the processes and their turn around time
	dit={}
	for i in range(len(line)):
		if line[i][0] in dit.keys():
			dit[line[i][0]]=line[i][1]
		elif line[i][0] not in dit.keys():
				dit.update({line[i][0]:line[i][1]})

	# print("processes and tat", dit)

	#to find the turn adound time from the dictionary above
	tat=[]
	for i in dit.keys():
		tat.append(dit[i])
	# print('turn around time: ', tat)


	#to find waiting time (wt=tat-bt)
	wt=[]
	for i in range(len(fbt)):
		wt.append(tat[i]-fbt[i])
	# print("waiting time: ",wt)

	#to present all the data in the form of a tabular-data
	t = PrettyTable(['Process', 'Turnaround Time', "Waiting Time"])
	for i in range(len(prc)):
		t.add_row([prc[i],tat[i],wt[i]])
	print(t)


	#average turn around time
	sum1=0
	for i in tat:
		sum1+=i
		h1=(sum1/len(tat))
	print("Average turn around time: ", h1)

	#average waiting time
	sum2=0
	for i in wt:
		sum2+=i
		h2=sum2/len(wt)
	print("Average waiting time: ", h2)


def priority():
	process_queue = []
	total_wtime = 0
	n = int(input('Enter the total no of processes: '))

	print("Do you want automated process?(y/n): ",end="")
	choice=input()
	if choice=="y" or choice=="Y":
		pr_list=list(range(0,n))
		for i in range(n):
		    process_queue.append([])
		    process_queue[i].append("pro_"+str(i))
		    process_queue[i].append(int(random.randint(1,20)))
		    bb=random.randint(0,len(pr_list)-1)
		    process_queue[i].append(pr_list[bb])
		    pr_list.pop(bb)

	elif choice=="n" or choice =="N":
		for i in range(n):
		    process_queue.append([])
		    process_queue[i].append(input('Enter p_name: '))
		    process_queue[i].append(int(input('Enter p_burst: ')))
		    process_queue[i].append(int(input('Enter Priority (<{}): '.format(n))))
		    print()
		
	print()	    

	process_queue.sort(key = lambda process_queue:process_queue[2])

	total_wtime = 0
	for i in process_queue[:n-1]:
		total_wtime+=total_wtime+i[1]
		
	print('ProcessName\tBurstTime\tPriority')
	for i in range(n):
	    print(process_queue[i][0],'\t\t',process_queue[i][1],'\t\t',process_queue[i][2])
	    
	print('Total waiting time: ',total_wtime)
	print('Average waiting time: ',(total_wtime/n))	

while True:
	print("#"*50,"\n")
	print("Select option\n1.FCFS \n2.SJF \n3.Round Robin \n4.Priority \n5.Exit \n")
	print("Option-> ",end="")
	option=input()
	if option=="1":
		print("#"*50,"\n")
		fcfs()

	elif option=="2":
		print("#"*50,"\n")
		sjf()

	elif option=="3":
		print("#"*50,"\n")
		roundRobin()


	elif option=="4":
		print("#"*50,"\n")
		priority()
	
	elif option=="5":
		print("Goodbye")
		exit()

	else:
		print("\n ####Select valid option!!#### \n")
