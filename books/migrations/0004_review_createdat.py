# Generated by Django 4.0.1 on 2022-08-11 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='createdAt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]