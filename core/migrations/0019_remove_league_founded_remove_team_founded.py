# Generated by Django 4.1 on 2022-09-25 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_alter_league_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="league",
            name="founded",
        ),
        migrations.RemoveField(
            model_name="team",
            name="founded",
        ),
    ]
