import pickle
from random import randint

gerador = lambda n: [randint(10, i+10) for i in range(n)]

with open("numeros100.pkl", "wb") as numeros100:
    pickle.dump(gerador(100), numeros100)

with open("numeros10000.pkl", "wb") as numeros10000:
    pickle.dump(gerador(10000), numeros10000)

with open("numeros100000.pkl", "wb") as numeros100000:
    pickle.dump(gerador(100000), numeros100000)
