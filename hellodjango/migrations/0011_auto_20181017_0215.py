# Generated by Django 2.1.1 on 2018-10-17 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hellodjango', '0010_auto_20181016_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empnew',
            name='gender',
            field=models.IntegerField(choices=[(1, '男'), (2, '女')], null=True),
        ),
    ]