# Generated by Django 2.2.17 on 2021-02-05 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20210204_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='uuid',
            field=models.CharField(default='a92b6', max_length=40),
        ),
    ]
