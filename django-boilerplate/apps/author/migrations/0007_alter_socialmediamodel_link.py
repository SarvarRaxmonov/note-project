# Generated by Django 4.2.1 on 2023-07-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("author", "0006_authormodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="socialmediamodel",
            name="link",
            field=models.CharField(max_length=1000),
        ),
    ]
