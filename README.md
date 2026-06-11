Definimos la función de error: 

$$
E(x) = \sum_{i=1}^n (y_i - x_{i1} \beta_{1} + x_{i2} \beta_{2} + ... + x_{ip} \beta_{p})^2
$$ 

Utilizando notación matricial.

$$
\begin{align*}
\implies E(x) &= \sum_{i=1}^n (y_i - x_i^T \beta)^2 \\
              &= \lVert y - X \beta \rVert ^2 \\
              &= (y - X \beta)^T ( y - X \beta) \\
              &= y^T y - \beta^T X^T y - y^T X \beta + \beta^T X^T X \beta 
\end{align*}
$$ 


