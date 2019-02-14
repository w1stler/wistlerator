from django.db import models


class Sample(models.Model):
    serial_number = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    arrival_date = models.DateTimeField('arrival date')
    content = models.CharField(max_length=1000)
    comments = models.CharField(max_length=1000)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.serial_number


class MediaCompany(models.Model):
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=25)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=25)

    def __str__(self):
        return self.name
