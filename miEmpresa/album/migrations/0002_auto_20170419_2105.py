# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 02:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Universidad',
            new_name='Cargo',
        ),
        migrations.RenameField(
            model_name='trabajo',
            old_name='universidad',
            new_name='Cargo',
        ),
        migrations.RenameField(
            model_name='trabajo',
            old_name='photo',
            new_name='foto',
        ),
        migrations.RenameField(
            model_name='trabajo',
            old_name='title',
            new_name='nombre',
        ),
    ]
