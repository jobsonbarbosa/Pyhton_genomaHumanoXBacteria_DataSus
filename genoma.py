# Comparação doo RNA bossomal de um Humano e uma bacteria

entrada = open("dados/genoma/human.fasta").read()
saida = open("humano.html", "w")

cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i + j] = 0

entrada = entrada.replace("\n", "")

for k in range(len(entrada) - 1):
    cont[entrada[k] + entrada[k+1]] += 1
print(cont)


#html

i = 1
for k in cont:
    transparencia = cont[k]/max(cont.values())
    saida.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0,0,150,"+str(transparencia)+"')>"+k+"</div>")
    
    if i%4 == 0:
        saida.write("<div style='clear:both'></div>")
    i += 1
    
saida.close()