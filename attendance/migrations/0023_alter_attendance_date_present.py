# Generated by Django 3.2.11 on 2022-01-12 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0022_alter_attendance_date_present'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date_present',
            field=models.DateField(blank=True),
        ),
    ]