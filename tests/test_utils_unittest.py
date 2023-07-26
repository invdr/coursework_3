import unittest
from config.utils import *


class TestUtils(unittest.TestCase):

    def test_load_file(self):
        self.assertEquals(type(load_file('config/operations.json')), list)

    def test_get_sorted_list(self):
        original_list_if = [
            {'id': 441945886,
             'state': "EXECUTED",
             'date': '2019-08-26T10:50:58.294041',
             'operationAmount':
                 {'amount': '31957.58',
                  'currency':
                      {'name': 'руб.',
                       'code': 'RUB'}},
             'description': 'Перевод организации',
             'from': 'Maestro 1596837868705199',
             'to': 'Счет 64686473678894779589'}]
        sorted_list_if = [
            {'id': 441945886,
             'state': "EXECUTED",
             'date': '26.08.2019',
             'operationAmount':
                 {'amount': '31957.58',
                  'currency':
                      {'name': 'руб.',
                       'code': 'RUB'}},
             'description': 'Перевод организации',
             'from': 'Maestro 1596837868705199',
             'to': 'Счет 64686473678894779589'}]

        self.assertEquals(get_sorted_list(original_list_if), sorted_list_if)

    def test_encoding_from(self):
        transaction_if = {'id': 441945886,
                          'state': "EXECUTED",
                          'date': '26.08.2019',
                          'operationAmount':
                              {'amount': '31957.58',
                               'currency':
                                   {'name': 'руб.',
                                    'code': 'RUB'}},
                          'description': 'Перевод организации',
                          'from': 'Maestro 1596837868705199',
                          'to': 'Счет 64686473678894779589'}
        transaction_else = {'id': 441945886,
                            'state': "EXECUTED",
                            'date': '26.08.2019',
                            'operationAmount':
                                {'amount': '31957.58',
                                 'currency':
                                     {'name': 'руб.',
                                      'code': 'RUB'}},
                            'description': 'Перевод организации',
                            'from': 'Счет 64686473678894779589',
                            'to': 'Счет 64686473678894779589'}

        encoding_fr = 'Maestro 1596 83** **** 5199'
        encoding_fr_else = 'Счет **9589'

        self.assertEquals(encoding_from(transaction_if), encoding_fr)
        self.assertEquals(encoding_from(transaction_else), encoding_fr_else)

    def test_encoding_to(self):
        transaction_if = {'id': 441945886,
                          'state': "EXECUTED",
                          'date': '26.08.2019',
                          'operationAmount':
                              {'amount': '31957.58',
                               'currency':
                                   {'name': 'руб.',
                                    'code': 'RUB'}},
                          'description': 'Перевод организации',
                          'from': 'Maestro 1596837868705199',
                          'to': 'Visa 6870519915968378'}
        transaction_else = {'id': 441945886,
                            'state': "EXECUTED",
                            'date': '26.08.2019',
                            'operationAmount':
                                {'amount': '31957.58',
                                 'currency':
                                     {'name': 'руб.',
                                      'code': 'RUB'}},
                            'description': 'Перевод организации',
                            'from': 'Maestro 1596837868705199',
                            'to': 'Счет 64686473678894779589'}

        encoding_t = 'Visa 6870 51** **** 8378'
        encoding_t_else = 'Счет **9589'

        self.assertEquals(encoding_to(transaction_if), encoding_t)
        self.assertEquals(encoding_to(transaction_else), encoding_t_else)

    def test_get_amount(self):
        transaction = {'id': 441945886,
                       'state': "EXECUTED",
                       'date': '26.08.2019',
                       'operationAmount':
                           {'amount': '31957.58',
                            'currency':
                                {'name': 'руб.',
                                 'code': 'RUB'}},
                       'description': 'Перевод организации',
                       'from': 'Maestro 1596837868705199',
                       'to': 'Visa 6870519915968378'}

        amount = '31957.58 руб.'

        self.assertEquals(get_amount(transaction), amount)
