import unittest

import config

from services import LoanService


class LoanServiceTest(unittest.TestCase):
    def test_aproved_loan(self):
        service = LoanService()
        response = service.validate_loan(config.decision_amount - 1)
        self.assertEqual(config.decision_aproved, response['decision'])

    def test_declined_loan(self):
        service = LoanService()
        response = service.validate_loan(config.decision_amount + 1)
        self.assertEqual(config.decision_declined, response['decision'])

    def test_undecided_loan(self):
        service = LoanService()
        response = service.validate_loan(config.decision_amount)
        self.assertEqual(config.decision_undecided, response['decision'])
