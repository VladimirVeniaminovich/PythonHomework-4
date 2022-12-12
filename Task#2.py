from random import randint

A = int(input("Введите А строк: "))
B = int(input("Введите B элементов строк: "))
matrix = []
for j in range(A):
    row = input("Введите элементы через запятую без пробела:\n").split(",")
    for i in range(B):
        row[i] = int(row[i])
    matrix.append(row)
for i in matrix: 
    for j in i: 
        print(j, end=' ') 
    print()
sum = 0
for i in matrix:
    for j in i:
        sum += j
    average = sum / B
    print(average)