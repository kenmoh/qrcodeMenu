# Generated by Django 4.0.6 on 2022-07-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_description', models.CharField(max_length=100)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
