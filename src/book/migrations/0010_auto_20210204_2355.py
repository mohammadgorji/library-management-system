# Generated by Django 2.2.17 on 2021-02-05 07:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_auto_20210204_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=40),
        ),
    ]
