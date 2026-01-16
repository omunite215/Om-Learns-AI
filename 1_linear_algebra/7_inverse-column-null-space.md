# Inverse Matrices, Column Space, and Null Space
> 📅 **Day**: 26
> 📺 **Video**: [Essence of Linear Algebra, Chapter 7](https://www.youtube.com/watch?v=uQhTuRlWMxw)  
> 🎯 **Goal**: Understand when transformations can be reversed, and what matrices "can reach"

---

## Linear Systems of Equations

Linear algebra's core purpose: **solving systems of equations**.

```
2x + 5y + 3z = -3
4x + 0y + 8z = 0
1x + 3y + 0z = 2
```

This can be written as a **matrix equation**:

```
┌         ┐   ┌   ┐     ┌    ┐
│ 2  5  3 │   │ x │     │ -3 │
│ 4  0  8 │ × │ y │  =  │  0 │
│ 1  3  0 │   │ z │     │  2 │
└         ┘   └   ┘     └    ┘

    A      ×    x⃗    =    v⃗
```

**Question**: Given A and v⃗, find x⃗.

---

## The Geometric View

Finding x⃗ means: **which vector, when transformed by A, lands on v⃗?**

```
    x⃗  ──[A]──→  v⃗

"What input gives this output?"
```

This is "playing the transformation in reverse."

---

## Inverse Matrices

The **inverse of A** (written A⁻¹) is the transformation that **undoes A**.

```
A⁻¹ × A = I  (identity — does nothing)
A × A⁻¹ = I
```

### Solving with Inverse

If A⁻¹ exists:
```
A × x⃗ = v⃗
A⁻¹ × A × x⃗ = A⁻¹ × v⃗
I × x⃗ = A⁻¹ × v⃗
x⃗ = A⁻¹ × v⃗
```

**Just multiply both sides by A⁻¹!**

### Geometric Intuition

```
If A rotates 30° clockwise:
   A⁻¹ rotates 30° counterclockwise

If A scales by 2:
   A⁻¹ scales by 1/2

If A shears right:
   A⁻¹ shears left
```

---

## When Does A⁻¹ Exist?

**A⁻¹ exists if and only if det(A) ≠ 0**

### Why?

If det(A) = 0, the transformation **squishes space** to a lower dimension.

```
2D squished to a line:

Before:          After A:
  •  •  •        
  •  •  •   →      •••••••  (a line)
  •  •  •        

Multiple points land on the same spot!
You can't reverse this — which original point was it?
```

**No function can "unsquish"** — information is lost.

### The Two Cases

| det(A) | Invertible? | Meaning |
|--------|-------------|---------|
| ≠ 0 | Yes | Full rank, unique solution exists |
| = 0 | No | Rank deficient, squishes space |

---

## Column Space

The **column space** of A is the set of all possible outputs of the transformation.

```
Column space = Span of the columns of A
             = All vectors of the form A × x⃗
             = "Where can this transformation reach?"
```

### Examples

**Full rank (det ≠ 0):**
```
A = ┌      ┐
    │ 1  0 │   Columns: [1,0] and [0,1]
    │ 0  1 │   
    └      ┘   
    
Column space = span{[1,0], [0,1]} = ALL of 2D
```

**Rank deficient (det = 0):**
```
A = ┌      ┐
    │ 1  2 │   Columns: [1,1] and [2,2]
    │ 1  2 │   
    └      ┘   Second column = 2 × first column!
    
Column space = span{[1,1]} = a LINE through origin
```

### Column Space Dimension = Rank

The **rank** of a matrix is the dimension of its column space.

| Matrix | Rank | Column Space |
|--------|------|--------------|
| 2×2, det ≠ 0 | 2 | All of 2D |
| 2×2, det = 0 | 1 | A line |
| 3×3, det ≠ 0 | 3 | All of 3D |
| 3×3, det = 0 | 1 or 2 | A line or plane |

---

## Null Space (Kernel)

The **null space** of A is the set of all vectors that land on the origin.

```
Null space = { x⃗ : A × x⃗ = 0⃗ }
           = "What gets squished to zero?"
```

### Full Rank Case

If det(A) ≠ 0:
```
Null space = { 0⃗ }  (only the zero vector)
```

Only the origin maps to the origin. Nothing gets squished.

### Rank Deficient Case

If det(A) = 0, the null space contains more than just 0⃗.

```
A = ┌      ┐
    │ 1  2 │   
    │ 1  2 │   
    └      ┘   

A × [-2, 1] = [1×(-2) + 2×1, 1×(-2) + 2×1] = [0, 0]

Null space = all multiples of [-2, 1] = a LINE
```

**Intuition**: The null space is everything that gets "squished" to zero during the transformation.

---

## The Big Picture

```
                    ┌─────────────────────────────────┐
                    │           All inputs            │
                    │              x⃗                  │
                    └───────────────┬─────────────────┘
                                    │
                                    ▼ A ×
                    ┌─────────────────────────────────┐
                    │         Column Space            │
                    │    (all possible outputs)       │
                    └─────────────────────────────────┘

    Null Space = inputs that map to origin (get "lost")
    Column Space = all reachable outputs
```

### Relationship

```
dim(Column Space) + dim(Null Space) = number of columns

"Rank" + "Nullity" = n
```

---

## Solving Ax⃗ = v⃗: The Three Cases

### Case 1: Unique Solution (det ≠ 0)
```
v⃗ is in column space (always true when full rank)
Null space = {0⃗}
Solution: x⃗ = A⁻¹ × v⃗ (exactly one!)
```

### Case 2: No Solution
```
v⃗ is NOT in column space
Example: A squishes to a line, but v⃗ is off that line
No x⃗ exists such that A × x⃗ = v⃗
```

### Case 3: Infinite Solutions
```
v⃗ IS in column space, but null space is non-trivial
If x⃗₀ is one solution, then x⃗₀ + (any null space vector) is also a solution!
```

---

## Why This Matters for Machine Learning

| Concept | ML Application |
|---------|----------------|
| Solving Ax = b | Linear regression (finding optimal weights) |
| Inverse matrices | Closed-form solutions (when they exist) |
| Column space | What outputs a layer can produce |
| Null space | Redundant features, dimensionality issues |
| Rank | Effective dimensionality of data |

### Linear Regression Connection

```
Normal equation: W = (XᵀX)⁻¹ Xᵀy

This requires (XᵀX)⁻¹ to exist!
If features are linearly dependent → det(XᵀX) = 0 → no inverse
This is "multicollinearity" problem.
```

### Checking for Problems

```python
import numpy as np

X = np.array([[1, 2, 3],
              [2, 4, 6],   # Row 2 = 2 × Row 1!
              [1, 1, 1]])

rank = np.linalg.matrix_rank(X)
print(f"Rank: {rank}")  # Will be < 3

if rank < X.shape[1]:
    print("Warning: Columns are linearly dependent!")
    print("Cannot invert this matrix.")
```

### Neural Network Perspective

```
Layer with weight matrix W:
- Column space of W = set of patterns this layer can output
- If W is rank-deficient, the layer can't produce all possible outputs
- "Dead neurons" can reduce effective rank
```

---

## Key Takeaways

1. **Inverse undoes transformation** — A⁻¹A = I, solves Ax = b as x = A⁻¹b

2. **Inverse exists ⟺ det ≠ 0** — Can't reverse a squishing transformation

3. **Column space = all possible outputs** — Span of the columns

4. **Null space = what maps to zero** — Everything that gets "lost"

5. **Rank tells dimension of output** — Full rank means full output space

---

## Self-Check Questions

- [ ] If A squishes 3D to a plane, what's the dimension of the null space?
- [ ] Can Ax = b have a solution if b is not in the column space?
- [ ] If A is 3×3 with rank 2, what's the nullity?
- [ ] Why does multicollinearity cause problems in linear regression?