# Angle between Vectors

Let $a$ and $b$ be two non-zero [[Vector|vectors]] in $ℝ^n$. We define the angle formed by $a$ and $b$ as the number $\theta ∈ [0, \pi]$ that satisfies:

$$
\cos{(\theta)} = \displaystyle\frac{a^T b}{||a|| \cdot ||b||}
$$


1. Given two vectors a and b, the angle $\theta$ between them is given by the formula: $\cos(\theta) = \displaystyle\frac{a^T \cdot b}{||a|| \cdot ||b||}$
2. To find θ, you need to take the inverse cosine ($\arccos$) of both sides: $\theta = \arccos \displaystyle\frac{a \cdot b}{||a|| \cdot ||b||}$

Here's a step-by-step process to calculate the angle:

1. Calculate the dot product of the vectors.
2. Calculate the magnitudes of both vectors.
3. Divide the dot product by the product of the magnitudes.
4. Take the inverse cosine (arccos) of this result.

For example, let's say we have vectors a = (1, 2, 3) and b = (4, 5, 6):

1. Dot product: a · b = 1(4) + 2(5) + 3(6) = 4 + 10 + 18 = 32
2. Magnitudes: ||a|| = √(1² + 2² + 3²) = √14 ||b|| = √(4² + 5² + 6²) = √77
3. (a · b) / (||a|| * ||b||) = 32 / (√14 * √77) ≈ 0.9746
4. θ = arccos(0.9746) ≈ 0.2257 radians or about 12.93 degrees



Notice that it is also possible to express the inner product in terms of the angle between two vectors:

$$
a^T b = ||a||\, ||b||\, \cos{(\theta)}
$$

### **Orthogonal Vectors**

We say that 2 vectors are orthogonal if they are perpendicular to each other. i.e. the dot product of the two vectors is zero.