## **Norm of a Vector**
A **norm** is a way to measure the size of a [[Vector|vector]], a [[Matrix||matrix]], or a tensor. In other words, norms are a class of functions that enable us to quantify the magnitude of a vector.

The norm is written as follows:

$$Norm~\vec{x}=||x||$$

If $\vec{x} = \begin{bmatrix}x_{1}\\ x_{2}\\ \vdots \\ x_{n}\end{bmatrix}\in R^{n}$, then its **norm** is by definition:

$$
||x|| = \displaystyle\sqrt{x_{1}^2 + x_{2}^2 + \cdots + x_{n}^{2}}
$$

#### Properties of the Norm:

**Non-negativity**
$||x||\ge0$


**Definiteness**
$||x|| = 0$  only if $x=0$


**Triangular Inequality**
$||x+y|| \le  ||x|| + ||y||$


**Homogeneity**
$||\lambda \cdot x|| = |\lambda| \cdot ||x||, where \; \lambda \in \mathbb{R}$


### **L1 Norm  (Manhattan Norm)**
The L1 norm is defined as the sum of the absolute values of the components of a given vector.

$$||x||_1=\sum_{i=1}^n |x_i|$$

### **L2 Norm  (Euclidean Norm)**
The L2 norm measures the shortest distance from the origin.
$$||x||_2=\sqrt{\sum_{i=1}^n {|x_i|}^2}$$

**Sum:**
$$||x+y|| = \displaystyle\sqrt{||x||^{2} + 2x^{T}y + ||y||^{2}}$$
**Subtraction:**
$$||x-y|| = \displaystyle\sqrt{||x||^{2} - 2x^{T}y + ||y||^{2}}$$


### **Infinity Norm  (Max Norm)**
Is defined as the absolute value of the largest component of the vector.

$$||x||_\infty=max_i(|x_i|)$$

