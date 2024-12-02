# Generated by Django 5.1 on 2024-11-30 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=20, verbose_name="Имя")),
                (
                    "login",
                    models.CharField(max_length=20, unique=True, verbose_name="Логин"),
                ),
                (
                    "password",
                    models.CharField(max_length=20, unique=True, verbose_name="Пароль"),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True, upload_to="photos/%Y/%m/%d", verbose_name="Фото"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="только латинские",
                        max_length=255,
                        unique=True,
                        verbose_name="URL",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
                "db_table": "users",
                "ordering": ["login"],
                "indexes": [
                    models.Index(fields=["login"], name="users_login_eda8f4_idx")
                ],
                "unique_together": {("name", "login")},
            },
        ),
    ]
