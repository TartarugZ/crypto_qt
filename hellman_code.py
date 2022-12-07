class DiffieHellmanAbonent(object):
    def __init__(self, primitive_element_1, crypto_system_module, secret_key_):
        self.primitive_element_1 = primitive_element_1
        self.crypto_system_module = crypto_system_module
        self.secret_key_ = secret_key_
        self.full_key = None

    def generate_secret_key(self):
        generating_secret_key = self.primitive_element_1 ** self.secret_key_
        generating_secret_key = generating_secret_key % self.crypto_system_module
        return generating_secret_key

    def generate_full_key(self, friend_secret_key):
        full_key = friend_secret_key ** self.secret_key_
        full_key = full_key % self.crypto_system_module
        self.full_key = full_key
        return full_key

    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c) + key)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.full_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c) - key)
        return decrypted_message


class DiffieHellmanGenerateAbonents(object):
    def __init__(self, crypto_system_module, primitive_element_1, secret_key_1,
                 secret_key_2):
        self.first_abonent = DiffieHellmanAbonent(primitive_element_1, crypto_system_module, secret_key_1)
        self.second_abonent = DiffieHellmanAbonent(primitive_element_1, crypto_system_module, secret_key_2)

        self.partical_key_first_abonent = self.first_abonent.generate_secret_key()
        self.partical_key_second_abonent = self.second_abonent.generate_secret_key()

        self.full_key_1 = self.first_abonent.generate_full_key(self.partical_key_second_abonent)
        self.full_key_2 = self.second_abonent.generate_full_key(self.partical_key_first_abonent)


### Создается объект класса  DiffieHellmanGenerateAbonents, аргументами которого являются :
# модуль криптосистемы,
# примитивный элемент 1 абонента,
# примитивный элемент 2 абонента,
# секретный ключ абонента 1,
# секретный ключ абонента 2

# Затем у этого абонента вызывается метод  first_abonent.encrypt_message(сообщения для зашифровки) для шифрования сообщения первого абоненета
# После вызывается метод second_abonent.decrypt_message(зашифрованное сообщение) для расшифровки сообщения вторым абонентом


#### Пример:


# 1
# crypto_system = DiffieHellmanGenerateAbonents(23, 5, 2, 3)
#
# print("Приватный ключ первого абонента:" + str(crypto_system.partical_key_first_abonent))
# print("Приватный ключ второго абонента:" + str(crypto_system.partical_key_second_abonent))
# print("Общий ключ первого абонента:" + str(crypto_system.full_key_1))
# print("Общий ключ второго абонента:" + str(crypto_system.full_key_2))
#
# message = "Качай Pubg"
# print("Шифруемое сообщением первым абонентом:" + message)
#
# # 2
# enc = crypto_system.first_abonent.encrypt_message(message)
# print("зашифрованное:" + enc)
#
# # 3
# dec = crypto_system.second_abonent.decrypt_message(enc)
#
# print("Второй зашифровал: " + dec)
