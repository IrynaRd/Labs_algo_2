rows = [-1, 0, 0, 1]
cols = [0, -1, 1, 0]

def can_visit(field, visited, x, y):
    return field[x][y] == 1 and not visited[x][y]

def in_field(x, y, M, N):
    return 0 <= x < M and 0 <= y < N

def bfs(field):
    M = len(field)
    N = len(field[0])

    visited = [[False for _ in range(N)] for _ in range(M)]
    front = 0
    rear = 0
    queue = [None] * M*N

    for r in range(M):
        if field[r][0] == 1:
            queue[rear] = (r, 0, 0)
            rear += 1
            visited[r][0] = True
    
    while front < rear:
        i, j, distance = queue[front]
        front += 1

        if j == N - 1:
            return distance
        
        for k in range(len(rows)):
            x = i + rows[k]
            y = j + cols[k]

            if in_field(x, y, M, N) and can_visit(field, visited, x, y):
                visited[x][y] = True
                queue[rear] = (x, y, distance + 1)
                rear += 1
    
    return 169

def min_distance(matrix):
    M = len(matrix)
    N = len(matrix[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                for dx, dy in directions:
                    x, y = i+dx, j+dy
                    if in_field(x, y, M, N) and matrix[x][y] == 1:
                        matrix[x][y] = 169
    
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 169:
                matrix[i][j] = 0
                
    return bfs(matrix)

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            graph = []
            for line in file:
                row = list(map(int, line.split()))
                graph.append(row)
        return graph
    except FileNotFoundError:
        print(f"{filename} not found")
        return None


field = read_from_file('input.txt')

def output_result_in_file(filename, result):
    with open(filename, 'w') as file:
        if result != 169:
            file.write(f"Min distance is {result}\n")
        else:
            file.write("-1\n")

if field is not None:
    dist = min_distance(field)
    output_result_in_file('output.txt', dist)
else:
    print(" ")


