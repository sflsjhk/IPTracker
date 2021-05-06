from collections import defaultdict
from Node import Node
import math

"""
Initialization:
ip_counter: defaultdict
heap: array serves as heap tree

Process:
request_handled:
    check if ip in dict:
    if yes:
        1. update dict[ip].count
        2. update the Ip's node's count. If count is greater than parent,
           swap location with parent.

    if not:
        1. create node for the new IP address
        2. update dict[ip].count
        3. try to insert node into heap tree 
            if heap size = 100, check if its count is bigger than a count value in the tree,
            if so, swap and update. if not, do not insert
            if heap size < 100, insert

top100:
    go through every node in the heap array, put each IP in a return array, return the array.

"""

class IPTracker:
    # Number of Most Frequent IP that should be returned
    TOP_K_FREQUENT_IP = 100
    
    # Initialize hash table
    def __init__(self) -> None:
        self.ip_counter = defaultdict(int)
        self.heap = []

    # Input IP: Str
    # Output 1 for success operation, 0 for for empty input
    # O(log100)
    def request_handled(self, ip_address: str):
        if not ip_address:
            return 0
        #  Case1 : first time the IP shows up.
        if ip_address not in self.ip_counter:
            node = Node(ip_address)
            self.ip_counter[ip_address] = node
            self.insert(node)
        # Case2: Already in dict.
        else:
            node = self.ip_counter[ip_address]
            node.count += 1
            self.updatePosition(node)

        return 1
    
    # Output list of top 100 IPs.
    # O(1)
    def top100(self):
        return self.heap
    
    # Clear the hash table and heap array
    def clear(self):
        self.ip_counter.clear()
        self.heap.clear()
        return

    def insert(self, node):
        # if the heap has already 100 most common IPs, we need to check if we can replace one with our current node.
        if len(self.heap) == 100:
            min_num, min_node_index = float('inf'), -1
            # Go through all the nodes to find the smallest, then replace with the current node.
            for index in range(100):
                n = self.heap[index]
                if min_num > n.count:
                    # update min, keep finding next smaller count
                    min_num = n.count
                    min_node_index = index
                # Find node with smaller count.
                if min_num < node.count:
                    # Set the node's index.
                    node.index = min_node_index
                    self.heap[min_node_index] = node
        # if the heap is not full yet, simply append the new IP address
        else:
            # Set the node's index
            node.index = len(self.heap)
            # Add node into heap's end
            self.heap.append(node)
    
    def updatePosition(self,node):
        position = node.index          
        # parent of any node N > 0 in an array will always be at index (N-1)/2
        parent_node_index = (node.index - 1) / 2  
        parent_node = self.heap[parent_node_index]
          
        if parent_node.count < node.count:
            self.heap[parent_node_index], self.heap[position] = self.heap[position], self.heap[parent_node_index]
            node.index = parent_node_index
            parent_node.index = position



