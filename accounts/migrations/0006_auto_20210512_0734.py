# Generated by Django 3.1.4 on 2021-05-12 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='ip_adress',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='old_data',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
