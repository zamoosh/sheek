# Generated by Django 3.2.9 on 2022-03-31 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0003_auto_20220331_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='article',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]