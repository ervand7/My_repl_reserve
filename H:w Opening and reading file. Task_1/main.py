from pprint import pprint

with open(r'task_1.txt') as f:
    cook_book = {}
    row = f.readline()
    while row != '':

        count_for_iter = int(f.readline())
        dict_of_one_dish = {}
        list_only_all_ing = []

        for i in range(count_for_iter):
            a = f.readline().split('|')

            name_of_ingredient = a[0]
            quantity = a[1].strip()
            measure = a[2].strip()

            line = {'ingredient_name': name_of_ingredient, 'quantity': quantity, 'measure': measure}
            list_only_all_ing.append(line)

            dict_of_one_dish[row.strip()] = list_only_all_ing
            cook_book.update(dict_of_one_dish)

        f.readline()
        row = f.readline()
pprint(cook_book) # ГЛАВНАЯ ПРОВЕРКА ВСЕГО КОДА

#         pprint(count_for_iter)
#         pprint(dict_of_one_dish)
#         pprint(list_only_all_ing)