import pickle, psutil, os, time

def selection_sort(lista):
    comparacoes = 0
    trocas = 0
    for i in range(len(lista)-1):
        eleito = lista[i]
        menor = lista[i+1]
        pos = i + 1
        for j in range(i+1, len(lista)):
            comparacoes += 1
            if lista[j] < menor:
                menor = lista[j]
                pos = j

        comparacoes += 1
        if menor < eleito:
            lista[i] = lista[pos]
            lista[pos] = eleito
            trocas += 1

    return comparacoes, trocas



cem_numeros = pickle.load(open("numeros100.pkl", "rb"))
dez_mil_numeros = pickle.load(open("numeros10000.pkl", "rb"))
cem_mil_numeros = pickle.load(open("numeros100000.pkl", "rb"))


### 100 Elementos
print("100 Elementos")
t = time.time()
comparacoes,trocas = selection_sort(cem_numeros)
print(f"Uso de CPU: {psutil.cpu_percent()}")
print(f"Tempo de execução: {time.time() - t}")
print(f"Número de comparções: {comparacoes}\nNúmero de Trocas: {trocas}")
memoryUse = psutil.virtual_memory()[2]
print(f"Uso de memórias: {memoryUse}%\n")

### 10000 Elementos
print("10000 Elementos")
t = time.time()
comparacoes,trocas = selection_sort(dez_mil_numeros)
print(f"Uso de CPU: {psutil.cpu_percent()}")
print(f"Tempo de execução: {time.time() - t}")
print(f"Número de comparções: {comparacoes}\nNúmero de Trocas: {trocas}")
memoryUse = psutil.virtual_memory()[2]
print(f"Uso de memórias: {memoryUse}%\n")


### 100000 Elementos
print("100000 Elementos")
t = time.time()
comparacoes,trocas = selection_sort(cem_mil_numeros)
print(f"Uso de CPU: {psutil.cpu_percent()}")
print(f"Tempo de execução: {time.time() - t}")
print(f"Número de comparções: {comparacoes}\nNúmero de Trocas: {trocas}")
memoryUse = psutil.virtual_memory()[2]
print(f"Uso de memórias: {memoryUse}%\n")

