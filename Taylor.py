import math


def f(x, y):
    return -y  


x0 = 0
y0 = 1
h = 0.1
order = 5  

derivs = [0]*order
derivs[0] = f(x0, y0)


for i in range(1, order):
    derivs[i] = (-1)**i * y0


y1 = y0
for i in range(order):
    y1 += (derivs[i] * (h**(i+1))) / math.factorial(i+1)


print("----------------------------------------------------")
print("Derivatives at x0 = %.1f, y0 = %.1f:" % (x0, y0))
print("----------------------------------------------------")
for i in range(order):
    print(f"y^({i})(0) = {derivs[i]:.6f}")

print("\n----------------------------------------------------")
print(f"Taylor approximation up to order {order}:")
print(f"y({x0+h}) ≈ {y1:.10f}")
print(f"Rounded to 4 decimal places: {round(y1,4)}")
print("----------------------------------------------------")
