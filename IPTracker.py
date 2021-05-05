from collections import defaultdict
import heapq

class IPTracker:
    # Number of Most Frequent IP that should be returned
    TOP_K_FREQUENT_IP = 100
    
    # Initialize hash table
    def __init__(self) -> None:
        self.ip_counter = defaultdict(int)

    # Input IP: Str
    # Output 1:int for success operation
    def request_handled(self, ip_address: str):
        # O(1)
        self.ip_counter[ip_address] += 1
        return 1
    
    # Output list of top 100(can be changed by the TOP_K_FREQUENT_IP) IPs.
    def top100(self):
        # O(n*log(100))
        ans = heapq.nlargest(self.TOP_K_FREQUENT_IP, self.ip_counter, key = self.ip_counter.get)
        return ans
    
    # Clear the hash table
    def clear(self):
        self.ip_counter.clear()
        return