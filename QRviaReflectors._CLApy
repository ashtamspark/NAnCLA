
# This performs QR Decomposition on an Order n Square Matrix.
# Method: Householder Reflections

n = int(input("Enter number of rows: "))
# Row major serialization
A = [[float(entry) for entry in input().split()] for row in range(n)]

# View Matrix A
def view(A):
    for row in A:
        print(*(f"{entry: .2f}" for entry in row))

print("Given matrix is ")
view(A)

# Initialize Q as Identity and R as A
Q = [[float(i == j) for j in range(n)] for i in range(n)]
R = [row[:] for row in A]

# QR Decomposition
eps = 1e-12

for col in range(n):
    # Extract the column below the diagonal
    x = [R[row][col] for row in range(col, n)]
    norm = sum(entry**2 for entry in x)**0.5

    if norm < eps:
        continue

    # Construct Householder Vector
    v = x[:]
    v[0] += norm if x[0] >= 0 else -norm

    norm_v = sum(entry**2 for entry in v)**0.5
    v = [entry/norm_v for entry in v]

    # Apply Reflection to R
    for j in range(col, n):
        factor = 2*sum(v[i]*R[col+i][j] for i in range(len(v)))

        for i in range(len(v)):
            R[col+i][j] -= factor*v[i]

    # Accumulate Reflections in Q
    for row in range(n):
        factor = 2*sum(Q[row][col+i]*v[i] for i in range(len(v)))

        for i in range(len(v)):
            Q[row][col+i] -= factor*v[i]

    print(f"Step {col+1}")
    view(R)

# Make diagonal entries of R non-negative
for i in range(n):
    if R[i][i] < 0:
        for j in range(n):
            R[i][j] *= -1
            Q[j][i] *= -1

# Remove floating-point residue
Q = [[0.0 if abs(x) < eps else x for x in row] for row in Q]
R = [[0.0 if abs(x) < eps else x for x in row] for row in R]

print("Orthogonal Matrix Q:")
view(Q)

print("Upper Triangular Matrix R:")
view(R)

'''
Input:
3 0
4 5

Output:

Orthogonal Matrix Q:
 0.60 -0.80
 0.80  0.60

Upper Triangular Matrix R:
 5.00  4.00
 0.00  3.00
'''
