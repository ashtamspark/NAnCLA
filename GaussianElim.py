# This performs Gaussian Elimination on an Order n Square Matrix.

n = int(input("Enter number of rows: "))
# Row major serialization (instead of the more common column major serialization in maths)
A = [[float(entry) for entry in input().split()] for row in range(n)]

# View Matrix A
def view(A):
	for row in A:
		print(*(f"{entry: .2f}" for entry in row))

print("Given matrix is ")
view(A)

# Gaussian Elimination
pivot = -1; c = 0
for col in range(0, n):
	for row in range(pivot+1, n):
		if A[row][col] != 0:
			pivot = row
			break

	for row in range(pivot+1, n):
		factor = (A[row][col]/A[pivot][col])
		for i in range(col+1, n):
			A[row][i] = A[row][i] - factor*A[pivot][i]
		A[row][col] = 0
		c += 1

		print(f"Step {c}")
		view(A)

'''
Input:
 5.00 -2.00  0.00  3.00 -1.00
-1.00  4.00  8.00 -2.00  5.00
 0.00  3.00 -6.00  1.00  2.00
 2.00 -5.00  1.00  7.00 -3.00
 4.00  1.00 -3.00  0.00  6.00

Output:
 5.00 -2.00  0.00  3.00 -1.00
 0.00  3.60  8.00 -1.40  4.80
 0.00  0.00 -12.67  2.17 -2.00
 0.00  0.00  0.00  5.93  1.37
 0.00  0.00  0.00  0.00  5.39