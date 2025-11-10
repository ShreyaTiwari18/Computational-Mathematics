# Regula Falsi (False Position) method with iteration table (pure Python)

def f(x):
    # --- change this function as needed ---
    return x**3 - 4*x - 9
    # -------------------------------------

def regula_falsi(a, b, tol=0.00001, max_iter=50):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs (root not guaranteed).")

    print("\nIter |     a       |     b       |     xr      |   f(a)      |   f(b)      |   f(xr)     ")
    print("-"*92)
    xr_old = None

    for it in range(1, max_iter+1):
        # xr from Regula Falsi formula
        xr = (a * fb - b * fa) / (fb - fa)
        fxr = f(xr)

        print(f"{it:4d} | {a:.6f} | {b:.6f} | {xr:.6f} | {fa:.6f} | {fb:.6f} | {fxr:.6f} ")

        # stopping criteria: function value close to zero or interval small
        if abs(fxr) < tol or abs(b - a) < tol:
            return xr, fxr, it

        # decide which subinterval contains the root
        if fa * fxr < 0:
            b = xr
            fb = fxr
        else:
            a = xr
            fa = fxr

        # avoid infinite loop if xr stops changing (very unlikely but safe)
        if xr_old is not None and abs(xr - xr_old) < 1e-15:
            return xr, fxr, it
        xr_old = xr

    # If reached here, max iterations used
    return xr, fxr, max_iter

if __name__ == "__main__":
    try:
        a = float(input("Enter lower limit a: "))
        b = float(input("Enter upper limit b: "))
        tol = float(input("Enter tolerance (e.g., 0.00001): ") or 1e-6)
        max_iter = int(input("Enter max iterations (e.g., 50): ") or 50)

        root, froot, iterations = regula_falsi(a, b, tol, max_iter)
        print("\nResult:")
        print(f"Approximate root = {root:.6f}")
        print(f"f(root) = {froot:.6f}")
        print(f"Iterations = {iterations}")

    except Exception as e:
        print("Error:", e)
