# Generated by Django 3.0.8 on 2021-09-16 21:40
from django.conf import settings
from django.db import migrations


def seed_scouting_websites(apps, schema_editor):
    if schema_editor.connection.alias != 'default':
        return
    ScoutingWebsite = apps.get_model('app_prime_league', 'ScoutingWebsite')

    _ = ScoutingWebsite.objects.create(id=1, name=settings.DEFAULT_SCOUTING_NAME,
                                       base_url=settings.DEFAULT_SCOUTING_URL, separator=settings.DEFAULT_SCOUTING_SEP)


class Migration(migrations.Migration):
    dependencies = [
        ('app_prime_league', '0013_scoutingwebsite'),
    ]

    operations = [
        migrations.RunPython(seed_scouting_websites),
    ]
