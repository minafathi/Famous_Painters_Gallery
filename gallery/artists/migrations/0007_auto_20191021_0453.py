# Generated by Django 2.2.6 on 2019-10-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0006_auto_20191021_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='born',
            field=models.CharField(max_length=255),
        ),
    ]
