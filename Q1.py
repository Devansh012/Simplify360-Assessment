from collections import defaultdict, deque

def find_earliest_and_latest_finish_times(tasks, durations, dependencies):
    n = len(tasks)
    adj_list = defaultdict(list)
    in_degree = {task: 0 for task in tasks}
    
    # Build the adjacency list and calculate in-degrees
    for task, deps in dependencies.items():
        for dep in deps:
            adj_list[dep].append(task)
            in_degree[task] += 1
    
    # Topological sorting using Kahn's Algorithm
    topo_order = []
    zero_in_degree = deque([task for task in tasks if in_degree[task] == 0])
    
    while zero_in_degree:
        task = zero_in_degree.popleft()
        topo_order.append(task)
        for neighbor in adj_list[task]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)
    
    # Earliest Start Time (EST) and Earliest Finish Time (EFT)
    EST = {task: 0 for task in tasks}
    EFT = {task: 0 for task in tasks}
    
    for task in topo_order:
        EFT[task] = EST[task] + durations[task]
        for neighbor in adj_list[task]:
            EST[neighbor] = max(EST[neighbor], EFT[task])
    
    # Latest Finish Time (LFT) and Latest Start Time (LST)
    LFT = {task: float('inf') for task in tasks}
    LST = {task: 0 for task in tasks}
    
    # Set the LFT for the last task to its EFT
    last_task = topo_order[-1]
    LFT[last_task] = EFT[last_task]
    
    for task in reversed(topo_order):
        LST[task] = LFT[task] - durations[task]
        for neighbor in adj_list[task]:
            LFT[task] = min(LFT[task], LST[neighbor])
    
    return max(EFT.values()), max(LFT.values()), EST, EFT, LST, LFT

# Example Usage
tasks = ['T_START', 'A', 'B', 'C', 'D', 'E']
durations = {'T_START': 0, 'A': 2, 'B': 4, 'C': 3, 'D': 5, 'E': 2}
dependencies = {
    'A': ['T_START'],
    'B': ['T_START'],
    'C': ['A', 'B'],
    'D': ['B'],
    'E': ['C', 'D']
}

earliest_finish, latest_finish, EST, EFT, LST, LFT = find_earliest_and_latest_finish_times(tasks, durations, dependencies)

print(f"Earliest Time all tasks will be completed: {earliest_finish}")
print(f"Latest Time all tasks will be completed: {latest_finish}")
print("Earliest Start Times:", EST)
print("Earliest Finish Times:", EFT)
print("Latest Start Times:", LST)
print("Latest Finish Times:", LFT)