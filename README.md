# Simplify360-Assessment
Q1) Explanation:
Topological Sorting: The tasks are first sorted in topological order, which is a linear ordering of the tasks that respect the dependencies.
Earliest Start Time (EST) and Earliest Finish Time (EFT): These are calculated by traversing the tasks in topological order. The earliest start time of a task is the maximum of the earliest finish times of all its dependencies.
Latest Finish Time (LFT) and Latest Start Time (LST): These are calculated by traversing the tasks in reverse topological order. The latest finish time of a task is the minimum of the latest start times of all its dependent tasks.
Output:
The earliest time when all tasks will be completed.
The latest time by which all tasks can be completed without delaying the project.
Detailed timings for EST, EFT, LST, and LFT for each task.
This code should give you a good understanding of the scheduling and timing for a complex task workflow.

Q2) Explanation:
add_friendship: This method adds a bidirectional friendship between two people.
find_common_friends: This method finds and returns the common friends between two people by intersecting their friend sets.
nth_connection: This method uses Breadth-First Search (BFS) to find the shortest path (or connection level) between two people in the social network. If a path is found, it returns the connection level; otherwise, it returns -1 if no connection exists
Output:
Friends of Alice: {'Charlie', 'Bob'}
Friends of Bob: {'Alice', 'Janice'}
Common friends of Alice and Bob: {'Charlie'}
The connection level between Alice and Janice is: 2
The connection level between Alice and Bob is: 1
The connection level between Alice and David is: 2
The connection level between Alice and Someone is: -1

Time and Space Complexity:
Time Complexity:

add_friendship: O(1) since adding to a set is O(1).
find_common_friends: O(min(F1, F2)) where F1 and F2 are the number of friends of person1 and person2 respectively. Set intersection is O(min(F1, F2)).
nth_connection: O(N + E), where N is the number of people (nodes) in the network and E is the number of friendships (edges). This is the complexity of BFS traversal.
Space Complexity:

The space complexity is O(N + E) where N is the number of people and E is the number of friendships because we store the adjacency list in a dictionary of sets, and the BFS queue and visited set can also hold up to N people.
