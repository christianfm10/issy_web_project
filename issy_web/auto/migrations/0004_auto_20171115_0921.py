# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 09:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0003_contrato'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auto',
            old_name='lugar_recodiga',
            new_name='lugar_recogida',
        ),
    ]