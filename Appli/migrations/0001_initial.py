# Generated by Django 4.2.4 on 2023-08-04 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sheet1",
            fields=[
                ("serialno", models.IntegerField(primary_key=True, serialize=False)),
                ("word", models.CharField(blank=True, max_length=150, null=True)),
                ("origin", models.CharField(blank=True, max_length=25, null=True)),
                ("meaning", models.CharField(blank=True, max_length=2000, null=True)),
                ("sentence", models.CharField(blank=True, max_length=2000, null=True)),
                ("used", models.BooleanField(blank=True, null=True)),
            ],
            options={"db_table": "sheet1", "managed": False,},
        ),
    ]
