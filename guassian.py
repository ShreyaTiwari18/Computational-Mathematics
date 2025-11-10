n = int(input("Enter number of equations: "))

# Input augmented matrix
a = []
for i in range(n):
    row = list(map(float, input(f"Enter coefficients of equation {i+1} (including RHS): ").split()))
    a.append(row)

def print_matrix(mat):
    for r in mat:
        print("\t".join(f"{val:8.3f}" for val in r))
    print()

print("\nInitial Augmented Matrix:")
print_matrix(a)

# Forward elimination
for i in range(n):
    if a[i][i] == 0:
        print("Mathematical Error! Pivot element is zero.")
        exit()
    for j in range(i+1, n):
        ratio = a[j][i] / a[i][i]
        for k in range(n+1):
            a[j][k] -= ratio * a[i][k]
    print(f"After eliminating column {i+1}:")
    print_matrix(a)

# Back substitution
x = [0 for _ in range(n)]
for i in range(n-1, -1, -1):
    x[i] = a[i][n]
    for j in range(i+1, n):
        x[i] -= a[i][j] * x[j]
    x[i] /= a[i][i]

print("Final Upper Triangular Matrix:")
print_matrix(a)

print("Solution:")
for i in range(n):
    print(f"x{i+1} = {x[i]:.4f}")
