import random
import numpy as np

# Target Concept
TARGET = "MATHEMATICAL OPTIMIZATION 2026"
GENES = " ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def get_fitness(guess):
    """Calculates the alignment score between the guess and the target."""
    score = sum(1 for g, t in zip(guess, TARGET) if g == t)
    return score / len(TARGET)

def mutate(parent):
    """Introduces a random genetic variation."""
    index = random.randrange(len(parent))
    child = list(parent)
    child[index] = random.choice(GENES)
    return "".join(child)

def run_evolution():
    print(f"--- 🧬 Evolutionary Computing Lab ---")
    print(f"Targeting convergence toward: '{TARGET}'\n")
    
    # Initialization with random noise
    best_guess = "".join(random.choice(GENES) for _ in range(len(TARGET)))
    best_fitness = get_fitness(best_guess)
    generation = 0

    while best_fitness < 1.0:
        generation += 1
        # Mutation process
        child = mutate(best_guess)
        child_fitness = get_fitness(child)

        # Selection: Only keep the mutation if it improves the system
        if child_fitness > best_fitness:
            best_guess = child
            best_fitness = child_fitness
            print(f"Gen {generation:04d} | Fitness: {best_fitness:.2f} | Current: '{best_guess}'")

    print(f"\n[STABILITY REACHED] Optimization completed in {generation} generations.")

if __name__ == "__main__":
    run_evolution()