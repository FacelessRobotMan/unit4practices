from django.db import models

# Create your models here.
class Taxi(models.Model):
    occupied = models.BooleanField()
    capacity = models.IntegerField()
    fare = models.FloatField()
    passengers = models.IntegerField()
    notes = models.TextField(null=True, default="")
    taxi_number = models.IntegerField(default=111)

    def save(self, *args, **kwargs):
        taxis = Taxi.objects.all()

        if taxis.exists() and self._state.adding:
            taxis_sorted = sorted(taxis, key=lambda c: c.taxi_number)
            last_taxi = taxis_sorted[-1]
            self.taxi_number = last_taxi.taxi_number + 11
        super().save(*args, **kwargs)


def create_taxi(occupied, capacity, fare, passengers, notes=""):
    taxi = Taxi(
        occupied=occupied,
        capacity=capacity,
        fare=fare,
        passengers=passengers,
        notes=notes,
    )
    taxi.save()
    return taxi


def find_taxi(taxi_number):
    try:
        return Taxi.objects.get(taxi_number=taxi_number)
    except Taxi.DoesNotExist:
        raise ValueError("Taxi does not exist")


def send_taxi_out(taxi_number, people):
    taxi = find_taxi(taxi_number)
    if people > taxi.capacity:
        raise ValueError("Taxi does not have big enough capacity")
    else:
        taxi.occupied = True
        taxi.passengers = people
        taxi.save()
        return taxi


def finish_fare(taxi_number, distance):
    taxi = find_taxi(taxi_number)
    if not taxi.occupied:
        raise ValueError("Taxi is Not Occupied.")
    else:
        cost = distance * taxi.fare
        taxi.occupied = False
        taxi.passengers = 0
        return cost


def remove_taxi(taxi_number):
    taxi = find_taxi(taxi_number)
    if taxi == None:
        raise ValueError("Taxi does not exist")
    else:
        taxi.delete()


def all_taxis():
    return Taxi.objects.all()


def filter_free_taxis():
    return Taxi.objects.filter(occupied=False)


def filter_free_capacity_taxis(capacity):
    return Taxi.objects.filter(occupied=False, capacity__gte=capacity)
