# 🎯 Graph Degree Sequence Generator & Visualizer

A simple yet powerful Python tool that:

- ✅ Generates a random degree sequence for a graph of a given order
- ✅ Checks whether the sequence is *graphic* (i.e., realizable as a simple undirected graph)
- ✅ Constructs the corresponding graph if the sequence is graphic
- ✅ Visualizes the graph using `networkx` and `matplotlib`

---

## 💡 Example Usage

1. User enters the desired graph order (e.g., 6 nodes)
2. A random degree sequence is generated
3. The sequence is checked for graphicity using the **Havel–Hakimi algorithm**
4. If the sequence is graphic, the graph is constructed and displayed

---

## 📐 How Graphicity Is Checked

This project uses the **Havel–Hakimi Theorem** to determine whether a degree sequence is *graphic* — i.e., whether it can represent a simple undirected graph.

### 🔍 Havel–Hakimi Theorem (Simplified)

A non-increasing sequence of non-negative integers  
  **( d₁ ≥ d₂ ≥ ... ≥ dₙ )**  
is **graphic** (i.e., it can represent the degree sequence of a simple undirected graph) **if and only if** the following recursive process ends in a sequence of all zeros:

1. Remove the first term **d₁**.
2. Subtract 1 from each of the next **d₁** terms.
3. If any value becomes negative, the sequence is **not graphic**.
4. Repeat the process with the new sequence.

If the process completes without producing negative numbers and results in all zeros, the original sequence is **graphic**.

#### Result:
- ✅ All values become 0 → the sequence is **graphic**
- ❌ A negative value appears or not enough elements to subtract from → the sequence is **not graphic**

The `is_graphic()` function is a direct implementation of this algorithm.

---
## 🚀 Installation


## 1. Clone the repository

git clone https://github.com/anna-tarasidou/graph-degree-checker.git
cd graph-degree-checker

## 2. Install dependencies

pip install networkx matplotlib


### ▶️ Run the Program
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

### 📌 To-Do

- [ ] Extend support for different graph types:
  - [ ] Directed graphs
  - [ ] Graphs with self-loops
  - [ ] Multigraphs
- [ ] Add user options to check graphicity under specific categories
- [ ] Improve visualization options
