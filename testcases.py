from IPTracker import IPTracker

iptracker = IPTracker()
# Set the top k frequent ip as 3 for easier testing
iptracker.TOP_K_FREQUENT_IP = 3

# Test request_handled method by mocking several IP inputs, test if system stores all Ips
iptracker.request_handled("192.168.1.1")
# Test Good input
print(iptracker.request_handled("192.168.1.2"))
# Test Null input
print(iptracker.request_handled(""))

iptracker.request_handled("192.168.1.1")
iptracker.request_handled("192.168.1.1")
iptracker.request_handled("192.168.1.2")
iptracker.request_handled("192.168.1.3")
iptracker.request_handled("192.168.1.2")
iptracker.request_handled("192.168.1.2")
iptracker.request_handled("192.168.1.2")
iptracker.request_handled("192.168.1.2")
iptracker.request_handled("192.168.1.2")
iptracker.request_handled("192.168.1.4")
iptracker.request_handled("192.168.1.1")
iptracker.request_handled("192.168.1.4")
iptracker.request_handled("192.168.1.2")
print("After request_handled", iptracker.ip_counter)

# Test top100 method by mocking several IP inputs, test if return correct top IPs list
print("Top", iptracker.TOP_K_FREQUENT_IP, "IPs:", iptracker.top100())

# Test clear method
iptracker.clear()
print("After clear", iptracker.ip_counter)
