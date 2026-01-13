# Linear Combinations, Span, and Basis Vectors
> 📅 **Day**: 23
> 📺 **Video**: [Essence of Linear Algebra, Chapter 2](https://www.youtube.com/watch?v=k7RM-ot2NWY)  
> 🎯 **Goal**: Understand basis vectors, linear combinations, and what "span" means geometrically

---

## Basis Vectors: î and ĵ

The **basis vectors** are the fundamental building blocks of our coordinate system.

```
        y
        ↑
        |  ĵ = [0, 1]
        ↑
        |
--------+---→----→ x
        |   î = [1, 0]
```

- **î (i-hat)**: Unit vector pointing right → `[1, 0]`
- **ĵ (j-hat)**: Unit vector pointing up → `[0, 1]`

### Any Vector is Built from Basis Vectors

The coordinates of a vector are actually **scalars for î and ĵ**:

```
[3, 2] = 3î + 2ĵ
       = 3[1, 0] + 2[0, 1]
       = [3, 0] + [0, 2]
       = [3, 2]
```

**Key insight**: When you write `[3, 2]`, you're really saying "3 times î plus 2 times ĵ"

---

## Linear Combinations

A **linear combination** of vectors is what you get when you:
1. Scale each vector by some number (scalar)
2. Add the results together

### Formula
For vectors **v** and **w** with scalars **a** and **b**:
```
a·v + b·w = linear combination
```

### Example
```
v = [1, 2]
w = [3, -1]

Linear combination with a=2, b=-1:
2·[1, 2] + (-1)·[3, -1]
= [2, 4] + [-3, 1]
= [-1, 5]
```

### Why "Linear"?

If you fix one scalar and vary the other, the tip of the resulting vector traces a **straight line**.

```
Fix a = 1, vary b:

    1·v + 0·w = v
    1·v + 1·w = v + w
    1·v + 2·w = v + 2w
    ...
    
These points form a line!
```

---

## Span

The **span** of a set of vectors is the set of ALL possible linear combinations of those vectors.

### Span of Two Vectors (Most Common Case)

**Question**: What are all possible vectors you can reach using `a·v + b·w` for ANY values of a and b?

**Three possibilities:**

#### Case 1: Vectors point in different directions → Span is entire 2D plane
```
v = [1, 0]
w = [0, 1]

Span = All of 2D space (you can reach any point!)
```

#### Case 2: Vectors point in same/opposite direction → Span is a line
```
v = [1, 2]
w = [2, 4]    ← w is just 2·v!

Span = A single line through origin
```

#### Case 3: Both vectors are zero → Span is just the origin
```
v = [0, 0]
w = [0, 0]

Span = Just the point (0, 0)
```

---

## Linearly Dependent vs Independent

### Linearly Dependent
Vectors are **linearly dependent** if one can be expressed as a linear combination of the others.

In other words: **one vector is "redundant"** — it doesn't add any new directions.

```
v = [1, 2]
w = [2, 4]    ← w = 2·v (dependent!)

Span of {v, w} = just a line (same as span of just {v})
```

**Geometric intuition**: The vectors lie on the same line.

### Linearly Independent
Vectors are **linearly independent** if NO vector can be written as a combination of the others.

Each vector adds a **new dimension** to the span.

```
v = [1, 0]
w = [0, 1]    ← Can't make w from v (independent!)

Span of {v, w} = entire 2D plane
```

**Geometric intuition**: The vectors point in genuinely different directions.

---

## Formal Definition (Basis)

A **basis** of a space is a set of linearly independent vectors that span that space.

For 2D space, any two linearly independent vectors form a basis:
- Standard basis: `{î, ĵ}` or `{[1,0], [0,1]}`
- Another valid basis: `{[1,1], [1,-1]}`
- Another valid basis: `{[2,1], [0,3]}`

**Key insight**: There are infinitely many valid bases, but they all have the same NUMBER of vectors (2 for 2D, 3 for 3D, etc.)

---

## Extending to 3D

In 3D, we add a third basis vector:

- **î** = `[1, 0, 0]` (x-direction)
- **ĵ** = `[0, 1, 0]` (y-direction)
- **k̂** = `[0, 0, 1]` (z-direction)

**Span scenarios in 3D:**
| Vectors | If Independent | Span |
|---------|----------------|------|
| 1 vector | — | A line |
| 2 vectors | Yes | A plane |
| 3 vectors | Yes | All of 3D space |

If vectors are dependent, you get a lower-dimensional span than expected.

---

## Why This Matters for Machine Learning

| Concept | ML Application |
|---------|----------------|
| Linear combinations | Neural network layers compute linear combinations of inputs |
| Span | The "reachable" outputs from a set of features |
| Linear dependence | Redundant features (one feature is just a scaled version of another) |
| Basis | Feature selection — finding minimal set of features that still spans the info |
| Independence | Why we want uncorrelated features (each adds new information) |

### Example: Redundant Features

```python
# These features are linearly dependent:
feature1 = height_in_cm
feature2 = height_in_inches  # Just 2.54 × feature1!

# feature2 adds NO new information — it's redundant
# This is why we check for multicollinearity in regression
```

### Example: PCA Preview

PCA finds a new basis where:
- Basis vectors are linearly independent
- Ordered by how much "information" (variance) each captures
- Lets you reduce dimensions while keeping most information

---

## Key Takeaways

1. **Basis vectors are building blocks** — Every vector is a linear combination of basis vectors

2. **Coordinates are scalars** — `[3, 2]` means `3î + 2ĵ`

3. **Span = all reachable points** — Using any scalar combinations

4. **Linear independence = no redundancy** — Each vector adds a new direction

5. **Basis = minimal spanning set** — Linearly independent vectors that span the whole space

---

## Self-Check Questions

- [ ] What is the span of `[1, 2]` and `[3, 6]`? Why?
- [ ] Are `[1, 0]` and `[1, 1]` linearly independent?
- [ ] How many vectors do you need to span 3D space?
- [ ] If `v` and `w` are independent, can `2v + 3w = 0`?


![Logo](<../final profile.png>)