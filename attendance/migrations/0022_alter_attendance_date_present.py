# Generated by Django 3.2.11 on 2022-01-12 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0021_student_enroll_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date_present',
            field=models.DateTimeField(blank=True),
        ),
    ]