
# This performs Gauss-Jordan Elimination on an Order n Square Matrix.

n = int(input("Enter number of rows: "))
# Row major serialization
A = [[float(entry) for entry in input().split()] for row in range(n)]

# View Matrix A
def view(A):
    for row in A:
        print(*(f"{entry: .2f}" for entry in row))

print("Given matrix is ")
view(A)

# Gauss-Jordan Elimination
pivot = 0; c = 0
eps = 1e-12

for col in range(n):
    # Find a non-zero pivot (Partial Pivoting)
    row = max(range(pivot, n), key=lambda i: abs(A[i][col]))

    if abs(A[row][col]) < eps:
        continue

    # Bring pivot to its correct position
    A[pivot], A[row] = A[row], A[pivot]

    # Normalize the pivot row
    factor = A[pivot][col]
    for i in range(n):
        A[pivot][i] /= factor

    # Eliminate all other entries in the pivot column
    for row in range(n):
        if row == pivot:
            continue

        factor = A[row][col]
        for i in range(n):
            A[row][i] -= factor*A[pivot][i]

    pivot += 1; c += 1

    print(f"Step {c}")
    view(A)

    if pivot == n:
        break

# Remove floating-point residue
A = [[0.0 if abs(x) < eps else x for x in row] for row in A]

print("Reduced Row Echelon Form:")
view(A)

'''
Input:
2 1 1
4 -6 0
-2 7 2

Output:
 1.00  0.00  0.00
 0.00  1.00  0.00
 0.00  0.00  1.00
'''
