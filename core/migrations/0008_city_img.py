# Generated by Django 3.0.2 on 2020-02-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_city_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]