# Generated by Django 3.2.9 on 2021-12-13 12:46

import client.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_user_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='upload_file',
            field=models.ImageField(blank=True, null=True, upload_to=client.models.user_image),
        ),
    ]