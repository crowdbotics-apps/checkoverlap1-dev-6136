# Generated by Django 2.2.13 on 2020-06-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20200616_1514"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bank",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bankName", models.BigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name="address",
            name="province",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
