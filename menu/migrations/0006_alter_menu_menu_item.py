# Generated by Django 4.0.6 on 2022-07-29 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_drinkcategory_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_item',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.category'),
        ),
    ]
