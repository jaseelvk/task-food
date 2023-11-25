# Generated by Django 4.2.7 on 2023-11-25 09:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_student_food'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='number',
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
