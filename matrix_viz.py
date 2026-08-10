import matplotlib.pyplot as plt
import numpy as np

# Ta matrice de transformation (Exemple : une rotation ou un étalement)
A = np.array([[2, 1], [1, 2]])

# Un vecteur unitaire
v = np.array([1, 0])

# On applique la matrice (l'application linéaire)
v_transformed = A.dot(v)

# Visualisation
plt.quiver([0, 0], [0, 0], [v[0], v_transformed[0]], [v[1], v_transformed[1]], 
           angles='xy', scale_units='xy', scale=1, color=['r', 'b'])
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.grid()
plt.title("Rouge: Départ | Bleu: Après transformation (f)")
plt.savefig('transformation_plot.png')
plt.show()
