from django.contrib import admin

from .models import Sample, MediaCompany, Category

admin.site.register(Sample)
admin.site.register(MediaCompany)
admin.site.register(Category)