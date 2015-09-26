# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField()),
                ('scheduled_date', models.DateTimeField()),
                ('venue', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Daimoku',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField()),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('target_date', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image_path', models.CharField(default=b'none', max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('permission', models.CharField(default=b'view', max_length=2, choices=[(b'edit', b'Edit'), (b'view', b'View-only')])),
                ('district', models.ForeignKey(to='dashboard.District')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='note',
            name='author',
            field=models.ForeignKey(to='dashboard.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='district',
            field=models.ForeignKey(to='dashboard.District'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='daimoku',
            name='district',
            field=models.ForeignKey(to='dashboard.District'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='daimoku',
            name='target',
            field=models.ForeignKey(to='dashboard.Target'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='daimoku',
            unique_together=set([('target', 'district', 'start_time', 'end_time')]),
        ),
        migrations.AddField(
            model_name='calendarevent',
            name='creator',
            field=models.ForeignKey(to='dashboard.User'),
            preserve_default=True,
        ),
    ]
