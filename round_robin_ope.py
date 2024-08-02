#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Process:
    def __init__(self, pid, arrival_time, burst_time): 
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0


# In[2]:


def round_robin_scheduling(processes, time_quantum):
    n = len(processes)
    time = 0
    queue = []
    execution_order = []
    context_switches = 0
    
    processes.sort(key=lambda x: x.arrival_time)
    for process in processes:
        if process.arrival_time <= time:
            queue.append(process)
    
    while queue:
        process = queue.pop(0)
        
        if process.remaining_time > time_quantum:
            time += time_quantum
            process.remaining_time -= time_quantum
            execution_order.append(process.pid)
            context_switches += 1
        else:
            time += process.remaining_time
            process.waiting_time = time - process.burst_time - process.arrival_time
            process.remaining_time = 0
            process.turnaround_time = time - process.arrival_time
            execution_order.append(process.pid)
            
        for proc in processes:
            if proc.arrival_time <= time and proc.remaining_time > 0 and proc not in queue:
                queue.append(proc)
        if process.remaining_time > 0:
            queue.append(process)
        else:
            context_switches += 1
    
    return processes, execution_order, context_switches


# In[3]:


def calculate_average_times(processes):
    total_waiting_time = 0
    total_turnaround_time = 0
    n = len(processes)
    for process in processes:
        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time
        
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n
    
    return avg_waiting_time, avg_turnaround_time


# In[4]:


def main():
    processes = []
    n = int(input("Enter the number of processes: "))
    
    for i in range(n):
        pid = i + 1
        arrival_time = int(input(f"Enter arrival time for process {pid}: "))
        burst_time = int(input(f"Enter burst time for process {pid}: "))
        processes.append(Process(pid, arrival_time, burst_time))
        
    time_quantum = int(input("Enter time quantum: "))
    
    scheduled_processes, execution_order, context_switches = round_robin_scheduling(processes, time_quantum)
    avg_waiting_time, avg_turnaround_time = calculate_average_times(scheduled_processes) 
    
    print("\nProcess ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for process in scheduled_processes:
        print(f"{process.pid}\t\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")
              
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
    print(f"\nExecution order: {execution_order}")
    print(f"Number of Context Switches: {context_switches}")

if __name__ == "__main__":
    main()


# In[ ]:




