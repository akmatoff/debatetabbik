# Generated by Django 5.0.3 on 2024-04-03 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournamentuserspeakerpoint',
            old_name='speaker_ponits',
            new_name='speaker_points',
        ),
    ]
