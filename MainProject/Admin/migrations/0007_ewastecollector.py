# Generated by Django 4.1.6 on 2023-03-21 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_assignservicebook'),
    ]

    operations = [
        migrations.CreateModel(
            name='EwasteCollector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EwasteCollector_name', models.CharField(max_length=50)),
                ('EwasteCollector_contact', models.CharField(max_length=50)),
                ('EwasteCollector_email', models.CharField(max_length=50)),
                ('EwasteCollector_photo', models.FileField(upload_to='CollectorDocs/')),
                ('user_proof', models.FileField(upload_to='CollectorDocs/')),
                ('user_password', models.CharField(max_length=50)),
                ('user_address', models.CharField(max_length=100)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.place')),
            ],
        ),
    ]
