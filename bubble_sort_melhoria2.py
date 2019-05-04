import pickle, psutil, os, time

def bubble_sort_melhoria2(lista):
    troca = True
    tamanho = len(lista) - 1
    trocas = 0
    comparacoes = 0
    while tamanho > 0 and troca:
        troca = False
        for i in range(tamanho):
            comparacoes +=1
            if lista[i] > lista[i + 1]:
                troca = True
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                trocas +=1
        tamanho -= 1
    return comparacoes, trocas



cem_numeros = pickle.load(open("numeros100.pkl", "rb"))
dez_mil_numeros = pickle.load(open("numeros10000.pkl", "rb"))
cem_mil_numeros = pickle.load(open("numeros100000.pkl", "rb"))


### 100 Elementos
print("100 Elementos\n")
t = time.time()
comparacoes,trocas = bubble_sort_melhoria2(cem_numeros)
print(f"Uso de CPU: {psutil.cpu_percent()}")
print(f"Tempo de execução: {time.time() - t}")
print(f"Número de comparções: {comparacoes}\nNúmero de Trocas: {trocas}")
memoryUse = psutil.virtual_memory()[2]
print(f"Uso de memórias: {memoryUse}%\n")

### 10000 Elementos
print("10000 Elementos\n")
t = time.time()
comparacoes,trocas = bubble_sort_melhoria2(dez_mil_numeros)
print(f"Uso de CPU: {psutil.cpu_percent()}")
print(f"Tempo de execução: {time.time() - t}")
print(f"Número de comparções: {comparacoes}\nNúmero de Trocas: {trocas}")
memoryUse = psutil.virtual_memory()[2]
print(f"Uso de memórias: {memoryUse}%\n")


### 100000 Elementos
print("100000 Elementos\n")
t = time.time()
comparacoes,trocas = bubble_sort_melhoria2(cem_mil_numeros)
print(f"Uso de CPU: {psutil.cpu_percent()}")
print(f"Tempo de execução: {time.time() - t}")
print(f"Número de comparções: {comparacoes}\nNúmero de Trocas: {trocas}")
memoryUse = psutil.virtual_memory()[2]
print(f"Uso de memórias: {memoryUse}%\n")
