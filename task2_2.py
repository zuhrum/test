my_list = []
amount = int(input("Введите желаемое количество элементов в списке: "))
count = 1
while count <= amount:
    element = input(f"введите элемент списка № {count}: ")
    my_list.append(element)
    count += 1
print(my_list)
j = 0
for i in range(int(len(my_list) / 2)):
    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    j += 2
print(my_list)
