# Generated by Django 3.2.11 on 2022-01-13 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0027_alter_attendance_date_present'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='submit_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
