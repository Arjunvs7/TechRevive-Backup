# Generated by Django 4.1.6 on 2023-04-13 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_yard'),
        ('EwasteCollector', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectedewaste',
            name='Ewaste',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.assignewastebooking'),
        ),
        migrations.AlterField(
            model_name='collectedewaste',
            name='yard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.yard'),
        ),
    ]
