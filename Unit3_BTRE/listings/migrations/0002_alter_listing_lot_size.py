# Generated by Django 5.1.4 on 2024-12-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]