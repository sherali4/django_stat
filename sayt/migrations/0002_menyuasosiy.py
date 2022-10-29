# Generated by Django 4.1.2 on 2022-10-17 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sayt", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Menyuasosiy",
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
                ("nomi", models.CharField(max_length=50, verbose_name="Bo'lim nomi")),
                ("url_nomi", models.SlugField(verbose_name="url nomi")),
                (
                    "hosil qilingan kun",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="menyu yaratilgan kun"
                    ),
                ),
                (
                    "qushish",
                    models.BooleanField(default=False, verbose_name="Qo'shish"),
                ),
            ],
        ),
    ]
