# Generated by Django 3.0.5 on 2020-04-23 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogtrilhas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trilha',
            name='fotos',
        ),
    ]
