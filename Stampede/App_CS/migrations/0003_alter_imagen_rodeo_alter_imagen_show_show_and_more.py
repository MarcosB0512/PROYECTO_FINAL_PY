# Generated by Django 4.1 on 2023-07-02 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("App_CS", "0002_alter_rodeo_user_alter_show_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagen",
            name="rodeo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="App_CS.rodeo",
            ),
        ),
        migrations.AlterField(
            model_name="imagen_show",
            name="show",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="App_CS.show",
            ),
        ),
        migrations.AlterField(
            model_name="rodeo",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="show",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]