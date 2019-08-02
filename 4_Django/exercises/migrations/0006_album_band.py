# Generated by Django 2.1 on 2019-05-26 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0005_album_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='exercises.Band'),
            preserve_default=False,
        ),
    ]