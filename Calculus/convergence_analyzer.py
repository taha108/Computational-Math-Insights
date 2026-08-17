from sympy import symbols, limit, oo, factorial, Abs, Function

def compute_radius_of_convergence():
    print("--- 📈 Power Series Convergence Analyzer ---")
    
    # 1. Define the symbolic variable n
    n = symbols('n', integer=True, positive=True)

    # 2. Define the general term a_n of your series
    # Example 1: a_n = 1 / factorial(n) -> Exponential series (R = oo)
    # Example 2: a_n = n**2 / 3**n -> R = 3
    a_n = 1 / factorial(n) 
    
    print(f"General term a_n = {a_n}")

    # 3. Apply D'Alembert's Ratio Test
    # we calculate the ratio |a_n / a_{n+1}|
    a_n_plus_1 = a_n.subs(n, n + 1)
    ratio = Abs(a_n / a_n_plus_1)

    # 4. Compute the limit as n approaches infinity
    radius = limit(ratio, n, oo)

    print("\n--- Results ---")
    print(f"Ratio |a_n / a_n+1|: {ratio}")
    print(f"Radius of Convergence R = {radius}")

    if radius == oo:
        print("Verdict: The series converges for all x in R.")
    elif radius == 0:
        print("Verdict: The series converges only at x = 0.")
    else:
        print(f"Verdict: The series converges for |x| < {radius}.")

if __name__ == "__main__":
    compute_radius_of_convergence()