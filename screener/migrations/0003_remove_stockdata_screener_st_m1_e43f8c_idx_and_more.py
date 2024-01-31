# Generated by Django 5.0.1 on 2024-01-31 03:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("screener", "0002_stockdata_screener_st_m1_e43f8c_idx"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="stockdata",
            name="screener_st_m1_e43f8c_idx",
        ),
        migrations.AddIndex(
            model_name="stockdata",
            index=models.Index(
                fields=[
                    "symbol",
                    "m1",
                    "m3",
                    "m5",
                    "m15",
                    "m30",
                    "m45",
                    "h1",
                    "h2",
                    "h4",
                    "h8",
                    "h12",
                    "h16",
                    "d1",
                    "d2",
                    "d3",
                    "d4",
                    "d5",
                    "d6",
                    "w1",
                    "w2",
                    "w3",
                    "w4",
                ],
                name="screener_st_symbol_37c8c7_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="stockdata",
            index=models.Index(
                fields=["symbol", "timestamp"], name="screener_st_symbol_4f3702_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="stockdata",
            index=models.Index(fields=["symbol"], name="screener_st_symbol_11ddd6_idx"),
        ),
    ]