from math import factorial


def forward_difference(y):
    n = len(y)
    diff_table = [y]
    for i in range(1, n):
        col = []
        for j in range(n - i):
            col.append(diff_table[i - 1][j + 1] - diff_table[i - 1][j])
        diff_table.append(col)
    return diff_table


def newton_forward(x, y, value):
    n = len(x)
    h = x[1] - x[0]   
    p = (value - x[0]) / h

    diff_table = forward_difference(y)

    result = y[0]
    term = 1
    for i in range(1, n):
        term *= (p - (i - 1))
        result += (term * diff_table[i][0]) / factorial(i)

    return result, diff_table
n = int(input("Enter number of data points: "))

x = []
y = []

print("Enter x values (equally spaced):")
for i in range(n):
    x.append(float(input(f"x[{i}] = ")))

print("Enter y values (corresponding to f(x), type 'null' if unknown):")
for i in range(n):
    val = input(f"y[{i}] = ")
    if val.lower() == "null":
        y.append(None)   
    else:
        y.append(float(val))


x_clean = []
y_clean = []
for xi, yi in zip(x, y):
    if yi is not None:
        x_clean.append(xi)
        y_clean.append(yi)

if len(x_clean) < 2:
    print("\nError: Not enough known y values for interpolation.")
else:
    x_val = float(input("Enter the value of x to interpolate: "))

    
    result, table = newton_forward(x_clean, y_clean, x_val)

   
    print("\nForward Difference Table:")
    for i in range(len(table)):
        print(f"Δ^{i}y:", table[i])

    print(f"\nInterpolated value at x = {x_val} is {result}")
