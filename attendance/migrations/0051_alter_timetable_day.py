# Generated by Django 3.2.11 on 2022-01-23 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0050_auto_20220123_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='day',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='attendance.dayname'),
        ),
    ]
