# Linear Combination

Let $\vec{a}_{0},\vec{a}_{1},\dots,\vec{a}_{n-1}$ be $n$-vectors and $\beta_{0},\beta_{1},\dots,\beta_{m-1}$ be scalars. Then, we can define the following $n$-vector:

$$
\beta_{0}\vec{a}_{0}+\beta_{1}\vec{a}_{1}+\cdots+\beta_{m-1}\vec{a}_{n-1}
$$

This is called a _linear combination_ of the [[Vector|vectors]] $\vec{a}_{0},\vec{a}_{1},\dots,\vec{a}_{n-1}$. The scalars $\beta_{0},\beta_{1},\dots,\beta_{m-1}$ are called the _coefficients_ of the linear combination.


## Linear Combinations of Unit Vectors 

Any $n$-vector $\vec{b}$ can be expressed as a linear combination of the standard unit vectors:

$$
\vec{b} = b_{0}\hat{e}_{0} + b_{1}\hat{e}_{1} + \cdots + b_{n-1}\hat{e}_{n-1}
$$

where $b_{i}$ are scalars and $\hat{e}_{i}$ is the $i$-th unit vector. A specific example would be:

$$
\begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix} = (1) \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} + (-1) \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} + (0) \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
$$

As a final note, if the vector space has dimension $n$, then it has $n$ unit vectors $\hat{e}_{i}$.