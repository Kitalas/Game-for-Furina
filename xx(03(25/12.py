# функция
import requests


def get_usd_to_uah_rate():
    """
    Отримує курс долара до гривні з API Монобанку.

    :return: Курс долара до гривні (float).
    :raises Exception: Якщо запит до API не вдався або дані недоступні.
    """
    url = "https://api.monobank.ua/bank/currency"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Не вдалося отримати дані з API.")

    currency_data = response.json()

    for currency in currency_data:
        if currency['currencyCodeA'] == 840:
            return currency['rateSell']

    raise Exception("Курс долара не знайдено.")


# тест
import unittest
from unittest.mock import patch


class TestGetUsdToUahRate(unittest.TestCase):

    @patch('requests.get')
    def test_get_usd_to_uah_rate_success(self, mock_get):
        # Створюємо змMock response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                "currencyCodeA": 840,
                "currencyCodeB": 980,
                "rateBuy": 27.00,
                "rateSell": 27.20,
            },
        ]

        rate = get_usd_to_uah_rate()
        self.assertEqual(rate, 27.20)

    @patch('requests.get')
    def test_get_usd_to_uah_rate_failure(self, mock_get):
        mock_get.return_value.status_code = 404

        with self.assertRaises(Exception):
            get_usd_to_uah_rate()

    @patch('requests.get')
    def test_get_usd_to_uah_rate_no_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                "currencyCodeA": 978,  # EUR
                "currencyCodeB": 980,
                "rateBuy": 30.00,
                "rateSell": 30.20,
            },
        ]

        with self.assertRaises(Exception):
            get_usd_to_uah_rate()


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
