import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

titulo = "Gráfico de barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Titulo
plt.title(titulo)

# Legendas
plt.xlabel(eixox)
plt.ylabel(eixoy)

# Definir o tipo de gráfico
plt.bar(x, x)
plt.show()