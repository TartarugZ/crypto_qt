import math


def is_simple_p(number):
    i = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            i = i + 1
    if i <= 0:
        return True
    else:
        return False


def check_right_g_and_x(primitive_or_secret, crypto):
    return 1 < primitive_or_secret < crypto


def check_right_k(sender_key, crypto):
    return (1 < sender_key < crypto - 1) and (math.gcd(sender_key, crypto - 1) == 1)


def encrypt(crypto, primitive, secret_key, sender_number, message):
    if not (8470 < crypto < 55296):
        return "Модуль криптосистемы не входит в промежуток от 8470 до 55296!"
    if not is_simple_p(crypto):
        return "Модуль криптосистемы не является простым числом!"
    if not check_right_g_and_x(primitive, crypto):
        return "Примитивный элемент не не входит в промежуток от 1 до модуля криптосистемы!"
    if not check_right_g_and_x(secret_key, crypto):
        return "Секретный ключ не входит в промежуток от 1 до модуля криптосистемы!"
    if not check_right_k(sender_number, crypto):
        return "Случайное число не входит в промежуток (от 1 до модуля криптосистемы - 1) или не взаимно просто " \
               "с модулем криптосистемы!"

    y = (primitive ** secret_key) % crypto
    ciphertext = []
    for letter in message:
        ciphertext.append(chr((primitive ** sender_number) % crypto))
        ciphertext.append(chr(((y ** sender_number) * ord(letter)) % crypto))
    return "".join(ciphertext)


def decrypt(crypto, secret_key, message):
    if len(message) % 2 == 0 and not len(message) == 0:
        if not check_right_g_and_x(secret_key, crypto):
            return "Число x не входит в промежуток!"
        deciphered_text = []
        for i in range(0, len(message) - 1, 2):
            deciphered_text.append(chr((ord(message[i + 1]) * (ord(message[i]) ** (crypto - 1 - secret_key))) % crypto))
        return "".join(deciphered_text)
    else:
        return "Нельзя расшифровать!"


# p = int(input("p = "))
# g = int(input("g = "))
# x = int(input("x = "))
# k = int(input("k = "))
# M = input("M = ")
#
# print("Шифровка:", encrypt(p, g, x, k, M))
# print("Расшифровка:", decrypt(p, x, encrypt(p, g, x, k, M)))
