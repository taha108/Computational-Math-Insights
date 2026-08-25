import numpy as np
import matplotlib.pyplot as plt
import os

def euclidean_distance(p1, p2):
    # Pure Pythagorean theorem: sqrt(sum((xi - yi)^2))
    return np.sqrt(np.sum((p1 - p2)**2))

def run_k_means():
    print("--- 🎯 K-Means Clustering: Unsupervised Learning from Scratch ---")

    # 1. Generate random data points (3 groups/clusters)
    X = np.vstack([
        np.random.randn(30, 2) + [2, 2],
        np.random.randn(30, 2) + [7, 7],
        np.random.randn(30, 2) + [2, 7]
    ])

    # 2. Algorithm Parameters
    K = 3 # We want to find 3 groups
    centroids = X[np.random.choice(len(X), K, replace=False)] # Pick 3 random starting points
    
    # 3. Optimization Loop
    for _ in range(10): # 10 iterations are usually enough for simple data
        # Step A: Assign each point to the closest centroid
        clusters = [[] for _ in range(K)]
        for x in X:
            distances = [euclidean_distance(x, c) for c in centroids]
            closest_idx = np.argmin(distances)
            clusters[closest_idx].append(x)
        
        # Step B: Update centroids (Move them to the center of their group)
        for i in range(K):
            if clusters[i]:
                centroids[i] = np.mean(clusters[i], axis=0)

    # 4. Final Visualization
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 7), facecolor='#121212')
    
    colors = ['cyan', '#FF5733', '#32CD32']
    for i, group in enumerate(clusters):
        group = np.array(group)
        plt.scatter(group[:, 0], group[:, 1], color=colors[i], label=f'Group {i+1}')
    
    plt.scatter(centroids[:, 0], centroids[:, 1], color='white', marker='X', s=200, label='Centroids')
    
    plt.title("K-Means Clustering: Emergent Order from Chaos", fontsize=15)
    plt.legend()
    plt.grid(alpha=0.1)

    # Save to portfolio
    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, 'clustering_plot.png'), facecolor='#121212')
    print("Clustering Map saved.")
    plt.show()

if __name__ == "__main__":
    run_k_means()