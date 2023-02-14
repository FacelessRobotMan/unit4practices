from django.db import models
import datetime as dt

# Create your models here.
class LeaveRequest(models.Model):
    date_requested = models.DateField(blank=True, null=True)
    employee_name = models.TextField()
    is_sick = models.BooleanField()
    is_personal = models.BooleanField()
    is_paid = models.BooleanField()
    is_approved = models.BooleanField()
    approved_by = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)


def create_request(
    name,
    is_sick,
    is_personal,
    is_paid,
    is_approved,
    date_requested=dt.date.today(),
    approved_by=None,
    notes=None,
):
    req = LeaveRequest(
        date_requested=date_requested,
        employee_name=name,
        is_sick=is_sick,
        is_personal=is_personal,
        is_paid=is_paid,
        is_approved=is_approved,
        approved_by=approved_by,
        notes=notes,
    )
    req.save()
    return req


def all_requests():
    return LeaveRequest.objects.all()


def find_request(id):
    req = LeaveRequest.objects.get(id=id)
    return req


def delete_request(id):
    req = find_request(id)
    req.delete()


def update_request(id, user, change):
    req = find_request(id)
    if user == "is sick":
        req.is_sick = change
    elif user == "is paid":
        req.is_paid = change
    elif user == "is personal":
        req.is_personal = change
    elif user == "employee":
        req.employee_name = change
    elif user == "date":
        req.date_requested = change


def filter_by_bool(filter_parameter):
    return LeaveRequest.objects.filter(filter_parameter=True)


def filter_by_name(name):
    return LeaveRequest.objects.filter(employee_name=name)


def approve_request(name, approver):
    req = LeaveRequest.objects.get(employee_name=name, is_approved=False)
    req.approved_by = approver
    req.is_approved = True
    req.save()
    return req
