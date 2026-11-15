
# This performs LU Decomposition on an Order n Square Matrix, with partial pivoting

n = int(input("Enter number of rows: "))
# Row major serialization
A = [[float(entry) for entry in input().split()] for row in range(n)]

# View Matrix A
def view(A):
    for row in A:
        print(*(f"{entry: .2f}" for entry in row))

print("Given matrix is ")
view(A)

# Initialize L, U and P
L = [[float(i == j) for j in range(n)] for i in range(n)]
U = [row[:] for row in A]
P = [[float(i == j) for j in range(n)] for i in range(n)]

# LU Decomposition
eps = 1e-12

for col in range(n):
    # Find the largest pivot (Partial Pivoting)
    pivot = max(range(col, n), key=lambda i: abs(U[i][col]))

    if abs(U[pivot][col]) < eps:
        continue

    # Interchange rows of U and P
    U[col], U[pivot] = U[pivot], U[col]
    P[col], P[pivot] = P[pivot], P[col]

    # Interchange previously computed entries of L
    for j in range(col):
        L[col][j], L[pivot][j] = L[pivot][j], L[col][j]

    # Gaussian Elimination
    for row in range(col+1, n):
        factor = U[row][col]/U[col][col]
        L[row][col] = factor

        for j in range(col+1, n):
            U[row][j] -= factor*U[col][j]

        U[row][col] = 0

    print(f"Step {col+1}")
    view(U)

# Remove floating-point residue
L = [[0.0 if abs(x) < eps else x for x in row] for row in L]
U = [[0.0 if abs(x) < eps else x for x in row] for row in U]

print("Permutation Matrix P:")
view(P)

print("Lower Triangular Matrix L:")
view(L)

print("Upper Triangular Matrix U:")
view(U)

'''
Input:
2 1
4 3

Output:

Permutation Matrix P:
 0.00  1.00
 1.00  0.00

Lower Triangular Matrix L:
 1.00  0.00
 0.50  1.00

Upper Triangular Matrix U:
 4.00  3.00
 0.00 -0.50
'''
