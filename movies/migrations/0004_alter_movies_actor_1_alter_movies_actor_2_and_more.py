# Generated by Django 4.0 on 2022-01-09 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movies_locations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='actor_1',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='actor_2',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='actor_3',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
