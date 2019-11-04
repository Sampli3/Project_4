# Данная программа закодирует ваше текстовое сообщение для передачи.

import hashlib

# Запрашиваем текст для кодирования.
text = input('Введите, пожалуйста, текст для шифрования: ')

# Попросим пользователья задать переменные для индивидуального кодирования.
first_number = int(input('Введите, пожалуйста, первое целое число в интервале от 0 до 100, '
                         'которое будет являться первым ключом для расшифровки: '))
while True:
    if 0 <= first_number <= 100:
        break
    else:
        first_number = int(input('Введите, пожалуйста, первое ЦЕЛОЕ число в ИНТЕРВАЛЕ от 0 до 100, '
                                 'которое будет являться первым ключом для расшифровки: '))

second_number = int(input('Введите, пожалуйста, второе целое число в интервале от 0 до 100, '
                          'которое будет являться вторым ключом для расшифровки: '))
while True:
    if 0 <= second_number <= 100:
        break
    else:
        second_number = int(input('Введите, пожалуйста, второе ЦЕЛОЕ число в ИНТЕРВАЛЕ от 0 до 100, '
                                  'которое будет являться первым ключом для расшифровки: '))
password = input('Введите, пожалуйста, пароль, состоящий из черырех цифр, '
                 'для доступа к программе расшифровки: ')
while True:
    if len(password) == 4:
        break
    else:
        password = input('Введите, пожалуйста, пароль, состоящий из ЧЕТЫРЕХ положительных цифр, '
                         'для доступа к программе расшифровки: ')

# Создаем хешированный пароль для доступа к программе расшифровки.
password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest()
print()

# Алгоритм кодирования.
code_first = ''
for symbol in text:
    ascii_number = ord(symbol)
    ascii_number = ((((ascii_number + 152) * 2) + (first_number * 2)) - 100) + (second_number * 2)
    print(ascii_number, end=' ')

# Вывод информации.
print()
print('Ваш текст закодирован.')
print()
print('Для расшифровки отправьте получателю следующие данные: ')
print('-первый ключ:', first_number)
print('-второй ключ:', second_number)
print('-четырехзначный пароль:', password)
print('-хешированный пароль:', password_hash)
print('-зашифрованный текст')