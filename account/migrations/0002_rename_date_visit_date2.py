# Generated by Django 4.1.4 on 2023-09-15 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='date',
            new_name='date2',
        ),
    ]
