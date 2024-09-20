import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

titulo = "Gráfico de barras 2"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Titulo
plt.title(titulo)

# Legendas
plt.xlabel(eixox)
plt.ylabel(eixoy)

# Definir o tipo de gráfico
plt.bar(x1, x1, label="Grupo 1")
plt.bar(x2, y2, label="Grupo 2")
plt.legend()
plt.show()