from sympy import symbols, diff, Matrix, solve

def analyze_optimization():
    # 1. Define symbolic variables for multivariable calculus
    x, y = symbols('x y')
    
    # 2. Define the target function f(x, y)
    f = x**3 - 3*x + y**2
    print(f"--- Analyzing Function: f(x, y) = {f} ---")

    # 3. Compute the Gradient (First-order partial derivatives)
    # We find where the slope is zero in both x and y directions
    f_x = diff(f, x) # Partial derivative with respect to x
    f_y = diff(f, y) # Partial derivative with respect to y
    print(f"Gradient: ∇f = [{f_x}, {f_y}]")

    # 4. Solve the system [fx=0, fy=0] to find critical points
    # solve() looks for the coordinates (x, y) where the function is "flat"
    critical_points = solve([f_x, f_y], (x, y))
    print(f"Critical points found at: {critical_points}")

    # 5. Compute the Hessian Matrix components (Second-order derivatives)
    f_xx = diff(f_x, x) # Second partial derivative wrt x
    f_yy = diff(f_y, y) # Second partial derivative wrt y
    f_xy = diff(f_x, y) # Mixed partial derivative
    
    # Organize them into a 2x2 Matrix
    H = Matrix([[f_xx, f_xy], 
                [f_xy, f_yy]])

    # 6. Iterate through each critical point to determine its nature
    for point in critical_points:
        curr_x, curr_y = point[0], point[1]
        
        # Substitute the point coordinates into the Hessian and the Function
        h_at_point = H.subs({x: curr_x, y: curr_y})
        val_at_point = f.subs({x: curr_x, y: curr_y})
        
        # Calculate the Determinant of the Hessian at this point
        det_H = h_at_point.det()
        
        print(f"\n--- Point {point} Analysis ---")
        print(f"Value at point f(x,y) = {val_at_point}")
        print(f"Determinant det(H) = {det_H}")

        # 7. Classification Logic (The Second Derivative Test)
        if det_H > 0:
            # If Det > 0 and f_xx > 0, it's a "bowl" shape facing up
            if h_at_point[0,0] > 0:
                print("Verdict: ✅ LOCAL MINIMUM")
            # If Det > 0 and f_xx < 0, it's a "dome" shape facing down
            else:
                print("Verdict: 🚩 LOCAL MAXIMUM")
        elif det_H < 0:
            # If Det < 0, it curves up in one axis and down in the other
            print("Verdict: 🌀 SADDLE POINT")
        else:
            # If Det = 0, the second-order information is not enough
            print("Verdict: ⚠️ INCONCLUSIVE")

if __name__ == "__main__":
    analyze_optimization()