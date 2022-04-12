# Generated by Django 2.2.17 on 2021-02-05 03:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_bookinstance_borrower'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
