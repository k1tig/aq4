# Generated by Django 5.0.2 on 2024-02-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='scapes_followed',
            field=models.ManyToManyField(blank=True, to='catalog.scape'),
        ),
    ]
