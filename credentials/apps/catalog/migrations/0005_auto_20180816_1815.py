# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-16 18:15


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('catalog', '0004_auto_20180810_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditpathway',
            name='uuid',
            field=models.UUIDField(verbose_name='UUID'),
        ),
        migrations.AlterUniqueTogether(
            name='creditpathway',
            unique_together=set([('site', 'uuid')]),
        ),
    ]
