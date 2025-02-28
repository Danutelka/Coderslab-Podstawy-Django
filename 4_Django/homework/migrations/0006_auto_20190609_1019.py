# Generated by Django 2.1 on 2019-06-09 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0005_auto_20190529_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='position',
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movie_director', to='homework.Person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='screenplay',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movie_screenplay', to='homework.Person'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='personmovie',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homework.Person'),
        ),
    ]
