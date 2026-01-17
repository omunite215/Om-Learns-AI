# Matrix Multiplication as Composition
> 📅 **Day**: 25
> 📺 **Video**: [Essence of Linear Algebra, Chapter 4](https://www.youtube.com/watch?v=XkY2DOUCWMU)  
> 🎯 **Goal**: Understand matrix multiplication as applying one transformation after another

---

## The Core Idea

Matrix multiplication represents **composition** — applying one transformation, then another.

```
First apply M₁, then apply M₂:

    v → [M₁] → [M₂] → result

This is the same as:

    v → [M₂ × M₁] → result
```

**One matrix that captures the combined effect of both transformations.**

---

## Composition: One Transformation After Another

### Example: Rotate, then Shear

**Step 1: Rotation (90° counterclockwise)**
```
Rotation matrix R:
┌       ┐
│ 0  -1 │
│ 1   0 │
└       ┘

î = [1,0] → [0, 1]
ĵ = [0,1] → [-1, 0]
```

**Step 2: Shear (after rotation)**
```
Shear matrix S:
┌      ┐
│ 1  1 │
│ 0  1 │
└      ┘

î = [1,0] → [1, 0]
ĵ = [0,1] → [1, 1]
```

**Combined effect?** Track where î and ĵ end up after BOTH transformations.

---

## How to Compute the Composition

To find `M₂ × M₁`, ask: **Where do î and ĵ land after applying M₁, then M₂?**

### Step-by-Step Process

```
M₂ × M₁ = ?

1. Apply M₁ to î → get new vector
2. Apply M₂ to that result → first column of answer

3. Apply M₁ to ĵ → get new vector  
4. Apply M₂ to that result → second column of answer
```

### Worked Example: Shear × Rotation

```
S × R = ?

S = ┌      ┐    R = ┌       ┐
    │ 1  1 │        │ 0  -1 │
    │ 0  1 │        │ 1   0 │
    └      ┘        └       ┘

First column (where î lands):
  R sends î to [0, 1]
  S sends [0, 1] to: 0·[1,0] + 1·[1,1] = [1, 1]
  
Second column (where ĵ lands):
  R sends ĵ to [-1, 0]
  S sends [-1, 0] to: -1·[1,0] + 0·[1,1] = [-1, 0]

Result:
S × R = ┌        ┐
        │  1  -1 │
        │  1   0 │
        └        ┘
```

---

## The Formula

For two 2×2 matrices:

```
┌      ┐   ┌      ┐       ┌                    ┐
│ a  b │ × │ e  f │   =   │ ae+bg    af+bh    │
│ c  d │   │ g  h │       │ ce+dg    cf+dh    │
└      ┘   └      ┘       └                    ┘
```

**Pattern for each entry:**
```
Result[row i, col j] = (row i of left matrix) · (col j of right matrix)
```

This is the **dot product** of a row and column.

### Visual Pattern

```
        ┌───────┐
        │ e   f │
        │ g   h │
        └───────┘
           ↓ ↓
┌───────┐ ┌───────┐
│→ a  b │ │ ·   · │   Row • Column = Entry
│  c  d │ │ ·   · │
└───────┘ └───────┘
```

---

## Order Matters!

**Matrix multiplication is NOT commutative.**

```
M₂ × M₁  ≠  M₁ × M₂  (in general)
```

### Why?

Applying Rotation then Shear gives a different result than Shear then Rotation.

```
Rotate then Shear:          Shear then Rotate:

    □                           □
    ↓ rotate                    ↓ shear
    ◇                           ▱
    ↓ shear                     ↓ rotate
    ◇̸                           ◊

Different final shapes!
```

**Reading order**: `M₂ × M₁` means "apply M₁ first, then M₂" (right to left!)

---

## Properties of Matrix Multiplication

### Associativity (YES)
```
(AB)C = A(BC)

You can group however you want — same result.
```

### Commutativity (NO)
```
AB ≠ BA (usually)

Order matters!
```

### Distributivity (YES)
```
A(B + C) = AB + AC
```

---

## Extending to Multiple Transformations

Chain as many as you want:

```
M₄ × M₃ × M₂ × M₁

Applied right to left: M₁ first, then M₂, then M₃, then M₄
```

**This is exactly how neural networks stack layers!**

---

## Why This Matters for Machine Learning

| Concept | ML Application |
|---------|----------------|
| Composition | Stacking neural network layers |
| Order matters | Layer order affects output (architecture design) |
| Associativity | Can pre-compute weight combinations |
| Single combined matrix | Compressing multiple linear layers |

### Neural Network as Composition

```python
# Three layer network (ignoring activation functions for now)
def network(x):
    x = W1 @ x  # First transformation
    x = W2 @ x  # Second transformation  
    x = W3 @ x  # Third transformation
    return x

# Mathematically equivalent to:
def network_combined(x):
    W_combined = W3 @ W2 @ W1  # One matrix!
    return W_combined @ x
```

**Important insight**: Without activation functions, stacking linear layers is pointless — it's just one big linear transformation. This is why we need non-linear activations!

### Transformation Pipeline

```
Input      Layer 1    Layer 2    Layer 3    Output
[784] ──→ [256] ──→ [128] ──→ [10]

Each arrow is a matrix multiplication (linear transformation).
The whole network is a composition of transformations.
```

---

## Key Takeaways

1. **Matrix multiplication = composition** — Applying transformations in sequence

2. **Right to left reading** — `AB` means "apply B first, then A"

3. **Order matters** — `AB ≠ BA` in general

4. **Track the basis vectors** — Where do î and ĵ end up after all transformations?

5. **Row × column = entry** — The computational rule follows from the geometric meaning

---

## Self-Check Questions

- [ ] If A rotates 90° and B reflects over x-axis, what does AB do? What about BA?
- [ ] Why is `(AB)C = A(BC)` true geometrically?
- [ ] Can you compute `[[1,2],[3,4]] × [[0,1],[1,0]]` by hand?
- [ ] Why do neural networks need non-linear activation functions?

![Logo](<../final profile.png>)