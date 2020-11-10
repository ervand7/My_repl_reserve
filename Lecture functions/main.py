# Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять ни один документ.
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.





documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

# Перечень полок, на которых находятся документы хранится в следующем виде:

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }







def search_by_number():
  doc_number = input('Введите номер документа: ')
  return doc_number

def request_meaning(key):
  meaning = input(f'Введите значение {key} документа: ')
  return meaning






def print_list():
  print('Список всех документов\n')
  for doc in documents:
    print([i for i in doc.values()])






def find_shelf(doc_number):
  for shelf in directories.items():
    if doc_number in shelf[1]:
      break
  else:
    print(f'Документ с номером {doc_number} не найден')
    shelf = None
  return shelf

def print_shelf(doc_number = None):
  while doc_number == None:
    doc_number = search_by_number()
    if find_shelf(doc_number) == None:
      doc_number = None
  shelf = find_shelf(doc_number)
  if shelf != None:
    print(f'Документ № {doc_number} находится на полке № {shelf[0]} по индексу {shelf[1].index(doc_number)}')






def find_doc(doc_number, print_stat = True):
  for doc in documents:
    if doc['number'] == doc_number:
      break
    else:
      doc = None
  if doc == None and print_stat == True:
    print(f'Документ № {doc_number} не найден')
  return doc



def print_people(doc_number = None):
  if doc_number == None:
    doc_number = search_by_number()
  doc = find_doc(doc_number)
  if doc != None:
    try:
          print(f'Документ № {doc_number} принадлежит пользователю {doc["name"]}')
    except KeyError:
          print(f'Внимание! Отсутствуют данные о владельце документа № {doc["number"]}')


def add_docs(number = None): 

  doc = dict.fromkeys(documents[0].keys())
  
  while True:
    for key in doc.keys():
      if number != None:
        if key == 'number':
          doc[key] = number
          continue
      doc[key] = request_meaning(key)
    
    if find_doc(doc['number'], False) != None:
      print(f'Документ с таким номером уже существует:')
    else:
      break

  documents.append(doc)


def main_menu():

    while True:


      print("\n".join([msg for msg in user_enviroment]))
      command = input('\nВведите команду: ')

      if command not in buttons.keys():
          print('Неверная команда, повторите ввод')
          continue

      if command == 'q':
          print('Ваш сеанс окончен.')
          break


      else:
          buttons[command]()




user_enviroment = [
  'команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин": [l]', 
  'команда, которая спросит номер документа и выведет имя человека, которому он принадлежит: [p]', 
  'команда, которая спросит номер документа и выведет номер полки, на которой он находится: [s]', 
  'команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться: [a]', 
  'Завершение сеанса: [q]'
  ]




buttons = {'l': print_list, 's': print_shelf, 'p': print_people, 'a': add_docs, 'q': None}





def main():
    main_menu()

if __name__ == '__main__':

  main()







