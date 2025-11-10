
def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1


x0 = 1.5
e = 0.0001
step = 1

print("------------------------------------------------------------")
print("                   NEWTON–RAPHSON METHOD")
print("------------------------------------------------------------")
print(" Step\t   x0\t\t   f(x0)\t   f'(x0)\t   x1")
print("------------------------------------------------------------")

while True:
    f0 = f(x0)
    df0 = df(x0)
    x1 = x0 - (f0 / df0)
    print(f" {step:<5d}\t {x0:<10.6f}\t {f0:<10.6f}\t {df0:<10.6f}\t {x1:<10.6f}")
    
    if abs(x1 - x0) < e:
        break
    
    x0 = x1
    step += 1

print("------------------------------------------------------------")
print(f" Root of the equation is approximately : {x1:.6f}")
print(f" Rounded to 4 decimal places : {round(x1,4)}")
print("------------------------------------------------------------")
