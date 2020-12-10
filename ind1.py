#!/usr/bin/env python3
# -*- config: utf-8 -*-
#4. Создайте рекурсивную функцию, печатающую все возможные перестановки для целых
#чисел от 1 до N .
def permutation(f):
    if len(f) == 1:
        return [f]  # терминальная ветвь
    else:
        a = f[0]  # первый элемент списка
        p = permutation(f[1:])  # все перестановки хвоста
        r = []  # вставляем a в каждую возможную позицию каждой
        for pp in p:  # перестановки хвоста
            for i in range(len(pp)):
                per = pp[0:i] + [a] + pp[i:]
                r.append(per)
            r.append(pp + [a])
        return r


n = int(input("n= "))
print(permutation([i for i in range(1, n + 1)]))
