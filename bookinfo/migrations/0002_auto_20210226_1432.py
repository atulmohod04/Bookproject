# Generated by Django 3.1.5 on 2021-02-26 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='prize',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
