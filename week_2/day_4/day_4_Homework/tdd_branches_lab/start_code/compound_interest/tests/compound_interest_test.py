import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):
    # Tests

    # # Should return 732.81 given 100 principal, 10 percent, 20 years
    def test_amount_after_investment(self):
        compound = CompoundInterest(100, 10, 20, 1)
        expected_outcome = 732.81
        actual_outcome = compound.invest_without_monthly_contribution()
        self.assertEqual(expected_outcome, actual_outcome)
    # Should return 181.94 given 100 principal, 6 percent, 10 years
    def test_amount_after_investment2(self):
        compound = CompoundInterest(100, 6, 10, 1)
        expected_outcome = 181.94
        actual_outcome = compound.invest_without_monthly_contribution()
        self.assertEqual(expected_outcome, actual_outcome)

    # # # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    def test_amount_after_investment3(self):
        compound = CompoundInterest(100000, 5, 8, 1)
        expected_outcome = 149058.55
        actual_outcome = compound.invest_without_monthly_contribution()
        self.assertEqual(expected_outcome, actual_outcome)
    # # Should return 0.00 given 0 principal, 10 percent, 1 year

    def test_amount_after_investment4(self):
        compound = CompoundInterest(0, 10, 1, 1)
        expected_outcome = 0
        actual_outcome = compound.invest_without_monthly_contribution()
        self.assertEqual(expected_outcome, actual_outcome)

    # # # Should return 100.00 given 100 principal, 0 percent, 10 years
    def test_amount_after_investment5(self):
        compound = CompoundInterest(100, 0, 10, 1)
        expected_outcome = 100
        actual_outcome = compound.invest_without_monthly_contribution()
        self.assertEqual(expected_outcome, actual_outcome)

    # # Extention tests

    # # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month
    def test_amount_after_investment6(self):
        compound = CompoundInterest(100, 5, 8, 1000)
        expected_outcome = 118380.16
        actual_outcome = compound.invest_with_monthly_contribution()
        self.assertEqual(expected_outcome, actual_outcome)
  
    # # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month
    def test_amount_after_investment7(self):
        compound = CompoundInterest(100, 5, 10, 1000)
        expected_outcome = 156093.99
        actual_outcome = compound.invest_with_monthly_contribution()
        self.assertEqual(expected_outcome, actual_outcome)
  
    # # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month
    def test_amount_after_investment8(self):
        compound = CompoundInterest(116028.86, 7.5, 8, 2006)
        expected_outcome = 475442.59
        actual_outcome = compound.invest_with_monthly_contribution()
        self.assertEqual(expected_outcome, actual_outcome)


    # # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month
    def test_amount_after_investment9(self):
        compound = CompoundInterest(116028.86, 9, 12, 1456)
        expected_outcome = 718335.96
        actual_outcome = compound.invest_with_monthly_contribution()
        self.assertEqual(expected_outcome, actual_outcome)