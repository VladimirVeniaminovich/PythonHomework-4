from random import randint

list1 = list()
for i in range(30):
    list1.append(randint(0, 100))
print("Сгенерированный список", list1)
for i in range(len(list1)-1):
    minIndex = i
    for j in range(i+1, len(list1)):
        if list1[j] < list1[minIndex]:
            list1.insert(i, list1[j])
            list1.pop(j+1)
print("Отсортированный список: ", list1)