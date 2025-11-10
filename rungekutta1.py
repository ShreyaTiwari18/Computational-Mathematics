def f(x, y):
    return x + y

x0 = 0
y0 = 1
h = 0.1
xn = 0.5

print("------------------------------------------------------------")
print("               RUNGE-KUTTA 2nd ORDER METHOD")
print("------------------------------------------------------------")
print(" x\t\t   y\t\t   k1\t\t   k2\t\t   y_new")
print("------------------------------------------------------------")

while x0 < xn:
    k1 = f(x0, y0)
    k2 = f(x0 + h, y0 + h * k1)
    y1 = y0 + (h / 2) * (k1 + k2)
    print(f" {x0:<8.2f}\t {y0:<10.6f}\t {k1:<10.6f}\t {k2:<10.6f}\t {y1:<10.6f}")
    x0 += h
    y0 = y1

print("------------------------------------------------------------")
print(f" Approximate value of y at x = {xn} is {y0:.6f}")
print(f" Rounded to 4 decimal places : {round(y0,4)}")
print("------------------------------------------------------------")
