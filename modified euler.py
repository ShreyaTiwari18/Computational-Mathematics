def f(x, y):
    return x + y

x0 = 0
y0 = 1
h = 0.1
xn = 0.5

print("------------------------------------------------------------")
print("              MODIFIED EULER (HEUN'S) METHOD")
print("------------------------------------------------------------")
print(" x0\t\t   y0\t\t   Pred\t\t   Corr\t\t    y")
print("------------------------------------------------------------")

while x0 < xn:
    y_pred = y0 + h * f(x0, y0)
    y_corr = y0 + (h / 2) * (f(x0, y0) + f(x0 + h, y_pred))
    print(f" {x0:<8.2f}\t {y0:<10.6f}\t {y_pred:<10.6f}\t {y_corr:<10.6f}\t {y_corr:<10.6f}")
    y0 = y_corr
    x0 += h

print("------------------------------------------------------------")
print(f" Approximate value of y at x = {xn} is {y0:.6f}")
print(f" Rounded to 4 decimal places : {round(y0,4)}")
print("------------------------------------------------------------")
