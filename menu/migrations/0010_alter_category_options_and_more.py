# Generated by Django 4.0.6 on 2022-07-29 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_alter_subcategory_options_alter_menu_menu_item_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Sub Category'},
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='menu_item',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='sub_category',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
