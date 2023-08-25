# Generated by Django 4.2.4 on 2023-08-08 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Appli", "0006_delete_sheet3"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sheet3",
            fields=[
                ("serialno", models.AutoField(primary_key=True, serialize=False)),
                ("word", models.CharField(blank=True, max_length=200, null=True)),
                ("origin", models.CharField(blank=True, max_length=25, null=True)),
                ("meaning", models.CharField(blank=True, max_length=3000, null=True)),
                ("sentence", models.CharField(blank=True, max_length=3000, null=True)),
                ("used", models.BooleanField(blank=True, null=True)),
            ],
            options={"db_table": "sheet3", "managed": False,},
        ),
    ]
