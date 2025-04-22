from math import inf
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        self.heap.append(element)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, i):
        parent = (i - 1) // 2
        while i != 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2
        
    def sift_down(self, i):
        left = 2*i + 1
        right = 2*i + 2

        while (left < len(self.heap) and self.heap[i] > self.heap[left]) \
            or (right < len(self.heap) and self.heap[i] > self.heap[right]):
            smallest = left if (right >= len(self.heap) or self.heap[right] > self.heap[left]) else right
            i = smallest
            left = 2*i + 1
            right = 2*i + 2

    def is_empty(self):
        return len(self.heap) == 0
    
    def pop(self):
        if not self.heap:
            return None
        root = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self.sift_down(0)
        return root

def dijkstra(graph, clients, start):
    distances = {node: inf for node in graph}
    heapq = PriorityQueue()
    heapq.insert((0, start))
    distances[start] = 0

    while not heapq.is_empty():
        current_distance, current_node = heapq.pop()
        if current_distance > distances[current_node]:
            continue
        for neighbor, latency in graph[current_node]:
            new_dist = latency + current_distance
            
            if new_dist > distances[neighbor]:
                continue
            distances[neighbor] = new_dist
            heapq.insert((new_dist, neighbor))

    min_max = -1
    for client in clients:
        if min_max < distances[client]:
            min_max = distances[client]
             
    return min_max

def find_min_max(graph, clients):
    max = inf
    for node in graph:
        if node not in clients:
            min_max = dijkstra(graph, clients, node)
            if min_max < max:
                max = min_max
    return max

def read_file(filename):
    with open(filename, "r") as f:
        N, M = map(int, f.readline().split())
        clients = list(map(int, f.readline().split()))
        graph = {i: [] for i in range(1, N + 1)}

        for _ in range(M):
            startnode, endnode, latency = map(int, f.readline().split())
            graph[startnode].append((endnode, latency))
            graph[endnode].append((startnode, latency))

    return graph, clients

def write_file(filename, result):
    with open(filename, "w") as f:
        f.write(str(result))



graph, clients = read_file("gamsrv_in.txt")
result = find_min_max(graph, clients)
write_file("gamsrv_out.txt", result)
  