# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 09:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0007_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room',
            new_name='room_pic',
        ),
    ]