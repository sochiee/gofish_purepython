## Uso

```bash
python similitud_geometrica.py
```

Regresa todo lo que nos pide la práctica, no tiene ninguna dependencia. 


Para graficar es necesario instalar las dependencias y posteriormente correr plot.py: 

```bash
pip install -r requirements.txt
python plot.py
```

## Desarrollo

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

Aquí podemos hacer dos cosas, si existe la inversa $$(X^T X)^{-1}$$ tenemos una solución para $$\beta$$. Sin embargo, encontrar la inversa de una matriz cuyas propiedades no conocemos puede ser dificil, por lo que utilizamos la descomposición QR.

$$
\begin{align*}
& X = QR \\
\iff & (QR)^T QR \beta = (QR)^T y \\  
\iff & R^T R \beta = R^T Q^T y \\  
\iff & R \beta = Q^T y  
\end{align*}
$$

Como R es una matriz triangular superior, es un sistema de ecuaciones facil de resolver. 


Lo demas esta aqui: https://sochiee.github.io/projects/practica_3/

