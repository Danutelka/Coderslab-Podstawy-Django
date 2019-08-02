# Generated by Django 2.1 on 2019-05-27 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0007_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='exercises.Person')),
                ('position_name', models.CharField(max_length=128)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
