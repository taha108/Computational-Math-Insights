import random
import numpy as np
import matplotlib.pyplot as plt
import os

# 1. Constants for the Optimization Task
TARGET = "STOCHASTIC CONVERGENCE 2026"
GENES = " ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def get_fitness(guess):
    """Measures the accuracy of the current individual."""
    score = sum(1 for g, t in zip(guess, TARGET) if g == t)
    return score / len(TARGET)

def mutate(parent):
    """Applies a random mutation to the gene sequence."""
    index = random.randrange(len(parent))
    child = list(parent)
    child[index] = random.choice(GENES)
    return "".join(child)

def run_visual_evolution():
    print(f"--- 🧬 Module 29: Heuristic Analysis ---")
    
    # Initialization
    best_guess = "".join(random.choice(GENES) for _ in range(len(TARGET)))
    best_fitness = get_fitness(best_guess)
    
    # Data tracking for research visualization
    history = [best_fitness]
    generation = 0

    # Optimization Loop
    while best_fitness < 1.0:
        generation += 1
        child = mutate(best_guess)
        child_fitness = get_fitness(child)

        if child_fitness > best_fitness:
            best_guess = child
            best_fitness = child_fitness
            print(f"Gen {generation:04d} | Fitness: {best_fitness:.2f} | Result: '{best_guess}'")
        
        history.append(best_fitness)

    # --- Scientific Visualization ---
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6), facecolor='#121212')
    ax = plt.gca()
    ax.set_facecolor('#121212')

    plt.plot(history, color='cyan', lw=2, label='Fitness (Convergence)')
    
    plt.title("Stochastic Optimization: Fitness Evolution", color='white', fontsize=14)
    plt.xlabel("Generations (Iterations)", color='white')
    plt.ylabel("Fitness Score (0 to 1)", color='white')
    plt.grid(alpha=0.1)
    plt.legend()

    # Save visualization to the local folder
    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, 'convergence_analysis.png'), facecolor='#121212')
    print(f"\n[DONE] Strategy evolved in {generation} steps. Plot saved.")
    plt.show()

if __name__ == "__main__":
    run_visual_evolution()