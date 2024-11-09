# import unittest
# from app import is_valid_credit_card

# class TestCreditCardValidation(unittest.TestCase):
#     def test_valid_credit_cards(self):
#         valid_cards = ["49927398716", "1234567812345670", "2222405343248877", "2222990905257051"]
#         for card in valid_cards:
#             self.assertTrue(is_valid_credit_card(card))

#     def test_invalid_credit_cards(self):
#         invalid_cards = ["49927398717", "1234567812345678"]
#         for card in invalid_cards:
#             self.assertFalse(is_valid_credit_card(card))

# if __name__ == '__main__':
#     unittest.main()


import unittest
from app.app import is_valid_credit_card

class TestCreditCardValidation(unittest.TestCase):
    def test_valid_credit_cards(self):
        valid_cards = ["49927398716", "1234567812345670", "2222405343248877", "2222990905257051"]
        for card in valid_cards:
            self.assertTrue(is_valid_credit_card(card))

    def test_invalid_credit_cards(self):
        invalid_cards = ["49927398717", "1234567812345678"]
        for card in invalid_cards:
            self.assertFalse(is_valid_credit_card(card))

if __name__ == '__main__':
    unittest.main()