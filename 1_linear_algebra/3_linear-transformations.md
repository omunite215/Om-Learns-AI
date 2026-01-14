# Linear Transformations and Matrices
> 📅 **Day**: 24
> 📺 **Video**: [Essence of Linear Algebra, Chapter 3](https://www.youtube.com/watch?v=kYB8IZa5AuE)  
> 🎯 **Goal**: See matrices not as grids of numbers, but as transformations of space

---

## What is a Transformation?

A **transformation** is a function that takes in a vector and outputs a new vector.

```
Input vector → [Transformation] → Output vector
    [x, y]    →                  →    [?, ?]
```

Think of it as "movement" — every point in space moves to a new location.

**Why "transformation" instead of "function"?**  
It suggests movement. Visualize every point in space moving to a new position simultaneously.

---

## What Makes a Transformation "Linear"?

A transformation is **linear** if it satisfies two properties:

### Property 1: All lines remain lines
Lines don't get curved. Straight things stay straight.

```
Before:     After linear transformation:
  /           /
 /           /
/           /  (still a line!)

Before:     After NON-linear transformation:
  /           ~
 /             \
/               )  (curved — NOT linear!)
```

### Property 2: Origin stays fixed
The point `[0, 0]` doesn't move.

```
Origin (0,0) → still at (0,0)
```

**Combined intuition**: Grid lines remain parallel and evenly spaced. The grid might rotate, stretch, shear, or flip — but it won't curve or warp unevenly.

---

## The Key Insight: Track the Basis Vectors

Here's the magic of linear transformations:

> **If you know where î and ĵ land, you know where EVERY vector lands.**

### Why?

Remember: every vector is a linear combination of î and ĵ.

```
v = [x, y] = x·î + y·ĵ
```

After transformation:
```
transformed(v) = x·(transformed î) + y·(transformed ĵ)
```

The scalars x and y stay the same! Only the basis vectors change.

### Example

```
Before transformation:
  î = [1, 0]
  ĵ = [0, 1]
  v = [3, 2] = 3î + 2ĵ

After transformation:
  î lands on [1, -1]
  ĵ lands on [2, 1]
  
Where does v land?
  v = 3·[1, -1] + 2·[2, 1]
    = [3, -3] + [4, 2]
    = [7, -1]
```

---

## Matrices: Packaging a Transformation

A **matrix** is just a way to package "where the basis vectors land."

```
     ┌         ┐
     │  a   b  │
     │  c   d  │
     └         ┘
        ↑   ↑
        │   └── where ĵ lands: [b, d]
        └────── where î lands: [a, c]
```

**Columns are transformed basis vectors!**

### Example: Rotation by 90°

```
î = [1, 0] lands on [0, 1]   (points up now)
ĵ = [0, 1] lands on [-1, 0]  (points left now)

Matrix:
┌       ┐
│ 0  -1 │
│ 1   0 │
└       ┘
```

### Example: Shear

```
î = [1, 0] lands on [1, 0]   (stays the same)
ĵ = [0, 1] lands on [1, 1]   (tilts right)

Matrix:
┌      ┐
│ 1  1 │
│ 0  1 │
└      ┘
```

---

## Matrix-Vector Multiplication

Multiplying a matrix by a vector = **applying the transformation**.

### The Formula

```
┌      ┐   ┌   ┐       ┌           ┐
│ a  b │ × │ x │   =   │ a·x + b·y │
│ c  d │   │ y │       │ c·x + d·y │
└      ┘   └   ┘       └           ┘
```

### How to Think About It

```
┌      ┐   ┌   ┐
│ a  b │ × │ x │  =  x · [a, c] + y · [b, d]
│ c  d │   │ y │         ↑           ↑
└      ┘   └   ┘      1st column  2nd column
                      (where î    (where ĵ
                       lands)      lands)
```

**Read it as**: "x times (first column) plus y times (second column)"

### Worked Example

```
┌       ┐   ┌   ┐
│ 2   1 │ × │ 3 │
│ 1   3 │   │ 2 │
└       ┘   └   ┘

= 3 · [2, 1] + 2 · [1, 3]
= [6, 3] + [2, 6]
= [8, 9]
```

---

## Common Transformations and Their Matrices

| Transformation | Matrix | What it Does |
|---------------|--------|--------------|
| Identity | `[[1,0], [0,1]]` | Nothing (vectors unchanged) |
| Scale by k | `[[k,0], [0,k]]` | Uniform stretch/shrink |
| Scale x by a, y by b | `[[a,0], [0,b]]` | Non-uniform stretch |
| Rotate 90° CCW | `[[0,-1], [1,0]]` | Quarter turn left |
| Rotate θ | `[[cos θ, -sin θ], [sin θ, cos θ]]` | Rotate by angle θ |
| Reflect over x-axis | `[[1,0], [0,-1]]` | Flip vertically |
| Reflect over y-axis | `[[-1,0], [0,1]]` | Flip horizontally |
| Shear (horizontal) | `[[1,k], [0,1]]` | Slant horizontally |

---

## Visualizing the Grid

**Before transformation:**
```
    │   │   │
────┼───┼───┼────
    │   │   │
────┼───┼───┼────
    │   │   │
```

**After shear:**
```
      /   /   /
────/───/───/────
    /   /   /
──/───/───/────
  /   /   /
```

Grid lines stay parallel and evenly spaced — that's linearity!

---

## Why This Matters for Machine Learning

| Concept | ML Application |
|---------|----------------|
| Matrix-vector multiplication | Every layer of a neural network! `output = W·input + b` |
| Transformation as function | Neural networks transform input space to output space |
| Tracking basis vectors | Understanding what features a layer "looks for" |
| Composing transformations | Stacking multiple layers |

### Neural Network Layer

```python
# A single layer is literally a linear transformation!
def layer(x, W, b):
    return W @ x + b  # Matrix multiplication + bias

# W is a matrix that transforms input vectors
# Each row of W defines what one output neuron "responds to"
```

### Data Transformation Pipeline

```
Raw pixels → [Layer 1: W₁] → [Layer 2: W₂] → [Layer 3: W₃] → Prediction
   ↓              ↓              ↓               ↓
[784 dims]   [256 dims]     [128 dims]       [10 dims]

Each layer is a linear transformation reducing/reshaping the space!
```

---

## Key Takeaways

1. **Matrices ARE transformations** — Not just grids of numbers, but actions on space

2. **Columns = where basis vectors land** — This is how to read any matrix

3. **Matrix × vector = apply transformation** — Compute where the vector lands

4. **Linear = lines stay lines, origin fixed** — Grid stays parallel and evenly spaced

5. **Track î and ĵ, everything else follows** — Linear combinations are preserved

---

## Self-Check Questions

- [ ] If î lands on `[2, 1]` and ĵ lands on `[-1, 1]`, what's the matrix?
- [ ] What does the matrix `[[2, 0], [0, 2]]` do geometrically?
- [ ] Where does `[1, 1]` land after applying `[[0, -1], [1, 0]]`?
- [ ] Why can't a linear transformation turn a line into a curve?

![Logo](<../final profile.png>)