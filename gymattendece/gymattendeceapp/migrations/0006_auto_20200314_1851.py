# Generated by Django 2.2.3 on 2020-03-14 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymattendeceapp', '0005_auto_20200314_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='endingdate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='joiningdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]