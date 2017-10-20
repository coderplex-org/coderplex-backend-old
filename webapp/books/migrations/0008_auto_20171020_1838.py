# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 18:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20171020_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookchapterrelationship',
            name='book',
        ),
        migrations.RemoveField(
            model_name='bookchapterrelationship',
            name='chapter',
        ),
        migrations.RemoveField(
            model_name='bookchapterrelationship',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='bookchapterrelationship',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='chapterpagerelationship',
            name='chapter',
        ),
        migrations.RemoveField(
            model_name='chapterpagerelationship',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='chapterpagerelationship',
            name='page',
        ),
        migrations.RemoveField(
            model_name='chapterpagerelationship',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='BookChapterRelationShip',
        ),
        migrations.DeleteModel(
            name='ChapterPageRelationShip',
        ),
    ]
