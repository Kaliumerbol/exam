
#1
# x = int(str(float(5)))
# int

#2
x = 'aa' == 'AA'
# boolian -- логичекий тип

#3
x = {i: i**2 for i in range(5)}
# dictionary --- словарь

#4
x = set(list((5, 6, 7)))
# set --- множества без дубликатов

#5
a = {1: 1, 2: 4, 3: 9}
x = a.get(4)
# None так как должно быть ключ и заначение

#6
x = [].append('j')
# None так как нельзя просто вызвать список. Надо ипользовать генератор

#7
for i in range(10):
    if i < 5:
        x = 'hello'
    else:
        x = 5
# 5 раз str и 5 раза int


#8
# x = input('Enter and integer: ')
# тип str  так как инпут по умолчанию str

#9
a = 5
b = [1, 3, 5, ]
x = 'x'
a, b, x = x, a, b
# тип list -- список
#10
def func(x, y=5):
		return x + y
x = func('Jaguar ', 'hunter')
# тип str


# Задание_2

def depos(user_money, user_pros, user_mon_want):
    mon = 0
    while user_money < user_mon_want:
        dep_cash = ((user_pros / 100) / 12) * user_money + user_money
        user_money = int(dep_cash) 
        # print(user_money)
        mon = mon + 1
    else:
        return('Для накопления необходимой суммы вам понадобятся ' +  str(mon) + ' месяца!')

# print(depos(int(input('Какую сумму вы хотите положить?: ')), int(input('Процент годовых?: ')), int(input('Сколько вы хотите получить?: '))))

# Задание_3_1
list_1 = ['Element', 'start', 'finish']
def func(*list_2):
    for i_i in list_2:
        for i in i_i:
            list_1.insert(-1, i)
    return list_1
print(func(['hello', 5, 'John', ]))
# ['Element', 'start', 'hello', 5, 'John', 'finish']

# Задание_3_2
dic_u = {}
def func(*arc):
    key = 1
    for i in arc:
        im = {i: key}
        dic_u.update(im)
        key = key + 1
    return dic_u
print(func('x', 5, 'John'))
# {'x':1, 5:2, 'John':3}