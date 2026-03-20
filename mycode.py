import random

class WordEncryptor:
    def __init__(self, value):
        self.__secret_value = value
        self.__cipher = {10: "В", 20: "О", 30: "Л", 40: "Я"}

    def __calculate(self):
        operation = random.choice([
            lambda x: x * 2,
            lambda x: x + 10,
            lambda x: x - 5,
            lambda x: x // 2
        ])
        return operation(self.__secret_value)

    def __str__(self):
        result = self.__calculate()
        char = self.__cipher.get(result, "Секрет")
        return f"Результат: {result} | Зашифроване слово: {char}"

if __name__ == "__main__":
    encrypted_obj = WordEncryptor(20)
    print(encrypted_obj)
    