import json
from datetime import datetime


def get_sorted_operations(path):
    """
    Функция получает список операций клиента из json файла
    по переданной ссылке и сортирует их по дате.
    Последние операции находятся в начале списка.
    Потом возвращает отсортированный список
    :param path: путь до json файла
    :return: отсортированный список
    """
    with open(path, "r", encoding="utf-8") as file:
        operations = json.load(file)

    for operation in operations:
        if "date" not in operation:
            operations.remove(operation)

    operations = sorted(operations, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)

    return operations


def encrypt_card_or_account(operation):
    """
    Функция зашифровывает номера карт и счетов
    у отправителя и получателя в передаваемой
    операции
    :param operation: Операция
    :return: Операция с зашифрованными номерами
    """
    to = operation["to"].split(" ")

    if to[0] == "Счет":
        to[1] = f"**{to[1][-4:]}"
    elif to[0] == "Visa":
        to[2] = f"{to[2][0:4]} {to[2][4:6]}** **** {to[2][12:16]}"
    else:
        to[1] = f"{to[1][0:4]} {to[1][4:6]}** **** {to[1][12:16]}"

    operation["to"] = " ".join(to)

    if "from" not in operation:
        return operation

    of = operation["from"].split(" ")

    if of[0] == "Счет":
        of[1] = f"**{of[1][-4:]}"
    elif of[0] == "Visa":
        of[2] = f"{of[2][0:4]} {of[2][4:6]}** **** {of[2][12:16]}"
    else:
        of[1] = f"{of[1][0:4]} {of[1][4:6]}** **** {of[1][12:16]}"

    operation["from"] = " ".join(of)

    return operation
