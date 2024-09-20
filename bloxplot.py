# Bloxplot - Diagrama de caixa

import matplotlib.pyplot as plt

#gerando valores aleatórios
import random

vetor = []

for i in range(10):
    num_aleatorio = random.randint(0, 5)
    vetor.append(num_aleatorio)

plt.boxplot(vetor)
plt.title("Bloxplot")
plt.show()