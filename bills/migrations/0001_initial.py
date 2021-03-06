# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 07:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=80)),
                ('created_date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_name', models.CharField(max_length=80)),
                ('bill_amount', models.IntegerField()),
                ('bill_date', models.DateField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.Account')),
            ],
        ),
    ]
