# Generated by Django 5.0.2 on 2024-02-08 00:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Fish',
            },
        ),
        migrations.CreateModel(
            name='Invertebrate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TankCo2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co2', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Co2',
            },
        ),
        migrations.CreateModel(
            name='TankFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TankHardscape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hardscape_type', models.CharField(choices=[('s', 'Stone'), ('w', 'Wood')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TankLight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TankSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TankSoil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TankVolume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=200)),
                ('instagram', models.CharField(max_length=200)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Scape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scape_name', models.CharField(max_length=100)),
                ('fish', models.ManyToManyField(blank=True, to='catalog.fish')),
                ('invertebrate', models.ManyToManyField(blank=True, to='catalog.invertebrate')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_name', to='catalog.profile')),
                ('plants', models.ManyToManyField(blank=True, related_name='fucking_scape_id', to='catalog.plant')),
                ('co2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.tankco2')),
                ('filtration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.tankfilter')),
                ('hardscape', models.ManyToManyField(blank=True, to='catalog.tankhardscape')),
                ('lighting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.tanklight')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.tanksize')),
                ('soil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.tanksoil')),
                ('volume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.tankvolume')),
            ],
        ),
    ]
