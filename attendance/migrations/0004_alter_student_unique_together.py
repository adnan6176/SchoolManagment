# Generated by Django 3.2.11 on 2022-01-12 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_alter_student_class_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('class_name', 'roll_number')},
        ),
    ]
