
from pprint import pprint
import os

file_path_1 = os.path.join(os.getcwd(), '1.txt')
with open(file_path_1) as f_1:
    file_name_1 = '1.txt'
    dct_1 = {}
    counter_1 = []
    for i in f_1:
        counter_1.append(i.strip())
        ln_1 = len(counter_1)
    dct_1[tuple(counter_1)] = ln_1
# pprint(dct_1)

file_path_2 = os.path.join(os.getcwd(), '2.txt')
with open(file_path_2) as f_2:
    file_name_2 = '2.txt'
    dct_2 = {}
    counter_2 = []
    for i in f_2:
        counter_2.append(i.strip())
        ln_2 = len(counter_2)
    dct_2[tuple(counter_2)] = ln_2
# pprint(dct_2)

file_path_3 = os.path.join(os.getcwd(), '3.txt')
with open(file_path_3) as f_3:
    file_name_3 = '3.txt'
    dct_3 = {}
    counter_3 = []
    for i in f_3:
        counter_3.append(i.strip())
        ln_3 = len(counter_3)
    dct_3[tuple(counter_3)] = ln_3
# pprint(dct_3)


dc = {}
dc.update(dct_1)
dc.update(dct_2)
dc.update(dct_3)
# pprint(dc)
a = sorted(dc.items(), key=lambda x: x[1])
# pprint(a)



filename_list = [file_name_1, file_name_2, file_name_3]
len_list = [ln_1, ln_2, ln_3]
z = zip(filename_list, len_list)
ee = list(z)



cc = {}
for i in ee:
    cc[i[0]] = i[1]
# print(cc)
vv = sorted(cc.items(), key=lambda x: x[1])
# print(vv)
for i in vv:
    print(i)



d = []
for i in a:
    d.append(list(i[0]))
d[0].extend(d[1])
d[0].extend(d[2])
k = (d[0])
for i in k:
    print(i)

