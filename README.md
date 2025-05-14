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
&nbsp;&nbsp;&nbsp;&nbsp;\( d_1 \geq d_2 \geq \dots \geq d_n \)  
is graphic **if and only if** the sequence obtained by:

- removing the first term \( d_1 \),
- subtracting 1 from the next \( d_1 \) terms,

is also a graphic sequence, as long as no negative values appear.  
This process continues recursively.

#### Result:
- ✅ All values become 0 → the sequence is **graphic**
- ❌ A negative value appears or not enough elements to subtract from → the sequence is **not graphic**

The `is_graphic()` function is a direct implementation of this algorithm.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/anna-tarasidou/graph-degree-checker.git
cd graph-degree-checker

pip install networkx matplotlib

python main.py

Graph_Checker/
├── graph_checker/
│   ├── generator.py       # Generates random degree sequences
│   ├── checker.py         # Checks if a sequence is graphic
│   ├── constructor.py     # Builds the graph from the sequence
│   ├── visualizer.py      # Visualizes the graph
├── main.py                # Main entry point
└── README.md              # Project documentation

## 📌 To-Do

- [ ] Extend support for different graph types:
  - [ ] Directed graphs
  - [ ] Graphs with self-loops
  - [ ] Multigraphs
- [ ] Add user options to check graphicity under specific categories
- [ ] Improve visualization options
