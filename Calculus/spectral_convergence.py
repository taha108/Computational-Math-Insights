from sympy import symbols, oo, integrate, exp, Matrix

def spectral_check():
    print("--- 💎 Spectral Theorem & Integration Lab ---")
    
    # 1. Spectral Theorem Application
    # Let's define a symmetric matrix
    A = Matrix([[4, 2], 
                [2, 1]])
    
    if A.is_symmetric():
        print("\nMatrix A is symmetric. Spectral Theorem applies!")
        P, D = A.diagonalize()
        print(f"Diagonal Matrix D (Eigenvalues):\n{D}")
        print(f"Orthogonal Basis P (Eigenvectors):\n{P}")
    
    # 2. Generalized Integral (Riemann / Gaussian)
    t = symbols('t')
    # Let's compute the integral of exp(-t^2) from 0 to infinity (Gaussian)
    f = exp(-t**2)
    result = integrate(f, (t, 0, oo))
    
    print(f"\nGeneralized Integral of exp(-t²) from 0 to +inf:")
    print(f"Result: {result} (Approx: {result.evalf():.4f})")

if __name__ == "__main__":
    spectral_check()