# Generated by Django 4.2 on 2025-03-30 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0017_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='yard',
            name='district',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Admin.district'),
        ),
    ]
