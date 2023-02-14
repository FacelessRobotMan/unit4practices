from django.test import TestCase
from app import models

# Create your tests here.
class Test_TaxiBusiness(TestCase):
    def test_can_create_taxi(self):
        taxi1 = models.create_taxi(False, 2, 0, 1)
        taxi2 = models.create_taxi(False, 3, 0, 1.5)
        taxi3 = models.create_taxi(False, 4, 0, 2)

        self.assertEqual(taxi1.id, 1)
        self.assertEqual(taxi1.occupied, False)
        self.assertEqual(taxi1.capacity, 2)
        self.assertEqual(taxi1.passengers, 0)
        self.assertEqual(taxi1.fare, 1)
        self.assertEqual(taxi1.notes, "")

        self.assertEqual(taxi2.id, 2)
        self.assertEqual(taxi2.occupied, False)
        self.assertEqual(taxi2.capacity, 3)
        self.assertEqual(taxi2.passengers, 0)
        self.assertEqual(taxi2.fare, 1.5)
        self.assertEqual(taxi2.taxi_number, 122)

        self.assertEqual(taxi3.id, 3)
        self.assertEqual(taxi3.occupied, False)
        self.assertEqual(taxi3.capacity, 4)
        self.assertEqual(taxi3.passengers, 0)
        self.assertEqual(taxi3.fare, 2)
        self.assertEqual(taxi3.taxi_number, 133)

    def test_can_view_all_taxis(self):
        taxi1 = models.create_taxi(False, 2, 0, 1)
        taxi2 = models.create_taxi(False, 3, 0, 1.5)
        taxi3 = models.create_taxi(False, 4, 0, 2)

        all_taxis = models.all_taxis()

        self.assertEqual(len(all_taxis), 3)

    def test_can_find_taxi(self):
        taxi1 = models.create_taxi(False, 2, 0, 1)
        taxi2 = models.create_taxi(False, 3, 0, 1.5)
        taxi3 = models.create_taxi(False, 4, 0, 2)

        test_taxi = models.find_taxi(133)

        self.assertEqual(test_taxi.taxi_number, 133)
        self.assertEqual(test_taxi.capacity, 4)

    def test_can_send_taxi(self):
        taxi1 = models.create_taxi(False, 2, 0, 1)
        taxi2 = models.create_taxi(False, 3, 0, 1.5)
        taxi3 = models.create_taxi(False, 4, 0, 2)

        self.assertEqual(taxi1.occupied, False)
        self.assertEqual(taxi1.passengers, 0)

        taxi1 = models.send_taxi(111, 2)

        self.assertEqual(taxi1.occupied, True)
        self.assertEqual(taxi1.passengers, 2)

        with self.assertRaises(ValueError):
            taxi2 = models.send_taxi(122, 4)

    def test_can_finish_fare(self):
        taxi1 = models.create_taxi(False, 2, 0, 1)
        taxi2 = models.create_taxi(False, 3, 0, 1.5)
        taxi3 = models.create_taxi(False, 4, 0, 2)

        taxi1 = models.send_taxi(111, 2)

        self.assertEqual(models.finish_fare(111, 20), 20)

    def test_finish_fare_not_occupied(self):
        taxi1 = models.create_taxi(False, 2, 0, 1)
        taxi2 = models.create_taxi(False, 3, 0, 1.5)
        taxi3 = models.create_taxi(False, 4, 0, 2)

        with self.assertRaises(ValueError):
            models.finish_fare(111, 20)

    def test_can_remove_taxi(self):
        taxi1 = models.create_taxi(False, 2, 0, 1)
        taxi2 = models.create_taxi(False, 3, 0, 1.5)
        taxi3 = models.create_taxi(False, 4, 0, 2)

        taxis = models.all_taxis()

        taxi1 = models.remove_taxi(111)

        self.assertEqual(len(taxis), 2)

    def test_remove_taxi_does_not_exist(self):
        with self.assertRaises(ValueError):
            models.remove_taxi(111)

    def test_can_filter_occupied(self):
        taxi1 = models.create_taxi(False, 2, 0, 1)
        taxi2 = models.create_taxi(False, 3, 0, 1.5)
        taxi3 = models.create_taxi(True, 4, 0, 2)

        taxis = models.filter_unoccupied()

        self.assertEqual(len(taxis), 2)

    def test_can_filter_occupied_capacity(self):
        taxi1 = models.create_taxi(False, 2, 0, 1)
        taxi2 = models.create_taxi(True, 3, 0, 1.5)
        taxi3 = models.create_taxi(False, 4, 0, 2)

        taxis = models.filter_unoccupied_capacity(3)

        self.assertEqual(len(taxis), 1)
