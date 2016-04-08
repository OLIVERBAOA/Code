# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-05 05:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BBS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('summary', models.CharField(blank=True, max_length=100)),
                ('posting', models.TextField()),
                ('view_count', models.IntegerField(default=0)),
                ('ranking', models.IntegerField(default=1000)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BBS_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.CharField(default=b'This guy is too lazy to left anything here.', max_length=128)),
                ('photo', models.ImageField(default=b'/upload_imgages/default.ico', upload_to=b'/upload_imgages/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, unique=True)),
                ('adminstrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.BBS_User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField()),
                ('text', models.TextField()),
                ('BBS_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.BBS')),
            ],
        ),
        migrations.AddField(
            model_name='bbs',
            name='auth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.BBS_User'),
        ),
    ]