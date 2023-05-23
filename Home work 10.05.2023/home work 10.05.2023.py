# Задание 1. Не знала, куда вставить цикл while. Спасибо за помощь, теперь всё получилось!

# Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список (тип
# списка нужно выбрать в зависимости от поставленной
# ниже задачи). После чего нужно показать меню, в котором
# предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число существует в списке,
# нужно вывести сообщение пользователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь
# вводит с клавиатуры число для удаления)
# 3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала
# или с конца)
# 4. Проверить есть ли значение в списке
# 5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все
# вхождения)
# В зависимости от выбора пользователя выполняется
# действие, после чего меню отображается снова.

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None
#
#
# class DualLinkedList:
#     def __init__(self, lst):
#         self.head = None
#         self.tail = None
#         self.lst = lst
#         for value in lst[0:]:
#             self.push(value, unique=False)
#
#     def push(self, value, unique=True):
#         if unique and self.is_there(value):
#             print('Это значение уже есть в списке!')
#             return
#         new_node = Node(value)
#
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
#
#         current_node = self.head
#         while current_node.next is not None:
#             current_node = current_node.next
#
#         current_node.next = new_node
#         new_node.prev = current_node
#         self.tail = new_node
#         print('Значение добавлено')
#
#     def delete(self, value):
#         if self.head is None:
#             return
#
#         if self.head.value == value:
#             self.head = self.head.next
#             self.head.prev = None
#             return
#
#         current_node = self.head
#         while current_node.next:
#             if current_node.next.value == value:
#                 current_node.next = current_node.next.next
#                 if current_node.next:
#                     current_node.next.prev = current_node
#                 return
#             current_node = current_node.next
#
#     def is_there(self, value):
#         if self.head is None:
#             return False
#
#         if self.head.value == value:
#             return True
#
#         current_node = self.head
#         while current_node.next is not None:
#             if current_node.next.value == value:
#                 return True
#             current_node = current_node.next
#         return False
#
#     def is_empty(self):
#         if self.head is None:
#             print('List is empty!')
#             return
#
#         print(None, end=' <-> ')
#         current_node = self.head
#         while current_node:
#             print(current_node.value, end=' <-> ')
#             current_node = current_node.next
#         # print(None)
#
#     def find(self, value):
#         if value not in self.lst:
#             print('Такого числа нет')
#         else:
#             print(f'Число {value} есть в списке')
#
#     def replace(self, old_value, new_value):
#         if self.head is None:
#             return
#         if self.head.value == old_value:
#             self.head.value = new_value
#             if not all:
#                 return
#
#         current_node = self.head
#         while current_node is not None:
#             if current_node.value == old_value:
#                 current_node.value = new_value
#                 if not all:
#                     return
#             current_node = current_node.next
#
#     def show(self, reverse=False):
#         if self.head is None:
#             print('List is empty!')
#             return
#         print('None', end=' <-> ')
#         if reverse:
#             current_node = self.tail
#             while current_node is not None:
#                 print(current_node.value, end=' <-> ')
#                 current_node = current_node.prev
#         else:
#             current_node = self.head
#             while current_node is not None:
#                 print(current_node.value, end=' <-> ')
#                 current_node = current_node.next
#         # print('None')
#
#     def command(self):
#         while True:
#             command = input('Введите номер команды:\n'
#                             '1. Добавить новое число в список\n'
#                             '2. Удалить все вхождения числа из списка\n'
#                             '3. Показать содержимое списка\n'
#                             '4. Проверить есть ли значение в списке\n'
#                             '5. Заменить значение в списке\n'
#                             '0. Выйти.\n')
#             if command == '0':
#                 break
#             elif command == '1':
#                 value = int(input('введите число: '))
#                 print(self.push(value))
#             elif command == '2':
#                 value = int(input('Введите число '))
#                 print(self.delete(value))
#             elif command == '3':
#                 print(self.show())
#             elif command == '4':
#                 value = int(input('Введите число:'))
#                 print(self.find(value))
#             elif command == '5':
#                 old_value = int(input('Введите старое число: '))
#                 new_value = int(input('Введите новое число: '))
#                 print(self.replace(old_value, new_value))
#
#
# a = DualLinkedList([int(input('Введите число ')) for i in range(3)])
# a.command()


# Задание 2
# Реализуйте класс стека для работы со строками (стек
# строк).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки
# из стека.
# При старте приложения нужно отобразить меню с
# помощью, которого пользователь может выбрать необходимую операцию.

# class Stack:
#     def __init__(self, lst, size):
#         self.lst = lst
#         self.size = size
#
#     def push(self, value):
#         if self.is_full():
#             print('Stack is full!')
#         else:
#             if not isinstance(value, str):
#                 try:
#                     value = str(value)
#                 except ValueError:
#                     print(f'Argument {value} is wrong data type')
#                 else:
#                     print('Warning! Your data type was reduced to str!'
#                           f'And tour value will be replaced with {value}')
#                     self.lst.append(value)
#             else:
#                 self.lst.append(value)
#                 print(f'Value \'{value}\' added!')
#
#     def length(self):
#         return len(self.lst)
#
#     def is_empty(self):
#         if self.length() == 0:
#             return 'Stack is empty!'
#         return False
#
#     def is_full(self):
#         if self.length() == self.size:
#             return 'Stack is full!'
#         return False
#
#     def pop(self):
#         return self.is_empty() or self.lst.pop()
#
#     def peek(self, value):
#         return self.is_empty() or self.lst[int(value)]
#
#     def clear(self):
#         self.lst.clear()
#         return 'Stack is cleared!'
#
#     def show(self):
#         return f' -> '.join(map(str, self.lst))
#
#     def commands(self):
#         while True:
#             command = input('Введите номер команды:\n'
#                             '1. Добавить новую строку в стек\n'
#                             '2. Вытолкнуть строку из стека\n'
#                             '3. Посчитать количество строк в стеке\n'
#                             '4. Проверить, пустой ли стек\n'
#                             '5. Проверить, полный ли стек\n'
#                             '6. Очистить стек\n'
#                             '7. Показать содержимое стека\n'
#                             '8. Получить значение без выталкивания верхней строки из стека\n'
#                             '0. Выйти.\n')
#             if command == '0':
#                 break
#             elif command == '1':
#                 value = input('Введите строку для добавления: ')
#                 print(self.push(value))
#             elif command == '2':
#                 print(f'Значение {self.pop()} удалено')
#             elif command == '3':
#                 print(self.length())
#             elif command == '4':
#                 print(self.is_empty())
#             elif command == '5':
#                 print(self.is_full())
#             elif command == '6':
#                 print(self.clear())
#             elif command == '7':
#                 print(self.show())
#             elif command == '8':
#                 value = input('Введите индекс значения: ')
#                 print(self.peek(value))
#
#
# start_nums = [input('Введите строку: ') for i in range(3)]
# stack = Stack(start_nums, 5)
# stack.commands()


# Задание 3
# Измените стек из второго задания, таким образом,
# чтобы его размер был нефиксированным.
#
# class Stack:
#     def __init__(self, lst):
#         self.lst = lst
#
#     def push(self, value):
#         if not isinstance(value, str):
#             try:
#                 value = str(value)
#             except ValueError:
#                 print(f'Argument {value} is wrong data type')
#             else:
#                 print('Warning! Your data type was reduced to str!'
#                       f'And tour value will be replaced with {value}')
#                 self.lst.append(value)
#         else:
#             self.lst.append(value)
#             print(f'Value \'{value}\' added!')
#
#     def length(self):
#         return len(self.lst)
#
#     def is_empty(self):
#         if len(self.lst) == 0:
#             return 'Stack is empty!'
#         return False
#
#     def pop(self):
#         return self.is_empty() or self.lst.pop()
#
#     def peek(self, value):
#         return self.is_empty() or self.lst[int(value)]
#
#     def clear(self):
#         self.lst.clear()
#         return 'Stack is cleared!'
#
#     def show(self):
#         return f' -> '.join(map(str, self.lst))
#
#     def commands(self):
#         while True:
#             command = input('Введите номер команды:\n'
#                             '1. Добавить новую строку в стек\n'
#                             '2. Вытолкнуть строку из стека\n'
#                             '3. Посчитать количество строк в стеке\n'
#                             '4. Проверить, пустой ли стек\n'
#                             '5. Очистить стек\n'
#                             '6. Показать содержимое стека\n'
#                             '7. Получить значение без выталкивания верхней строки из стека\n'
#                             '0. Выйти.\n')
#             if command == '0':
#                 break
#             elif command == '1':
#                 value = input('Введите строку для добавления: ')
#                 print(self.push(value))
#             elif command == '2':
#                 print(f'Значение {self.pop()} удалено')
#             elif command == '3':
#                 print(self.length())
#             elif command == '4':
#                 print(self.is_empty())
#             elif command == '5':
#                 print(self.clear())
#             elif command == '6':
#                 print(self.show())
#             elif command == '7':
#                 value = input('Введите индекс значения: ')
#                 print(self.peek(value))
#
#
# start_nums = [input('Введите строку: ') for i in range(3)]
# stack = Stack(start_nums)
# stack.commands()
