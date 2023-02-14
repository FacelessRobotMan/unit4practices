from django.test import TestCase
from app import models as m
import datetime as dt


# Create your tests here.


class Test_LeaveRequest(TestCase):
    def test_create_request(self):
        req1 = m.create_request("joe", False, False, False, False)
        req2 = m.create_request(
            "luis",
            False,
            False,
            False,
            True,
            "2023-02-02",
            "alyx",
            "He got stuff to do.",
        )

        self.assertEqual(req1.id, 1)
        self.assertEqual(req1.employee_name, "joe")
        self.assertEqual(req1.is_sick, False)
        self.assertEqual(req1.is_personal, False)
        self.assertEqual(req1.is_paid, False)
        self.assertEqual(req1.is_approved, False)
        self.assertIsNone(req1.approved_by)
        self.assertIsNone(req1.notes)
        self.assertEqual(req1.date_requested, dt.date.today())

        self.assertEqual(req2.id, 2)
        self.assertEqual(req2.employee_name, "luis")
        self.assertEqual(req2.is_sick, False)
        self.assertEqual(req2.is_personal, False)
        self.assertEqual(req2.is_paid, False)
        self.assertEqual(req2.is_approved, True)
        self.assertEqual(req2.approved_by, "alyx")
        self.assertEqual(req2.notes, "He got stuff to do.")
        self.assertEqual(req2.date_requested, "2023-02-02")

    def test_delete_request(self):
        req1 = m.create_request("joe", False, False, False, False)
        req2 = m.create_request(
            "luis",
            False,
            False,
            False,
            True,
            "2023-02-02",
            "alyx",
            "He got stuff to do.",
        )

        reqs = [req1, req2]

        m.delete_request(1)

        reqs_after = m.all_requests()

        self.assertEqual(len(reqs), 2)
        self.assertEqual(len(reqs_after), 1)

    def test_update_request():
        req1 = m.create_request("joe", False, False, False, False)
        req2 = m.create_request(
            "luis",
            False,
            False,
            False,
            True,
            "2023-02-02",
            "alyx",
            "He got stuff to do.",
        )
