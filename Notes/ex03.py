# lista = ["José", "Pedro", "Raúl", "María"]
#
# i = 0
# while i < len(lista):
#     print(lista[i])
#     i += 1
#
# for nombre in lista:
#      print(nombre)

'''
1. Guardar en una nueva lista los cuadrados de la lista "numbers"
2. Imprimir los valores de la nueva lista y sus respectivas posiicones (indices)
I: {i}, V: {v}
'''

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for k, v in enumerate(numbers):
#     print(f"I: {k}, V: {v ** 2}")


repeated_numbers = [1,2,2,10,11,13,2,8,9,16,26,50,51,56,89,150,2,3,6,7,67,98]

# find_number = int(input("Gimme a number between 1 to 150: "))
# count_0 = 0
# count_1 = 0
# repeat = 0
# index = []
#
# for v in repeated_numbers:
#     if find_number == v:
#         count_0 += 1
#
# print(f"The number {find_number} is repeat {count_0}")


# for k, v in enumerate(repeated_numbers):
#     if find_number == v and repeat == 0:
#         print(f"The number {find_number} is have a first index {k}")
#         repeat += 1


# for k, v in enumerate(repeated_numbers):
#     if find_number == v:
#         count_1 += 1
#         index.append(k)
#
# print(f"The number {find_number} is repeat {count_1} with all indexes {index}")


# numbers_2 = [1,2,4,6,8,20,30,1]
#
# for num in numbers_2:
#     if num % 2 == 0:
#         continue
#         print(f"{num} es par")
#     else:
#         pass
#         print(f"{num} es impar")


unique_numbers = []
for num in repeated_numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(f"The final list is: {sorted(unique_numbers)}")
print(f"This final list order ascendants: {sorted(unique_numbers)}")
print(f"This final list order descending: {sorted(unique_numbers, reverse=True)}")


list_pair = []
list_impair = []
for num in unique_numbers:
    if num % 2 == 0:
        list_pair.append(num)
    else:
        list_impair.append(num)

print(f"The list PAIR is: {list_pair}")
print(f"The list IMPAIR is: {list_impair}")


pow_repeated_numbers = []
for num in repeated_numbers:
    pow_repeated_numbers.append(num ** 2)

print(f"The pow list is: {pow_repeated_numbers}")
print(f"The media of list is: {sum(pow_repeated_numbers) / len(pow_repeated_numbers)}")


num = 0
for k, v in enumerate(pow_repeated_numbers):
    if v > num:
        num = v
        key = k
pow_repeated_numbers[key] = 1000

print(f"The new list is: {pow_repeated_numbers}")

repeated_numbers[repeated_numbers.index(max(repeated_numbers))] = 1000
print(f"The new list is: {repeated_numbers}")

sum_list = []
result = 0
for k, v in enumerate(pow_repeated_numbers):
    if k in [4, 5, 6, 7, 8, 9]:
        sum_list.append(v)
        result = sum(sum_list)
print(f"The sum of the list is: {result}")


# Fibonacci
limit = int(input("What is the limit?: "))
fibonacci = [0, 1]

for num in range(1, limit + 1):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(f"The sequence of fifteen Fibonacci series is: {fibonacci}")


# Suma Secuencia
num_limit = int(input("Limit number: "))
list_temp = []
result = 0

for num in range(1, num_limit + 1):
    list_temp.append(num)
    result += num

print(f"The total sum of the sequence {list_temp} is: {result}")

a, b, c = [1, 2, 3]

print(a,b,c)