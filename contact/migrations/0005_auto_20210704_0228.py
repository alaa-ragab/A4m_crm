# Generated by Django 3.1.4 on 2021-07-04 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
