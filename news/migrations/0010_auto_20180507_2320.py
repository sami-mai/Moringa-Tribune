# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 20:20
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_delete_editor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
    ]
