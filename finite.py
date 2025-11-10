# Newton’s Forward Difference Table

n = int(input("Enter number of data points: "))
x = []
y = []

for i in range(n):
    x_val = float(input(f"x[{i}] = "))
    y_val = float(input(f"y[{i}] = "))
    x.append(x_val)
    y.append(y_val)

# Create table
diff_table = [y]
for i in range(1, n):
    column = []
    for j in range(n - i):
        column.append(diff_table[i-1][j+1] - diff_table[i-1][j])
    diff_table.append(column)

# Display table
print("\nNewton’s Forward Difference Table:")
for i in range(n):
    print(f"{x[i]:.4f}", end="\t")
    for j in range(n - i):
        print(f"{diff_table[j][i]:.4f}", end="\t")
    print()
