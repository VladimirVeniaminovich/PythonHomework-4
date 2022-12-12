#N = int(input("Введите колличество элементов списка: "))
list1 = [2, 1, 4, 3]
summ = 0
#for i in range(N):
#    list1.append(int(input("Введите число списка: ")))
#print("Ваш список:\n", list1)
for i in range(len(list1)):
    if i % 2 > 0:
        summ += list1[i]
print("Сумма нечетных позиций элементов списка равна ", summ)