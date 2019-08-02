# Generated by Django 2.1 on 2019-05-25 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_populate'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='genre',
            field=models.IntegerField(choices=[(-1, 'not defined'), (0, 'rock'), (1, 'metal'), (2, 'pop'), (3, 'hip-hop'), (4, 'electronic'), (5, 'raegge'), (6, 'other')], default=-1),
        ),
        migrations.AddField(
            model_name='band',
            name='still_active',
            field=models.BooleanField(default=True),
        ),
    ]