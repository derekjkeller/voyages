# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2022-01-05 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0015_auto_20211116_1650'),
        ('past', '0013_auto_20220104_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='enslaveridentity',
            name='first_active_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='enslaveridentity',
            name='last_active_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='enslaveridentity',
            name='number_enslaved',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='enslaveridentity',
            name='principal_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='voyage.Place'),
        ),
        migrations.AddField(
            model_name='enslavermerger',
            name='first_active_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='enslavermerger',
            name='last_active_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='enslavermerger',
            name='number_enslaved',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='enslavermerger',
            name='principal_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='voyage.Place'),
        ),
    ]