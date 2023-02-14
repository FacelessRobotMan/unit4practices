from django.db import models

# Create your models here.
class TaxiBusiness(models.Model):
    occupied = models.BooleanField()
    capacity = models.IntegerField()
    passengers = models.IntegerField()
    fare = models.FloatField()
    taxi_number = models.IntegerField(default=111)
    notes = models.TextField(null=True, default="")

    def save(self, *args, **kwargs):
        all_taxis = TaxiBusiness.objects.all()

        if all_taxis.exists() and self._state.adding:
            sorted_taxis = sorted(all_taxis, key=lambda c: c.taxi_number)
            last_taxi = sorted_taxis[-1]
            self.taxi_number = last_taxi.taxi_number + 11
        super().save(*args, **kwargs)


def create_taxi(occupied, capacity, passengers, fare, notes=""):
    new_taxi = TaxiBusiness(
        occupied=occupied,
        capacity=capacity,
        passengers=passengers,
        fare=fare,
        notes=notes,
    )
    new_taxi.save()
    return new_taxi


def all_taxis():
    taxis = TaxiBusiness.objects.all()
    return taxis


def find_taxi(taxi_number):
    try:
        return TaxiBusiness.objects.get(taxi_number=taxi_number)
    except TaxiBusiness.DoesNotExist:
        raise ValueError("Taxi doesn't exist")


def send_taxi(taxi_number, people):
    taxi = find_taxi(taxi_number)
    if people > taxi.capacity:
        raise ValueError("Too many people")
    else:
        taxi.occupied = True
        taxi.passengers = people
        taxi.save()
        return taxi


def finish_fare(taxi_number, distance):
    taxi = find_taxi(taxi_number)
    if not taxi.occupied:
        raise ValueError("Taxi not occupied")
    else:
        taxi.occupied = False
        taxi.passengers = 0
        cost = taxi.fare * distance
        return cost


def remove_taxi(taxi_number):
    taxi = find_taxi(taxi_number)
    if taxi == None:
        raise ValueError("Taxi does not exist")
    else:
        taxi.delete()


def filter_unoccupied():
    taxis = TaxiBusiness.objects.filter(occupied=False)
    return taxis


def filter_unoccupied_capacity(people):
    taxis = TaxiBusiness.objects.filter(occupied=False, capacity__gte=people)
    return taxis
