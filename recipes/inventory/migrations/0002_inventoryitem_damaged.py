# Generated by Django 3.2.5 on 2022-08-03 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='damaged',
            field=models.BooleanField(default=False),
        ),
    ]
