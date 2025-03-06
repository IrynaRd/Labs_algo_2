def diagonal_traversing(rows, cols):
    matrix = [[0] * cols for _ in range(rows)]
    number = 1
    x = 0
    y = 0
    matrix[y][x] = number

    while number < rows*cols:
        while y > 0 and x < cols - 1: 
            y -= 1
            x += 1
            number += 1
            matrix[y][x] = number
        
        if x < cols - 1:
            x += 1
        else:
            y += 1
        
        if number >= rows*cols:
            break
        number += 1
        matrix[y][x] = number
        
        
        while y < rows - 1 and x > 0:
            y += 1
            x -= 1
            number += 1
            matrix[y][x] = number
        
        if y < rows - 1:
            y += 1
        else:
            x += 1

        if number >= rows*cols:
            break
        number += 1
        matrix[y][x] = number
        

    matrix = [i for row in matrix for i in row]
    return matrix

rows, cols = map(int, input("Enter the matrix size via comma: ").split(","))
new_matrix = diagonal_traversing(rows, cols)
print(new_matrix)


