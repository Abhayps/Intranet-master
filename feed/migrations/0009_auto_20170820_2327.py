# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0008_auto_20170818_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='commit',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]