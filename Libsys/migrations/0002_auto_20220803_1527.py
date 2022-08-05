# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2022-08-03 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libsys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebook',
            name='approval_status',
            field=models.SmallIntegerField(choices=[(1, 'Approved'), (0, 'Rejected'), (2, 'Pending for approval')], default=2),
        ),
        migrations.AlterField(
            model_name='language',
            name='about',
            field=models.TextField(),
        ),
    ]