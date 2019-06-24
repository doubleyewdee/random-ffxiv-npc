used = set()

with open('used.txt', 'r') as used_fp:
    for line in used_fp.readlines():
        used.add(line.strip().lower())

npcs = list()
with open('npcs.csv', 'r') as npcs_fp:
    for line in npcs_fp.readlines():
        line = line.strip()
        name, url = line.split(',')
        npcs.append(line.split(','))

import random
while True:
    npc = npcs[random.randrange(0, len(npcs) - 1)]
    name, url = npc
    if name.lower() in used:
        continue

    print('{} {}'.format(name, url))
    break