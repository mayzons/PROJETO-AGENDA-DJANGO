# Generated by Django 5.1.7 on 2025-03-28 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_category_options_alter_contact_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 28, 15, 57, 47, 920488, tzinfo=datetime.timezone.utc)),
        ),
    ]
