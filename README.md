## 🎯 Graph Degree Sequence Generator & Visualizer
#### Author: Anna Tarasidou

### Overview
A terminal-based Python tool for exploring the relationship between degree sequences and graph construction.
It provides an interactive way to understand and visualize graphic sequences through clean and modular code.

---
### Features
- Generates a random degree sequence for a graph of a chosen order
- Checks whether the sequence is graphic (i.e., realizable as a simple undirected graph)
- Constructs the corresponding graph if the sequence is valid
- Visualizes the result using NetworkX and Matplotlib

### 💡 Example Usage

1. The user enters the desired graph order (e.g., 6 nodes).
2. A random degree sequence is generated.
3. The Havel–Hakimi algorithm checks if the sequence is graphic.
4. If valid, the graph is automatically constructed and displayed.
---

### 📐 How Graphicity Is Determined
This project implements the **Havel–Hakimi Theorem** to verify whether a degree sequence can represent a simple undirected graph.

### 🔍 Havel–Hakimi Theorem (Simplified)

Given a non-increasing sequence of non-negative integers **(d₁ ≥ d₂ ≥ ... ≥ dₙ)**,
the sequence is graphic if the following recursive process ends with all zeros:

1. Remove the first term d₁.
2. Subtract 1 from each of the next d₁ terms.
3. If any term becomes negative → the sequence is not graphic.
4. Repeat until all values are zero.

**Outcome:**

All zeros → Graphic sequence

Negative or incomplete step → Not graphic

The `is_graphic()` function provides a direct and efficient implementation of this process.

---
### 📂 Project Structure
```bash
python main.py

Graph_Checker/
├── graph_checker/
│   ├── generator.py       # Generates random degree sequences
│   ├── checker.py         # Checks if a sequence is graphic
│   ├── constructor.py     # Builds the graph from the sequence
│   ├── visualizer.py      # Visualizes the graph
├── main.py                # Main entry point
└── README.md              # Project documentation

```
### ⚙️ Requirements
Requires **networkx** and **matplotlib**

### ▶️ Run the Program
```bash
python main.py
```
