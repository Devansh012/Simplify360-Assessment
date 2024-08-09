from collections import deque, defaultdict

class SocialNetwork:
    def __init__(self):  # Corrected constructor
        self.friends = defaultdict(set)
    
    def add_friendship(self, person1, person2):
        self.friends[person1].add(person2)
        self.friends[person2].add(person1)
    
    def find_common_friends(self, person1, person2):
        if person1 not in self.friends or person2 not in self.friends:
            return set()
        return self.friends[person1].intersection(self.friends[person2])
    
    def nth_connection(self, person1, person2):
        if person1 not in self.friends or person2 not in self.friends:
            return -1
        
        # BFS to find the shortest path
        queue = deque([(person1, 0)])
        visited = set([person1])
        
        while queue:
            current_person, connection_level = queue.popleft()
            if current_person == person2:
                return connection_level
            
            for friend in self.friends[current_person]:
                if friend not in visited:
                    visited.add(friend)
                    queue.append((friend, connection_level + 1))
        
        return -1  # No connection found

# Example Usage
network = SocialNetwork()

# Adding friendships
network.add_friendship("Alice", "Bob")
network.add_friendship("Bob", "Janice")
network.add_friendship("Alice", "Charlie")
network.add_friendship("Charlie", "David")

# Finding all friends of Alice
print(f"Friends of Alice: {network.friends['Alice']}")

# Finding all friends of Bob
print(f"Friends of Bob: {network.friends['Bob']}")

# Finding common friends between Alice and Bob
common_friends = network.find_common_friends("Alice", "Bob")
print(f"Common friends of Alice and Bob: {common_friends}")

# Finding nth connection between Alice and Janice
connection = network.nth_connection("Alice", "Janice")
print(f"The connection level between Alice and Janice is: {connection}")

# Finding nth connection between Alice and Bob
connection = network.nth_connection("Alice", "Bob")
print(f"The connection level between Alice and Bob is: {connection}")

# Finding nth connection between Alice and David
connection = network.nth_connection("Alice", "David")
print(f"The connection level between Alice and David is: {connection}")

# If there is no connection at all
connection = network.nth_connection("Alice", "Someone")
print(f"The connection level between Alice and Someone is: {connection}")
