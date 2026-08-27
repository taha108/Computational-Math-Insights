import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
import os

def evaluate_ai_performance(y_true, y_pred):
    print("--- 📊 AI Research Audit: Performance Metrics ---")

    # 1. Generate the Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)
    
    # 2. Detailed Classification Report (Precision, Recall, F1)
    report = classification_report(y_true, y_pred, zero_division=0)
    print("\nDetailed Scientific Report:")
    print(report)

    # 3. Visualization: Heatmap of Confusion
    plt.figure(figsize=(10, 8), facecolor='#121212')
    sns.heatmap(cm, annot=True, fmt='d', cmap='magma', cbar=False)
    
    plt.title("MNIST Confusion Matrix: Identifying Weak Spots", color='white', fontsize=15)
    plt.xlabel("Predicted Label", color='white')
    plt.ylabel("Actual Label", color='white')
    
    # Save the audit for GitHub
    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, 'confusion_matrix.png'), facecolor='#121212')
    print("\n[ANALYSIS COMPLETE] Confusion Matrix saved as png.")
    plt.show()

# --- Integration with MNIST results ---
if __name__ == "__main__":
    # Simulate some results for the demo (Actual vs Predicted)
    y_test_example = [3, 4, 4, 7, 1, 8, 2, 2]
    y_pred_example = [8, 7, 4, 7, 1, 8, 2, 2] # Note the 3->8 and 4->7 errors
    
    evaluate_ai_performance(y_test_example, y_pred_example)