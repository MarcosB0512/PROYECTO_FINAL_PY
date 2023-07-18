# Generated by Django 4.1 on 2023-07-02 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("App_CS", "0003_alter_imagen_rodeo_alter_imagen_show_show_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="imagen",
            name="id",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="imagen_show",
            name="id",
            field=models.AutoField(default=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="imagen",
            name="rodeo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="App_CS.rodeo"
            ),
        ),
        migrations.AlterField(
            model_name="imagen_show",
            name="show",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="App_CS.show"
            ),
        ),
    ]
