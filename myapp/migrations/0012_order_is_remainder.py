# Generated by Django 4.2.1 on 2023-05-08 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_delete_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_remainder',
            field=models.BooleanField(default=False),
        ),
    ]
