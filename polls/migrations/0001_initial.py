# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('answer1_text', models.TextField(default='')),
                ('answer2_text', models.TextField(default='')),
                ('answer3_text', models.TextField(default='')),
                ('answer4_text', models.TextField(default='')),
                ('correct', models.IntegerField(default=1)),
            ],
        ),
    ]