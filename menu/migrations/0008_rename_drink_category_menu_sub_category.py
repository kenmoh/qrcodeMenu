# Generated by Django 4.0.6 on 2022-07-29 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_rename_drinkcategory_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='drink_category',
            new_name='sub_category',
        ),
    ]
