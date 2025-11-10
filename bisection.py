def f(x):
    
    return x**3 - 4*x - 9


a = float(input("Enter  a: "))
b = float(input("Enter  b: "))
tolerance = float(input("Enter tolerance (e.g., 0.0001): "))


if f(a) * f(b) > 0:
    print("No root found in this interval. Try different values of a and b.")
else:
    print("\nIteration\t a\t\t b\t\t xr\t\t f(a)\t\t f(b)\t\t f(xr)")
    iteration = 1

    while True:
        xr = (a + b) / 2
        fa = f(a)
        fb = f(b)
        fxr = f(xr)

        
        print(f"{iteration:>5}\t {a:.6f}\t {b:.6f}\t {xr:.6f}\t {fa:.6f}\t {fb:.6f}\t {fxr:.6f}")

        
        if abs(fxr) < tolerance:
            print("\nApproximate root:", xr)
            break
        
        if fa * fxr < 0:
            b = xr
        else:
            a = xr

        iteration += 1
