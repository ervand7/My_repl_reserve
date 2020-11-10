# Using of dictionaries
contacts = {
    'Ivan ivanov':{
        'birthday': '13 jul 1988', 'city': 'New-York', 'phone': '111-111-111', 'children': 4
    },
    'Petr Petrov': {
        'birthday': '23 jul 1953', 'city': 'Moscow', 'phone': '888-999-555', 'children': 3
    },
    'Vasya Xxx': {
        'birthday': '3 may 1953', 'city': 'Piter', 'phone': '123-321-234', 'children': 1
    }
}
# # 1-st variant of using
# for i in contacts:
#     print(i, contacts[i]['birthday'], contacts[i]['city'])

# # 2-nd vafiant of using
# for i in contacts:
#   print(i)
#   for data in contacts[i]:
#     print(contacts[i][data])





# # lambda - functions
# r = lambda x: x**2
# print(r(1123423))

# # you can write instead this:
# def f(x):
#   if x > 0:
#     return 'positive'
#   else:
#     return 'negative'

# # this
# t = lambda x: 'positive' if x > 0 else 'negative'

# instead this:
# def f(x):
#   return x % 10
# a = [78, 56, 23, 8, 54512, 65, 95, 2354, 41, 5000]
# a.sort(key=f)
# print(a)

#this:
# a = [78, 56, 23, 8, 54512, 65, 95, 2354, 41, 5000]
# a.sort(key=lambda x: x % 10)
# print(a)