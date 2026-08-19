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

### 6. 🎲 Probability: Stochastic Random Walk
- **Code:** [random_walk_drift.py](./Probability/random_walk_drift.py)

Simulation of a discrete-time random walk with a positive drift. This project illustrates how deterministic effort can overcome stochastic volatility over time.

<p align="center">
  <img src="./Probability/stochastic_process.png" alt="Stochastic Process" width="600">
</p>

### 7. 💎 Linear Algebra: Eigen-Analysis Geometry
- **Code:** [eigen_analysis_2d.py](./Linear-Algebra/eigen_analysis_2d.py)

Visualizing the geometric essence of Eigenvalues and Eigenvectors. This project shows how a matrix $A$ transforms a unit circle into an ellipse, highlighting the invariant directions (Eigenvectors) and their scaling factors (Eigenvalues).

<p align="center">
  <img src="./Linear-Algebra/eigen_geometry.png" alt="Eigen Geometry" width="500">
</p>

### 8. 📈 Calculus: Power Series Convergence Analyzer
- **Code:** [convergence_analyzer.py](./Calculus/convergence_analyzer.py)

An automated tool to compute the **Radius of Convergence** $R$ of a power series $\sum a_n x^n$. It uses D'Alembert's Ratio Test through symbolic computation.

### 9. 💎 Advanced Algebra & Calculus: Spectral Theory & Symbolic Integration
- **Code:** [spectral_convergence.py](./Calculus/spectral_convergence.py)

A dual-purpose scientific module demonstrating the power of symbolic computation in high-level mathematics.

- **Spectral Analysis:** Automated verification of matrix symmetry and application of the **Spectral Theorem** to find orthogonal bases and eigenvalues.
- **Generalized Calculus:** Symbolic evaluation of improper integrals (Riemann convergence at $+\infty$), including the Gaussian integral $\int_{0}^{+\infty} e^{-t^2} dt$.
- **Tool:** Using `SymPy` for exact mathematical proofs rather than numerical approximations.

---

## 📂 Repository Structure

```text
.
├── Linear-Algebra/      # Matrix mappings & Vector analysis
├── Calculus/            # Taylor Series & Multivariable Optimization
├── Probability/         # Stochastic processes & Random walks
└── README.md            # Project documentation
```

## 🛠️ Technical Stack

- **Language:** Python 3.12+
- **Math Engines:** NumPy, SymPy (Symbolic Math)
- **Visualization:** Matplotlib
- **Typesetting:** LaTeX ($\LaTeX$)

## 🗺️ Future Roadmap

- [x] **Eigenvalues & Eigenvectors:** Visualizing characteristic subspaces.
- [x] **Numerical Optimization:** Hessian-based critical point classification.
- [x] **Differential Equations:** Modeling dynamic systems using ODE solvers.

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