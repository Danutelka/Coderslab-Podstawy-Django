# Generated by Django 2.1 on 2019-05-29 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.OneToOneField(default=6, on_delete=django.db.models.deletion.CASCADE, to='homework.Person'),
            preserve_default=False,
        ),
    ]
