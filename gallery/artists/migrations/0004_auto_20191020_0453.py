# Generated by Django 2.2.6 on 2019-10-20 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_auto_20191020_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='pic',
            field=models.ImageField(upload_to='assets/img'),
        ),
    ]
