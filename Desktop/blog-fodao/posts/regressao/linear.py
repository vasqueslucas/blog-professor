import numpy as np
from plotnine import ggplot, aes, geom_point, geom_abline
import pandas as pd

X = np.loadtxt("/Users/pricollaltopavanelli/Desktop/linear/X.txt")
y = np.loadtxt("/Users/pricollaltopavanelli/Desktop/linear/y.txt")

# matriz da regressão
X_matriz = np.column_stack((np.ones(len(X)), X))
beta = np.linalg.inv(X_matriz.T @ X_matriz) @ X_matriz.T @ y

a, b = beta[0], beta[1]

print("a (intercepto) =", a)
print("b (inclinação) =", b)

df = pd.DataFrame({"x": X, "y": y})

plot = (
    ggplot(df, aes("x", "y"))
    + geom_point()
    + geom_abline(intercept=a, slope=b)
)

# salvar corretamente
plot.save("/Users/pricollaltopavanelli/Desktop/linear/grafico.png")
