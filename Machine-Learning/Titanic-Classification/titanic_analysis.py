import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os

def run_titanic_study():
    print("--- 🚢 Titanic Survival Prediction: Logistic Regression Study ---")

    # 1. Load Dataset
    df = sns.load_dataset('titanic')
    
    # 2. Preprocessing (Handling categorical variables and missing values)
    # Using 'pclass', 'sex' (encoded), 'age' (imputed) and 'fare'
    df['sex'] = df['sex'].map({'female': 1, 'male': 0})
    df['age'] = df['age'].fillna(df['age'].mean())
    
    features = ['pclass', 'sex', 'age', 'fare']
    X = df[features]
    y = df['survived']

    # 3. Model Training
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # 4. Accuracy Evaluation
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    print(f"Model Generalization Accuracy: {acc*100:.2f}%")

# 5. Visualization: High-Contrast Dark Theme for Research Presentation
    plt.style.use('dark_background') # Set base theme to dark
    plt.figure(figsize=(10, 6), facecolor='#121212')
    
    ax = plt.gca()
    ax.set_facecolor('#1e1e1e') # Slightly lighter grey for the plot area

    # Using 'magma' palette for better contrast between classes
    sns.countplot(x='sex', hue='survived', data=df, palette='magma')

    # Titling and Labeling
    plt.title("Titanic Survival Analysis: Impact of Gender", color='white', fontsize=15, pad=20)
    plt.xlabel("Gender (0 = Male, 1 = Female)", color='white', fontsize=12)
    plt.ylabel("Passenger Count", color='white', fontsize=12)
    
    # Custom Legend configuration for clarity
    legend = plt.legend(title='Outcome', labels=['Perished', 'Survived'], 
                        facecolor='#1e1e1e', edgecolor='white')
    plt.setp(legend.get_texts(), color='white') # Set legend text color
    plt.setp(legend.get_title(), color='white') # Set legend title color

    # Adding a subtle grid for better readability
    plt.grid(axis='y', alpha=0.1)

    # Save output with tight bounding box to prevent label clipping
    script_dir = os.path.dirname(__file__)
    output_path = os.path.join(script_dir, 'survival_plot.png')
    plt.savefig(output_path, facecolor='#121212', bbox_inches='tight')
    
    print(f"\n[SUCCESS] Professional high-contrast plot saved at: {output_path}")
    plt.show()

if __name__ == "__main__":
    run_titanic_study()