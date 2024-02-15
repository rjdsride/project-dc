# Generated by Django 5.0.1 on 2024-02-15 01:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0007_rename_group_cable_group_dev'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='datacenter.device')),
            ],
        ),
        migrations.AddField(
            model_name='cable',
            name='dev_a',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='datacenter.deva'),
        ),
        migrations.CreateModel(
            name='DevB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='datacenter.device')),
            ],
        ),
        migrations.AddField(
            model_name='cable',
            name='dev_b',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='datacenter.devb'),
        ),
    ]
