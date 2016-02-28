# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0008_auto_20160228_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storypoint',
            name='photo',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='storypoint',
            name='story_choices',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]