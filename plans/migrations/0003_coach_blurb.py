# Generated by Django 3.1.1 on 2020-10-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_section_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='blurb',
            field=models.TextField(default='This is the coach blurb'),
            preserve_default=False,
        ),
    ]