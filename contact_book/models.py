from django.db import models


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=16)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)



