from random import shuffle

f = open('scientist.txt', encoding='UTF-8').readlines()[1:] #открываем файл
f = [i.split('#') for i in f] #создаем массив по разделителям
y = [j for j in range(0, 1024)] #массив с числами от 0 до 1023 включительно
shuffle(y) #мешаем этот массив
hh = open('scientist_with_hash.txt', 'w', encoding='utf-8') #создаем файл, в который будут приходить ученые с хешем
hh.write('ScientistName#preparation#date#components\n')
for i in f: #процесс добавления хешей в начало строки
    a = list(i[0])
    b = 0
    for j in a:
        b += y[ord(j) % 1024]
    b = b % 2048
    hh.write(f"{b}#{'#'.join(i)}") # запись в файл
hh.close()