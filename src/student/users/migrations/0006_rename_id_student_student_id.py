# Generated by Django 4.2.7 on 2023-11-25 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_student_number_alter_student_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='id',
            new_name='student_id',
        ),
    ]
