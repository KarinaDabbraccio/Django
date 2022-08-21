# Generated by Django 3.2.5 on 2022-08-03 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delivered',
            new_name='picked_up',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
        migrations.AddField(
            model_name='order',
            name='paid_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]