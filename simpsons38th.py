def f(x):
    return x**2 + 1

a = 0
b = 1
n = 6  # Must be multiple of 3
h = (b - a) / n

sum3 = 0
sum2 = 0

print("------------------------------------------------------------")
print("                 SIMPSON'S 3/8 RULE")
print("------------------------------------------------------------")
print(" i\t   x\t\t     f(x)")
print("------------------------------------------------------------")

for i in range(1, n):
    x = a + i * h
    fx = f(x)
    print(f" {i:<2}\t {x:<10.6f}\t {fx:<10.6f}")
    if i % 3 == 0:
        sum2 += fx
    else:
        sum3 += fx

I = (3 * h / 8) * (f(a) + f(b) + 3 * sum3 + 2 * sum2)
print("------------------------------------------------------------")
print(f" Approximate value of integral = {I:.6f}")
print(f" Rounded to 4 decimal places : {round(I,4)}")
print("------------------------------------------------------------")
