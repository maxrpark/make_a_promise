# Generated by Django 4.0 on 2022-01-04 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promise', '0002_alter_promisemodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='promisemodel',
            name='color',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
