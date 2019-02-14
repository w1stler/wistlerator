# Generated by Django 2.1.7 on 2019-02-14 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=25)),
                ('postal_code', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=50)),
                ('arrival_date', models.DateTimeField(verbose_name='arrival date')),
                ('content', models.CharField(max_length=1000)),
                ('comments', models.CharField(max_length=1000)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]
