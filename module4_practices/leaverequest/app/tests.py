from django.test import TestCase
from app import models

# Create your tests here.
class Test_Leave_Request(TestCase):
    def test_can_create_request(self):
        request1 = models.create_request(
            "Phillip", True, False, False, "", "", False, "2021-01-01"
        )
        request2 = models.create_request(
            "Patrick", True, False, False, "", "", False, "2022-02-02"
        )
        request3 = models.create_request(
            "Logan", True, False, True, "", "", False, "2023-03-03"
        )

        self.assertEqual(request1.employee_name, "Phillip")
        self.assertTrue(request1.is_sick)
        self.assertFalse(request1.is_personal)

        self.assertEqual(request2.employee_name, "Patrick")
        self.assertFalse(request2.is_paid)
        self.assertFalse(request2.is_approved)

        self.assertEqual(request3.employee_name, "Logan")
        self.assertTrue(request3.is_paid)
        self.assertEqual(request3.approved_by, "")

    def test_can_approve_request(self):
        request1 = models.create_request(
            "Phillip", True, False, False, "", "", False, "2021-01-01"
        )
        request1 = models.approve_request("Phillip")

        self.assertTrue(request1.is_approved)

    def test_can_filter_by_date(self):
        request1 = models.create_request(
            "Phillip", True, False, False, "", "", False, "2021-01-01"
        )
        request2 = models.create_request(
            "Patrick", True, False, False, "", "", False, "2022-02-02"
        )
        request3 = models.create_request(
            "Logan", True, False, True, "", "", False, "2023-03-03"
        )
        filtered_requests = models.filter_by_date("2021-01-01")

        self.assertEqual(len(filtered_requests), 1)

    def test_can_filter_by_is_sick(self):
        request1 = models.create_request(
            "Phillip", True, False, False, "", "", False, "2021-01-01"
        )
        request2 = models.create_request(
            "Patrick", False, False, False, "", "", False, "2022-02-02"
        )
        request3 = models.create_request(
            "Logan", True, False, True, "", "", False, "2023-03-03"
        )
        requests = models.filter_by_is_sick()

        self.assertEqual(len(requests), 2)

    def test_can_filter_by_is_sick_employee(self):
        request1 = models.create_request(
            "Phillip", True, False, False, "", "", False, "2021-01-01"
        )
        request2 = models.create_request(
            "Phillip", False, False, False, "", "", False, "2022-02-02"
        )
        request3 = models.create_request(
            "Phillip", True, False, True, "", "", False, "2023-03-03"
        )
        requests = models.filter_by_is_sick_employee("Phillip")

        self.assertEqual(len(requests), 2)

    def test_can_delete_request(self):
        request1 = models.create_request(
            "Phillip", True, False, False, "", "", False, "2021-01-01"
        )
        request2 = models.create_request(
            "Patrick", False, False, False, "", "", False, "2022-02-02"
        )
        request3 = models.create_request(
            "Logan", True, False, True, "", "", False, "2023-03-03"
        )
        requests = models.LeaveRequest.objects.all()

        self.assertEqual(len(requests), 3)

        models.delete_request(3)

        requests = models.LeaveRequest.objects.all()

        self.assertEqual(len(requests), 2)

    def test_can_update_request(self):
        request1 = models.create_request(
            "Phillip", True, False, False, "", "", False, "2021-01-01"
        )
        request1 = models.update_request(1, "date_requested", "2021-01-02")

        self.assertEqual(request1.date_requested, "2021-01-02")

    def test_update_request_is_approved(self):
        request1 = models.create_request(
            "Phillip", True, False, False, "", "", False, "2021-01-01"
        )
        with self.assertRaises(ValueError):
            models.update_request(1, "is_approved", True)
