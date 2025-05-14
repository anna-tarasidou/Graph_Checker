# 🎯 Graph Degree Sequence Generator & Visualizer

A simple Python tool that:

- Generates a random degree sequence for a graph of a given order.
- Checks whether the sequence is graphic (i.e., realizable as a simple undirected graph).
- Constructs the corresponding graph if the sequence is graphic.
- Visualizes the graph using `networkx` and `matplotlib`.

---

## 💡 Example Usage

1. The user enters the order of the graph
2. A random degree sequence is generated
3. The sequence is checked for graphicity
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

is also a graphic sequence (as long as no negative values appear). This process repeats recursively.

If, at any step:

- All terms become 0 → the sequence is **graphic** ✅  
- A negative value appears or there aren't enough terms → the sequence is **not graphic** ❌

The function `is_graphic()` in the code is a direct implementation of this algorithm.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/anna-tarasidou/graph-degree-checker.git
cd graph-degree-checker

### 2. Install dependencies

```bash
pip install networkx matplotlib

## ▶️ How to Run

```bash
python main.py

# 📁 Project Structure
graph-degree-checker/
├── graph_checker/
│   ├── __init__.py
│   ├── generator.py       # Generates random degree sequences
│   ├── checker.py         # Checks if a sequence is graphic
│   ├── constructor.py     # Builds the graph from the sequence
│   ├── visualizer.py      # Visualizes the graph
├── tests/
│   └── test_checker.py    # Unit tests for the checker
├── main.py                # Main program
├── requirements.txt       # Dependencies
├── README.md              # This file
└── LICENSE



#### TO-DO
 Επέκταση για Κατηγορίες Γραφημάτων
Αν ο χρήστης θέλει να ελέγξει την γραφικότητα σε συγκεκριμένους τύπους γραφημάτων, όπως:

Απλοί γράφοι, κατευθυνόμενοι γράφοι, γραφήματα με αυτοσύνδεση.

Παράλληλα, μπορείς να ενσωματώσεις κριτήρια για ειδικούς τύπους γραφημάτων.