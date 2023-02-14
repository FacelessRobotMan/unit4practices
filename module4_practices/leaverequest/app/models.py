from django.db import models
from datetime import date

# Create your models here.
class LeaveRequest(models.Model):
    employee_name = models.TextField()
    is_sick = models.BooleanField()
    is_personal = models.BooleanField()
    is_paid = models.BooleanField()
    approved_by = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    date_requested = models.DateField(blank=True, null=True, default=date.today)


def create_request(
    employee_name,
    is_sick,
    is_personal,
    is_paid,
    approved_by,
    notes,
    is_approved,
    date_requested=date.today(),
):
    request = LeaveRequest(
        employee_name=employee_name,
        is_sick=is_sick,
        is_personal=is_personal,
        is_paid=is_paid,
        approved_by=approved_by,
        notes=notes,
        is_approved=is_approved,
        date_requested=date_requested,
    )
    request.save()
    return request


def approve_request(employee_name):
    request = LeaveRequest.objects.get(employee_name=employee_name)
    request.is_approved = True
    request.save()
    return request


def filter_by_date(date):
    requests = LeaveRequest.objects.filter(date_requested=date)
    return requests


def filter_by_is_sick():
    requests = LeaveRequest.objects.filter(is_sick=True)
    return requests


def filter_by_is_sick_employee(employee_name):
    requests = LeaveRequest.objects.filter(is_sick=True, employee_name=employee_name)
    return requests


def delete_request(id):
    request = LeaveRequest.objects.get(id=id)
    request.delete()


def update_request(id, field, change):
    request = LeaveRequest.objects.get(id=id)
    if field == "is_sick":
        request.is_sick = change
        return request
    elif field == "is_personal":
        request.is_personal = change
        return request
    elif field == "is_paid":
        request.is_paid = change
        return request
    elif field == "approved_by":
        request.approved_by = change
        return request
    elif field == "date_requested":
        request.date_requested = change
        return request
    elif field == "is_approved":
        raise ValueError("Can't update this")
