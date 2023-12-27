from django.db import models

# Create your models here.


class musicians(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    instruments = [
        ("Guitar", "Guitar"),
        ("Piano", "Piano"),
        ("Violin", "Violin"),
        ("Cello", "Cello"),
        ("Brass instrument", "Brass instrument"),
    ]
    instrument_type = models.CharField(max_length=50,choices=instruments)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
