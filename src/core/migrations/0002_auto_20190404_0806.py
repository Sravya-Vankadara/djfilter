# Generated by Django 2.2 on 2019-04-04 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='publish_date',
            field=models.DateTimeField(),
        ),
    ]
