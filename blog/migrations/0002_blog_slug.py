# Generated by Django 4.0.2 on 2022-02-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.CharField(default='', max_length=150),
        ),
    ]
