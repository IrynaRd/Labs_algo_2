def counting_sort(matrix, index):
    max_value = matrix[0][index]
    for row in matrix:
        if row[index] > max_value:
            max_value = row[index]
    
    counter = [0]*(max_value + 1) 
    output_matrix = [[0] * 2 for _ in range(len(matrix))]

    for row in matrix:
        counter[row[index]] += 1

    for i in range(1, len(counter)):
        counter[i] += counter[i - 1]

    i = len(matrix) - 1
    for row in matrix:
        value = row[index]
        counter[value] -= 1
        output_matrix[counter[value]] = row
        i -= 1

    return output_matrix

def counting_sort_greed(matrix, k):
    return counting_sort(matrix[:k], 1)
    
def can_feed(matrix, daily_supply, k):
    sorted_for_greed = counting_sort_greed(matrix, k)
    total_sum = 0
    
    for i in range(k):
        total_sum += sorted_for_greed[i][0] + sorted_for_greed[i][1] * i
        if total_sum > daily_supply:
            return False
    return True

def max_hamsters_number(matrix, daily_supply):
    left = 0
    right = len(matrix)
    best_k = 0

    while left <= right:
        mid = (left + right) // 2
        if can_feed(matrix, daily_supply, mid):
            best_k = mid  
            left = mid + 1  
        else:
            right = mid - 1  
    return best_k

print(max_hamsters_number([[5, 0], [2, 2], [1, 4], [5, 1]], 19))