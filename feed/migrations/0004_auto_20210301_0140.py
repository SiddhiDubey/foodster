# Generated by Django 3.1.7 on 2021-02-28 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20210226_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='fname',
            field=models.CharField(default='', max_length=280),
        ),
    ]
