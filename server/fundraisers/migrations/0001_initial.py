# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-05-26 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fundraiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pageId', models.IntegerField()),
                ('pageStatus', models.BooleanField(default=True)),
                ('pageUrl', models.URLField()),
                ('signOnUrl', models.URLField(blank=True, null=True)),
                ('currency', models.CharField(default=b'GBP', max_length=3)),
                ('manuallyCreated', models.BooleanField(default=False)),
                ('fundraisingTarget', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
                ('totalRaisedOffline', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
                ('totalRaisedOnline', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
                ('totalRaisedSms', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
                ('totalRaised', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
                ('giftAid', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
            ],
            options={
                'db_table': 'fundraisers',
            },
        ),
    ]
