# Matrix Determinant

The **determinant** is a scalar-valued function of the entries of a square [[Matrix|matrix]]. Its value characterizes some properties of the matrix and the linear map represented, on a given basis, by the matrix. In particular, the determinant is nonzero if and only if the matrix is invertible and the corresponding linear map is an isomorphism.

The determinant of a matrix $A$ is commonly denoted: $$det(A) \; \text{or} \; |A|$$

The determinant of a $2 \times 2$ matrix is:

$$
\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}
=
ad - bc
$$

The determinant of a $3 \times 3$ matrix is:

$$
\begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix}
=
aei + bgf + cdh - ceg - bdi - afh
$$


The determinan of a superior order matrix is:
We use the method of cofactor expansion along any row or column. Here's the step-by-step process:

1. **Select a Row or Column for Expansion**: Typically, you would choose the row or column with the most zeros to simplify calculations, but any row or column will work.
2. **Calculate Cofactors**: For each element in the chosen row or column, calculate its cofactor.
3. **Expand the Determinant**: Multiply each element by its corresponding cofactor and sum them up.


Example:
Calculate the determinant of a $4 \times 4$ matrix:

$$
A = \begin{bmatrix}
a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24} \\
a_{31} & a_{32} & a_{33} & a_{34} \\
a_{41} & a_{42} & a_{43} & a_{44}
\end{bmatrix}
$$



1. **Expand along the first row**:

$$
\det(A) = a_{11} C_{11} + a_{12} C_{12} + a_{13} C_{13} + a_{14} C_{14}
$$

where $C_{ij}$ are the cofactors defined as:

$$
C_{ij} = (-1)^{i+j} M_{ij}
$$



2. **Calculate Each Minor**:

For each element $a_{ij}$ in the first row, calculate the determinant of the $3 \times 3$ submatrix obtained by removing the $i$-th row and $j$-th column. For example:

$$
M_{11} = \begin{bmatrix}
a_{22} & a_{23} & a_{24} \\
a_{32} & a_{33} & a_{34} \\
a_{42} & a_{43} & a_{44}
\end{bmatrix}
$$

Calculate this $3 \times 3$ determinant using the formula for a $3 \times 3$ matrix:

$$
\det(M_{11}) = a_{22}(a_{33}a_{44} - a_{34}a_{43}) - a_{23}(a_{32}a_{44} - a_{34}a_{42}) + a_{24}(a_{32}a_{43} - a_{33}a_{42})
$$

3. **Calculate Cofactors and Determinant**:

Compute $C_{11} = (-1)^{1+1} \det(M_{11})$, $C_{12} = (-1)^{1+2} \det(M_{12})$, etc. Then, plug these into the expansion formula:

$$
\det(A) = a_{11} C_{11} + a_{12} C_{12} + a_{13} C_{13} + a_{14} C_{14}
$$

This process will give you the determinant of the $4 \times 4$ matrix.



### **Useful properties**

1. If all the elements of a row or column of a square matrix are split into two addends, then its determinant is equal to the sum of two determinants, each having identical lines except for the line in question, where the addends correspond to each of the determinants respectively.

$$ 
\begin{bmatrix} 1 + 2 & 2 + 4 & 3 + 6 \\ 1 & 3 & 5 \\ 7 & 4 & 8 \end{bmatrix} = \begin{bmatrix} 1 & 2 & 3 \\ 1 & 3 & 5 \\ 7 & 4 & 8 \end{bmatrix} + \begin{bmatrix} 2 & 4 & 6 \\ 1 & 3 & 5 \\ 7 & 4 & 8 \end{bmatrix} 
$$

$$
21 = 7 + 14
$$

We can also state this as follows: 

$$
\det(F_{1} + F'_{1}, F_{2}, F_{3}) = \det(F_{1}, F_{2}, F_{3}) + \det(F'_{1}, F_{2}, F_{3})
$$

2. If the $i$-th row or the $j$-th column of a matrix $A$ is multiplied by a scalar $c$, then the determinant of $A$ is also multiplied by $c$.
3. If any two rows or columns of a matrix $A$ are interchanged, the determinant of the resulting matrix is equal to the determinant of $A$ multiplied by $-1$.
4. If any row or column of $A$ is zero, then its determinant is $0$.
5. If a matrix $A$ has two identical rows or columns, then its determinant is $0$.
6. If one row (or column) of a matrix $A$ is a multiple of another row (or column), then the determinant of $A$ is $0$.
7. If a multiple of one row (or column) of $A$ is added to another row (or column) of $A$, the determinant remains unchanged.
8. If $A$ is an $n \times n$ matrix, then $\det(A) = \det(A^T)$.
9. If $A$ and $B$ are $n \times n$ matrices, then $\det(AB) = \det(A) \cdot \det(B)$.
10. If $A$ is invertible and not the zero matrix, then $\det(A^{-1}) = \frac{1}{\det(A)}$.
11. If $A$ is an $n \times n$ matrix, and $k$ is a scalar, then $\det(kA) = k^n \cdot \det(A)$.