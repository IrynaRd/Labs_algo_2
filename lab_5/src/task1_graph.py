rows = [-1, 0, 0, 1]
cols = [0, -1, 1, 0]

def bfs(graph, M, N):
    visited = set()
    queue = []
    path_dict = {}

    for node in graph:
        if node[1] == 0:
            queue.append((node, 0))
            visited.add(node)
            path_dict[node] = None
    
    while queue:
        (x, y), dist = queue.pop(0)
        if y == N - 1:
            path = []
            current_node = (x, y)

            while current_node != None:
                path.insert(0, current_node)
                current_node = path_dict[current_node]
            return dist, path
        
        for neighbor in graph.get((x, y), []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
                path_dict[neighbor] = (x, y)

    return 169, None

def min_distance(graph, M, N):
    return bfs(graph, M, N)

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            graph = {}
            M = 0
            N = 0

            for i, line in enumerate(file):
                row = list(map(int, line.split()))
                N = len(row)

                for j, val in enumerate(row):
                    if val == 1:
                        node = (i, j)
                        neighbors = []
                        for k in range(len(rows)):
                            x = i + rows[k]
                            y = j + cols[k]
                            if 0 <= x < M + 1 and 0 <= y < N:
                                neighbor = (x, y)
                                if neighbor in graph:
                                    neighbors.append(neighbor)
                        graph[node] = neighbors
                M = i + 1
            
            for node in graph:
                for k in range(len(rows)):
                    x = node[0] + rows[k]
                    y = node[1] + cols[k]
                    if (x, y) in graph:
                        graph[(x, y)].append(node)
            
            to_remove = set()
            for node in graph:
                x, y = node
                for k in range(len(rows)):
                    nx = x + rows[k]
                    ny = y + cols[k]
                    if 0 <= nx < M and 0 <= ny < N:
                        if (nx, ny) not in graph:
                            to_remove.add(node)
                            break
            
            for node in to_remove:
                graph.pop(node, None)
            
            for node in graph:
                graph[node] = [neighbor for neighbor in graph[node] if neighbor not in to_remove]
            
            return graph, M, N
    except FileNotFoundError:
        print(f"{filename} not found")
        return None, None, None

field = read_from_file('input.txt')

def output_result_in_file(filename, result):
    with open(filename, 'w') as file:
        if result != 169:
            file.write(f"Min distance is {result}\n")
        else:
            file.write("-1\n")

if field is not None:
    graph, M, N = field
    dist, path = min_distance(graph, M, N)
    output_result_in_file('output.txt', (dist, path))
else:
    print(" ")
