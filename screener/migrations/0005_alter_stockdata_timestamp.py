# Generated by Django 5.0.1 on 2024-01-31 05:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("screener", "0004_stockdata_timezone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stockdata",
            name="timestamp",
            field=models.DateTimeField(),
        ),
    ]