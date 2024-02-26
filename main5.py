from random import shuffle

f = open('scientist.txt', encoding='UTF-8').readlines()[1:]
f = [i.split('#') for i in f]
y = [j for j in range(0, 1024)]
shuffle(y)
hh = open('scientist_with_hash.txt', 'w', encoding='utf-8')
hh.write('ScientistName#preparation#date#components\n')
for i in f:
    a = list(i[0])
    b = 0
    for j in a:
        b += y[ord(j) % 1024]
    b = b % 2048
    hh.write(f"{b}#{'#'.join(i)}")
hh.close()