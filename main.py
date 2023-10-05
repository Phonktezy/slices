# s = input()
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[0:-2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-2])
# print(len(s))
# print(s.count)
# word = input()
# middle = len(word) // 2
# print(middle)
# new_word = word[middle:] + word[:middle]
# print(new_word)s
# first_word = input("Введите слово: ")
# find_letter = first_word.find('f')
# find_letterf = first_word.rfind('f')
# if find_letter != -1:
#     if find_letterf == find_letter:
#         print("Первая инициируемая буква найдена: ", find_letter)
#     else:
#         print("Буква в начале 'f':", find_letter)
#         print("Буква в конце 'f':", find_letterf)
# s = input("Введите слово: ")
# a = s.find('h')
# b = s.rfind('h') + 1
# print("Результат: ", s[:a] + s[b:])
# s = input("Введите номер: ")
# s = s.replace('1','one')
# print("Результат: ", s)
# s = input()
# s = s.replace('@', '')
# print(s)
#
# s = input()
# a = s[:s.find('h') + 1]
# b = s[s.find('h') + 1:s.rfind('h')]
# c = s[s.rfind('h'):]
# print(a + b.replace('h', 'H') + c)
#1
a = int(input())
b = int(input())
if a < b:
    print(a)
else:
    print(b)
#2
x = int(input(''))
if x > 0:
    print('sign(x)=1')
elif x < 0:
    print('sign(x)=-1')
else:
    print('sign(x)=0')
#3
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')
#4
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')
#5
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
#6
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
#7
n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
#8
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
#9
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
    #10
n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')




