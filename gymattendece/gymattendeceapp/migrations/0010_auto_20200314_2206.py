# Generated by Django 2.2.3 on 2020-03-14 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymattendeceapp', '0009_attendence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='status',
            field=models.CharField(max_length=500),
        ),
    ]
