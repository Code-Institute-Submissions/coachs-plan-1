# Generated by Django 3.1.1 on 2020-10-26 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='description',
            field=models.TextField(blank=True, default='Section Description'),
        ),
    ]
