# Generated by Django 4.1.2 on 2022-11-10 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem", name="floor", field=models.IntegerField(default=1),
        ),
    ]
