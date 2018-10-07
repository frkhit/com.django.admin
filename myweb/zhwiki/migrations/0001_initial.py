# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-29 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WikiPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u8bcd\u6761',
                'verbose_name_plural': '\u8bcd\u6761',
            },
        ),
    ]