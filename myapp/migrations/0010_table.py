# Generated by Django 4.2 on 2023-05-07 19:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_orderreminder_delete_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(unique=True)),
                ('summary_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('is_occupied', models.BooleanField(default=False)),
            ],
        ),
    ]