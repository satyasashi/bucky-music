# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-09 10:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='fileType',
            new_name='file_type',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='songType',
            new_name='song_title',
        ),
    ]
