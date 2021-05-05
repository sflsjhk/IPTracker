from collections import defaultdict
import heapq

class IPTracker:
    TOP_K_FREQUENT_IP = 2
    def __init__(self) -> None:
        self.ip_counter = defaultdict(int)

    def request_handled(self, ip_address: str):
        # O(1)
        self.ip_counter[ip_address] += 1
        return
    
    def top100(self):
        # O(n*log(100))
        ans = heapq.nlargest(self.TOP_K_FREQUENT_IP, self.ip_counter, key = self.ip_counter.get)
        return ans

    def clear(self):
        self.ip_counter.clear()
        return