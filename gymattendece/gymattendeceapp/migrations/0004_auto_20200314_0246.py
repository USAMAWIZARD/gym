# Generated by Django 2.2.3 on 2020-03-13 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymattendeceapp', '0003_auto_20200314_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='endingdate',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gym',
            name='joiningdate',
            field=models.CharField(max_length=255),
        ),
    ]
