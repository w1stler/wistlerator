from django.db import models
from django.forms import ModelForm


class Sample(models.Model):
    serial_number = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    arrival_date = models.DateField('arrival date')
    content = models.CharField(max_length=1000)
    comments = models.CharField(max_length=1000, blank=True, null=False)
    category = models.ForeignKey("Category", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class MediaCompany(models.Model):
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=25)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "MediaCompanies"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        # fields = ['serial_number', 'name', 'arrival_date', 'content', 'comments', 'category']
        fields = ['name', 'description']


class SampleForm(ModelForm):
    class Meta:
        model = Sample
        fields = ['serial_number', 'name', 'arrival_date', 'content', 'comments', 'category']
