# Generated by Django 3.1.8 on 2021-12-21 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('droid', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='droid',
            options={'ordering': ['-id']},
        ),
    ]