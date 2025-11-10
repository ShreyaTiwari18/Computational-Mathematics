def f(x):
    return x**2 + 1

a = 0
b = 1
n = 6  
h = (b - a) / n

sum_val = f(a) + f(b)

print("------------------------------------------------------------")
print("                 TRAPEZOIDAL RULE")
print("------------------------------------------------------------")
print(" i\t   x\t\t     f(x)")
print("------------------------------------------------------------")

for i in range(1, n):
    x = a + i * h
    fx = f(x)
    print(f" {i:<2}\t {x:<10.6f}\t {fx:<10.6f}")
    sum_val += 2 * fx

I = (h / 2) * sum_val
print("------------------------------------------------------------")
print(f" Approximate value of integral = {I:.6f}")
print(f" Rounded to 4 decimal places : {round(I,4)}")
print("------------------------------------------------------------")
