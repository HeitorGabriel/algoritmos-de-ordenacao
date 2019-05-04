import pickle, psutil, os, time

def insertion_sort(lista):
    comparacoes = 0
    trocas = 0
    for i in range(1, len(lista)):
        eleito = lista[i]
        j = i - 1
        comparacoes += 2
        while j >= 0 and lista[j] > eleito:
            lista[j+1] = lista[j]
            j -= 1
            comparacoes += 2

        lista[j+1] = eleito
        trocas += 1

    return comparacoes, trocas


cem_numeros = pickle.load(open("numeros100.pkl", "rb"))
dez_mil_numeros = pickle.load(open("numeros10000.pkl", "rb"))
cem_mil_numeros = pickle.load(open("numeros100000.pkl", "rb"))


### 100 Elementos
print("100 Elementos\n")
t = time.time()
comparacoes,trocas = insertion_sort(cem_numeros)
print(f"Uso de CPU: {psutil.cpu_percent()}")
print(f"Tempo de execução: {time.time() - t}")
print(f"Número de comparções: {comparacoes}\nNúmero de Trocas: {trocas}")
memoryUse = psutil.virtual_memory()[2]
print(f"Uso de memórias: {memoryUse}%\n")


### 10000 Elementos
print("10000 Elementos")
t = time.time()
comparacoes,trocas = insertion_sort(dez_mil_numeros)
print(f"Uso de CPU: {psutil.cpu_percent()}")
print(f"Tempo de execução: {time.time() - t}")
print(f"Número de comparções: {comparacoes}\nNúmero de Trocas: {trocas}")
memoryUse = psutil.virtual_memory()[2]
print(f"Uso de memórias: {memoryUse}%\n")


### 100000 Elementos
print("100000 Elementos")
t = time.time()
comparacoes,trocas = insertion_sort(cem_mil_numeros)
print(f"Uso de CPU: {psutil.cpu_percent()}")
print(f"Tempo de execução: {time.time() - t}")
print(f"Número de comparções: {comparacoes}\nNúmero de Trocas: {trocas}")
memoryUse = psutil.virtual_memory()[2]
print(f"Uso de memórias: {memoryUse}%\n")


