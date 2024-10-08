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
    Seq(X,Y) = \max
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


### Alternative Setup

Let's start by defining the same rules as the [[Sequence Alignment Problem#Problem Setup|first problem setup]] but instead of maximize the total score, we are going to minimize the penalty cost, so the equation will be: 

$$
 \begin{align}
    Seq(X,Y) = \min
	    \begin{dcases*}
        Seq(X_{n-1}, Y_{m-1}) + \alpha_{[X_n, Y_m]}\\
		Seq(X_{n-1}, Y_{m}) + \alpha_{[X_n, -]}\\
		Seq(X_{n}, Y_{m-1}) + \alpha_{[-, Y_m]}
        \end{dcases*}
  \end{align}
$$


Backtracking in the context of sequence alignment using dynamic programming is the process of reconstructing the optimal alignment of two sequences after filling in the dynamic programming (DP) table. Here’s a detailed explanation of how the backtracking works:


### Backtracking Process

**Initialization**:
Start from the bottom-right corner of the $DP$ table, which contains the minimum penalty for aligning the full lengths of both sequences.

2. **Moving through the DP Table**:
   - At each cell `(i, j)` in the table, determine how you arrived at that cell by checking the three possible origins:
     - **Diagonal move**: If `dp[i][j]` came from `dp[i-1][j-1]`, it means there was a match or mismatch. 
     - **Vertical move**: If `dp[i][j]` came from `dp[i-1][j]`, it indicates that a gap was inserted in `seq2`, meaning the character from `seq1` is aligned with a gap.
     - **Horizontal move**: If `dp[i][j]` came from `dp[i][j-1]`, it indicates that a gap was inserted in `seq1`, meaning the character from `seq2` is aligned with a gap.

3. **Choosing the Path**:
   - If the characters from both sequences are the same, you typically choose the diagonal move.
   - If they are different, you still may choose the diagonal if it represents a mismatch (adding the mismatch penalty).
   - If you find that the penalty for a gap (either vertical or horizontal) is less than a mismatch, you would choose to move vertically or horizontally.

4. **Constructing the Alignment**:
   - As you move through the table, append characters from both sequences (or gaps) to the aligned sequences.
   - This process continues until you reach the top-left corner of the table.

5. **Handling Remaining Characters**:
   - If you finish backtracking and one sequence still has characters left, you append gaps for the other sequence for each remaining character.





> [!exercise]
> Given the following sequences: $$GATTACA \quad and \quad TAGGACA$$
> assuming that a gap has a penalty cost of $1$ and a mismatch $x \neq y$ has a cost of $3$.
> 
> Calculate the minimum penalty and display a alignment that meets that minimum.


We consider:
- Gap penalty cost $=1$
- Mismatch penalty cost $=3$
- The next equation $$ \begin{align}
    Seq(X,Y) = \min
	    \begin{dcases*}
        Seq(X_{n-1}, Y_{m-1}) + M\\
		Seq(X_{n-1}, Y_{m}) + 1\\
		Seq(X_{n}, Y_{m-1}) + 1
        \end{dcases*}
  \end{align}
$$ where $M$ is the match/mismatch penalty cost, 0 if match, 3 if mismatch.


We create a table of size $(m+1) \times (n+1)$, where $m$ and $n$ are the lengths of the two sequences, plus 1 to account for the empty prefix.

|     |     | $T$ | $A$ | $G$ | $G$ | $A$ | $C$ | $A$ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|     |  0  |     |     |     |     |     |     |     |
| $G$ |     |     |     |     |     |     |     |     |
| $A$ |     |     |     |     |     |     |     |     |
| $T$ |     |     |     |     |     |     |     |     |
| $T$ |     |     |     |     |     |     |     |     |
| $A$ |     |     |     |     |     |     |     |     |
| $C$ |     |     |     |     |     |     |     |     |
| $A$ |     |     |     |     |     |     |     |     |


The first row represents aligning the empty sequence with the second sequence $TAGGACA$. The first column represents aligning the first sequence $GATTACA$ with the empty sequence.

|     |     | $T$ | $A$ | $G$ | $G$ | $A$ | $C$ | $A$ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|     |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |
| $G$ |  1  |  2  |  3  |  2  |  3  |  4  |  5  |  6  |
| $A$ |  2  |  3  |  2  |  3  |  4  |  3  |  4  |  5  |
| $T$ |  3  |  2  |  3  |  4  |  5  |  4  |  5  |  6  |
| $T$ |  4  |  3  |  4  |  5  |  6  |  5  |  6  |  7  |
| $A$ |  5  |  4  |  3  |  4  |  5  |  6  |  7  |  6  |
| $C$ |  6  |  5  |  4  |  5  |  6  |  7  |  6  |  7  |
| $A$ |  7  |  6  |  5  |  6  |  7  |  6  |  7  |  6  |

A possible solution with a score of 6 is:

$\texttt{---GATTACA}$
$\texttt{TAGG---ACA}$

