from math import factorial
def backward_difference_table(y):
    n = len(y)
    table = [[0 for _ in range(n)] for _ in range(n)]    
    for i in range(n):
        table[i][0] = y[i]
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            table[i][j] = table[i][j-1] - table[i-1][j-1]
    return table
def newton_backward(x, y, xp):
    n = len(x)
    h = x[1] - x[0]
    p = (xp - x[-1]) / h
    table = backward_difference_table(y)
    yp = y[-1]
    term = 1
    for i in range(1, n):
        term *= (p + i - 1)
        yp += (term * table[n-1][i]) / factorial(i)

    return yp, table

n = int(input("Enter number of data points: "))
x = []
y = []
print("Enter x values (equally spaced):")
for i in range(n):
    x.append(float(input(f"x[{i}] = ")))
print("Enter y values:")
for i in range(n):
    y.append(float(input(f"y[{i}] = ")))
xp = float(input("Enter x value to interpolate: "))
result, table = newton_backward(x, y, xp)
print("\nBackward Difference Table:")
for i in range(n):
    for j in range(i + 1):    
        print(table[i][j], end="   ")
    print()
print(f"\nInterpolated value at x = {xp} is {result}")
