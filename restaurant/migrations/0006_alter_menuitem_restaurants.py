# Generated by Django 4.0.4 on 2022-06-27 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_remove_menuitem_restaurants_menuitem_restaurants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='restaurants',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='MenuItem', to='restaurant.restaurant'),
        ),
    ]
