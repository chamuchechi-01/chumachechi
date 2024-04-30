# def factorial_recusuve(n):
#     if n == 1:
#         return n
#     else:
#         return n*factorial_recusuve(n-1)
# print(factorial_recusuve(6))


# a = lambda b,t : b + 1
# print(a(5,6))


# a = lambda b : b**3
# print(a(1))


# def a(b):
#     return b**3
# print(a(5))


# def name(a):
#     return a * a * a 
# lam = lambda a: a * a * a
# while True:
#     b = input("vedite chislo dla a:")
#     try:
#         a = int(b)
#         break
#     except ValueError:
#         print("error vedi polnoy chislo")


# print("result ->:", name(a))
# print("result lambda funtion:", lam(a))


# name = input("ведите своё имя пожалуста")
# age = input("укажите свой возраст")

# print("привет " + name + "!")
# print("тебе уже " + age + "гда это круто")



# a = (1,2,3,4,5,6)
# print(a[0])


# b = (1,2,3,4,5,6)
# print(b[5])


# d = (1,2,3,4,5,6)
# print(d[0] + d[5])

# chislo = (1,2,3,4,5,6,7)
# print(chislo[0] + chislo[6])





# a = [1,2,3,4,5]
# print(a)


# list1 = [1,2,3,4]
# list2 = [6,7,8,9]
# print(list1 + list2)


# tuple1 = (1,2,3,4)
# tuple2 = (5,6,7,8)
# print(tuple1 + tuple2)

# dict1 = {
#     "c":1,
#     'b':2
# }



# dict2 = {
#     "c":1,
#     'b':2
# }


# dict1.update(dict2)
# print(dict1)


# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1.intersection(set2))
# print(set2.union(set1))


# text1 = '12345'
# text2 = '45678'
# for i in text1:
#     for x in text2:
#         if i== x:
#             print(i)




# def creat_x_pyramid(rows):
#     for i in range(1, rows + 1):
#         print("x" * i)



# rows = 5 
# creat_x_pyramid(rows)

# def creat_x_pyramid(rows):
#     for i in range(1, rows + 1):
#         print("xx" * i)



# rows = 5 
# creat_x_pyramid(rows)



# a = 111
# for i in range(1):
#     print(a)
# a = 111
# for i in range(1):
#     print(a)
#     a = 222
# for i in range(1):
#     print(a)
#     a = 333
# for i in range(1):
#     print(a)
#     a = 444
# for i in range(1):
#     print(a)
#     a = 555
# for i in range(1):
#     print(a)
#     a = 666
# for i in range(1):
#     print(a)
#     a = 777
# for i in range(1):
#     print(a)



# def creat_x_pyramid(rows):
#     for num in range(1, rows + 1):
#         print("x" * num)
        
        



# rows = 5 
# creat_x_pyramid(rows)


# events = [
#             {
#     'date':  '2019-12',
#     'event': 'name1'
#   },
#   {
#     'date':  '2019-12',
#     'event': 'name2'
#   },
#   {
#     'date':  '2019-12',
#     'event': 'name3'
#   },
#   {
#     'date':  '2019-12',
#     'event': 'name4'
#   },
#   {
#     'date':  '2020-12',
#     'event': 'name5'
#   },
#   {
#     'date':  '2020-12',
#     'event': 'name6'
#   },
#   {
#     'date':  '2020-12',
#     'event': 'name5'
#   },
#   {
#     'date':  '2020-12',
#     'event': 'name6'
#   },
#   {
#     'date':  '2020-12',
#     'event': 'name7'
#   },
#   {
#     'date':  '2020-12',
#     'event': 'name8'
#   },
#   {
#     'date':  '2020-12',
#     'event': 'name9'
#   },
# ]

# osasa = {}
# for event in events:
#     name = event['date']
#     event_t = event['event']
#     if name not in osasa:
#         osasa[name] = [event_t]
#     else:
#         osasa[name].append(event_t)
# print(osasa)




# a = [1,2,3,4,5,6,7,8,9,10]
# b = filter(lambda num: num % 2 == 0, a)
# if a % 2 == 0:
#     print(list(a))


# #Найти символы в строке
# my_string = "Это строка для поиска символов"
# char_to_find = "о"
# if char_to_find in my_string:
#     print(f"Символ '{char_to_find}' найден в строке.")
# else:
#     print(f"Символ '{char_to_find}' не найден в строке.")

# my_string = "Это строка для поиска символов"
# char_to_find = "о"
# count = my_string.count(char_to_find)
# print(f"Символ '{char_to_find}' встречается {count} раз(а) в строке.")

#                                                                        #Количество символов в строке
# my_string = "Это строка с символами"
# length = len(my_string)
# print(length)  # Выведет: 20

#                                                              #Посчитать количество определенных символов в строке
# my_string = "Это строка с символами"
# char_to_count = "о"
# count = my_string.count(char_to_count)
# print(f"Символ '{char_to_count}' встречается {count} раз(а) в строке.")

# my_string = "Это строка с символами"
# char_to_count = "о"
# count = sum(1 for char in my_string if char == char_to_count)
# print(f"Символ '{char_to_count}' встречается {count} раз(а) в строке.")

#                                                                     #Как сделать кортеж
# empty_tuple = ()

# my_list = [1, 2, 3, 4]
# tuple_from_list = tuple(my_list)

#                                                                   #Как объединить кортежи
# tuple1 = (1, 2, 3)
# tuple2 = ("a", "b", "c")
# tuple1 += tuple2
# print(tuple1)  # Выведет: (1, 2, 3, "a", "b", "c")

# #Как сравнить кортежи
# #== ><

#                                                                         #Как создать список
# empty_list = []

# my_tuple = (1, 2, 3, 4)
# list_from_tuple = list(my_tuple)

#                                                                       #Создать список циклом
# my_list = []
# for i in range(1, 11):
#     my_list.append(i)
# print(my_list)  # Выведет: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]










a = [1,2,3,4,5]
b = [1,2,3,4,5]




























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































