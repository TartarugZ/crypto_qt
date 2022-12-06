import math


def create_CryproRSA(p, q, e):
    if p == 1 or q == 1 or e == 1:
        return 'p,q,e не должны быть равны 1'
    if not is_simple_number(p):
        return 'p - не простое число'
    if not is_simple_number(p):
        return 'q - не простое число'

    phi = euler(p, q)
    if not check_exponent(e, phi):
        return 'e - либо не простое число, либо не взаимно простое с функцией Эллера'

    return CryptoRSA(p, q, e, phi)


class CryptoRSA:
    def __init__(self, p, q, e, phi):
        self.p = p
        self.q = q
        self.e = e
        self.n = p * q
        self.phi = phi
        self.d = self.generate_secret_exponent()
        self.error_encrypt = False

    def generate_secret_exponent(self):
        d = 2
        while not (d * self.e) % self.phi == 1:
            d += 1
        return d

    def encrypt_message(self, message):
        self.error_encrypt = False
        new = []
        for c in message:
            if ord(c) > self.n:
                self.error_encrypt = True
                return 'Модуль n меньше кода символа'
            new.append(chr(ord(c) ** self.e % self.n))
        print(''.join(new))
        return ''.join(new)

    def decrypt_message(self, enc_message):
        if self.error_encrypt:
            return 'Ошибка шифрования'
        new = []
        for c in enc_message:
            new.append(chr(ord(c) ** self.d % self.n))
        return ''.join(new)


def is_simple_number(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            k = k + 1
    if k <= 0:
        return True
    else:
        return False


def check_exponent(exp, phi):
    return math.gcd(exp, phi) == 1 and is_simple_number(exp)


def euler(p, q):
    return (p - 1) * (q - 1)
