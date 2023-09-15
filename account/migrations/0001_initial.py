# Generated by Django 4.1.4 on 2023-09-15 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(default='salll', max_length=50)),
                ('username', models.CharField(default=' ', max_length=50)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('first_name', models.CharField(default=' ', max_length=50)),
                ('last_name', models.CharField(default=' ', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('date', models.DateField()),
            ],
        ),
    ]