# Generated by Django 3.1.4 on 2021-05-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210512_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='model_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
