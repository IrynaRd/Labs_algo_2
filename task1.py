def merge_sort(matrix):
    if len(matrix) <= 1:
        return matrix
    
    n = len(matrix) // 2
    matrix_left = matrix[:n]
    matrix_right = matrix[n:]
    
    if len(matrix_right) > 1:
        matrix_right = merge_sort(matrix_right)
    if len(matrix_left) > 1:
        matrix_left = merge_sort(matrix_left)

    arr = []
    L = len(matrix_left)
    R = len(matrix_right)

    i = 0
    j = 0
    
    while i < L and j < R:
        if matrix_left[i][0]<= matrix_right[j][0] or (matrix_left[i][0] == matrix_right[j][0] and matrix_left[i][1] <= matrix_right[j][1]):
            arr.append(matrix_left[i])
            i += 1
        else:
            arr.append(matrix_right[j])
            j += 1
    
    arr += matrix_left[i:] + matrix_right[j:]
    return arr

def merge_sort_greed(matrix, k):
    if k <= 1:
        return matrix[:k]

    mid = k // 2
    left = merge_sort_greed(matrix[:mid], mid)
    right = merge_sort_greed(matrix[mid:k], k - mid)

    sorted_arr = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    sorted_arr += left[i:] + right[j:]
    return sorted_arr    

def can_feed(matrix, daily_supply, k):
    
    calculated_sums = merge_sort_greed(matrix, k)
    
    total_sum = 0
    for i in range(k):
        total_sum += calculated_sums[i][0] + calculated_sums[i][1] * i
        if total_sum > daily_supply:
            return False
    return True

def max_hamsters_number(matrix, daily_supply):
    matrix = merge_sort(matrix)
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

print(max_hamsters_number([[1, 50000], [1, 60000]], 2))

          
    

