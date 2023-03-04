# Generated by Django 3.2.12 on 2023-03-04 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='price',
        ),
        migrations.RemoveField(
            model_name='price',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='price',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='price',
            name='price_usd',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]