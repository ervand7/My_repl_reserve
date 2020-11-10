
# |||||||||||||||Изучаем функцию enumerate||||||||||||||||||||
# a = [10, 20, 30, 40, 50, 60]

# print(list(enumerate(a)))

# for index, value in enumerate(a):
#   if value %20 == 0:
#     print(f'{index} - {value}')



# a = [10, 20, 30, 40, 50, 60]
# for index, value in enumerate(a):
#   a[index] += 1

# print(*a)


# s = 'hello'
# for index, value in enumerate(s):
#   print(index, value)


# t = ('apple', 'banana', 'mango')
# for index, value in enumerate(t):
#   print(index, value)


# d = {'a': 1, 'b': 2, 'c': 3}
# for index, value in enumerate(d):
#   print(index, value)



# for index, value in enumerate(range(10, 20)):
#   print(index, value)



# t = ('apple', 'banana', 'mango')
# for index, value in enumerate(t, 13):
#   print(index, value)



# |||||||||||||||Изучаем функцию zip||||||||||||||||||||



# a = [5, 6, 7, 8]
# b = [100, 200, 300, 400]

# for i in range(4):
#   print(a[i], b[i])

# rez = list(zip(a, b))
# print(rez)




# a = [5, 6, 7, 8]
# b = [100, 200, 300, 400]
# c = 'abcd'

# for t1, t2, t3 in zip(a, b, c):
#   print(t1, t2, t3)




# a = [5, 6, 7, 8]
# b = [100, 200, 300, 400]
# c = 'abcd'

# rez = zip(a, b, c)
# print(list(rez))




# a = [5, 6, 7, 8]
# b = [100, 200, 300, 400]
# c = 'abcd'

# rez = zip(a, b, c)
# col1, col2, col3 = zip(*rez)
# print(col1, col2, col3)



# |||||||||||||||Изучаем функцию sotr() и sorted()||||||||||||||||||||

# a = [5, 6, 7, 8]
# a.sort()
# print(a)
# print(sorted(a, reverse = True))





# |||||||||||||||Изучаем функцию split и join ||||||||||||||||||||

# s = 'Ivanov Ivan Ivanovich'
# print(s.split()) # в аргменте сплита указываем , по какому символу разделять



# s = input().split() # так мы сразу получим список с элементами-строками
# print(s)



# s = ['12121', 'wewe', 'dfdf', 'rererererer', '4r2efwqecqwfcqw', 'dfdsf']
# print(' - '.join(s)) # ПРЕЖДЕ ЧЕМ ПОЛЬЗОВАТЬСЯ МЕТОДОМ JOIN НУЖНО ВСЕ ЭЛЕМЕНТЫ СПИСКА ПРИВЕСТИ В СТРОКУ!!!!!!!!!!!!!!!!


# # А ВОТ МЫ СКЛЕИВАЕМ ЧИСЛА С ПОМОЩЬЮ ГЕНЕРАТОРА СПИСКОВ
# s = [1, 2, 3, 4, 5, 6, 7, 89, 0, 8]
# print(''.join([str(i) for i in s]))

# a = [12121, 32323, 565656, 67676]
# print(''.join([str(i) for i in a]))

# a = [12121, 32323, 565656, 67676]
# print('\n'.join([str(i) for i in a]))





# a = 'sdfsdfgdhnjghkjmkhjbvgsfgs'
# s = (a.split('j'))
# print(s)
# print('\n'.join(s))

# w = [42342, 23423, 345345]
# print('\n'.join([str(i) for i in w]))





# # |||||||||||||||Изучаем функцию map ||||||||||||||||||||
# a = [-1, 2, -3, 4, -500]
# b = (map(abs, a))
# print(set(b))

# s = ['sxs', 'SDSDS', 'Lsd']
# e = map(len, s)
# print(tuple(e))



# # ВОТ АНАЛОГ РЕШЕНИЯ ЭТОЙ ЗАДАЧИ, ТОЛЬКО ЧЕРЕЗ ГЕНЕРАТОР СПИСКОВ
# a = [-1, 2, -3, 4, -500]
# c = [abs(i) for i in a]
# print(c)




# def f(x):
#   return x**2

# a = [-1, 2, -3, 4, -500]
# b = list(map(f, a))
# print(b)



# # Вот так мы применяем встроенные методы: пишем тим, точка и метод без скобок
# s = ['sxs', 'SDSDS', 'Lsd']
# q = map(str.upper, s)
# print(tuple(q))


# Фишки генераторов списков
# a = [1, 2, 3, 4, 23]
# b = [str(i) for i in a]
# c = [i[::-1] for i in b]
# print(c)



# # Вот фишка для того, чтобы вводить много значений через пробел и не только
# s = input().split()
# print(s)

# s = list(map(int, input().split()))
# print(s)


# ||||||||||||ПОДРОБНЕЕ О ГЕНЕРАТОРАХ СПИСКОВ||||||||
# a = [1 for i in range(1000)]
# print(a)

# a = [i**2 for i in range(100)]
# print(a)


# a = [int(i) for i in range(10) if i%2 != 0]
# print(a)

# a = input().split()
# a = [int(i) for i in a]
# print(a)



# from collections import Counter

# s = 'jiujyiuyjoliyouyouhytytrfeexsnghm.k;o,j;oihyuf'
# print(dict(Counter(s)))



# a = input().split()
# b = map(int, a)
# t = (sorted(list(b)))
# print(t[-2])




# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1, n + 1):
#       print(i, end = '')





# a_0 = int(input())
# for i in range(a_0):
#   a = input().split()
#   b = map(int, a)
#   t = (sorted(list(b)))
#   print(t[-2])



# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
    
#     print(sorted(list(set(arr))))[-2]



# # Тяжелая задача на хакерранке с интересным вариантом форматирования для вывода чисел с округлением и двумя символами после запятой
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *otsenka = input().split()
#         scores = list(map(float, otsenka))
#         student_marks[name] = scores
#     posledny_name = input()

#     counter = 0
#     for i in student_marks[posledny_name]:
#         counter += i
#     print('{0:.2f}'.format(counter / 3))







# a = input()
# s = a.split(' ')
# w = '-'.join(s)
# print(w)

# # или вот как хакерранк предлагает обернуть в функцию решение этой задачи. Можно сразу 2 переменные объедтнть в 1 и присвоить ей '-'.join(line.split(' '))

# def split_and_join(line):
#     return '-'.join(line.split(' '))

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)




# |||||||||||||||||||||||||||||||||||||||||||||||||||||||
# a = input()
# l = list(a)
# b = input().split()
# c = list(b)
# l[int(c[0])] = c[1]
# print(''.join(l))



# Вот какое решение нам предлагает Хакерранк
# Здесь предлагается 2 варианта
# 1)
# >>> string = "abracadabra"
# >>> l = list(string)
# >>> l[5] = 'k'
# >>> string = ''.join(l)
# >>> print string
# abrackdabra

# 2)
# >>> string = string[:5] + "k" + string[6:]
# >>> print string
# abrackdabra


# Вот как решил индиец:
# def mutate_string(string, position, character):

#     return string [: position] + character + string[position + 1:]

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# |||||||||||||||||||||||ПОМЕНЯТЬ МЕРСТАМИ РЕГИСТРЫ||||||||||||||||||||||||||||||||

# Мое решение
# s = input()
# t = list(s)

# for i in t:
#   if i == i.lower():
#     i.upper()
#     print(i.upper(), end = '')
#   elif i == i.upper():
#     print(i.lower(), end = '')


# А вот решение индийца
# def change(s):

#     if str.islower(s):
#         return str.upper(s)
#     else:
#         return str.lower(s)

# def swap_case(s):
#     return ''.join(map(change, s))


# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)





# width = 20
# print('HackerRank'.ljust(width,'-'))
# print('HackerRank'.center(width,'-'))
# print('HackerRank'.rjust(width,'-'))






# ||||||||||Задачка с rjust, ljust и center ||||||||||||

#Replace all ______ with rjust, ljust or center. 

# thickness = int(input()) #This must be an odd number
# c = 'H'

# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))    

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



# Вот еще подобная ей задача с WELCOME
# r, c = map(int, input().split(' '))
# for i in range(1, r, 2):
#   print(('.|.' * i).center(c, '-'))
# print('WELCOME'.center(c, '-'))
# for i in range(r-2, -1, -2):
#   print(('.|.' * i).center(c, '-'))





# Обычная задачка на множества
# counter = []
# a = int(input())
# for i in range(a):
#   t = input()
#   counter.append(t)
# q = set(counter)
# l = len(list(q))
# print(l)



# counter = []
# a = int(input())
# for i in range(a):
#   t = int(input())
#   counter.append(t)
# d = set(counter)
# print(*d)
# # b = int(input())



# # |||||||Задача на определение симметричной разности |||||
# a = int(input())
# n = range(a)
# n = input().split()
# b = int(input())
# e = range(b)
# e = input().split()
# p = set(n)
# k = set(e)
# z = (p ^ k)
# g = list(z)
# v = map(int, g)
# m = (sorted(list(v)))
# for i in m:
#   print(i)





# # ||||||||||Вычитание множества из множества||||||||||
# a = int(input())
# n = range(a)
# n = input().split()
# n1 = set(list(map(int, n)))
# b = int(input())
# e = range(b)
# e = input().split()
# e1 = set(list(map(int, e)))
# tt = n1 - e1
# x = len(list(tt))
# print(x)



# Задача со множествами. Найти среднее значение
# a = int(input())
# n = range(a)
# n = input().split()
# n1 = sum(list(set(list(map(int, n)))))
# n2 = n1 / len(list(set(list(map(int, n)))))
# print(n2)


# # Вот вариант решения индийца
# def average(x):
#     x = set(x)
#     return sum(x) / len(x)
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)



# ||| .isalnum() .isalpha() .isdigit() .islower() .isupper() |||||
# Мой вариант решения
# if __name__ == '__main__':
#     s = input()

#     if s.isalnum():
#       print(True)
#     else:
#       print(False)
#     if s.isalpha():
#       print(True)
#     else:
#       print(False)
#     if s.isdigit():
#       print(True)
#     else:
#       print(False)
#     if s.islower():
#       print(True)
#     else:
#       print(False)
#     if s.isupper():
#       print(True)
#     else:
#       print(False)


# # Вариант решения индийца
# if __name__ == '__main__':

#     s = input()

#     print(any([i.isalnum() for i in s]))
#     print(any([i.isalpha() for i in s]))
#     print(any([i.isdigit() for i in s]))
#     print(any([i.islower() for i in s]))
#     print(any([i.isupper() for i in s]))



# # |||||||||||| Импорт переноса текста |||||||||||||||||||||||
# import textwrap

# def wrap(string, max_width):
#     return textwrap.fill(string, max_width)

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)


# #||||||||||||КРАЙНЕ СЛОЖНАЯ И НЕПОНЯТНАЯ ЗАДАЧА. НА БУДУЩЕЕ|||||||||||||||||
# def print_formatted(number):
#     l = len('{0:b}'.format(number))
#     for i in range(1, number + 1):
#         print('{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}'.format(i, w = l))

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)




# a, b = input().split()
# a = a.capitalize()
# b = b.capitalize()
# print(a, b)




# x  = int(input())
# while x > 0:
#   print(x % 10)
#   x = x // 10





# x = int(input())
# kol = 0
# sum_ = 0
# kol_chet = 0
# kol_nech = 0
# pr = 1
# max_ = 0
# min_ = 10**10
# while x > 0:
#   last = x % 10
#   kol += 1
#   sum_ += last
#   if last %2 == 0:
#     kol_chet += 1
#   else:
#     kol_nech +=1
#   pr *= last
#   x = x // 10
#   if last > max_:
#     max_ = last
#   if last < min_:
#     min_ = last


# print(f'Кол-во цифр: {kol}')
# print(f'Сумма всех цифр: {sum_}')
# print(f'Кол-во четных цифр: {kol_chet}')
# print(f'Кол-во нечетных цифр: {kol_nech}')
# print(f'Произведение всех цифр: {pr}')
# print(f'Максимальное число: {max_}')
# print(f'Минимальное число: {min_}')
  


# # Пробуем исполнить вышеуказанный пример в двоичной системе

# x = int(input())
# while x > 0:
#   last = x % 2
#   print(last)
#   x = x // 2




# #|||||||||||||| Алгоритм Евклида ||||||||||||||||||||||||
# # Но если хотя бы одно из чисел очень большое, что программа становится неэффективной, так как тратит слишком много времени на вычисление
# a, b = map(int, input().split())
# while a != b:
#   if a > b:
#     a = a - b
#   else:
#     b = b - a
# print(a)




# # Поэтому есь такой альтернативный вариант
# a = int(input())
# b = int(input()) # b по умолчанию должен быть меньше a
# # a, b = map(int, input().split()) - а здесь не важно, какая переменная больше какой
# while b > 0:
#   # c = a%b
#   # a = b
#   # b = c
#   # ИЛИ
#   a, b = b, a%b
# print(a)



# # |||||||||| Нахождение всех делителей числа ||||||||||| 
# # Эта программа может быть неэффективной, так как займет много времени на вычисление
# n = int(input())
# i = 1
# while i <= n:
#   if n %i == 0:
#     print(i)
#   i += 1



# # Этот алгоритм эффективнее предыдущего в 2 раза, но все равно не идеален
# n = int(input())
# i = 1
# while i <= n // 2:
#   if n %i == 0:
#     print(i)
#   i += 1
# print(n)


# # Данный алгоритм в 1000 раз эффективнее первого
# n = int(input())
# i = 1
# a = []
# while i*i <= n: # или i <= n**0.5:
#   if n %i == 0:
#     a.append(i)
#     if i !=n // i:
#       a.append(n // i)

#   i += 1
# a.sort()
# print(a)



# i = 1
# while True:
#   print(f'Итерация № {i}')
#   if i == 10:
#     break
#   i += 1


#|||||||||||||||| iter и next ||||||||||||||||
# m = iter('hi')
# print(next(m))




# a = [43, 65, 3, 54, 6]
# # count = 0
# for i in a:
#   print(i+5, a.index(i))
#   # count += 1
#   # print(f'{count} обход')
#   # input()




# a = [43, 65, 3, 54, 6]
# for i in range(len(a)):
#   print(i, a[i])




# a = [1, 2, 34, 65, 87, 45, 0, 5, 5]
# b = []
# for i in a:
#   if not i in b:
#     b.append(i)
# print(b)



# a = [1, 2, 34, 65, 87, 45, 0, 5, 5]
# print(sorted(list(set(a))))



# ||||||||||||||||||lambda|||||||||||||||||||||||||||||||
# r = lambda x: x**2
# print(r(7))




# x = int(input())
# t = lambda x: 'positive' if x > 0 else 'negative'
# print(t(x))



# a = [78, 56, 23, 8, 54512, 65, 98, 2354, 41, 5000]
# a.sort(key = lambda x: x // 10%10)
# print(a)



# # |||||||||||||||| Факториал |||||||||||||||||||||||
# s = int(input())
# res = 1
# for i in range(1, s + 1):
#   res *= i
#   i += 1
# print(res)



# # ||||||||||||||||||Метод подсчета|||||||||||||||||||||||
# from collections import Counter
# s = [2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 4, 2]
# print(dict(Counter(s)))

# # Или то же самое более сложным методом подсчета
# s = [2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 4, 2]
# c = [0] * 6 # 6 потому что здесь цифры от 0 до 5 (всего 6)
# for i in s:
#   c[i] += 1
# for i in range(6):
#   print(i, c[i])





# |||||||||||||||||||Вложенный циклы|||||||||||||||||||
# for i in range(3):
#   for j in range(5):
#     print(j, end = '')
#   print()




# # Преребираем все значения пароля
# from string import printable

# for b1 in printable:
#   for b2 in printable:
#     for b3 in printable:
#       print(b1, b2, b3)




# # # Создаем таблицу умножения
# for i in range(1, 10):
#   for j in range(1, 11):
#     print(f'{i} * {j} = {i * j}', end = ' ')
#   print()




# ||||||||||||||||||||||||||Задание из ЕГЭ ТЫКВА |||||||||||||||||||||
# c = 0
# for b1 in 'tukva':
#   for b2 in 'tukva':
#     for b3 in 'tukva':
#       for b4 in 'tukva':
#         for b5 in 'tukva':
#           for b6 in 'tukva':
#             for b7 in 'tukva':
#               rez = b1 + b2 + b3 + b4 + b5 + b6 + b7
#               if rez[0] in 'tkv' and rez[-1] in 'tkv':
#                 if rez.count('a') + rez.count('u') == 2:
#                   c += 1
# print(c)





# # ||||||||||||||||||| И снова факториал ||||||||||||||||
# x = int(input())
# s = 0
# while x > 0:
#   s += x%10 # таким образом мы итерируемся из, к примеру, числа 1234 сначала по значению 4 и его в счетчик добавляем, потом 3 и так далее

#   x //= 10 # здесь мы задаем шаг итерации, что сначала у нас 1234, потом при след шаге 123 и так до тех пор, пока цифр не останется и цикл не закончится
# print(s)






# for i in range(1, 100001):
#   x = i
#   s = 0
#   while x > 0:
#     s += x%10
#     x //= 10
#   print(i, s)


# print(sum(range(4)))



#_______________________________________________________
# Задание со степика, которое я сам не смог решить

# Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.
# В классе Counter нужно определить метод start_from, который принимает один необязательный аргумент - значение, с которого начинается подсчет, по умолчанию равно 0
# Также нужно создать метод increment, который увеличивает счетчик на 1.
# Затем необходимо создать метод display, который печатает фразу "Текущее значение счетчика = <value>" и метод reset,  который обнуляет экземпляр счетчика
# Пример работы с классом Counter
# c1 = Counter()
# c1.start_from()
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 1"
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 2"
# c1.reset()
# c1.display() # печатает "Текущее значение счетчика = 0"
#
# c2 = Counter()
# c2.start_from(3)
# c2.display() # печатает "Текущее значение счетчика = 3"
# c2.increment()
# c2.display() # печатает "Текущее значение счетчика = 4"

class Counter:
    d = 0

    def start_from(self, d=0):
        self.d = d

    def increment(self):
        self.d += 1

    def display(self):
        print(f"Текущее значение счетчика: {self.d}")

    def reset(self):
        self.d = 0





# Кошки
# class Cat:
#     breed = 'pers'

#     def set_value(self, value, age=0):
#         self.name = value
#         self.age = age





# __init__
class Cat:


    def set_value(self, value, age=0):
        self.name = value
        self.age = age

    def __init__(self, name, breed='pers', age=1, color='white'):
        print(f'hello, new object is {self, name, breed, age, color}')
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color












class Goose:
# задаем аттрибуты класса
    weight = 0
    egg = 0
    voice = ''
    eggs_counter = 0
# пишем все методы таким образом, чтобы при вызове не было обязательных аргументов. Чтобы все было уже по умолчанию
    def collect_eggs(self, egg = 1):
        self.eggs_counter += egg
        print(self.eggs_counter)

    def feed(self, food=1):
        self.weight += food
        print(self.weight)

    def distinguish_by_voices(self, voice_of_goose='Внимание! Я гусь, я говорю на гусином языке!'):
        self.voice = voice_of_goose
        print(self.voice)
# прописываем экземпляры
gray_goose = Goose()
white_goose = Goose()

# Проверяем работоспособность методов
gray_goose.collect_eggs()

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Cow:
    milk_volume = 0
    weight = 0
    voice = ''
    milk_counter = 0

    def collect_milk(self, milk_volume = 1):
        self.milk_counter += milk_volume
        print(self.milk_counter)

    def feed(self, food = 1):
        self.weight += food
        print(self.weight)

    def distinguish_by_voices(self, voice_of_cow='Внимание! Я корова, и вот я произношу мууу!'):
        self.voice = voice_of_cow
        print(self.voice)

manka = Cow()

# проверка кода
manka.collect_milk()

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Sheep:
    weight = 0
    haircut_level = 0
    voice = ''

    def cut(self, haircut = 1):
        self.haircut_level += haircut
        print(self.haircut_level)

    def feed(self, food = 1):
        self.weight += food
        print(self.weight)

    def distinguish_by_voices(self, voice_of_sheep='Внимание! Я овен, и вот я произношу мееее!'):
        self.voice = voice_of_sheep
        print(self.voice)

curly = Sheep()
lamb = Sheep()

# проверка кода
lamb.distinguish_by_voices()

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Chicken:
    weight = 0
    egg = 0
    voice = ''
    eggs_counter = 0

    def collect_eggs(self, egg = 1):
        self.eggs_counter += egg
        print(self.eggs_counter)

    def feed(self, food=1):
        self.weight += food
        print(self.weight)

    def distinguish_by_voices(self, voice_of_chicken='Внимание! Я курица, и вот я произношу кукареку!'):
        self.voice = voice_of_chicken
        print(self.voice)

ko_ko = Chicken()
kuka_re_ku = Chicken()

# проверка кода
kuka_re_ku.collect_eggs()

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Goats:
    milk_volume = 0
    weight = 0
    voice = ''
    milk_counter = 0

    def collect_milk(self, milk_volume = 1):
        self.milk_counter += milk_volume
        print(self.milk_counter)

    def feed(self, food = 1):
        self.weight += food
        print(self.weight)

    def distinguish_by_voices(self, voice_of_goat='Внимание! Я козел, и вот я говорю на козьем языке!'):
        self.voice = voice_of_goat
        print(self.voice)

horns = Goats()
hooves = Goats()

# проверка кода
hooves.distinguish_by_voices()

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Duck:
    weight = 0
    egg = 0
    voice = ''
    eggs_counter = 0

    def collect_eggs(self, egg = 1):
        self.eggs_counter += egg
        print(self.eggs_counter)

    def feed(self, food=1):
        self.weight += food
        print(self.weight)

    def distinguish_by_voices(self, voice_of_duck='Внимание! Я утка, и вот я произношу говорю на утином языке!'):
        self.voice = voice_of_duck
        print(self.voice)

kryakva = Duck()

# проверка кода
kryakva.collect_eggs()


#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
