def f(x):
    
    return x**3 - x - 2

a = float(input("Enter  a: "))
b = float(input("Enter  b: "))


if f(a) * f(b) > 0:
    print("No root found in this interval. Try different values of a and b.")
else:
    print("\nIteration\t a\t\t b\t\t xr\t\t f(a)\t\t f(b)\t\t f(xr)")
    xr_old = 0
    iteration = 1

    while True:
        fa = f(a)
        fb = f(b)
        xr = (a*fb-b*fa)/(fb-fa)
        fxr = f(xr)

        
        print(f"{iteration:>5}\t {a:.6f}\t {b:.6f}\t {xr:.6f}\t {fa:.6f}\t {fb:.6f}\t {fxr:.6f}")

        
        if abs(xr-xr_old) < 0.0001 or abs(fxr)<0.0001:
            print("\nApproximate root:", xr)
            break

        
        if fa * fxr < 0:
            b = xr
        else:
            a = xr
            
            xr_old = xr

        iteration += 1
