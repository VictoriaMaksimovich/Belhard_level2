# Generated by Django 5.1 on 2024-09-20 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="books",
            name="style_book",
            field=models.CharField(
                default="Не указано", max_length=20, verbose_name="Жанр"
            ),
        ),
    ]
