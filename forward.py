# Newton Forward Interpolation

n = int(input("Enter number of data points: "))
x = []
y = []

for i in range(n):
    x_val = float(input(f"x[{i}] = "))
    y_val = float(input(f"y[{i}] = "))
    x.append(x_val)
    y.append(y_val)

# Compute forward difference table
diff_table = [y]
for i in range(1, n):
    column = []
    for j in range(n - i):
        column.append(diff_table[i-1][j+1] - diff_table[i-1][j])
    diff_table.append(column)

print("\nNewton’s Forward interpolation:")
for i in range(n):
    print(f"{x[i]:.4f}", end="\t")
    for j in range(n - i):
        print(f"{diff_table[j][i]:.4f}", end="\t")
    print()

value = float(input("Enter the value of x for interpolation: "))
h = x[1] - x[0]
p = (value - x[0]) / h

# Apply Newton forward formula
result = y[0]
p_term = 1
for i in range(1, n):
    p_term *= (p - i + 1) / i
    result += p_term * diff_table[i][0]

print(f"\nInterpolated value at x = {value} is {result:.6f}")
