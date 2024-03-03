from django.db import models

class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    num_people = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    preferred_contact_method = models.CharField(choices=[('email', 'Email'), ('phone', 'Phone'), ('both', 'Both')])

    def __str__(self):
        return f"Reservation for {self.num_people} people on {self.date} at {self.time}"
