# Vectors, What Even Are They?
> 📅 **Day**: 22
> 📺 **Video**: [Essence of Linear Algebra, Chapter 1](https://www.youtube.com/watch?v=fNk_zzaMoSs)  
> 🎯 **Goal**: Understand vectors from multiple perspectives and build geometric intuition

---

## Three Perspectives on Vectors

### 1. Physics Student View
- Vector = **arrow** pointing in space
- Defined by **length** (magnitude) and **direction**
- Can live anywhere in space (position doesn't matter)

### 2. Computer Science View
- Vector = **ordered list of numbers**
- Example: `[3, 2]` or `[1.5, -0.7, 4.2]`
- Useful for storing data (house features, pixel values, etc.)

### 3. Mathematician View (3Blue1Brown's approach)
- Vector = **arrow rooted at the origin**
- Combines both: arrow with geometric meaning AND coordinates as numbers
- This perspective bridges intuition and computation

**Key insight**: Linear algebra gives us tools to switch between geometric intuition and numerical computation.

---

## The Coordinate System

```
        y
        ↑
        |
        |     • (3, 2)
        |    /
        |   /
        |  /
        | /
--------+-------→ x
        |
```

- **Origin**: Where axes meet (0, 0)
- Every vector starts at origin and points to its coordinates
- `[3, 2]` means: "Walk 3 units right, then 2 units up"

### What Coordinates Mean
- **First number**: How far along the x-axis (horizontal)
- **Second number**: How far along the y-axis (vertical)
- In 3D, add a third number for z-axis (depth)

---

## Vector Operations

### 1. Vector Addition

**Geometric intuition**: Place the second vector's tail at the first vector's tip. The sum is from origin to the final tip.

```
    v + w
      ↗
     /
    / w
   ↗---→
  /
 / v
↗
```

**Why it makes sense**: Think of walking. First walk along v, then walk along w. Where do you end up?

**Numerically**: Add corresponding components
```
[3, 2] + [1, -1] = [3+1, 2+(-1)] = [4, 1]
```

### 2. Scalar Multiplication

**Scalar** = A single number (it "scales" the vector)

**Geometric intuition**: 
- Multiply by 2 → stretch to double length
- Multiply by 0.5 → shrink to half length  
- Multiply by -1 → flip direction
- Multiply by -2 → flip AND stretch

**Numerically**: Multiply each component
```
3 × [2, 1] = [3×2, 3×1] = [6, 3]
```

**Key insight**: Scalars scale vectors. Negative scalars flip direction.

---

## Why This Matters for Machine Learning

| Concept | ML Application |
|---------|----------------|
| Vector as list of numbers | Feature vectors (each data point is a vector!) |
| Vector addition | Combining features, residuals |
| Scalar multiplication | Weights in neural networks, learning rate |
| High-dimensional vectors | Real data has many features (not just 2D or 3D) |

### Example: House as a Vector
```python
house = [1500,    # square feet
         3,       # bedrooms
         2,       # bathrooms  
         15]      # years old

# This house is a point in 4D space!
```

### Example: Word Embeddings
Words are represented as vectors (e.g., 300 dimensions):
```
"king"  → [0.2, -0.5, 0.8, ...]   # 300 numbers
"queen" → [0.21, -0.48, 0.79, ...] # Similar vectors = similar meaning
```

---

## Key Takeaways

1. **Think geometrically, compute numerically** — This is the core skill of linear algebra

2. **Vectors are not just arrows OR lists** — They're both, and switching between views is powerful

3. **Everything extends to higher dimensions** — 2D/3D intuition applies to 100D, 1000D (ML territory)

4. **Two fundamental operations**: Addition and scalar multiplication — Everything else builds on these

---

## Self-Check Questions

- [ ] Can you visualize `[3, -2]` as an arrow?
- [ ] What does `2 × [1, 3]` look like geometrically?
- [ ] What's `-1 × v` for any vector v?
- [ ] How would you add `[1, 2]` and `[3, 1]` both geometrically and numerically?

![Logo](<../final profile.png>)