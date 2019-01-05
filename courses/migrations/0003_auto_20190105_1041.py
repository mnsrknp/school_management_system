# Generated by Django 2.0.6 on 2019-01-05 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20181106_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses_joined', to='students.StudentProfile'),
        ),
    ]