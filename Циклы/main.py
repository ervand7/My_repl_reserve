boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
a = sorted(boys)
b = sorted(girls)
c = (zip(a, b))
d = list(c)

print('Идеальные пары: ')

if len(boys) != len(girls):
  print('Уважаемый пользователь! Если количество мужчин и женщин на сайте не равно, то есть вероятность, что вы останетесь без пары(')
else:
  for couple in d:
    print(f'{couple[0]} и {couple[1]}')


# couple1 = (d[0])
# couple2 = (d[1])
# couple3 = (d[2])
# couple4 = (d[3])
# couple5 = (d[4])


  







# perfect_couple = zip(a, b)
# print(perfect_couple)
# print('Идеальные пары: ', (list(perfect_couple)))

# print(couple1, couple2, couple3, couple4, couple5)

# perfect_couple2 = [
#  ['Alex', 'Emma'],
#  ['Arthur', 'Kate'],
#  ['John', 'Kira'],
#  ['Peter', 'Liza'], 
#  ['Richard', 'Trisha']
# ]
# for couple in perfect_couple2:
# #   # print(company)
#   print(f'{couple[0]} и {couple[1]}')



