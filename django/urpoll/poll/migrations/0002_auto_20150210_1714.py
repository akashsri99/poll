# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='option_2',
            name='ques',
            field=models.ForeignKey(default=1, to='poll.Question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='option_4',
            name='option3',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='option_4',
            name='option4',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='option_4',
            name='ques',
            field=models.ForeignKey(default=1, to='poll.Question'),
            preserve_default=False,
        ),
    ]
