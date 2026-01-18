# Cross Products
> 📅 **Day**: 28
> 📺 **Video**: [Essence of Linear Algebra, Chapter 10](https://www.youtube.com/watch?v=eu6i7WJeinw)  
> 🎯 **Goal**: Understand the cross product — a way to multiply two 3D vectors to get a new vector

---

## Cross Product vs Dot Product

| | Dot Product | Cross Product |
|--|-------------|---------------|
| **Input** | Two vectors (any dimension) | Two vectors (3D only!) |
| **Output** | A scalar (number) | A vector |
| **Notation** | v⃗ · w⃗ | v⃗ × w⃗ |
| **Measures** | How much vectors align | Area of parallelogram + perpendicular direction |

---

## The Geometric Meaning

The cross product v⃗ × w⃗ gives a vector that:

1. **Magnitude** = Area of the parallelogram formed by v⃗ and w⃗
2. **Direction** = Perpendicular to both v⃗ and w⃗ (using right-hand rule)

```
         v⃗ × w⃗ (result points UP, perpendicular to both)
           ↑
           │
           │
           │    w⃗
           │   /
           │  /
           │ /
           │/_________ v⃗
          
Parallelogram area = |v⃗ × w⃗|
```

---

## The Right-Hand Rule

To find the direction of v⃗ × w⃗:

```
1. Point fingers along v⃗
2. Curl fingers toward w⃗
3. Thumb points in direction of v⃗ × w⃗
```

```
        v⃗ × w⃗
          ↑
          │  
    ┌─────┴─────┐
    │   thumb   │
    │     ↑     │
    │  fingers  │
    │  v⃗ → w⃗   │
    └───────────┘
```

**Important**: Order matters! v⃗ × w⃗ = -(w⃗ × v⃗)

---

## Computing the Cross Product

For v⃗ = [v₁, v₂, v₃] and w⃗ = [w₁, w₂, w₃]:

```
v⃗ × w⃗ = [ v₂w₃ - v₃w₂ ]
         [ v₃w₁ - v₁w₃ ]
         [ v₁w₂ - v₂w₁ ]
```

### Memory Trick: Determinant Form

```
v⃗ × w⃗ = det | î   ĵ   k̂  |
             | v₁  v₂  v₃ |
             | w₁  w₂  w₃ |
```

Expand along first row:

```
= î(v₂w₃ - v₃w₂) - ĵ(v₁w₃ - v₃w₁) + k̂(v₁w₂ - v₂w₁)
```

### Example

```
v⃗ = [1, 2, 3]
w⃗ = [4, 5, 6]

v⃗ × w⃗ = [ (2×6 - 3×5) ]   [ 12 - 15 ]   [ -3 ]
         [ (3×4 - 1×6) ] = [ 12 - 6  ] = [  6 ]
         [ (1×5 - 2×4) ]   [ 5 - 8   ]   [ -3 ]
```

---

## Properties of Cross Product

### Anti-Commutative
```
v⃗ × w⃗ = -(w⃗ × v⃗)

Swapping order flips direction!
```

### Distributive
```
v⃗ × (w⃗ + u⃗) = v⃗ × w⃗ + v⃗ × u⃗
```

### NOT Associative
```
(v⃗ × w⃗) × u⃗  ≠  v⃗ × (w⃗ × u⃗)  in general
```

### Parallel Vectors → Zero
```
v⃗ × w⃗ = 0⃗  when v⃗ and w⃗ are parallel

(Parallelogram has zero area)
```

### Perpendicular to Both Inputs
```
(v⃗ × w⃗) · v⃗ = 0
(v⃗ × w⃗) · w⃗ = 0
```

---

## Special Cases

### Basis Vector Cross Products

```
î × ĵ = k̂       ĵ × î = -k̂
ĵ × k̂ = î       k̂ × ĵ = -î
k̂ × î = ĵ       î × k̂ = -ĵ
```

Visualize with right-hand rule — follows cyclic pattern: i→j→k→i→j→k

### Cross Product with Self

```
v⃗ × v⃗ = 0⃗

(Zero area parallelogram)
```

---

## Connection to Area and Determinant

The magnitude of the cross product equals the **area of the parallelogram**:

```
|v⃗ × w⃗| = |v⃗| × |w⃗| × sin(θ)
```

Compare to dot product:
```
v⃗ · w⃗ = |v⃗| × |w⃗| × cos(θ)
```

| | Dot Product | Cross Product |
|--|-------------|---------------|
| Uses | cos(θ) | sin(θ) |
| Max when | Parallel (θ=0°) | Perpendicular (θ=90°) |
| Zero when | Perpendicular | Parallel |

---

## Why This Matters for Machine Learning

Cross products are **less common** in ML than dot products, but appear in:

| Application | Use Case |
|-------------|----------|
| Computer graphics | Surface normals, lighting calculations |
| Robotics | Torque, angular velocity |
| 3D computer vision | Camera geometry, pose estimation |
| Physics simulations | Rotational dynamics |

### Finding Surface Normals

```python
# Two edges of a triangle in 3D
edge1 = point2 - point1
edge2 = point3 - point1

# Normal vector (perpendicular to surface)
normal = np.cross(edge1, edge2)
normal = normal / np.linalg.norm(normal)  # Normalize
```

---

## Key Takeaways

1. **Cross product outputs a vector** — Unlike dot product which outputs a scalar

2. **Magnitude = parallelogram area** — Measures "how perpendicular" the vectors are

3. **Direction via right-hand rule** — Perpendicular to both input vectors

4. **Order matters** — v⃗ × w⃗ = -(w⃗ × v⃗)

5. **3D only** — Cross product is specific to three dimensions

---

## Self-Check Questions

- [ ] What's [1, 0, 0] × [0, 1, 0]?
- [ ] If v⃗ × w⃗ = 0⃗, what does that tell you about v⃗ and w⃗?
- [ ] Why is v⃗ × v⃗ always zero?
- [ ] Which gives max value when perpendicular: dot or cross product?

![Logo](<../final profile.png>)