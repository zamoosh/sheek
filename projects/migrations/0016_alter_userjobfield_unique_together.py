# Generated by Django 3.2.9 on 2022-02-21 08:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0015_rename_national_card_userjobfield_document_image'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userjobfield',
            unique_together={('jobField', 'owner')},
        ),
    ]
