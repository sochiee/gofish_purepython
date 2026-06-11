Definimos la función de error: 

$$
E(\beta) = \sum_{i=1}^n (y_i - x_{i1} \beta_{1} + x_{i2} \beta_{2} + ... + x_{ip} \beta_{p})^2
$$ 

Utilizando notación matricial.

$$
\begin{align*}
\implies E(\beta) &= \sum_{i=1}^n (y_i - x_i^T \beta)^2 \\
                  &= \lVert y - X \beta \rVert ^2 \\
                  &= (y - X \beta)^T ( y - X \beta) \\
                  &= y^T y - \beta^T X^T y - y^T X \beta + \beta^T X^T X \beta 
\end{align*}
$$ 

Encontramos el gradiente de E e igualamos a cero para encontrar el minimo global.

$$
\nabla E(\beta) = 2 X ^T X \beta - 2 X^T y
$$


$$
\begin{align*}
     & \nabla E(\beta) = 0 \\
\iff & 2 X ^T X \beta - 2 X^T y = 0 \\
\iff & X ^T X \beta = X^T y
\end{align*}
$$




