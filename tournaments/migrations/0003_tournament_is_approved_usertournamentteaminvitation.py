# Generated by Django 5.0.3 on 2024-04-06 20:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_rename_speaker_ponits_tournamentuserspeakerpoint_speaker_points'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='UserTournamentTeamInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False)),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inviter_team_invitations', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receiver_team_invitations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
