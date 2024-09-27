# Vector

For this note, I'm considering the vector as a special case of a [[Matrix|matrix]], where the vector is a matrix with one and only one row (or column), but at the end still a matrix.

## **Addition**
Vectors of the same dimension can be added element by element. This operation between vectors is known as **addition** and is denoted by the operator $+$

Given $a,b,c$ $n$-vectors on $\mathbb{R}^{n}$ where $c=a+b$, the operation is:

$$
c = a+b = \begin{bmatrix}a_{0}\\ a_{1}\\\vdots \\ a_{n}\end{bmatrix} + \begin{bmatrix}b_{0}\\ b_{1}\\\vdots \\ b_{n}\end{bmatrix} = \begin{bmatrix}a_{0} + b_{0}\\ a_{1}+b_{1}\\\vdots \\ a_{n}+b_{n}\end{bmatrix}
$$

For example:

$$
\begin{bmatrix} 0\\ 1\\ 2\end{bmatrix} + \begin{bmatrix}2\\ 3\\ -1\end{bmatrix} = \begin{bmatrix}0+2\\ 1+3 \\ 2-1\end{bmatrix} = \begin{bmatrix}2\\ 4 \\ 1\end{bmatrix}
$$


## **Multiplying a Vector by an Scalar**
Given a vector $\vec{v}$ on $\mathbb{R}^{n}$ and a scalar $\alpha \in \mathbb{R}$.

$$
\alpha \vec{v} = \alpha\begin{bmatrix}v_{0}\\ v_{1}\\ \vdots \\ v_{n}\end{bmatrix} = \begin{bmatrix}\alpha \cdot v_{0}\\ \alpha \cdot v_{1}\\ \vdots \\ \alpha \cdot v_{n}\end{bmatrix}
$$

### Some properties:

Sean $\vec{x},\vec{y}$ dos vectores y $\alpha, \beta$ dos escalares cualquiera. Las propiedades que cumple el producto escalar-vector son las siguientes:

* **Conmutatividad**: $\alpha \vec{x} = \vec{x}\alpha$
* **Asociatividad**: $(\beta \alpha)\vec{x} = \beta (\alpha\vec{x})$
* **Distribución sobre suma escalar**: $(\alpha + \beta)\vec{x} = \alpha \vec{x} + \beta\vec{x} =\beta\vec{x} + \alpha\vec{x} = \vec{x}(\alpha + \beta)$
* **Distribución sobre suma de vectores**: $\alpha (\vec{x}+\vec{y}) = \alpha\vec{x} + \alpha\vec{y}$



## **Multiplying a Vector by another Vector**
The two vectors must have the **same number of elements**. This is because the dot product involves multiplying corresponding components of the two vectors and then summing the results.
The dot product of two $n$-vectors $\vec{a},\vec{b}$ is defined as the scalar:
$$
<\vec{a},\vec{b}> = \vec{a} \cdot \vec{b} = a_{1}b_{1}+a_{2}b_{2}+\cdots+a_{n}b_{n} = \displaystyle\sum_{i=1}^{n} a_{i}b_{i}
$$
For example, if $\vec{a}=(1,2,3)$ and $\vec{b}=(4,5,6)$ then, the dot product will be:

$$
\vec{a}\cdot\vec{b} = (1,2,3)\cdot (4,5,6) = 1\cdot 4+2\cdot 5 + 3\cdot 6 = 4+10+18=32
$$


## **Transposing a Vector**
Given a vector $\vec{a}$:

$$
\vec{a} = \begin{bmatrix}a_{1}\\ a_{2}\\ \vdots \\ a_{n}\end{bmatrix}
$$

The transpose operation returns the same vector flipped over it's diagonal:

$$
\vec{a}^{T} = \begin{bmatrix}a_{1}\\ a_{2}\\ \vdots \\ a_{n}\end{bmatrix}^{T} = [a_{1}\; a_{2}\; \cdots \; a_{n}]
$$

It's also posible to transpose a transposed vector, as it will return the original one:

$$
\left(\vec{a}^{T}\right)^{T} = \left(\begin{bmatrix}a_{1}\\ a_{2}\\ \vdots \\ a_{n}\end{bmatrix}^{T}\right)^{T} = [a_{1}\; a_{2}\; \cdots \; a_{n}]^{T} = \begin{bmatrix}a_{1}\\ a_{2}\\ \vdots \\ a_{n}\end{bmatrix} = \vec{a}
$$

## **Distance between Vectors**

$$
d(\mathbf{a},\mathbf{b}) = ||\mathbf{a} - \mathbf{b}|| = \displaystyle\sqrt{(a_{0}-b_{0})^2 + (a_{1}-b_{1})^2 + \cdots + (a_{n-1}-b_{n-1})^2}
$$
