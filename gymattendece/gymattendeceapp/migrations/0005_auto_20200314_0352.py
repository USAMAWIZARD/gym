# Generated by Django 2.2.3 on 2020-03-13 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymattendeceapp', '0004_auto_20200314_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='phoneno',
            field=models.CharField(max_length=11),
        ),
    ]
