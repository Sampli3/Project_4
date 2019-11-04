# Данная программа раскодирует ваше сообщение.

import hashlib

# Запрос индивидуальных данные для расшифровки.

print('Для расшифровки текста отправитель должен вам сообщить индивидульные параметры шифрования.')
first_number = int(input('Введите, пожалуйста, первый ключ: ').strip())
second_number = int(input('Введите, пожалуйста, второй ключ: ').strip())
password = hashlib.sha1(input('Введите, пожалуйста, четырехзначный пароль '
                              'для доступа к программе расшифровки: ').strip().encode('utf-8')).hexdigest()
password_hesh = input('Введите, пожалуйста, хешированный пароль  для проверки подлинности введенного вами '
                      'четырехзначного пароля к программе расшифровки: ').strip()
while True:
    if password == password_hesh:
        print('Верный пароль!')
        print('Доступ к программе открыт.')
        print()
        break
    else:
        print('Неверный пароль!')
        password = hashlib.sha1(input('Введите, пожалуйста, правильный четырехзначный пароль '
                                      'для доступа к программе расшифровки: ').strip().encode('utf-8')).hexdigest()

# Преобразуем зашифрованный текст для корректной работы программы расшифровки.
cipher_text = input('Введите, пожалуйста, зашифрованный текст: ').strip()
cipher_text = cipher_text + ' -1'
lis = []
stroka = ''
for i in cipher_text:
    if i != ' ':
        stroka += i
    if i == ' ':
        lis += [int(stroka)]
        stroka = ''

# Программа расшифровки.
print()
for number in lis:
    ascii_number = int(((((number - (second_number * 2)) + 100) - (first_number * 2)) / 2) - 152)
    letter = chr(ascii_number)
    print(letter, end='')
print()
print('Расшифрованный текст.')
print()
print('Если расшифрованная информация нечитаема - убедитесь в корректности индивидуальных параметров шифрования.')
