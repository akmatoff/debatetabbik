# Generated by Django 5.0.3 on 2024-03-19 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_alter_club_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='icon',
            field=models.ImageField(upload_to='uploads/club_icons/'),
        ),
    ]
