# Generated by Django 5.2.4 on 2025-07-04 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(max_length=100),
        ),
    ]
