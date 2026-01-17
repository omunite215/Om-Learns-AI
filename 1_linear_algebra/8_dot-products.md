# Dot Products and Duality
> 📅 **Day**: 27
> 📺 **Video**: [Essence of Linear Algebra, Chapter 9](https://www.youtube.com/watch?v=LyGKycYT2v0)  
> 🎯 **Goal**: Understand the deep connection between dot products and linear transformations

---

## Two Definitions of Dot Product

### Definition 1: Numeric (What You Compute)

Multiply corresponding entries and add:

```
[a, b] · [c, d] = ac + bd

[1, 2, 3] · [4, 5, 6] = 1×4 + 2×5 + 3×6 = 4 + 10 + 18 = 32
```

Simple to compute, but why does this formula exist?

### Definition 2: Geometric (What It Means)

```
v⃗ · w⃗ = |v⃗| × |w⃗| × cos(θ)

where θ is the angle between the vectors
```

Or equivalently:

```
v⃗ · w⃗ = (length of v⃗) × (length of projection of w⃗ onto v⃗)
```

```
        w⃗
       /
      /
     /
    /θ
   ●────────────→ v⃗
   └──────┘
   projection of w⃗ onto v⃗
   
Dot product = |v⃗| × (this projection length)
```

---

## The Mystery

Why do these two definitions give the same answer?

```
Numeric:   ac + bd
Geometric: |v⃗| × |w⃗| × cos(θ)
```

**3Blue1Brown's insight**: The connection comes from **duality** — the relationship between vectors and linear transformations.

---

## Duality: Vectors ↔ Linear Transformations

### The Key Insight

There's a **one-to-one correspondence** between:
- **1×n matrices** (linear transformations from nD → 1D)
- **n-dimensional vectors**

```
The vector [2, 1] corresponds to the 1×2 matrix [2  1]

      ┌   ┐                    ┌     ┐   
      │ 2 │   ←──────────→     │ 2 1 │   
      │ 1 │                    └     ┘   
      └   ┘                              
    2D vector              1×2 matrix (2D → 1D)
```

### Why This Matters

Applying the 1×2 matrix to any vector **is the same as** taking the dot product with [2, 1]:

```
┌     ┐   ┌   ┐
│ 2 1 │ × │ x │  =  2x + 1y  =  [2, 1] · [x, y]
└     ┘   │ y │
          └   ┘

Matrix multiplication = Dot product!
```

---

## Visualizing the 1×n Transformation

A 1×n matrix transforms n-dimensional space onto a **number line**.

### Example: [2, 1] as a Transformation

```
2D space gets "projected" onto a number line:

    y
    ↑
    │   •(1,2) ────────→ 2×1 + 1×2 = 4
    │  /                              │
    │ /                               ▼
    │/                    ────●───────●────────
    ●────→ x                  0       4
   /│                      number line
  / │
```

Every 2D point maps to a single number.

### Where Do Basis Vectors Land?

```
î = [1, 0] → [2, 1] · [1, 0] = 2
ĵ = [0, 1] → [2, 1] · [0, 1] = 1

î lands at 2 on the number line
ĵ lands at 1 on the number line
```

**These are exactly the entries of the vector [2, 1]!**

---

## The Geometric Connection Explained

### Setup

Imagine a unit vector û sitting on the number line embedded in 2D:

```
    y
    ↑
    │
    │     û (unit vector on number line)
    │    /
    │   /
    │  /
    │ /
    ●────────→ x
    
Number line at some angle through origin
```

### Projection as Linear Transformation

Projecting any vector onto this line is a **linear transformation**:
- Lines map to lines (actually points on the number line)
- Origin stays fixed

Since it's linear, it can be represented by a 1×2 matrix!

### The Duality

The 1×2 matrix that performs this projection **is exactly the coordinates of û** (written as a row).

```
û = [u₁, u₂] (as a column vector)

Projection matrix = [u₁  u₂] (as a row)

Projection of v⃗ onto û = [u₁  u₂] × v⃗ = û · v⃗
```

**Dot product IS projection!** (When one vector is a unit vector)

---

## Dot Product Properties (Now They Make Sense!)

### Property 1: Commutative
```
v⃗ · w⃗ = w⃗ · v⃗
```
Projecting v onto w times |w| = Projecting w onto v times |v|

### Property 2: Distributive
```
v⃗ · (w⃗ + u⃗) = v⃗ · w⃗ + v⃗ · u⃗
```
Linear transformation property!

### Property 3: Sign Indicates Direction
```
v⃗ · w⃗ > 0  →  vectors point roughly same direction (θ < 90°)
v⃗ · w⃗ = 0  →  vectors are perpendicular (θ = 90°)
v⃗ · w⃗ < 0  →  vectors point roughly opposite directions (θ > 90°)
```

### Property 4: Dot Product with Self = Length Squared
```
v⃗ · v⃗ = |v⃗|²
```

---

## Special Cases

### Perpendicular Vectors
```
v⃗ · w⃗ = 0

The projection of one onto the other has zero length.
```

### Parallel Vectors (Same Direction)
```
v⃗ · w⃗ = |v⃗| × |w⃗|

cos(0°) = 1, full projection
```

### Parallel Vectors (Opposite Direction)
```
v⃗ · w⃗ = -|v⃗| × |w⃗|

cos(180°) = -1, full negative projection
```

---

## Why This Matters for Machine Learning

| Concept | ML Application |
|---------|----------------|
| Dot product as similarity | Cosine similarity, attention mechanisms |
| Perpendicularity (dot = 0) | Orthogonal features, decorrelated representations |
| Projection | PCA, finding components along directions |
| 1×n matrix as neuron | Single neuron computes dot product + bias! |

### A Single Neuron IS a Dot Product

```python
def neuron(input_vector, weights, bias):
    # This is literally a dot product!
    return activation(np.dot(weights, input_vector) + bias)

# weights · input = projection of input onto weight direction
# Neuron "measures" how much input aligns with its weights
```

### Cosine Similarity

```python
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Returns cos(θ) between vectors
# Used everywhere: word embeddings, recommendation systems, search
```

### Attention Mechanism (Transformers)

```
Attention(Q, K, V) = softmax(Q × Kᵀ / √d) × V
                           └───┘
                        Dot products!

Query · Key = "how much does this query match this key?"
```

### Why Orthogonal Features Matter

```
If features are orthogonal (dot product = 0):
- They capture independent information
- No redundancy
- This is why PCA finds orthogonal principal components!
```

---

## The Duality Principle (Summary)

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   Every n-dimensional VECTOR                            │
│              ↕                                          │
│   corresponds to a LINEAR TRANSFORMATION (nD → 1D)      │
│              ↕                                          │
│   which is computed via DOT PRODUCT                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

This is **duality** — two different perspectives on the same mathematical object.

---

## Key Takeaways

1. **Dot product = matrix multiplication** — `[a b] × [x, y]ᵀ = ax + by = [a,b] · [x,y]`

2. **Geometric meaning is projection** — Dot product measures "how much" one vector goes in another's direction

3. **Duality connects vectors and transformations** — Every vector defines a projection transformation

4. **Sign tells direction relationship** — Positive (same), zero (perpendicular), negative (opposite)

5. **Neurons compute dot products** — This is why neural networks work the way they do!

---

## Self-Check Questions

- [ ] What's `[1, 2, 3] · [4, 5, 6]`?
- [ ] If v⃗ · w⃗ = 0, what's the angle between them?
- [ ] Why is `v⃗ · v⃗ = |v⃗|²`?
- [ ] How does a single neuron use dot products?

![Logo](<../final profile.png>)
