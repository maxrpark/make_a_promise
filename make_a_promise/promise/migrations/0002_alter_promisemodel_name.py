# Generated by Django 4.0 on 2022-01-01 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promisemodel',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
    ]
