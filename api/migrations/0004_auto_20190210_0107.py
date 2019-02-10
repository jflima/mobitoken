# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-10 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190210_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='input',
            name='paid_at',
            field=models.DateTimeField(),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='input',
            name='method',
            field=models.IntegerField(choices=[(0, 'Boleto')]),
        ),
    ]
