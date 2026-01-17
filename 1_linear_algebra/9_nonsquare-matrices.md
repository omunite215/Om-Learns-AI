# Nonsquare Matrices as Transformations Between Dimensions
> 📅 **Day**: 27
> 📺 **Video**: [Essence of Linear Algebra, Chapter 8](https://www.youtube.com/watch?v=v8VSDg_WQlA)  
> 🎯 **Goal**: Understand what nonsquare matrices do — transforming between different dimensional spaces

---

## The Core Idea

Nonsquare matrices represent transformations **between spaces of different dimensions**.

```
3×2 matrix: Takes 2D vectors → outputs 3D vectors
2×3 matrix: Takes 3D vectors → outputs 2D vectors
```

This is fundamentally different from square matrices, which transform within the same dimension.

---

## Reading Nonsquare Matrices

### The Rule (Same as Before!)

**Columns = where basis vectors land**

But now input and output dimensions differ.

### Example: 3×2 Matrix

```
┌      ┐
│ 2  0 │
│ 1  1 │   3 rows × 2 columns
│ 0  1 │
└      ┘

Input: 2D (because 2 columns → 2 basis vectors: î, ĵ)
Output: 3D (because 3 rows → landing spots are 3D vectors)

î = [1,0] lands on [2, 1, 0]  (first column)
ĵ = [0,1] lands on [0, 1, 1]  (second column)
```

**This matrix takes a 2D plane and embeds it into 3D space.**

### Example: 2×3 Matrix

```
┌         ┐
│ 1  2  1 │   2 rows × 3 columns
│ 0  1  1 │
└         ┘

Input: 3D (3 columns → 3 basis vectors: î, ĵ, k̂)
Output: 2D (2 rows → landing spots are 2D vectors)

î = [1,0,0] lands on [1, 0]
ĵ = [0,1,0] lands on [2, 1]
k̂ = [0,0,1] lands on [1, 1]
```

**This matrix projects 3D space down to a 2D plane.**

---

## Geometric Interpretations

### Going Up in Dimension (e.g., 3×2)

```
2D plane → embedded in 3D space

    2D                      3D
    
    │                        │  /
    │     ──[3×2]──→        │ /  (plane sitting in 3D)
────┼────                ───┼/────
    │                      /│
                          / │
```

The 2D plane doesn't fill all of 3D — it's a **flat surface** within the larger space.

**Column space**: A 2D plane inside 3D (at most rank 2)

### Going Down in Dimension (e.g., 2×3)

```
3D space → projected onto 2D plane

    3D                      2D
   /│                        │
  / │     ──[2×3]──→        │
 /  │                   ────┼────
────┼────                   │
    │
```

3D gets "flattened" — information is lost! Multiple 3D points can land on the same 2D point.

**Null space**: Non-trivial! A line (or more) of 3D vectors map to origin.

---

## Matrix Dimensions: A Quick Reference

```
Matrix size: m × n

m = number of rows = dimension of OUTPUT
n = number of columns = dimension of INPUT
```

| Matrix | Input Dim | Output Dim | What it Does |
|--------|-----------|------------|--------------|
| 2×2 | 2D | 2D | Transform within 2D |
| 3×3 | 3D | 3D | Transform within 3D |
| 3×2 | 2D | 3D | Embed 2D into 3D |
| 2×3 | 3D | 2D | Project 3D onto 2D |
| 1×3 | 3D | 1D | Project onto a line |
| 3×1 | 1D | 3D | Embed line into 3D |

---

## Matrix Multiplication Revisited

For multiplication A × B to be valid:

```
A is m × n
B is n × p
───────────
     └─┬─┘
       └── These must match!

Result: m × p
```

### Why?

B transforms p-dimensional input to n-dimensional output.
A transforms n-dimensional input to m-dimensional output.

```
p-dim ──[B]──→ n-dim ──[A]──→ m-dim
         └───────────────────────┘
              A × B: p-dim → m-dim
```

### Example

```
A: 2×3 (takes 3D → 2D)
B: 3×4 (takes 4D → 3D)

A × B: 2×4 (takes 4D → 2D)

4D ──[B]──→ 3D ──[A]──→ 2D
```

---

## Rank of Nonsquare Matrices

The **rank** is still the dimension of the column space.

```
Maximum possible rank = min(m, n)
```

### Examples

```
3×2 matrix: max rank = 2 (at most a 2D plane in 3D)
2×3 matrix: max rank = 2 (output is 2D, can't exceed that)
5×3 matrix: max rank = 3
3×5 matrix: max rank = 3
```

**Full rank** means the matrix achieves this maximum.

---

## Special Case: 1×n Matrices (Row Vectors)

A 1×n matrix transforms n-dimensional vectors to **1D (a number)**.

```
┌         ┐   ┌   ┐
│ 1  2  3 │ × │ x │  =  [1x + 2y + 3z]  (a single number!)
└         ┘   │ y │
              │ z │
              └   ┘
```

This is the **dot product** in disguise! (More in Chapter 9)

---

## Special Case: m×1 Matrices (Column Vectors)

An m×1 matrix transforms **1D (a number) to m-dimensional space**.

```
┌   ┐        ┌    ┐
│ 2 │        │ 2t │
│ 3 │ × [t] =│ 3t │
│ 1 │        │ 1t │
└   ┘        └    ┘
```

This traces out a **line** through the origin in m-dimensional space.

---

## Why This Matters for Machine Learning

| Concept | ML Application |
|---------|----------------|
| Dimensionality reduction (m < n) | PCA, autoencoders (compress data) |
| Dimensionality expansion (m > n) | Feature expansion, embeddings |
| Layer shape mismatch | Neural network layer dimensions |
| Projection | Mapping high-D data to visualizable 2D/3D |

### Neural Network Layers

```python
# Input layer: 784 features (28×28 image flattened)
# Hidden layer: 256 neurons
# Output layer: 10 classes

W1: 256 × 784  # 784D → 256D (compression)
W2: 10 × 256   # 256D → 10D (compression to classes)

# Each layer is a nonsquare matrix transforming between dimensions!
```

### The Dimension Journey

```
Image        Layer 1      Layer 2      Output
[784] ────→ [256] ────→ [10]

  784×1       256×784      10×256
  vector      matrix       matrix
```

### Embedding Layers

```python
# Word embedding: maps word index to dense vector
# Vocabulary: 10,000 words
# Embedding dimension: 300

embedding_matrix: 300 × 10000

# One-hot word vector (10000D) → dense embedding (300D)
# This is a 300×10000 matrix multiplication!
```

### Autoencoder Structure

```
Input ──[Encoder]──→ Bottleneck ──[Decoder]──→ Reconstruction
784D     784→64        64D          64→784        784D

Encoder: 64 × 784 (compress)
Decoder: 784 × 64 (expand)
```

---

## Key Takeaways

1. **Columns still = where basis vectors land** — Same interpretation, different dimensions

2. **m×n: n-dim input, m-dim output** — Rows = output dim, columns = input dim

3. **Going down loses information** — Projection to lower dimension has non-trivial null space

4. **Going up embeds in larger space** — Lower-dimensional object sitting in higher-dimensional space

5. **Neural networks chain these** — Each layer is a (usually nonsquare) matrix transformation

---

## Self-Check Questions

- [ ] What does a 5×3 matrix do to a 3D vector?
- [ ] Can a 2×3 matrix have rank 3? Why or why not?
- [ ] If A is 4×3 and B is 3×5, what size is AB?
- [ ] Why do neural network layers often reduce dimensionality toward the output?

![Logo](<../final profile.png>)