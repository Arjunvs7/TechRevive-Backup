# Generated by Django 4.2 on 2025-03-25 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
