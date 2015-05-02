# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lfc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('basecontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lfc.BaseContent')),
                ('text', models.TextField(verbose_name='Text', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('lfc.basecontent',),
        ),
    ]
