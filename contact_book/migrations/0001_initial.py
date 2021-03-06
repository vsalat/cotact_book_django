# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 22:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=20)),
                ('patronymic', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=16)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact_book.Contact')),
            ],
        ),
    ]
