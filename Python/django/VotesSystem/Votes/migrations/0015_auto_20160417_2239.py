# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-17 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Votes', '0014_auto_20160417_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activeuser',
            name='user',
        ),
        migrations.AddField(
            model_name='activeuser',
            name='username',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]