# Generated by Django 3.0.2 on 2020-02-24 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200224_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='data',
            field=models.TextField(null=True),
        ),
    ]