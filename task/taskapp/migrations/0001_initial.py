# Generated by Django 4.2.7 on 2023-11-14 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=200)),
                ('Lname', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Dob', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=200)),
                ('Mobile', models.CharField(max_length=200)),
                ('Domain', models.CharField(max_length=200)),
                ('Company', models.CharField(max_length=200)),
                ('Salary', models.CharField(max_length=200)),
            ],
        ),
    ]
