# Generated by Django 5.0.3 on 2024-03-19 02:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='club_leader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='club',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='icon',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
