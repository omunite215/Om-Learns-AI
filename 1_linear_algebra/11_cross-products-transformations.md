# Cross Products in the Light of Linear Transformations
> 📅 **Day**: 28
> 📺 **Video**: [Essence of Linear Algebra, Chapter 11](https://www.youtube.com/watch?v=BaM7OCEm3G0)  
> 🎯 **Goal**: Understand WHY the cross product formula works using duality and determinants

---

## The Mystery

The cross product formula looks arbitrary:

```
v⃗ × w⃗ = [ v₂w₃ - v₃w₂ ]
         [ v₃w₁ - v₁w₃ ]
         [ v₁w₂ - v₂w₁ ]
```

Why these specific combinations? This chapter reveals the elegant reason.

---

## The Setup: A Special Linear Transformation

### Step 1: Define a Function

Consider this function that takes any 3D vector [x, y, z] and outputs a **number**:

```
f([x, y, z]) = det | x   v₁  w₁ |
                   | y   v₂  w₂ |
                   | z   v₃  w₃ |
```

This computes the **volume** of the parallelepiped formed by [x,y,z], v⃗, and w⃗.

### Step 2: Recognize It's Linear

This function is **linear** (takes 3D → 1D):
- f(a⃗ + b⃗) = f(a⃗) + f(b⃗)
- f(c · a⃗) = c · f(a⃗)

---

## Applying Duality

From Chapter 9, we learned:

> Every linear transformation from nD → 1D corresponds to a unique vector (via dot product)

So there must exist some vector **p⃗** such that:

```
f([x, y, z]) = p⃗ · [x, y, z]
```

For ALL vectors [x, y, z]!

```
det | x   v₁  w₁ |
    | y   v₂  w₂ |  =  p⃗ · [x, y, z]  =  p₁x + p₂y + p₃z
    | z   v₃  w₃ |
```

**This vector p⃗ IS the cross product v⃗ × w⃗!**

---

## Finding the Cross Product

### The Geometric Insight

```
p⃗ · [x, y, z] = volume of parallelepiped with sides [x,y,z], v⃗, w⃗
```

What vector p⃗ makes this true?

**Answer**: p⃗ must be:
- **Perpendicular** to both v⃗ and w⃗ (so the dot product measures height)
- **Magnitude** = area of the base (parallelogram formed by v⃗ and w⃗)

This is exactly the definition of the cross product!

### Visual Intuition

```
           [x,y,z]
             ↗
            /
           /  height = component of [x,y,z]
          /            along p⃗ direction
         /
        ┌──────────┐
       /          /│
      /    v⃗    / │
     /          /  │
    └──────────┘   │
    │    w⃗     │  /
    │          │ /
    └──────────┘

Volume = Base area × Height
       = |v⃗ × w⃗| × (projection of [x,y,z] onto p⃗ direction)
       = p⃗ · [x,y,z]
```

---

## Deriving the Formula

### Using the Determinant

```
det | x   v₁  w₁ |
    | y   v₂  w₂ |
    | z   v₃  w₃ |
```

Expand along the first column:

```
= x · det|v₂  w₂| - y · det|v₁  w₁| + z · det|v₁  w₁|
         |v₃  w₃|          |v₃  w₃|          |v₂  w₂|

= x(v₂w₃ - v₃w₂) - y(v₁w₃ - v₃w₁) + z(v₁w₂ - v₂w₁)

= x(v₂w₃ - v₃w₂) + y(v₃w₁ - v₁w₃) + z(v₁w₂ - v₂w₁)
```

This equals p⃗ · [x, y, z] where:

```
p⃗ = [ v₂w₃ - v₃w₂ ]
     [ v₃w₁ - v₁w₃ ]   =  v⃗ × w⃗
     [ v₁w₂ - v₂w₁ ]
```

**The formula emerges naturally from the determinant!**

---

## The Notational Trick

The "fake" determinant notation actually encodes this:

```
v⃗ × w⃗ = det | î   ĵ   k̂  |
             | v₁  v₂  v₃ |
             | w₁  w₂  w₃ |
```

This isn't a "real" determinant (î, ĵ, k̂ are vectors, not numbers), but it's a **mnemonic** that gives the right answer:

```
= î(v₂w₃ - v₃w₂) - ĵ(v₁w₃ - v₃w₁) + k̂(v₁w₂ - v₂w₁)

= (v₂w₃ - v₃w₂)î + (v₃w₁ - v₁w₃)ĵ + (v₁w₂ - v₂w₁)k̂
```

---

## Summary: The Big Picture

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  Start: Volume function (3D → 1D linear map)           │
│                    ↓                                   │
│  Duality: Must correspond to some vector p⃗            │
│                    ↓                                   │
│  Geometry: p⃗ must be ⊥ to v⃗ and w⃗, magnitude = area  │
│                    ↓                                   │
│  Result: p⃗ = v⃗ × w⃗ (the cross product!)              │
│                                                        │
└────────────────────────────────────────────────────────┘
```

The cross product formula isn't arbitrary — it's the **unique vector** that turns volume calculation into a dot product.

---

## Why This Perspective Matters

### Deeper Understanding

The formula `v₂w₃ - v₃w₂, ...` now has meaning:
- These are 2×2 determinants (areas of projected parallelograms)
- They come from expanding a 3×3 determinant
- Together they form the unique vector satisfying the duality relationship

### Connection to Determinants

```
Cross product magnitude = Area (2D determinant)
Dot with third vector = Volume (3D determinant)

v⃗ × w⃗ · u⃗ = det | u₁  v₁  w₁ |
                  | u₂  v₂  w₂ |
                  | u₃  v₃  w₃ |
```

This is called the **scalar triple product**.

---

## Why This Matters for Machine Learning

This chapter is more about mathematical elegance than direct ML applications. However, the concepts reinforce:

| Concept | Relevance |
|---------|-----------|
| Duality | Vectors ↔ linear functionals (appears in optimization, dual problems) |
| Determinant as volume | Understanding geometric meaning of transformations |
| Coordinate-free thinking | Many ML concepts are cleaner without coordinates |

### The Deeper Lesson

The cross product seems like a weird formula until you see it through the lens of:
1. Linear transformations
2. Duality
3. Determinants

**This is the power of linear algebra** — seemingly arbitrary formulas have deep geometric meaning.

---

## Key Takeaways

1. **Cross product emerges from duality** — It's the unique vector that turns volume into a dot product

2. **The formula comes from determinants** — Expanding a 3×3 determinant along the first column

3. **Geometry drives algebra** — The formula exists because of perpendicularity and area requirements

4. **Scalar triple product** — (v⃗ × w⃗) · u⃗ = signed volume of parallelepiped

5. **Notation as mnemonic** — The "determinant with vectors" is a memory trick encoding the real derivation

---

## Self-Check Questions

- [ ] Why must the cross product be perpendicular to both input vectors?
- [ ] What does (v⃗ × w⃗) · u⃗ compute geometrically?
- [ ] How does duality connect 3D vectors to linear functionals?
- [ ] Why is the cross product only defined in 3D?

![Logo](<../final profile.png>)