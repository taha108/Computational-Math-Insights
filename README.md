# Computational Mathematics Insights

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/)
[![Math](https://img.shields.io/badge/Focus-Linear%20Algebra%20%26%20Calculus-orange.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository documents my academic journey in Mathematics, focusing on the bridge between theoretical foundations and computational implementation.

## 🎯 Research Vision

I am a Mathematics student (L2) dedicated to mastering **Applied Mathematics and Artificial Intelligence**.

---

## 📂 Project Showcase

### 0. 🦋 Chaos Theory: The Lorenz Attractor
- **Code:** [lorenz_attractor.py](./Chaos_Theory/lorenz_attractor.py)

Modeling a system of three coupled non-linear ordinary differential equations (ODEs). This project visualizes the "Butterfly Effect," where tiny changes in initial conditions lead to vastly different outcomes.

<p align="center">
  <img src="./Chaos_Theory/lorenz_butterfly.png" alt="Lorenz Attractor" width="600">
</p>

---

### 1. 📐 Linear Algebra: Mapping & Transformations
- **Code:** [matrix_viz.py](./Linear-Algebra/matrix_viz.py)

Visualizing how linear mappings $f: \mathbb{R}^2 \to \mathbb{R}^2$ transform the standard basis.

<p align="center">
  <img src="./Linear-Algebra/transformation_plot.png" alt="Matrix Transformation" width="500">
</p>

### 2. 📈 Calculus: Convergence of Taylor Series
- **Code:** [taylor_sin_viz.py](./Calculus/taylor_sin_viz.py)

Analyzing the local approximation of functions through Taylor-Young expansions.

<p align="center">
  <img src="./Calculus/taylor_plot.png" alt="Taylor Approximation" width="500">
</p>

### 3. 🛡️ Linear Algebra: Vector Analysis Tool
- **Code:** [vector_analysis_2d.py](./Linear-Algebra/vector_analysis_2d.py)

An interactive terminal-based tool developed from scratch to evaluate linear independence (Determinant) and orthogonality (Scalar Product) in $\mathbb{R}^2$.

### 4. 🧠 Calculus/Optimization: Hessian Matrix Analysis
- **Code:** [hessian_analysis.py](./Calculus/hessian_analysis.py)

A multivariable calculus tool that automates the search for critical points and classifies them (Local Minimum, Maximum, or Saddle Point) using the Gradient and the Hessian Matrix.

### 5. ♾️ Calculus: Integral Visualization
- **Code:** [integral_visualization.py](./Calculus/integral_visualization.py)

Visualizing the definite integral as the area under a curve $f(x) = x^2$ using numerical integration concepts.

<p align="center">
  <img src="./Calculus/integral_plot.png" alt="Integral Visualization" width="500">
</p>

---

## 📂 Repository Structure

```text
.
├── Linear-Algebra/      # Matrix mappings & Vector analysis
├── Calculus/            # Taylor Series & Multivariable Optimization
└── README.md            # Project documentation
```

## 🛠️ Technical Stack

- **Language:** Python 3.12+
- **Math Engines:** NumPy, SymPy (Symbolic Math)
- **Visualization:** Matplotlib
- **Typesetting:** LaTeX ($\LaTeX$)

## 🗺️ Future Roadmap

- [ ] **Eigenvalues & Eigenvectors:** Visualizing characteristic subspaces.
- [x] **Numerical Optimization:** Hessian-based critical point classification.
- [ ] **Differential Equations:** Modeling dynamic systems using ODE solvers.

---

## 🚀 Getting Started

### Install dependencies
```bash
pip install numpy matplotlib sympy
```

### Clone and run
```bash
git clone https://github.com/taha108/Computational-Math-Insights.git
python Calculus/hessian_analysis.py
```