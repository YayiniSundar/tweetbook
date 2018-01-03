# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-29 06:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20171229_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
