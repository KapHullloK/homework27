# Generated by Django 4.2.1 on 2023-05-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ads",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=25)),
                ("price", models.IntegerField()),
                ("description", models.CharField(max_length=2500)),
                ("address", models.CharField(max_length=250)),
                ("is_published", models.CharField(max_length=10)),
            ],
        ),
    ]
