import json
import config
from datetime import date


def load_file(filename):
    """Функция возвращает список транзакций из json-файла."""
    with open(filename, encoding='utf8') as f:
        data = json.load(f)
    return data


def get_normal_list(temp_list) -> list :
    """Функция возвращает нормализованный список, который содержит все непустые
    и "EXECUTED" транзакции."""
    normal_list = [
        line for line in temp_list if line if line["state"] == "EXECUTED"
    ]
    return normal_list


def get_date(transaction: dict) -> str:
    """Функция возвращает дату транзакции в необходимом формате - ДД.ММ.ГГГГ"""
    normalized_date = date.fromisoformat(transaction["date"][:10])
    strtime_date = normalized_date.strftime("%d.%m.%Y")
    return strtime_date


def encoding_from(transaction: dict) -> str:
    """Функция закрывает часть номера карты(счета) отправителя и возвращает
    наименование и номер карты(счета)."""
    from_name, from_account = transaction["from"].rsplit(" ", 1)
    if len(from_account) == 16:
        encoding_from_account = f'{from_account[:4]} {from_account[4:6]}** ' \
                            f'**** {from_account[-4:]}'
    else:
        encoding_from_account = f'**{from_account[-4:]}'

    encoding_from = from_name + " " + encoding_from_account

    return encoding_from


def encoding_to(transaction: dict) -> str:
    """Функция закрывает часть номера карты(счета) получателя и возвращает
    наименование и номер карты(счета)."""
    to_name, to_account = transaction["to"].rsplit(" ", 1)
    if len(to_account) == 16:
        encoding_to_account = f'{to_account[:4]} {to_account[4:6]}** ' \
                            f'**** {to_account[-4:]}'
    else:
        encoding_to_account = f'**{to_account[-4:]}'

    encoding_to = to_name + " " + encoding_to_account

    return encoding_to


def get_amount(transaction: dict) -> str:
    """Функция возвращает сумму и валюту транзакции."""
    amount = f'{transaction["operationAmount"]["amount"]} ' \
             f'{transaction["operationAmount"]["currency"]["name"]} '
    return amount

