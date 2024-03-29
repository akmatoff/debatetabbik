# Generated by Django 5.0.3 on 2024-03-24 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0010_alter_club_created_alter_clubjoinrequest_created'),
        ('users', '0006_alter_user_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='users', to='clubs.club'),
        ),
    ]
