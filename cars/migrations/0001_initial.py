# Generated by Django 5.0 on 2023-12-16 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.brandmodel')),
            ],
        ),
    ]
