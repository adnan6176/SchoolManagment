# Generated by Django 3.2.11 on 2022-01-12 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('class_name', models.TextField(blank=True)),
                ('roll_number', models.TextField(blank=True)),
            ],
        ),
    ]