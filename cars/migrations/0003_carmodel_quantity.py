# Generated by Django 5.0 on 2023-12-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_carmodel_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]