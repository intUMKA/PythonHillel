#Hillel homework
#TASK: create a matrix with the ability to adjust the number of rows and columns.
# Print sum of each row/column


from random import randint
rows = int(input('Enter number of lines:'))
cols = int(input('Enter the number of columns:'))
matrix = []
cnt2 = 0
for i in range(rows):
    matrix.append([])
    cnt2 = 0
    for j in range(cols):
        matrix[i].append(randint(1, 50))
        print('{:02}'.format(matrix[i][j]), end=' ')
        cnt2 += matrix[i][j]
    print(' | ', '{: }'.format(cnt2))

sum_col = [0] * cols
for row in matrix:
    for i, item in enumerate(row):
        sum_col[i] += item
print('-- ' * cols)
print(sum_col, end='')








