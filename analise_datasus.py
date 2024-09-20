# Analise da população brasileira 1980 - 2016
# Fonte: DataSUS

import matplotlib.pyplot as plt

dados = open("dados/populacao_brasileira.csv").readlines()

x = []
y = []

for item in range(len(dados)):
    if item != 0:
        linha = dados[item].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.bar(x, y, color="#66cdaa")
plt.plot(x, y, color="k", linestyle="--")


plt.title("Crescimento da Populução Brasileira 1980 - 2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
plt.show()

#plt.savefig("populacao_brasileiro.png", dpi=300)
