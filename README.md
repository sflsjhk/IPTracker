# IPTracker V2

## Improved Design and Implementation

The IP tracker system is initiated with 

1. a hash table(defaultlist), ip_counter, which stores the IP address and its occurence count. 

2. a heap array list, heap, which stores a max-heap tree structure using index. ![Structure](Structure.png)

3. a Node class. A class for representing IPs in tree implementation. Includes IP, count, index(position at heap array).

**request_handled(ip_address)**
When getting an IP:
    
    check if ip in dict:
    
    if yes:
        1. update dict[ip].count. O(1) operation
        2. update the Ip's node's count. If count is greater than parent,
           swap location with parent. O(log(100)) operation

    if not:
        1. create node for the new IP address. 
        2. update dict[ip].count. O(1) operation
        3. try to insert node into heap tree. O(log(100)) operation
            if heap size = 100, check if its count is bigger than a count value in the tree,
            if so, swap and update. if not, do not insert.
            if heap size < 100, insert.

The insertion and update operation in the tree is O(log(100)) time complexity as we have a fixed size of 100 for the heap tree, and moving an element has a max  log(100) time complexity.

**top100()**

Simply return the existing heap array. O(1) operation.

**clear()**

The clear() cleans out key and values of the system's hash table and heap array.
The method has time complexity of O(1), Space Compelxity O(1).

## Original Design and Implementation
The system is implemented by Python, the code runs well with the test cases that are included in the Repo. 

The IP tracker system is initiated with a hash table(defaultlist), ip_counter, which stores the IP address and its occurence count. 

**request_handled(ip_address)**

Each time the method is called, the system will increase the count of the ip_address in ip_counter(defaultlist) by 1. With the nature of defaultlist, if the input ip_address does not occur before, it will have a count of 1 (0+1).

The method has time complexity of O(1) as it is a simple insertion operation of hash table(Python dictionary). Space complexity is O(n) as the system needs to maintain a table as big as the IP input count.

**top100()**

The top100 method use Python's built-in Priority Queue's implementation "heapq". When top100() is called, the system will return a list of IPs created by the method "heapq.nlargest".

The method has time complexity of O(nlogk), k = 100 as it takes log(100) to sort each entry of the input data into heap of size 100, and n for n times of input data. The space complexity is O(1) as we have a constant size(100) of heap for priority queue.

**clear()**

The clear() cleans out key and values of the system's hash table.
The method has time complexity of O(1), Space Compelxity O(1).

## Concerns

**What would you do differently if you had more time?**

Coding wise, I would implement more mechanism for code security, such as IP address validation, input protection etc. Having more test cases to test out edge cases, such as bad format/values of input.

Performance wise, I would think more about developing a system that handles load better, most likely creating a mechanism to parallel process the input data. By having multiple threads handling the reuqest, and using a mutex mechanism to update the count for each IPs. This should sigfnificantly increase the system's ability to handle the requests.

**What other approaches did you decide not to pursue?**

Initially I decided to modify the heap every time a request is made. I decided to persue the current solution because I think realistically the system should have most of the calls of request_handled(). Having an O(1) operation is crucial for the system's response time. Saving the heap modification to the top100 method is more reasonable as our system use the top100 functin much less than request_handled().

**How would you test this?**

There is a test file included in the repo. We test each of the methods. Explained by Comment in code.
