# Three-Dimensional Linear Transformations
> 📅 **Day**: 25
> 📺 **Video**: [Essence of Linear Algebra, Chapter 5](https://www.youtube.com/watch?v=rHLEWRxRGiM)  
> 🎯 **Goal**: Extend 2D intuition to 3D — same concepts, one more dimension

---

## The Good News

**Everything from 2D works the same way in 3D.**

The only difference: three basis vectors instead of two.

---

## 3D Basis Vectors

```
        y (ĵ)
        ↑
        │
        │
        │
        └───────→ x (î)
       /
      /
     ↙ z (k̂)
```

| Basis Vector | Coordinates | Direction |
|--------------|-------------|-----------|
| **î** (i-hat) | `[1, 0, 0]` | Along x-axis |
| **ĵ** (j-hat) | `[0, 1, 0]` | Along y-axis |
| **k̂** (k-hat) | `[0, 0, 1]` | Along z-axis |

### Any 3D Vector as Linear Combination

```
[2, 3, 1] = 2î + 3ĵ + 1k̂
          = 2[1,0,0] + 3[0,1,0] + 1[0,0,1]
```

---

## 3D Transformation Matrices

A 3D linear transformation is represented by a **3×3 matrix**.

```
┌         ┐
│ a  b  c │  ← where î lands: [a, d, g]
│ d  e  f │  ← where ĵ lands: [b, e, h]  
│ g  h  i │  ← where k̂ lands: [c, f, i]
└         ┘
     ↑
  Columns are transformed basis vectors!
```

**Same rule as 2D**: Each column tells you where a basis vector lands.

---

## Reading a 3×3 Matrix

```
Example matrix:
┌          ┐
│ 1  0  0  │
│ 0  0 -1  │
│ 0  1  0  │
└          ┘

Column 1: î → [1, 0, 0]  (stays the same)
Column 2: ĵ → [0, 0, 1]  (now points along z)
Column 3: k̂ → [0, -1, 0] (now points along -y)

This is a rotation around the x-axis!
```

---

## Matrix-Vector Multiplication in 3D

```
┌         ┐   ┌   ┐       ┌                    ┐
│ a  b  c │   │ x │       │ ax + by + cz       │
│ d  e  f │ × │ y │   =   │ dx + ey + fz       │
│ g  h  i │   │ z │       │ gx + hy + iz       │
└         ┘   └   ┘       └                    ┘
```

**Same interpretation**:
```
result = x·(column 1) + y·(column 2) + z·(column 3)
       = x·(where î lands) + y·(where ĵ lands) + z·(where k̂ lands)
```

---

## Common 3D Transformations

### Identity (No Change)
```
┌         ┐
│ 1  0  0 │
│ 0  1  0 │
│ 0  0  1 │
└         ┘
```

### Uniform Scaling by k
```
┌         ┐
│ k  0  0 │
│ 0  k  0 │
│ 0  0  k │
└         ┘
```

### Rotation Around Z-Axis by θ
```
┌                   ┐
│ cos θ  -sin θ   0 │
│ sin θ   cos θ   0 │
│   0       0     1 │
└                   ┘

(x-y plane rotates, z unchanged)
```

### Rotation Around X-Axis by θ
```
┌                   ┐
│  1      0       0 │
│  0    cos θ  -sin θ │
│  0    sin θ   cos θ │
└                   ┘

(y-z plane rotates, x unchanged)
```

### Rotation Around Y-Axis by θ
```
┌                   ┐
│  cos θ   0   sin θ │
│    0     1     0   │
│ -sin θ   0   cos θ │
└                   ┘

(x-z plane rotates, y unchanged)
```

---

## 3D Matrix Multiplication

**Same as 2D**: Composition of transformations.

```
3×3 matrix × 3×3 matrix = 3×3 matrix

(M₂ × M₁) means: apply M₁ first, then M₂
```

### Computing Each Entry

```
Result[row i, col j] = dot product of (row i of left) and (col j of right)
```

For 3×3:
```
┌         ┐   ┌         ┐
│ · · · │ × │ | | | │
│ →→→ │   │ | | | │   ← Row • Column = one entry
│ · · · │   │ | | | │
└         ┘   └         ┘
```

---

## Visualizing 3D Transformations

In 3D, linear transformations:
- Keep the origin fixed
- Keep all lines straight
- Keep grid planes flat (parallel planes stay parallel)

**What can happen:**
- Rotation (around any axis)
- Scaling (uniform or non-uniform)
- Shearing
- Reflection
- Any combination of above

**What CANNOT happen (if linear):**
- Bending or curving
- Moving the origin
- Non-uniform warping

---

## The Pattern: Generalizing to Any Dimension

| Dimension | Basis Vectors | Matrix Size | Vector Size |
|-----------|---------------|-------------|-------------|
| 2D | î, ĵ | 2×2 | 2 entries |
| 3D | î, ĵ, k̂ | 3×3 | 3 entries |
| nD | n basis vectors | n×n | n entries |

**The insight**: All the concepts scale up. In ML, we work with hundreds or thousands of dimensions — same math, just more numbers.

---

## Why This Matters for Machine Learning

| Concept | ML Application |
|---------|----------------|
| High-dimensional transforms | Real data lives in high-D space (images: 784D, embeddings: 768D) |
| 3D specifically | Computer vision, robotics, 3D reconstruction |
| Rotation matrices | Data augmentation, pose estimation |
| General n×n matrices | Every fully-connected layer |

### High-Dimensional Reality

```
# MNIST image: 28×28 pixels = 784 dimensions
image_vector = [pixel_1, pixel_2, ..., pixel_784]

# Neural network layer: 784 → 256
# This is a 256×784 matrix transformation!
W = [[...], [...], ...]  # 256 rows, 784 columns

output = W @ image_vector  # 256-dimensional output
```

### 3D Applications

```
# Rotating a 3D point cloud
rotated_points = rotation_matrix @ points

# Camera projection (3D to 2D)
image_coords = projection_matrix @ world_coords

# Robot arm kinematics
end_position = T1 @ T2 @ T3 @ base_position
```

---

## Key Takeaways

1. **Same concepts, more dimensions** — 3D (and n-D) works just like 2D

2. **3×3 matrix = three columns** — Each column is where a basis vector lands

3. **Columns are transformed î, ĵ, k̂** — Reading matrices works the same way

4. **ML lives in high-D** — We routinely work with 100s or 1000s of dimensions

5. **Intuition transfers** — Build intuition in 2D/3D, apply it to n-D

---

## Self-Check Questions

- [ ] How many numbers define a 3D linear transformation? (Hint: size of matrix)
- [ ] If a 3×3 matrix has columns `[1,0,0]`, `[0,1,0]`, `[0,0,1]`, what transformation is it?
- [ ] What size matrix transforms a 784D vector to a 256D vector?
- [ ] Why can't we visualize a 784-dimensional transformation directly?

