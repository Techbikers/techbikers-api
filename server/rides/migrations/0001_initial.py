# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-05-26 13:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chapters', '0001_initial'),
        ('sales', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('strapline', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('start_location', models.CharField(max_length=255)),
                ('end_location', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('preregistration_required', models.BooleanField(default=False)),
                ('rider_capacity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('full_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('currency', models.CharField(choices=[(b'gbp', b'GBP'), (b'usd', b'USD'), (b'eur', b'EUR')], default=b'gbp', max_length=3)),
                ('terms_and_conditions', models.TextField(blank=True, default=b'', null=True)),
                ('mailchimp_group_id', models.CharField(blank=True, max_length=20, null=True)),
                ('fundraising_target', models.DecimalField(decimal_places=2, default=500.0, max_digits=6)),
                ('just_giving_event_id', models.IntegerField(blank=True, null=True)),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chapters.Chapter')),
            ],
            options={
                'db_table': 'rides',
            },
        ),
        migrations.CreateModel(
            name='RideRiders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(b'PEN', b'Pending'), (b'ACC', b'Accepted'), (b'REG', b'Registered'), (b'REJ', b'Rejected'), (b'WIT', b'Withdrawn')], default=b'PEN', max_length=3)),
                ('signup_date', models.DateField()),
                ('signup_expires', models.DateField(blank=True, null=True)),
                ('payload', models.TextField(blank=True)),
                ('paid', models.BooleanField()),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rides.Ride')),
                ('sale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.Sale')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'rides_riders',
            },
        ),
        migrations.AddField(
            model_name='ride',
            name='riders',
            field=models.ManyToManyField(blank=True, through='rides.RideRiders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='rideriders',
            unique_together=set([('user', 'ride')]),
        ),
    ]
