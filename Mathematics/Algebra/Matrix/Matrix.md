# Matrix
A **matrix** is an arrangement of numbers, expressions or symbols in a rectangular array. This arrangement is done in horizontal-rows and vertical-columns, having an order of **number of rows x number of columns.**


## **Addition/Subtraction**
Two matrices can be added/subtracted, iff (if and only if) the number of rows and columns of both the matrices are same, or the order of the matrices are equal.

For addition/subtraction, each element of the first matrix is added/subtracted to the elements present in the 2nd matrix.

$$ A +B= \begin{bmatrix} a_{11} &a_{12} & \cdots &a_{1n} \\ a_{21} & a_{22}&\cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots\\ a_{m1} & a_{m2} &\cdots & a_{mn}\\\end{bmatrix}+\begin{bmatrix}\ b_{11} &b_{12} &\cdots & b_{1n} \\ b_{21} & b_{22}& \cdots & b_{2n} \\ \vdots & \vdots & \ddots & \vdots\\ b_{m1} & b_{m2} & \cdots & b_{mn}\\\end{bmatrix}=\begin{bmatrix}\ a_{11}+b_{11} & a_{12}+b_{12} & \cdots & a_{1n}+b_{1n} \\ a_{21}+b_{21} & a_{22}+b_{22}& \cdots &a_{2n}+b_{2n} \\ \vdots & \vdots & \ddots & \vdots\\ a_{m1}+b_{m1} & a_{m2}+b_{m2} & \cdots & a_{mn}+b_{mn}\\\end{bmatrix} $$


**Properties:** 
$A + B = B + A$
$A + (B + C) = (A + B) + C$


## **Multiplication**
A matrix can be multiplied in two ways:

1. Scalar Multiplication
2. Multiplication with another matrix

***Scalar Multiplication*** **-** It involves multiplying a scalar quantity to the matrix. Every element inside the matrix is to be multiplied by the scalar quantity to form a new matrix.

$$ k \;\cdot \begin{bmatrix} a_{11} &a_{12} & \cdots &a_{1n} \\ a_{21} & a_{22}&\cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots\\ a_{m1} & a_{m2} &\cdots & a_{mn}\\\end{bmatrix}=\begin{bmatrix}\ k\cdot a_{11} &k \cdot a_{12} &\cdots & k  \cdot a_{1n} \\ k  \cdot a_{21} & k \cdot a_{22}& \cdots & k  \cdot a_{2n} \\ \vdots & \vdots & \ddots & \vdots\\ k \cdot a_{m1} & k \cdot a_{m2} & \cdots & k \cdot a_{mn}\\\end{bmatrix} $$

**Example:**
$$
\begin{align*}
5 \times
\begin{bmatrix}
5 & 7 \\
12 & 3 \\
6 & 2
\end{bmatrix}
=
\begin{bmatrix}
25 & 35 \\
60 & 15 \\
30 & 10
\end{bmatrix}
\end{align*}
$$

***Multiplication of a matrix with another matrix*** **-** Two matrices can be multiplied if and only if the number of columns of of the first matrix is equal to the number of rows of the second matrix.


**Example:**

$$
\begin{bmatrix}
1 & 2 & 3
\end{bmatrix}
\times
\begin{bmatrix}
4 & 5 & 6 \\
7 & 8 & 9 \\
10 & 11 & 12
\end{bmatrix}
=
\begin{bmatrix}
1 \times 4 + 2 \times 7 + 3 \times 10 & 1 \times 5 + 2 \times 8 + 3 \times 11 & 1 \times 6 + 2 \times 9 + 3 \times 12
\end{bmatrix}
=
\begin{bmatrix}
48 & 57 & 66
\end{bmatrix}
$$

**IMPORTANT:** The product of matrices is **NOT** commutative.

**Properties:**
$A \cdot B \cdot C = A \cdot (B \cdot C) = (A \cdot B) \cdot C$
$A \cdot (B + C) = A \cdot B + A \cdot C$



## **Transposing a Matrix**
The **transpose** of a matrix is an operator which flips a matrix over its diagonal; that is, it switches the row and column indices of the matrix $A$ by producing another matrix, often denoted by $A^T$ (among other notations).

**Properties:**
$(A^T)^T = A$ 
$(A + B)^T = A^T + B^T$
$(A \cdot B)^T = B^T \cdot A^T$
$(A \cdot B \cdot C)^T = C^T \cdot B^T \cdot A^T$


## **Matrix Trace**
In a square matrix, the sum of elements of the principal diagonal is called the ‘trace of a matrix’.

$$tr(A)=\sum_{i=1}^{n}a_{ii}=a_{11}+a_{22}+a_{33}+…+a_{nn}$$
**Properties:**
$tr(A+B)=tr(A)+tr(B)$
$tr(αA)=αtr(A)$
$tr(A^T)=tr(A)$



## **Complementary Minor and Cofactor**
A **complementary minor** (or **cofactor minor**) of an element in a matrix is the determinant of a submatrix obtained by removing the row and column containing that element. For an element $a_{ij}$ in an $n \times n$ matrix:

1. Remove the $i$-th row and the $j$-th column containing $a_{ij}$.
2. The remaining matrix, which is of order $(n-1) \times (n-1)$, is called the **minor** of $a_{ij}$.
3. The determinant of this minor is called the **complementary minor** (or just **minor**) of $a_{ij}$ and is denoted as $M_{ij}$​.

**Example:**
Given the matrix $A$:
$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
$$

The complementary minor of $6$ (that is the element $A_{23}$) is:

$$
M_{23} =
\begin{bmatrix}
1 & 2 \\
7 & 8
\end{bmatrix}
= 1 \cdot 8 - 2 \cdot 7 = -6
$$


The **Cofactor** of $a_{ij}​$ is given by:

$$C_{ij} = (-1)^{i+j} M_{ij}$$


**Example:**
Given the exact same matrix, the cofactor of $A_{23}$ is:

$$C_{23} = (-1)^{2+3} \cdot (-6) = (-1)^5 \cdot (-6) = 6$$


## **Range of a Matrix**







## **Inverse of a Matrix**
If $A$ is a non-singular square matrix, there is an existence of $n \times n$ matrix $A^{-1}$, which is called the **inverse matrix** of $A$ such that it satisfies the property:

$A \cdot A^{-1} = A^{-1} \cdot A = I$, where $I$ is the *identity* matrix.

**Properties:**
$A \cdot I = I \cdot A = A$
$A \cdot A^{-1} = A^ \cdot {-1}A = I$
$(A^{-1})^{-1} = A$ 
$(A \cdot B)^{-1} = B^{-1} \cdot A^{-1}$
$(A \cdot B \cdot C)^{-1} = C^{-1} \cdot B^{-1} \cdot A^{-1}$
$(A')^{-1} = (A^{-1})'$


#### **Finding the Inverse**




