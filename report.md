UECM3033 Assignment #2 Report
========================================================

- Prepared by: Chai Kun Ting
- Tutorial Group: T3

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are uploaded to Github at: 

[https://github.com/chaikt12/UECM3033_assign2](https://github.com/your_github_id/UECM3033_assign2)

### Selection criteria ( LU or SOR )
The condition is set to check whether it is positive definite or not. If matrix A is positive definite, it can be solve by cholesky factorization. So the condition is make so that if matrix A is positive definite, it will solve by SOR method, if not it will solve by LU method. By using LU method, it will have some numerical errors but is useful for consecutive solution. By using SOR method, it have much better precision but possibly no convergenc if the omega more than 2. It will converge if the omega is between 0 and 1.

### Implementation for `task1.py`

In task 1, the self-defined function lu(A,b) take in matrix A and b. Inside the lu(A,b), there is a function call Ludecomp(A) which take in matrix A. This function will make matrix A into LU matrix. lu(A,b) then solve it to return A and b. For sor(A,b), under the two loops, it will create diagonal matrix of D and lower triangular matrix L from matrix A. Then, we find the omega in omegafind(A，D）function. It will find the omega with the formula omega = 2*(1-np.sqrt(1-eig**2))/eig**2, where the eig is the maximum eigenvalue. Next, we will compute Q and use it for dot multiplication to find Tj, which is the inverse of Q multiple by Q minus A. We also find c, which is the inverse of Q multiple by b matrix. Finally, we can find the itereation, start with x(0) zero vector. We will use the intial x(0) vector to find next x(j) until the it loops until the iteration limit. The range of 1<omega<2 that will converge for any initial vector if A matrix is symmetric and positive definite. This procedures called under-relaxation method.If the omega<1, they are called over-relaxation method. They are used to accelerate the convergence for the system that are convergent by the Gauss-Seidel technique.  If omega is greater than 2 , SOR method will diverge.  In the main section, the matrix A and b will move into np.linalg.solve(A,b) and solve(A,b) to check with the condition. The condition is as mentions above.


## Task 2 -- SVD method and image compression

![SnakeDance.png](SnakeDance.png)

## Zero elements in $\Sigma$
Q: How many non zero element in $\Sigma$?
A: All elements in $\Sigma$ are non zero elements

### Generating pictures from `task2.py`
![resolution30.png](resolution30.png)
##resolution of 30

### Generating pictures from `task2.py`
![resolution200.png](resolution200.png)
##resolution of 200

1. First, we need to read the SnakeDance.jpeg into img where it contain 3 matrixs, which is r,g and b. Each r,g and b is a 3 dimensions matrix. We further decomposes each matrixs it into U, $\Sigma$ and  V, which is r1,r2 and r3 for the original red by using linalg.svd. Repeat the process for green and blue, namely g and b.

2.  Then, Create a new matrix $\Sigma_{30}$ which is the same dimensions as $\Sigma$, but keeping the first 30 none zero elements as in $\Sigma$, and set all other none zero elements to zero. this can be done by setting r2[30:800]=np.zeros_like(r2[30:800]). Repeat it with green and blue $\Sigma$.

3.  Next, we need to combine it back by dot multiplication of the U, $\Sigma_{30}$, V. But before this, we need to make the dimension of $\Sigma_{30}$ into (800,1000) so that it no dimensional error occur during the process. Noted that the $\Sigma_{30}$ is (800,1) originally. This can be done by r2 = linalg.diagsvd(r2,800,1000). Repeat it with green and blue $\Sigma_{30}$.

4. Now, the three newly generated matrix can be combined into a new r,g and b, namely as r_new, g_new, and b_new in the code. Put it back into img respectively.

5. Finally we can plot all the lower resolution matrix.

   In the code task2, two groups of 4 pictures will be plotted. Each group contain the original color type, red, green and blue. The first group of picture is the original set, while the second group is the lower resolution pictures.

# What is a sparse matrix?
Sparse matrix is a matrix which most of the element is zero. In our case, after we keep the first 30 non zero elements and set other elements to be zero, we change the dimension of the sigma from (800,1) to (800,1000) which created a sparse matrix of (800,1000) dimension matrix. This matrix is used for dot multiplication as mention above. Because the sparse matrix most elements is zero, this eventually help to make the lower resolutuon pictures.


-----------------------------------

<sup>last modified: 10/3/2016</sup>
