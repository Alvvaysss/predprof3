f = open('scientist.txt', encoding='UTF-8').readlines()[1:]
f = [i.split('#') for i in f]
f.sort(key=lambda x: int(x[2].split('-')[2]) and int(x[2].split('-')[1]) and int(x[2].split('-')[0]))
origin = open('scientist_origin.txt', 'w', encoding='UTF-8')
origin.write('ScientistName#preparation#date#components\n')
a1 = set()
for j in f:
    if j[1] in a1:
        continue
    else:
        a1.add(j[1])
        origin.write('#'.join(j))
origin.close()

otchet = open('otchet.txt', 'w', encoding='UTF-8')
spisok = []
for x in f:
    if x[1] == 'Аллопуринол':
        spisok.append([x[0], '.'.join(x[2].split('-'))])
otchet.write('Разработчиками Аллопуринола были такие люди:\n')
for y in range(len(spisok)):
    if y >= 1:
        otchet.write(f"{'-'.join(spisok[y])}\n")
otchet.write(f'\nОригинальный рецепт принадлежит: {spisok[0][0]}')
otchet.close()
