# Generated by Django 5.0.3 on 2024-03-19 01:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='club_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='clubs.club'),
        ),
    ]