# Generated by Django 3.2.9 on 2022-01-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_project_status_jobfield_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userjobfield',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]