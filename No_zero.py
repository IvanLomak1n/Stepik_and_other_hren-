# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
#
# Формат входных данных
# На вход программе подаются 10 целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести произведение отличных от нуля чисел.
#
# Примечание 1. Гарантируется, что хотя бы одно из 10 чисел является ненулевым.
#
# Примечание 2. Отличные от нуля числа – те числа, которые не равны нулю.


total = 1
for i in range(1,11):
    n = int(input())
    if n!=0:
        total*=n
print(total)


# Даются 10 чисел всяких разных ,больше нуля или нольбне по порядку. Создаем цикл с количеством
# вводимых чисел, а сам ввод этих чисел указываем в цикле,там они все и считываются!!