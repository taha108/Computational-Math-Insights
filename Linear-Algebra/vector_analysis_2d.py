# Script to verify if two vectors in R^2 form a basis and check orthogonality.

print("--- 📐 Linear Algebra Tool: Basis & Orthogonality ---")

# 1. Get user input for vector U
Ux = float(input("Enter x for vector U: "))
Uy = float(input("Enter y for vector U: ")) 

# 2. Get user input for vector V
Vx = float(input("Enter x for vector V: "))
Vy = float(input("Enter y for vector V: "))

# 3. Independence check (Determinant)
# Formula: ad - bc
det = (Ux * Vy) - (Uy * Vx)

# 4. Orthogonality check (Scalar Product)
# Formula: xx' + yy'
sc = (Ux * Vx) + (Uy * Vy)

print("\n" + "="*30)
print(f"Results for U({Ux}, {Uy}) and V({Vx}, {Vy}):")
print("="*30)

# Verdict for Basis
if det != 0:
    print(f"✅ Independent: They form a BASIS (Det = {det})")
else:
    print("❌ Dependent: They are COLLINEAR (Det = 0)")

# Verdict for Orthogonality
if sc == 0:
    print("✅ Orthogonal: They are perpendicular (Scalar Product = 0)")
else:
    print(f"⚠️ Not Orthogonal (Scalar Product = {sc})")