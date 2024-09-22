# Sequence Alignment Problem

The **Sequence Alignment Problem** is a classic problem in **bioinformatics** that involves finding the optimal alignment between two (or more) sequences, such as DNA, RNA, or protein sequences. The goal is to maximize the similarity between sequences by aligning them, potentially introducing **gaps** (represented by `-`) to accommodate differences like insertions, deletions, or substitutions.

In the context of [[Dynamic Programming|dynamic programming]], sequence alignment is tackled using algorithms like the **Needleman-Wunsch** (for global alignment) or **Smith-Waterman** (for local alignment). The key idea is to build an optimal solution by combining solutions to subproblems.

### Problem Setup

You are given two sequences:
- Sequence $X$ of length $n$
- Sequence $Y$ of length $m$

You want to align them by:
1. **Inserting gaps** in one or both sequences.
2. **Matching** or **mismatching** characters between the sequences.

Each operation has a score (reward for a match, penalty for a mismatch or gap). The objective is to find the alignment that maximizes (or minimizes, if considering cost) the total score.


Let's suppose that:

$$
\begin{align*} X &= x_1, \dotsc, x_n \\ Y &= y_1, \dotsc, y_m \end{align*}
$$
is optimum, so how is the last "column"?

Since it's optimum there are three possibilities:

$$
\begin{equation} 
	\begin{array}{c} 
		\begin{bmatrix} 
		x_n \\ 
		y_m 
		\end{bmatrix} 
		\\ 
		Seq(X_{n-1}, Y_{m-1}) + \alpha_{[X_n, Y_m]} 
	\end{array} \quad or \quad 
	\begin{array}{c} 
		\begin{bmatrix} 
		x_n \\ 
		- 
		\end{bmatrix} 
		\\ 
		Seq(X_{n-1}, Y_{m}) + \alpha_{[X_n, -]} 
	\end{array} 
	\quad or \quad 
	\begin{array}{c} 
		\begin{bmatrix} 
		- \\ 
		y_m 
		\end{bmatrix} 
		\\ 
		Seq(X_{n}, Y_{m-1}) + \alpha_{[-, Y_m]} 
	\end{array} 
\end{equation}
$$
As we need to maximize the total score, then:

$$ \begin{align}
    Seq(X,Y) = max
	    \begin{dcases*}
        Seq(X_{n-1}, Y_{m-1}) + \alpha_{[X_n, Y_m]}\\
		Seq(X_{n-1}, Y_{m}) + \alpha_{[X_n, -]}\\
		Seq(X_{n}, Y_{m-1}) + \alpha_{[-, Y_m]}
        \end{dcases*}
  \end{align}
$$

Is the solution.

Let's define $q$ as the length property of a sequence, then the time complexity is $O(X_q \cdot Y_q)$


https://www.cs.mtsu.edu/~rbutler/courses/sdd/dynamic_programming/dynamic.html
