# Generated by Django 3.2.11 on 2022-01-27 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0055_alter_student_roll_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='enroll_teacher',
            new_name='enroll_by',
        ),
    ]
