import os.path
from src import function


PATH = os.path.join("../src/operations.json")


def main(path):
    # Получаем отсортированный список с операциями клиента
    operations = function.get_sorted_operations(path)

    # Берем первые пять операций
    operations = operations[0:5]

    # Запускаем итерацию по списку
    for operation in operations:
        # Зашифровываем номера карт/счетов
        operation = function.encrypt_card_or_account(operation)

        # Получаем дату в формате ДД.ММ.ГГГГ
        date = operation["date"].split("T")[0]
        date = ".".join(reversed(date.split("-")))

        # Если нет информации об отправители, то добавляем неизвестно
        if "from" not in operation:
            operation["from"] = "Неизвестно"

        # Выводим информацию по последним операциям клиента
        print(f"{date} {operation['description']}\n"
              f"{operation['from']} -> {operation['to']}\n"
              f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")


if __name__ == "__main__":
    main(PATH)
