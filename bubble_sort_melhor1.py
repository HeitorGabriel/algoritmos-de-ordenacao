import pickle, psutil, os, time

def bubble_sort_melhoria1(lista):
    trocas = 0
    comparacoes = 0
    for j in range(len(lista)):
        for i in range(len(lista)-1, j, -1):
            comparacoes += 1
            if lista[i] < lista[i-1]:
                aux = lista[i]
                lista[i] = lista[i-1]
                lista[i-1] = aux
                trocas += 1
    return comparacoes, trocas



cem_numeros = pickle.load(open("numeros100.pkl", "rb"))
dez_mil_numeros = pickle.load(open("numeros10000.pkl", "rb"))
cem_mil_numeros = pickle.load(open("numeros100000.pkl", "rb"))


### 100 Elementos
print("100 Elementos\n")
t = time.time()
comparacoes,trocas = bubble_sort_melhoria1(cem_numeros)
print(f"Uso de CPU: {psutil.cpu_percent()}")
print(f"Tempo de execução: {time.time() - t}")
print(f"Número de comparções: {comparacoes}\nNúmero de Trocas: {trocas}")
memoryUse = psutil.virtual_memory()[2]
print(f"Uso de memórias: {memoryUse}%\n")

### 10000 Elementos
print("10000 Elementos\n")
t = time.time()
comparacoes,trocas = bubble_sort_melhoria1(dez_mil_numeros)
print(f"Uso de CPU: {psutil.cpu_percent()}")
print(f"Tempo de execução: {time.time() - t}")
print(f"Número de comparções: {comparacoes}\nNúmero de Trocas: {trocas}")
memoryUse = psutil.virtual_memory()[2]
print(f"Uso de memórias: {memoryUse}%\n")


### 100000 Elementos
print("100000 Elementos\n")
t = time.time()
comparacoes,trocas = bubble_sort_melhoria1(cem_mil_numeros)
print(f"Uso de CPU: {psutil.cpu_percent()}")
print(f"Tempo de execução: {time.time() - t}")
print(f"Número de comparções: {comparacoes}\nNúmero de Trocas: {trocas}")
memoryUse = psutil.virtual_memory()[2]
print(f"Uso de memórias: {memoryUse}%\n")