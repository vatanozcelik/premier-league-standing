# Generated by Django 4.1 on 2022-09-25 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0017_team_slug_alter_league_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="league",
            name="slug",
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
