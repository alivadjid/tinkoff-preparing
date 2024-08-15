"""
Виталик увлекается машинным обучением и алгоритмами. Он поступил на курсы, где он может изучать обе эти темы.
Курсы делятся на циклы, каждый из которых состоит из двух частей. В первой части цикла Виталик A дней подряд занимается машинным обучением, а во второй части - B дней подряд решает задачи на Codeforces. Затем начинается новый цикл, и так далее.
Виталик хочет посвящать машинному обучению C часов в день, а алгоритмам - D часов. Курсы идут N недель. 
Виталик интересуется, сколько времени он потратит на обучение за все N недель. Помогите ему это выяснить.
Формат входных данных
В первой строке дается целое число A (1≤A≤1000) — количество подряд идущих дней, которые Виталик посвящает машинному обучению.
Во второй строке дается целое число B (1≤B≤1000) — количество подряд идущих дней, которые Виталик посвящает алгоритмам.
В третьей строке дается целое число C (1≤C≤500) — количество часов, которые Виталик будет в день проводить за машинным обучением.
В четвертой строке дается целое число D ﻿(1≤D≤500)(1≤D≤500)﻿ — количество часов, которые Виталик будет в день проводить за алгоритмами.
В пятой строке дается целое число N ﻿(1≤N≤500)(1≤N≤500)﻿ — количество недель подготовки Виталика.
Формат выходных данных
Выведите одно число — общее количество часов, которые посвятит Виталик обучению на этих курсах.Пример данных:32454Вывод: 122

"""

def calculate_total_hours():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    N = int(input())

    total_hours_per_cycle = A * C + B * D
    total_cycles = N * 7 // (A + B)

    total_hours = total_hours_per_cycle * total_cycles

    return total_hours

print(calculate_total_hours())