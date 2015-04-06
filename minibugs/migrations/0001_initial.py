# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250, null=True, blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_time'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('viewname', models.CharField(max_length=250, null=True, blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_time'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TicketUpdate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('attachment', models.FileField(null=True, upload_to=b'minibugs', blank=True)),
                ('status', models.CharField(default=b'N', max_length=1, choices=[(b'N', b'New'), (b'W', b'Working'), (b'V', b'Verified'), (b'F', b'Fixed'), (b'T', b"Won't Fix"), (b'B', b'Not a Bug'), (b'C', b'Closed')])),
                ('type', models.CharField(default=b'N', max_length=1, choices=[(b'D', b'Defect'), (b'E', b'Enhancement')])),
                ('priority', models.CharField(default=b'D', max_length=1, choices=[(b'L', b'Low'), (b'M', b'Medium'), (b'H', b'High')])),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('ticket', models.ForeignKey(to='minibugs.Ticket')),
            ],
            options={
                'ordering': ['-created_time'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ticket',
            name='current',
            field=models.ForeignKey(related_name='current', blank=True, to='minibugs.TicketUpdate', null=True),
            preserve_default=True,
        ),
    ]
