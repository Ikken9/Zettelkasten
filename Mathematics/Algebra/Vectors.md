# Vectors (Informatics)

**Un vector (matriz) es una colección ordenada de datos** (tanto primitivos u objetos dependiendo del lenguaje). Los vectores (matrices) se emplean para almacenar múltiples valores en una sola variable, frente a las variables que sólo pueden almacenar un valor (por cada variable).

## Addition

Vectors of the same dimension can be added element by element. This operation between vectors is known as **addition** and is denoted by the operator $+$

Given $a,b,c$ $n$-vectors on $\mathbb{R}^{n}$ where $c=a+b$, the operation is:

$$
c = a+b = \begin{bmatrix}a_{0}\\ a_{1}\\\vdots \\ a_{n}\end{bmatrix} + \begin{bmatrix}b_{0}\\ b_{1}\\\vdots \\ b_{n}\end{bmatrix} = \begin{bmatrix}a_{0} + b_{0}\\ a_{1}+b_{1}\\\vdots \\ a_{n}+b_{n}\end{bmatrix}
$$

For example:

$$
\begin{bmatrix} 0\\ 1\\ 2\end{bmatrix} + \begin{bmatrix}2\\ 3\\ -1\end{bmatrix} = \begin{bmatrix}0+2\\ 1+3 \\ 2-1\end{bmatrix} = \begin{bmatrix}2\\ 4 \\ 1\end{bmatrix}
$$


## Multiplying a Vector by an Scalar

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


##  Multiplying a Vector by another Vector

The dot product of two $n$-vectors $\vec{a},\vec{b}$ is defined as the scalar:
$$
<\vec{a},\vec{b}> = \vec{a} \cdot \vec{b} = a_{1}b_{1}+a_{2}b_{2}+\cdots+a_{n}b_{n} = \displaystyle\sum_{i=1}^{n} a_{i}b_{i}
$$
For example, if $\vec{a}=(1,2,3)$ and $\vec{b}=(4,5,6)$ then, the dot product will be:

$$
\vec{a}\cdot\vec{b} = (1,2,3)\cdot (4,5,6) = 1\cdot 4+2\cdot 5 + 3\cdot 6 = 4+10+18=32
$$

## Norm of a Vector

A **norm** is a way to measure the size of a vector, a matrix, or a tensor. In other words, norms are a class of functions that enable us to quantify the magnitude of a vector.

if $\vec{x} = \begin{bmatrix}x_{1}\\ x_{2}\\ \vdots \\ x_{n}\end{bmatrix}\in R^{n}$, then its **norm** is by definition:

$$
||x|| = \displaystyle\sqrt{x_{1}^2 + x_{2}^2 + \cdots + x_{n}^{2}}
$$

