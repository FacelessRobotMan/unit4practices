from django.db import models

# Create your models here.
class ExpenseTracker(models.Model):
    date_tr = models.DateField()
    location = models.TextField()
    amount = models.FloatField()
    notes = models.TextField(blank=True)


def create_expense(date_tr, location, amount, notes):
    expense = ExpenseTracker(
        date_tr=date_tr, location=location, amount=amount, notes=notes
    )
    expense.save()
    return expense


def convert_to_currency(amount):
    result = f"${amount:,.2f}"
    return result


def update_expense(id, field, change):
    expense = ExpenseTracker.objects.get(id=id)
    if field == "date_tr":
        expense.date_tr = change
    elif field == "location":
        expense.location = change
    elif field == "amount":
        expense.amount = change
    elif field == "notes":
        expense.notes = change
    expense.save()
    return expense


def all_expenses():
    expense_list = []
    expenses = ExpenseTracker.objects.all()
    for x in expenses:
        expense_list.append(x)
    return expense_list


def delete_expense(id):
    expense = ExpenseTracker.objects.get(id=id)
    expense.delete()


def filter_expenses(location, amount):
    expenses_list = ExpenseTracker.objects.filter(location=location, amount=amount)
    return expenses_list
