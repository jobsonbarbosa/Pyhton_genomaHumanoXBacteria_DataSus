import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 330, 100]

titulo = "Scatterplot gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.xlabel(eixoy)

# Gerando gráfico
plt.scatter(x, y, label="Pontos", color="r", marker=".", s=z)

# gerando linhas ligando os pontos
plt.plot(x, y, color="#000000", linestyle="--")
plt.legend()

# exibindo a tela
#plt.show()

# Metodo para salvar
# as imagens salvar geralmente são salvar em PNG.
# são salvar no diretório raiz do projeto.
# para aumentar o tamanho da imagam podemos salvar em formado .pdf
# onde será gerado um vetos de alta resolução.
# também pode ser incluido o paramentro dpi, para aumenta a resolução do png

plt.savefig("figura1.png", dpi=300)