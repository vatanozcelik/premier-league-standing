# Generated by Django 4.1 on 2022-10-03 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0023_alter_footballer_player_alter_footballer_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="footballer",
            name="position",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]