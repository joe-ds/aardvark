import os
import random
from time import sleep
import winsound

data = {}
colors = list(range(31, 38)) + list(range(90, 98)) + list(range(40, 48)) + list(range(100, 108))

with open('data.csv', 'r') as f:
    for line in f:
        entry = line.strip().split('\t')
        data[entry[0]] = int(entry[1])

pool = []
for key in data.keys():
    pool.extend([key] * data[key])

random.seed(os.urandom(64))

winsound.PlaySound('villainous.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
for n in range(0, 30, 1):
    print('\033[{code}m{name:=<{n}}\033[0m'.format(name=random.choice(pool), n=n*2, code=random.choice(colors), flush=True))
    sleep(0.5)
for n in range(30, 0, -1):
    print('\033[{code}m{name:=<{n}}\033[0m'.format(name=random.choice(pool), n=n*2, code=random.choice(colors), flush=True))
    sleep(0.5)

print("\nAnd now our winner is...", flush=True)
sleep(2.5)
winner = random.choice(pool)
print(f"\033[93m{'*^*':=^80}]\033[0m")
print(f"\n\n\033[93m{winner:.^80}\033[0m")
print(f"\033[93m{'*v*':=^80}]\033[0m")
print("\n" * 4)
sleep(10)
