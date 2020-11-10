# CSV |||||||||||||||||||||||||||||||||||||||||||
import csv

csv.register_dialect("customcsv", delimiter=",", quoting=csv.QUOTE_NONE, quotechar="`", escapechar="\\") # Это возможные параметры настроек, собранные в диалект 
# Это наши ключи: guid, _id, pubDate, description, link, title
# newline="" - прописываем в менеджере контекста, чтобы избежать пустых строк





# # Без всякого преобразования итерируемся:
# with open("files/newsafr.csv", newline="") as f:
# 	reader = csv.reader(f, delimiter=',')
# 	for item in reader:
# 		print(item)




# # Преобразуем в список:
# with open("files/newsafr.csv", newline="") as f:
# 	reader = csv.reader(f, delimiter=',')
# 	news_list = list(reader)

# header = news_list.pop(0) # убираем заголовок
# print(len(news_list))
# print(news_list[:3])




# # Преобразуем в словарь:
# with open("files/newsafr.csv", newline="") as f:
# 	reader = csv.DictReader(f, delimiter=",")
# 	for item in reader:
# 		print(item)




# # Теперь после открытия файла, записываем данные в новый файл
# with open("files/newsafr.csv", newline="") as f:
# 	reader = csv.reader(f, delimiter=',')
# 	news_list = list(reader)
# with open("files/newsafr2.csv", "w", newline="") as f:
#   writer = csv.writer(f)
#   writer.writerows(news_list[:3])




# # Теперь воспользуемся всеми параметрами настроек
# with open("files/newsafr.csv", newline="") as f:
# 	reader = csv.reader(f, delimiter=',')
# 	news_list = list(reader)
# with open("files/newsafr2.csv", "w", newline="") as f:
#   writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar="`", escapechar="\\")
#   writer.writerows(news_list[:3])




# # Теперь воспользуемся всеми параметрами настроек в виде диалекта
# with open("files/newsafr.csv", newline="") as f:
# 	reader = csv.reader(f, delimiter=',')
# 	news_list = list(reader)
# with open("files/newsafr2.csv", "w", newline="") as f:
#   writer = csv.writer(f, "customcsv")
#   writer.writerows(news_list[:3])
# CSV |||||||||||||||||||||||||||||||||||||||||||




# JSON |||||||||||||||||||||||||||||||||||||||||||
import json
from pprint import pprint

# # Читаем. Добываем тайтлы через pprint
# with open("files/newsafr.json") as f:
# 	json_data = json.load(f)
# titles = json_data["rss"]["channel"]["items"]
# pprint(titles)




# # Добываем тайтлы через итерацию
# with open("files/newsafr.json") as f:
# 	json_data = json.load(f)
# titles = json_data["rss"]["channel"]["items"]
# for title in titles:
# 	print(title["title"])
# 	print()




# # Если хотим записать в другой кодировке
# with open("files/newsafr.json") as f:
# 	json_data = json.load(f)
# titles = json_data["rss"]["channel"]["items"]
# with open("files/newsafr2.json", "w", encoding="cp1251") as f:
#   json_data = json.dump(titles, f, ensure_ascii=False, indent=2)
# JSON |||||||||||||||||||||||||||||||||||||||||||
  



# XML |||||||||||||||||||||||||||||||||||||||||||
import xml.etree.ElementTree as ET
# для xml вместо менеджера контекста используются след. 2 строки:
# parser = ET.XMLParser(encoding="utf-8")
# tree = ET.parse("files/newsafr.xml", parser) # в этой переменной находится весь развернутый xml
# root = tree.getroot() # обязательно для дальнейшей работы получаем корень




# # print(root) # <Element 'rss' at 0x7f76cd95fd60>
# print(root.tag)
# print(root.text) # тут пусто, так как у корня нет текста в этом файле
# print(root.attrib)
# print(root.attrib.keys())




# items = root.findall("channel/item") # находим все items
# print(len(items)) # узнаем из кол-во
# for item in items:
#   print(item.find("title")) # так мы получим только указатели
#   print(item.find("title").text) # а так мы получим текст
#   print()




# # Пробуем сохранить (записать)
# tree.write("files/newsafr2.xml", encoding="utf_8_sig")
# В данном случае флаг "utf_8_sig" позволяет прочитать все варианты кодировки utf_8