# Generated by Django 3.2.9 on 2022-04-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_auto_20220316_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobfield',
            name='competence',
            field=models.BooleanField(default=False),
        ),
    ]