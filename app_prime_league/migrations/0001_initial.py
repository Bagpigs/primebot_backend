# Generated by Django 3.0.7 on 2020-07-01 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('game_day', models.IntegerField()),
                ('game_closed', models.BooleanField()),
            ],
            options={
                'db_table': 'games',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('group_link', models.CharField(max_length=300, null=True)),
                ('telegram_channel_id', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'teams',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_prime_league.Team')),
            ],
            options={
                'db_table': 'players',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('action', models.CharField(max_length=30)),
                ('details', models.TextField(null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_prime_league.Game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_prime_league.Player')),
            ],
            options={
                'db_table': 'logs',
            },
        ),
        migrations.AddField(
            model_name='game',
            name='enemy_lineup',
            field=models.ManyToManyField(to='app_prime_league.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='enemy_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_enemy_team', to='app_prime_league.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_against', to='app_prime_league.Team'),
        ),
    ]
