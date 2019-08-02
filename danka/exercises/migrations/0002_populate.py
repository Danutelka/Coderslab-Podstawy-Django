# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from exercises.models import Band


def populate(apps, schema_editor):
    Band.objects.create(name="The Beatles")
    Band.objects.create(name="The Rolling Stones")
    Band.objects.create(name="Metallica", year=1982)
    Band.objects.create(name="Pink Floyd", year=1965)
    Band.objects.create(name="Deep Purple")
    Band.objects.create(name="The Clash", year=1976)
    Band.objects.create(name="AC/DC", year=1973)
    Band.objects.create(name="Nirvana", year=1987)
    Band.objects.create(name="Blur", year=1988)
    Band.objects.create(name="Oasis", year=1991)
    Band.objects.create(name="Red Hot Chili Peppers", year=1983)
    Band.objects.create(name="System Of A Down", year=1994)
    Band.objects.create(name="Dire Straits")
    Band.objects.create(name="Twenty One Pilots", year=2009)


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]
