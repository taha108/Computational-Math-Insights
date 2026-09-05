import numpy as np
import matplotlib.pyplot as plt
import os

def run_pagerank():
    print("--- 🕸️ PageRank Engine: The Mathematics of Influence ---")

    # 1. Define the Link Structure (Adjacency Matrix)
    # A link to B, B to C, C to A, D to C
    # Rows/Cols: [A, B, C, D]
    links = np.array([
        [0, 0, 1, 0], # A is linked by C
        [1, 0, 0, 0], # B is linked by A
        [0, 1, 0, 1], # C is linked by B and D
        [0, 0, 0, 0]  # D has no links
    ])

    # 2. Stochastic Matrix (Transition Matrix M)
    # Each column must sum to 1 (Probability distribution)
    # We add a "Damping Factor" (d) to handle dead-ends (teleportation)
    n = len(links)
    d = 0.85
    M = d * (links / np.sum(links, axis=0, keepdims=True) + 1e-10) + (1-d)/n
    M = M / np.sum(M, axis=0) # Re-normalize

    # 3. Power Iteration: Finding the dominant Eigenvector
    # Start with equal importance for everyone
    v = np.ones(n) / n
    history = [v]

    for i in range(20):
        v_next = M @ v
        # Check convergence
        if np.allclose(v, v_next, atol=1e-6):
            print(f"Converged in {i} iterations.")
            break
        v = v_next
        history.append(v)

    print(f"\nFinal Rankings (Importance):\n{v}")
    pages = ['Page A', 'Page B', 'Page C', 'Page D']

    # 4. Visualization
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6), facecolor='#121212')
    
    plt.bar(pages, v, color='cyan', alpha=0.7)
    plt.title("PageRank: Node Importance Distribution", fontsize=15)
    plt.ylabel("Probability Score (Influence)")
    plt.grid(axis='y', alpha=0.1)

    # Save to portfolio
    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, 'pagerank_distribution.png'), facecolor='#121212')
    print("[SUCCESS] Influence map generated.")
    plt.show()

if __name__ == "__main__":
    run_pagerank()