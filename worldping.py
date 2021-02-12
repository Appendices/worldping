from pythonping import ping

def Sort_Tuple(tup):
    return sorted(tup, key = lambda x: -1*x[1])

worldlist = []
for i in range(1,236):
    r = ping('oldschool{}.runescape.com'.format(i))
    if r.success:
        worldlist.append((i, r.rtt_max_ms))

with open('worldlist.csv', 'w+') as f:
    for i,j in Sort_Tuple(worldlist):
        print('{},{}'.format(i, j))
        f.write('{},{}\n'.format(i, j))