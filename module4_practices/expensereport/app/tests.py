from django.test import TestCase
from app import models
from datetime import date

# Create your tests here.
class Test_ExpenseTracker(TestCase):
    def test_can_create_expense(self):
        expense = models.create_expense(
            "2001-01-01",
            "Walmart",
            12.34,
            "snacks",
        )
        self.assertEqual(expense.date_tr, "2001-01-01")
        self.assertEqual(expense.location, "Walmart")
        self.assertEqual(expense.amount, 12.34)
        self.assertEqual(expense.notes, "snacks")

        expense2 = models.create_expense(
            "2022-01-01",
            "Sam's",
            45.67,
            "",
        )

        self.assertEqual(expense2.date_tr, "2022-01-01")
        self.assertEqual(expense2.location, "Sam's")
        self.assertEqual(expense2.amount, 45.67)
        self.assertEqual(expense2.notes, "")

    def test_can_update_expense(self):
        expense = models.create_expense(
            "2001-01-01",
            "Walmart",
            12.34,
            "snacks",
        )

        expense = models.update_expense(1, "location", "Dollar General")

        self.assertEqual(expense.location, "Dollar General")
        self.assertEqual(expense.amount, 12.34)
        self.assertEqual(expense.notes, "snacks")

    def test_can_delete_expense(self):
        expenses_data = [
            {
                "date": "2001-01-01",
                "location": "Walmart",
                "amount": 11.11,
                "notes": "",
            },
            {
                "date": "2002-02-02",
                "location": "Dollar General",
                "amount": 22.22,
                "notes": "food",
            },
            {
                "date": "2003-03-03",
                "location": "CVS",
                "amount": 33.33,
                "notes": "medicine",
            },
        ]

        for expense_data in expenses_data:
            models.create_expense(
                expense_data["date"],
                expense_data["location"],
                expense_data["amount"],
                expense_data["notes"],
            )

        models.delete_expense(1)

        self.assertEqual(len(models.all_expenses()), 2)

    def test_can_view_all_expenses(self):
        expenses_data = [
            {
                "date": "2001-01-01",
                "location": "Walmart",
                "amount": 11.11,
                "notes": "",
            },
            {
                "date": "2002-02-02",
                "location": "Dollar General",
                "amount": 22.22,
                "notes": "food",
            },
            {
                "date": "2003-03-03",
                "location": "CVS",
                "amount": 33.33,
                "notes": "medicine",
            },
        ]

        for expense_data in expenses_data:
            models.create_expense(
                expense_data["date"],
                expense_data["location"],
                expense_data["amount"],
                expense_data["notes"],
            )
        expense_list = models.all_expenses()
        self.assertEqual(len(expense_list), 3)

    def test_can_filter_expenses(self):
        expenses_data = [
            {
                "date": "2001-01-01",
                "location": "Walmart",
                "amount": 11.11,
                "notes": "",
            },
            {
                "date": "2002-02-02",
                "location": "Dollar General",
                "amount": 22.22,
                "notes": "food",
            },
            {
                "date": "2003-03-03",
                "location": "CVS",
                "amount": 33.33,
                "notes": "medicine",
            },
        ]

        for expense_data in expenses_data:
            models.create_expense(
                expense_data["date"],
                expense_data["location"],
                expense_data["amount"],
                expense_data["notes"],
            )
        filtered_expense_list = models.filter_expenses("Walmart", 11.11)

        self.assertEqual(len(filtered_expense_list), 1)
