# Generated by Django 4.1 on 2022-10-02 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0022_remove_footballer_age_remove_footballer_pos_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="footballer",
            name="player",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="footballer",
            name="position",
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]