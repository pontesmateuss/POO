import random


print("  Pontec Lotery  ")

sorteio = random.sample(range(1, 77), 13)
sorteio.sort()

print(f"numeros serteados foram estes: \n{sorteio}")