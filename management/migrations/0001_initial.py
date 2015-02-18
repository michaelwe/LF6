# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mitarbeiter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('vorname', models.CharField(max_length=50)),
                ('geburtsdatum', models.DateField()),
                ('anlegedatum', models.DateTimeField(auto_now_add=True)),
                ('strasse', models.CharField(max_length=50)),
                ('hausnummer', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MitarbeiterPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('von', models.DateField()),
                ('bis', models.DateField()),
                ('aktiv', models.BooleanField(default=False)),
                ('mitarbeiter', models.ForeignKey(to='management.Mitarbeiter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PLZ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zahl', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bezeichnung', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wohnort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mitarbeiterposition',
            name='position',
            field=models.ForeignKey(to='management.Position'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mitarbeiter',
            name='plz',
            field=models.ForeignKey(to='management.PLZ'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mitarbeiter',
            name='position',
            field=models.ManyToManyField(to='management.Position', through='management.MitarbeiterPosition'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mitarbeiter',
            name='wohnort',
            field=models.ForeignKey(to='management.Wohnort'),
            preserve_default=True,
        ),
    ]
