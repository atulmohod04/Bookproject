# Generated by Django 3.1.5 on 2021-02-26 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookinfo', '0002_auto_20210226_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='prize',
            field=models.CharField(max_length=150),
        ),
    ]
