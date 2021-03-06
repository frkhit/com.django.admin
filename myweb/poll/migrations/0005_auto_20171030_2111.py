# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 13:11
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Author2')),
            ],
        ),
        migrations.CreateModel(
            name='EditRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_time', models.DateTimeField(verbose_name='\u7f16\u8f91\u65f6\u95f4')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Paper', verbose_name='\u6587\u7ae0')),
            ],
            options={
                'verbose_name': '\u7f16\u8f91\u8bb0\u5f55',
                'verbose_name_plural': '\u7f16\u8f91\u8bb0\u5f55',
            },
        ),
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u8d26\u53f7'),
        ),
    ]
