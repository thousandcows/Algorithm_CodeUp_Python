# Read row and column number
row, col = map(int, input().split(' '))

# Use dynamic programming to find the location
# Initialize pascal array
pascal = [[0 for i in range(col)] for j in range(row)]

# Set the default: values of first column and row should be 1
for i in range(col):
    pascal[0][i] = 1

for i in range(row):
    pascal[i][0] = 1

# Assign the values to array by its rule
for i in range(1, row):
    for j in range(1, col):
        pascal[i][j] = (pascal[i-1][j] + pascal[i][j-1]) % 100000000

# Print the answer divided by 100000000
print(pascal[row-1][col-1])
