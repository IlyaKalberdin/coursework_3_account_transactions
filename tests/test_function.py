from src import function


def test_get_sorted_operations():
    assert function.get_sorted_operations("tests/test_operations.json") == [
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
        },
        {
            "id": 522357576,
            "state": "EXECUTED",
            "date": "2019-07-12T20:41:47.882230",
            "operationAmount": {
                "amount": "51463.70",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 48894435694657014368",
            "to": "Счет 38976430693692818358"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2018-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
    ]


def test_encrypt_card_or_account():
    test_operation_1 = {"from": "Visa Platinum 1596837868705199",
                        "to": "Счет 64686473678894779589"}

    test_operation_2 = {"from": "Maestro 1596837868705199",
                        "to": "Visa Platinum 1596837868705199"}

    test_operation_3 = {"to": "Maestro 1596837868705199"}

    test_operation_4 = {"from": "Счет 64686473678894779589",
                        "to": "Счет 64686473678894779589"}

    assert function.encrypt_card_or_account(test_operation_1) == {"from": "Visa Platinum 1596 83** **** 5199",
                                                                  "to": "Счет **9589"}

    assert function.encrypt_card_or_account(test_operation_2) == {"from": "Maestro 1596 83** **** 5199",
                                                                  "to": "Visa Platinum 1596 83** **** 5199"}

    assert function.encrypt_card_or_account(test_operation_3) == {"to": "Maestro 1596 83** **** 5199"}

    assert function.encrypt_card_or_account(test_operation_4) == {"from": "Счет **9589",
                                                                  "to": "Счет **9589"}
